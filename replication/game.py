"""
Referential (Lewis signaling) game for studying symbol emergence.

Two neural agents:
  Sender   sees an object (attribute-value vector) and emits a discrete message.
  Receiver sees the message and a set of candidate objects, picks one.
Nobody designs the language. We measure what emerges.

Objects live in an attribute-value world (n_attrs attributes, n_vals values each).
A fraction of attribute combinations is HELD OUT during training; success on
them is the operational test of compositionality / displacement ("can you refer
to something you never saw?").
"""
from __future__ import annotations
import itertools, math, random
from dataclasses import dataclass, field
from typing import Optional

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


# ----------------------------------------------------------------------------
# World
# ----------------------------------------------------------------------------
class World:
    def __init__(self, n_attrs=3, n_vals=4, holdout_frac=0.25, seed=0):
        self.n_attrs, self.n_vals = n_attrs, n_vals
        self.objects = np.array(list(itertools.product(range(n_vals), repeat=n_attrs)))
        rng = np.random.RandomState(seed)
        idx = rng.permutation(len(self.objects))
        n_test = int(len(idx) * holdout_frac)
        self.test_idx = np.sort(idx[:n_test])
        self.train_idx = np.sort(idx[n_test:])
        self.dim = n_attrs * n_vals
        # one-hot feature table, built once: encode() is then a single index op
        onehot = np.zeros((len(self.objects), n_attrs, n_vals), dtype=np.float32)
        for a in range(n_attrs):
            onehot[np.arange(len(self.objects)), a, self.objects[:, a]] = 1.0
        self.feats = torch.from_numpy(onehot.reshape(len(self.objects), -1))
        # v4: optional hard distractors — a share `hard_frac` of rounds draws distractors from the target's
        # Hamming-1 neighbours (each differs in ONE attribute), so a single attribute cannot identify the target.
        self.hard_frac = 0.0
        d = (self.objects[:, None, :] != self.objects[None, :, :]).sum(-1)
        self.h1 = np.array([np.where(d[i] == 1)[0] for i in range(len(self.objects))])   # n x (n_attrs*(n_vals-1))

    def encode(self, obj_ids) -> torch.Tensor:
        return self.feats[torch.as_tensor(np.asarray(obj_ids), dtype=torch.long)]

    def candidates(self, targets, n_distractors, rng):
        """Target + n_distractors DISTINCT other objects, shuffled. Returns (cands, labels).
        Distractors come from the full object set (harder, and standard).
        v3 fix: the old `(others + 1) % n` collision fix-up could duplicate a distractor
        (~0.3% of rows); now we draw from [0, n-2] and skip the target with a bijection."""
        targets = np.asarray(targets)
        B, n = len(targets), len(self.objects)
        # a uniform k-subset of [0, n-2] per row (first k of a random permutation), then skip the
        # target with a bijection [0, n-2] -> [0, n-1] \ {t}. Vectorised: no per-row Python loop.
        others = np.argpartition(rng.rand(B, n - 1), n_distractors - 1, axis=1)[:, :n_distractors]
        others = others + (others >= targets[:, None])
        if self.hard_frac > 0:
            hard = rng.rand(B) < self.hard_frac
            if hard.any():
                nb = self.h1[targets[hard]]                                   # (Bh, k) Hamming-1 neighbours
                pick = np.argpartition(rng.rand(len(nb), nb.shape[1]), n_distractors - 1, axis=1)[:, :n_distractors]
                others[hard] = np.take_along_axis(nb, pick, axis=1)
        cands = np.concatenate([targets[:, None], others], axis=1)
        perm = np.argsort(rng.rand(B, n_distractors + 1), axis=1)
        cands = np.take_along_axis(cands, perm, axis=1)
        labels = np.argmax(cands == targets[:, None], axis=1)
        return cands, labels

    def sample_batch(self, batch, n_distractors, split="train", rng=None):
        rng = rng or np.random
        pool = self.train_idx if split == "train" else self.test_idx
        targets = rng.choice(pool, size=batch)
        cands, labels = self.candidates(targets, n_distractors, rng)
        return targets, cands, labels


# ----------------------------------------------------------------------------
# Agents
# ----------------------------------------------------------------------------
class Sender(nn.Module):
    def __init__(self, in_dim, vocab, msg_len, hidden=64):
        super().__init__()
        self.vocab, self.msg_len, self.hidden = vocab, msg_len, hidden
        self.enc = nn.Sequential(nn.Linear(in_dim, hidden), nn.Tanh())
        self.embed = nn.Embedding(vocab + 1, hidden)      # +1 = start token
        self.gru = nn.GRUCell(hidden, hidden)
        self.out = nn.Linear(hidden, vocab)

    def forward(self, x, greedy=False):
        B = x.size(0)
        h = self.enc(x)
        tok = torch.full((B,), self.vocab, dtype=torch.long)  # start token
        msgs, logps, ents = [], [], []
        for _ in range(self.msg_len):
            h = self.gru(self.embed(tok), h)
            logits = self.out(h)
            logp = F.log_softmax(logits, -1)                # same math as Categorical, ~3x cheaper
            if greedy:
                tok = logits.argmax(-1)
            else:
                tok = torch.multinomial(logp.exp(), 1).squeeze(1)
            msgs.append(tok)
            logps.append(logp.gather(1, tok[:, None]).squeeze(1))
            ents.append(-(logp.exp() * logp).sum(-1))
        return torch.stack(msgs, 1), torch.stack(logps, 1).sum(1), torch.stack(ents, 1).mean(1)

    def supervised_loss(self, x, target_msgs):
        """Teacher-force the sender to reproduce given messages (used for 'reading the bone')."""
        B = x.size(0)
        h = self.enc(x)
        tok = torch.full((B,), self.vocab, dtype=torch.long)
        loss = 0.0
        for t in range(self.msg_len):
            h = self.gru(self.embed(tok), h)
            logits = self.out(h)
            loss = loss + F.cross_entropy(logits, target_msgs[:, t])
            tok = target_msgs[:, t]
        return loss / self.msg_len


class Receiver(nn.Module):
    def __init__(self, in_dim, vocab, hidden=64):
        super().__init__()
        self.embed = nn.Embedding(vocab, hidden)
        self.gru = nn.GRU(hidden, hidden, batch_first=True)
        self.obj_enc = nn.Sequential(nn.Linear(in_dim, hidden), nn.Tanh())

    def forward(self, msgs, cand_feats):
        # msgs: (B, L) ; cand_feats: (B, C, in_dim)
        _, h = self.gru(self.embed(msgs))
        m = h[-1]                                            # (B, hidden)
        c = self.obj_enc(cand_feats)                         # (B, C, hidden)
        return torch.einsum("bh,bch->bc", m, c)              # logits over candidates


# ----------------------------------------------------------------------------
# Metrics
# ----------------------------------------------------------------------------
def _rank_avg(x):
    """Average ranks for ties (fractional ranking). Distances here are small integers,
    so ties are everywhere; plain argsort ranking is wrong."""
    x = np.asarray(x, float)
    order = np.argsort(x, kind="mergesort")
    ranks = np.empty(len(x), float)
    i = 0
    while i < len(x):
        j = i
        while j + 1 < len(x) and x[order[j + 1]] == x[order[i]]:
            j += 1
        ranks[order[i:j + 1]] = (i + j) / 2.0 + 1
        i = j + 1
    return ranks


def _spearman(a, b):
    ra, rb = _rank_avg(a), _rank_avg(b)
    ra -= ra.mean(); rb -= rb.mean()
    d = math.sqrt((ra ** 2).sum() * (rb ** 2).sum())
    return float((ra * rb).sum() / d) if d > 0 else 0.0


@torch.no_grad()
def language_of(sender: Sender, world: World):
    """Greedy message for every object. Returns (n_objects, msg_len) int array."""
    sender.eval()
    x = world.encode(np.arange(len(world.objects)))
    msgs, _, _ = sender(x, greedy=True)
    sender.train()
    return msgs.numpy()


def topographic_similarity(world: World, msgs: np.ndarray) -> float:
    """Spearman correlation between object distance (Hamming over attributes) and
    message distance (Hamming over symbols). ~1 = perfectly compositional; ~0 = holistic."""
    objs = world.objects
    n = len(objs)
    od, md = [], []
    for i in range(n):
        for j in range(i + 1, n):
            od.append((objs[i] != objs[j]).sum())
            md.append((msgs[i] != msgs[j]).sum())
    return _spearman(np.array(od), np.array(md))


def positional_disentanglement(world: World, msgs: np.ndarray) -> float:
    """Chaabouni et al. 2020: for each message position, how much its symbol
    is explained by the single best attribute vs the second best (mutual information gap)."""
    def mi(x, y):
        xs, ys = np.unique(x), np.unique(y)
        pxy = np.zeros((len(xs), len(ys)))
        for a, b in zip(x, y):
            pxy[np.searchsorted(xs, a), np.searchsorted(ys, b)] += 1
        pxy /= pxy.sum(); px = pxy.sum(1, keepdims=True); py = pxy.sum(0, keepdims=True)
        nz = pxy > 0
        return float((pxy[nz] * np.log(pxy[nz] / (px @ py)[nz])).sum())
    def ent(x):
        _, c = np.unique(x, return_counts=True); p = c / c.sum()
        return float(-(p * np.log(p)).sum())
    scores, weights = [], []
    for pos in range(msgs.shape[1]):
        h = ent(msgs[:, pos])
        if h < 1e-9:
            continue
        mis = sorted([mi(msgs[:, pos], world.objects[:, a]) for a in range(world.n_attrs)], reverse=True)
        scores.append((mis[0] - mis[1]) / h); weights.append(h)
    return float(np.average(scores, weights=weights)) if scores else 0.0


@torch.no_grad()
def evaluate(sender, receiver, world, n_distractors, split, n=512, rng=None):
    sender.eval(); receiver.eval()
    rng = rng or np.random.RandomState(123)
    t, cands, labels = world.sample_batch(n, n_distractors, split, rng)
    msgs, _, _ = sender(world.encode(t), greedy=True)
    logits = receiver(msgs, world.encode(cands.reshape(-1)).view(n, -1, world.dim))
    acc = (logits.argmax(-1).numpy() == labels).mean()
    sender.train(); receiver.train()
    return float(acc)


# ----------------------------------------------------------------------------
# The external artifact ("notched bone"): a shared, persistent, capacity-limited
# lexicon that lives OUTSIDE any agent and survives generational turnover.
# ----------------------------------------------------------------------------
class Bone:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.entries: dict[int, tuple] = {}     # object id -> message tuple
        self.successes: dict[int, int] = {}     # how often this entry proved useful

    def record(self, obj_ids, msgs, correct):
        """After a round, successful (object, message) pairs are carved into the bone."""
        for o, m, ok in zip(obj_ids, msgs, correct):
            if not ok:
                continue
            o = int(o); m = tuple(int(s) for s in m)
            if o in self.entries and self.entries[o] == m:
                self.successes[o] += 1
            elif o in self.entries:
                # a competing form: keep the incumbent unless it has been weak
                if self.successes[o] < 2:
                    self.entries[o], self.successes[o] = m, 1
            elif len(self.entries) < self.capacity:
                self.entries[o], self.successes[o] = m, 1
            else:
                # bone is full: overwrite the least useful entry
                weakest = min(self.successes, key=self.successes.get)
                if self.successes[weakest] < 2:
                    del self.entries[weakest]; del self.successes[weakest]
                    self.entries[o], self.successes[o] = m, 1

    def read(self):
        if not self.entries:
            return None, None
        objs = np.array(list(self.entries.keys()))
        msgs = np.array([self.entries[o] for o in objs])
        return objs, msgs

    def rewrite_from(self, sender: "Sender", world: "World"):
        """'New edition': keep the same slots (objects) but re-carve every entry from the
        parent's FINAL language. Separates 'persistent external record' from
        'accumulated stale forms'."""
        if not self.entries:
            return
        objs = np.array(list(self.entries.keys()))
        with torch.no_grad():
            msgs, _, _ = sender(world.encode(objs), greedy=True)
        for o, m in zip(objs, msgs.numpy()):
            self.entries[int(o)] = tuple(int(s) for s in m)
            self.successes[int(o)] = 1


# ----------------------------------------------------------------------------
# Training
# ----------------------------------------------------------------------------
@dataclass
class Config:
    condition: str = "pair"        # pair | population | generations | oral | oral_fixed | bone | bone_edition
    n_attrs: int = 3
    n_vals: int = 4
    vocab: int = 8
    msg_len: int = 3
    n_distractors: int = 4
    batch: int = 64
    hidden: int = 64
    lr: float = 1e-3
    entropy_coef: float = 0.02
    steps: int = 3000              # per generation
    generations: int = 6           # for generations/oral/bone
    population: int = 4            # for population condition
    n_transmit: int = 19           # ALL transmission channels carry exactly this many (object, message) pairs
    transmit_steps: int = 200      # supervised imitation steps at start of a generation
    bone_capacity: int = -1        # -1 = same as n_transmit (matched channels)
    holdout_frac: float = 0.25
    eval_every: int = 250
    seed: int = 0


def make_agents(cfg: Config, world: World, seed: int):
    torch.manual_seed(seed)
    s = Sender(world.dim, cfg.vocab, cfg.msg_len, cfg.hidden)
    r = Receiver(world.dim, cfg.vocab, cfg.hidden)
    return s, r


def train_generation(cfg, world, senders, receivers, rng, bone: Optional[Bone], log, gen, step_offset):
    params = [p for a in senders + receivers for p in a.parameters()]
    opt = torch.optim.Adam(params, lr=cfg.lr)
    baseline = 0.0
    for step in range(1, cfg.steps + 1):
        s = senders[rng.randint(len(senders))]
        r = receivers[rng.randint(len(receivers))]
        t, cands, labels = world.sample_batch(cfg.batch, cfg.n_distractors, "train", rng)
        x = world.encode(t)
        msgs, logp, ent = s(x)
        logits = r(msgs, world.encode(cands.reshape(-1)).view(cfg.batch, -1, world.dim))
        labels_t = torch.from_numpy(labels)
        r_loss = F.cross_entropy(logits, labels_t)
        with torch.no_grad():
            reward = (logits.argmax(-1) == labels_t).float()
        adv = reward - baseline
        baseline = 0.95 * baseline + 0.05 * reward.mean().item()
        s_loss = -(logp * adv).mean() - cfg.entropy_coef * ent.mean()
        opt.zero_grad(); (r_loss + s_loss).backward(); opt.step()

        if bone is not None:
            bone.record(t, msgs.numpy(), reward.numpy().astype(bool))

        if step % cfg.eval_every == 0 or step == cfg.steps:
            s0, r0 = senders[0], receivers[0]
            lang = language_of(s0, world)
            rec = dict(
                gen=gen, step=step_offset + step, gen_step=step,
                train_acc=evaluate(s0, r0, world, cfg.n_distractors, "train"),
                test_acc=evaluate(s0, r0, world, cfg.n_distractors, "test"),
                topsim=topographic_similarity(world, lang),
                posdis=positional_disentanglement(world, lang),
                n_unique_msgs=int(len({tuple(m) for m in lang})),
                bone_size=(len(bone.entries) if bone is not None else None),
            )
            if step == cfg.steps:
                rec["language"] = lang.tolist()      # final language of the generation
            log.append(rec)
    return step_offset + cfg.steps


def transmit_oral(cfg, world, parent: Sender, child: Sender, objs):
    """Iterated learning: the child hears the parent name a SUBSET of objects
    (the bottleneck) and imitates. Nothing persists outside heads."""
    with torch.no_grad():
        target, _, _ = parent(world.encode(objs), greedy=True)
    _imitate(cfg, world, child, objs, target)


def transmit_bone(cfg, world, child: Sender, bone: Bone):
    """The child reads the external artifact: every entry ever carved, by anyone."""
    objs, msgs = bone.read()
    if objs is None:
        return
    _imitate(cfg, world, child, objs, torch.from_numpy(msgs))


def _imitate(cfg, world, child, objs, target):
    opt = torch.optim.Adam(child.parameters(), lr=cfg.lr * 3)
    x = world.encode(objs)
    for _ in range(cfg.transmit_steps):
        opt.zero_grad(); child.supervised_loss(x, target).backward(); opt.step()


def run(cfg: Config):
    rng = np.random.RandomState(cfg.seed)
    random.seed(cfg.seed); torch.manual_seed(cfg.seed)
    world = World(cfg.n_attrs, cfg.n_vals, cfg.holdout_frac, seed=cfg.seed)
    log: list[dict] = []
    off = 0

    if cfg.condition == "pair":
        s, r = make_agents(cfg, world, cfg.seed)
        cfg_one = Config(**{**cfg.__dict__, "steps": cfg.steps * cfg.generations})
        train_generation(cfg_one, world, [s], [r], rng, None, log, gen=0, step_offset=0)

    elif cfg.condition == "population":
        agents = [make_agents(cfg, world, cfg.seed * 100 + i) for i in range(cfg.population)]
        cfg_one = Config(**{**cfg.__dict__, "steps": cfg.steps * cfg.generations})
        train_generation(cfg_one, world, [a[0] for a in agents], [a[1] for a in agents],
                         rng, None, log, gen=0, step_offset=0)

    elif cfg.condition in ("generations", "oral", "oral_fixed", "bone", "bone_edition"):
        cap = cfg.n_transmit if cfg.bone_capacity < 0 else cfg.bone_capacity
        bone = Bone(cap) if cfg.condition.startswith("bone") else None
        fixed_objs = rng.choice(world.train_idx, size=cfg.n_transmit, replace=False)
        parent_s = None
        for g in range(cfg.generations):
            s, r = make_agents(cfg, world, cfg.seed * 100 + g)
            if g > 0:
                if cfg.condition == "oral":          # fresh random subset each generation
                    objs = rng.choice(world.train_idx, size=cfg.n_transmit, replace=False)
                    transmit_oral(cfg, world, parent_s, s, objs)
                elif cfg.condition == "oral_fixed":  # same subset every generation
                    transmit_oral(cfg, world, parent_s, s, fixed_objs)
                elif cfg.condition in ("bone", "bone_edition"):
                    transmit_bone(cfg, world, s, bone)
            off = train_generation(cfg, world, [s], [r], rng, bone, log, gen=g, step_offset=off)
            if cfg.condition == "bone_edition":
                bone.rewrite_from(s, world)
            parent_s = s
    else:
        raise ValueError(cfg.condition)

    return log

# ----------------------------------------------------------------------------
# Second architecture (v4): MLP agents with straight-through Gumbel-softmax, no REINFORCE, no entropy bonus
# ----------------------------------------------------------------------------
class GumbelSender(nn.Module):
    """Non-autoregressive MLP sender. forward() keeps the (msgs, logp, ent) interface; the straight-through one-hot
    sample of the last call is kept in .onehot so the receiver loss can back-propagate into the sender."""
    def __init__(self, in_dim, vocab, msg_len, hidden=64, tau=1.0):
        super().__init__()
        self.vocab, self.msg_len, self.hidden, self.tau = vocab, msg_len, hidden, tau
        self.net = nn.Sequential(nn.Linear(in_dim, hidden), nn.Tanh(), nn.Linear(hidden, hidden), nn.Tanh(), nn.Linear(hidden, msg_len * vocab))
        self.onehot = None

    def logits(self, x):
        return self.net(x).view(x.shape[0], self.msg_len, self.vocab)

    def forward(self, x, greedy=False):
        lg = self.logits(x); logp = F.log_softmax(lg, -1)
        if greedy:
            msgs = lg.argmax(-1); self.onehot = F.one_hot(msgs, self.vocab).float()
        else:
            y = F.gumbel_softmax(lg, tau=self.tau, hard=True); msgs = y.argmax(-1); self.onehot = y
        lp = logp.gather(2, msgs[..., None]).squeeze(-1).sum(1)
        ent = -(logp.exp() * logp).sum(-1).mean(1)
        return msgs, lp, ent

    def supervised_loss(self, x, target_msgs):
        lg = self.logits(x)
        return F.cross_entropy(lg.reshape(-1, self.vocab), target_msgs.reshape(-1))


class GumbelReceiver(nn.Module):
    """MLP receiver over one-hot messages; accepts integer messages too (converted to one-hot)."""
    def __init__(self, in_dim, vocab, msg_len, hidden=64):
        super().__init__()
        self.vocab, self.msg_len = vocab, msg_len
        self.msg_net = nn.Sequential(nn.Linear(msg_len * vocab, hidden), nn.Tanh(), nn.Linear(hidden, hidden))
        self.cand = nn.Linear(in_dim, hidden)

    def forward(self, msgs, cand_feats, onehot=None):
        if onehot is None:
            onehot = F.one_hot(msgs.long(), self.vocab).float()
        m = self.msg_net(onehot.reshape(onehot.shape[0], -1))
        c = self.cand(cand_feats)
        return torch.einsum("bh,bch->bc", m, c)
