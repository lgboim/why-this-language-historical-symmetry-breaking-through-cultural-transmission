"""
lab.py — v3: the factorial transmission-channel lab. One file, four jobs:

  1. A single `Cell` (channel spec) that spans every v2 condition AND the new axes, so
     "oral vs bone" becomes a table of orthogonal knobs instead of a list of named recipes:
        select   who decides which objects get recorded: random | success | hard | none
        slots    are the recorded objects fixed across generations or redrawn (random only)
        fresh    accumulate carved forms across generations, or rewrite from the parent's final language
        capacity how many (object, message) pairs the record holds
        noise    per-generation probability that an entry gets one symbol corrupted
        reader   only the child sender reads the record, or both sender and receiver
  2. Extended logging: every eval point stores the full sender language AND the receiver's
     decode map; every generation end stores per-object accuracy, the record contents, what was
     transmitted, and (optionally) both agents' weights. Run once, measure forever.
  3. A resumable parallel sweep over (world x cell x seed), with a pre-registration file
     written BEFORE the runs (hypotheses, decision rule, git hash).
  4. A pre-registered analysis: paired-by-seed main effects, interactions, hypothesis verdicts,
     replication of the v2 named conditions, and a main-effects figure.

    python lab.py list     [--worlds small big] [--grid full|reduced]      # dry run + time estimate
    python lab.py run      --out results_v3 --workers 4 [--seeds 0 1 ...]  # resumable
    python lab.py analyze  results_v3                                       # -> summary_v3.md + png
    python lab.py named    --out results_v3 --quick                          # the 7 v2 conditions only
    python lab.py run --out results_v3_confirm --seeds 10..29 --cells cap-19_noise-0.0_rd-sender __generations __pair
    python lab.py confirm  results_v3_confirm                               # C1-C6 on the new seeds

Seeds are shared across cells (same held-out split, same generation-0 init), so EVERY
comparison is paired by seed. Keep it that way.
"""
from __future__ import annotations
import argparse, glob, itertools, json, os, subprocess, sys, time, traceback
from collections import defaultdict
from dataclasses import dataclass, asdict, replace
from math import comb
from multiprocessing import Pool

import numpy as np
import torch
import torch.nn.functional as F

from game import World, Sender, Receiver, GumbelSender, GumbelReceiver, positional_disentanglement

# =============================================================================
# 1. Worlds and cells
# =============================================================================
WORLDS = {
    #            attrs vals vocab len  steps/gen  capacities (≈ 17%, 40%, 80% of the training set)
    "small": dict(n_attrs=3, n_vals=4, vocab=8, msg_len=3, steps=2000, caps=(8, 19, 40), mid=19),
    "big":   dict(n_attrs=4, n_vals=5, vocab=16, msg_len=4, steps=4000, caps=(80, 188, 375), mid=188),
    "medium": dict(n_attrs=4, n_vals=4, vocab=8, msg_len=4, steps=4000, caps=(32, 77, 154), mid=77),
}
SELECTS, FRESHES, READERS, NOISES = ("random", "success", "hard"), ("accumulate", "rewrite"), ("sender", "both"), (0.0, 0.2)


@dataclass(frozen=True)
class Cell:
    world: str = "small"
    mode: str = "gens"            # pair | population | gens
    select: str = "none"          # none | random | success | hard
    slots: str = "fixed"          # fixed | redraw | dynamic
    fresh: str = "rewrite"        # accumulate | rewrite
    capacity: int = 19
    noise: float = 0.0
    reader: str = "sender"        # sender | both

    def name(self) -> str:
        if self.mode != "gens":
            return f"{self.world}__{self.mode}"
        if self.select == "none":
            return f"{self.world}__generations"
        return (f"{self.world}__sel-{self.select}_slots-{self.slots}_fresh-{self.fresh}"
                f"_cap-{self.capacity}_noise-{self.noise}_rd-{self.reader}")

    @property
    def is_record(self) -> bool:
        return self.mode == "gens" and self.select != "none"


def named_cells(world: str) -> dict[str, Cell]:
    """The seven v2 conditions, expressed as cells."""
    mid = WORLDS[world]["mid"]
    return {
        "pair":         Cell(world, "pair"),
        "population":   Cell(world, "population"),
        "generations":  Cell(world, "gens"),
        "oral":         Cell(world, "gens", "random", "redraw", "rewrite", mid),
        "oral_fixed":   Cell(world, "gens", "random", "fixed", "rewrite", mid),
        "bone":         Cell(world, "gens", "success", "dynamic", "accumulate", mid),
        "bone_edition": Cell(world, "gens", "success", "dynamic", "rewrite", mid),
    }


def build_grid(world: str, kind: str) -> list[Cell]:
    W = WORLDS[world]; mid = W["mid"]
    cells = [Cell(world, "pair"), Cell(world, "population"), Cell(world, "gens")]
    caps, noises, readers = (W["caps"], NOISES, READERS) if kind == "full" else ((mid,), (0.0,), ("sender",))
    for cap, sel, fresh, noise, rd in itertools.product(caps, SELECTS, FRESHES, noises, readers):
        cells.append(Cell(world, "gens", sel, "fixed" if sel == "random" else "dynamic", fresh, cap, noise, rd))
    for fresh in FRESHES:                      # the 'oral' family: random subset REDRAWN each generation
        cells.append(Cell(world, "gens", "random", "redraw", fresh, mid, 0.0, "sender"))
    return cells


@dataclass
class RunCfg:
    cell: Cell
    seed: int = 0
    n_attrs: int = 3
    n_vals: int = 4
    vocab: int = 8
    msg_len: int = 3
    steps: int = 2000             # per generation
    generations: int = 6
    population: int = 4
    n_distractors: int = 4
    batch: int = 64
    hidden: int = 64
    lr: float = 1e-3
    entropy_coef: float = 0.02
    transmit_steps: int = 200
    holdout_frac: float = 0.25
    eval_every: int = 250
    save_weights: bool = True
    hard_frac: float = 0.0            # share of rounds with Hamming-1 distractors
    arch: str = "gru"                 # 'gru' (REINFORCE + entropy bonus) or 'gumbel' (MLP, straight-through Gumbel-softmax)


def make_cfg(cell: Cell, seed: int, **over) -> RunCfg:
    W = WORLDS[cell.world]
    kw = dict(n_attrs=W["n_attrs"], n_vals=W["n_vals"], vocab=W["vocab"], msg_len=W["msg_len"], steps=W["steps"])
    kw.update(over)
    return RunCfg(cell=cell, seed=seed, **kw)


# =============================================================================
# 2. Fast metrics (vectorised; identical values to game.py's, tested in tests.py)
# =============================================================================
def rank_avg(x):
    x = np.asarray(x, float)
    u, inv, cnt = np.unique(x, return_inverse=True, return_counts=True)
    start = np.cumsum(np.concatenate([[0], cnt[:-1]])) + 1
    return (start + (cnt - 1) / 2.0)[inv]


def spearman(a, b):
    ra, rb = rank_avg(a), rank_avg(b)
    ra = ra - ra.mean(); rb = rb - rb.mean()
    d = np.sqrt((ra ** 2).sum() * (rb ** 2).sum())
    return float((ra * rb).sum() / d) if d > 0 else 0.0


def topsim(objs: np.ndarray, msgs: np.ndarray) -> float:
    iu = np.triu_indices(len(objs), 1)
    od = (objs[:, None, :] != objs[None, :, :]).sum(-1)[iu]
    md = (msgs[:, None, :] != msgs[None, :, :]).sum(-1)[iu]
    return spearman(od, md)


@torch.no_grad()
def sender_language(sender, world):
    sender.eval()
    msgs, _, ents = sender(world.encode(np.arange(len(world.objects))), greedy=True)
    sender.train()
    return msgs, float(ents.mean())


@torch.no_grad()
def receiver_decode(receiver, world, msgs):
    """For each object's message, the object the receiver would pick among ALL objects."""
    receiver.eval()
    N = len(world.objects)
    feats = world.encode(np.arange(N))[None].expand(N, N, world.dim)
    dec = receiver(msgs, feats).argmax(-1).numpy()
    receiver.train()
    return dec


@torch.no_grad()
def accuracy(sender, receiver, world, k, split, n=512):
    sender.eval(); receiver.eval()
    rng = np.random.RandomState(123)
    t, cands, labels = world.sample_batch(n, k, split, rng)
    msgs = sender(world.encode(t), greedy=True)[0]
    logits = receiver(msgs, world.encode(cands.reshape(-1)).view(n, -1, world.dim))
    sender.train(); receiver.train()
    return float((logits.argmax(-1).numpy() == labels).mean())


@torch.no_grad()
def per_object_accuracy(sender, receiver, world, k, per_obj=32):
    """Balanced: every object is the target `per_obj` times with fresh distractors."""
    sender.eval(); receiver.eval()
    N = len(world.objects); rng = np.random.RandomState(321)
    targets = np.repeat(np.arange(N), per_obj)
    cands, labels = world.candidates(targets, k, rng)
    msgs = sender(world.encode(targets), greedy=True)[0]
    logits = receiver(msgs, world.encode(cands.reshape(-1)).view(len(targets), -1, world.dim))
    correct = (logits.argmax(-1).numpy() == labels).astype(float)
    sender.train(); receiver.train()
    return correct.reshape(N, per_obj).mean(1)


# =============================================================================
# 3. The record — one class for every transmission channel
# =============================================================================
class Record:
    """A capacity-limited store of (object, message) pairs that lives outside any head.
    `select` decides which objects may occupy it, `fresh` whether carved forms persist or
    are re-carved from the parent's final language, `noise` erodes it between generations."""

    def __init__(self, cell: Cell, world: World, vocab: int, rng: np.random.RandomState):
        self.c, self.world, self.vocab, self.rng = cell, world, vocab, rng
        self.entries: dict[int, tuple] = {}
        self.succ: dict[int, int] = {}
        # slot_set: None = open (success decides), set() = closed until end-of-generation selection
        self.slot_set = None
        if cell.select == "random":
            self.slot_set = self._draw()
        elif cell.select == "hard":
            self.slot_set = set()

    def _draw(self):
        return {int(o) for o in self.rng.choice(self.world.train_idx, self.c.capacity, replace=False)}

    def observe(self, objs, msgs, ok):
        """During training: successful pairs are carved in (incumbent rule from v2's Bone)."""
        if self.c.select == "none":
            return
        cap = self.c.capacity
        for o, m, k in zip(objs, msgs, ok):
            if not k:
                continue
            o = int(o); m = tuple(int(s) for s in m)
            if self.slot_set is not None and o not in self.slot_set:
                continue
            if o in self.entries and self.entries[o] == m:
                self.succ[o] += 1
            elif o in self.entries:
                if self.succ[o] < 2:                       # weak incumbent -> replaced
                    self.entries[o], self.succ[o] = m, 1
            elif len(self.entries) < cap:
                self.entries[o], self.succ[o] = m, 1
            else:
                weakest = min(self.succ, key=self.succ.get)
                if self.succ[weakest] < 2:
                    del self.entries[weakest]; del self.succ[weakest]
                    self.entries[o], self.succ[o] = m, 1

    def end_of_generation(self, lang: np.ndarray, per_obj_acc: np.ndarray):
        """Prepare what the NEXT generation will read."""
        c = self.c
        if c.select == "none":
            return
        tr = self.world.train_idx
        # (1) slots
        if c.select == "random" and c.slots == "redraw":
            self.slot_set = self._draw()
        elif c.select == "hard":
            order = np.lexsort((self.rng.rand(len(tr)), per_obj_acc[tr]))      # lowest accuracy first
            self.slot_set = {int(o) for o in tr[order[:c.capacity]]}
        if self.slot_set is not None:
            for o in [o for o in self.entries if o not in self.slot_set]:
                del self.entries[o]; del self.succ[o]
            fill = sorted(o for o in self.slot_set if o not in self.entries)
        else:                                                                    # success: fill spare capacity
            spare = c.capacity - len(self.entries)
            pool = [int(o) for o in tr if int(o) not in self.entries]
            fill = [int(o) for o in self.rng.choice(pool, spare, replace=False)] if spare > 0 else []
        for o in fill:
            self.entries[o], self.succ[o] = tuple(int(s) for s in lang[o]), 1
        # (2) freshness
        if c.fresh == "rewrite":
            for o in self.entries:
                self.entries[o], self.succ[o] = tuple(int(s) for s in lang[o]), 1
        # (3) erosion
        if c.noise > 0:
            for o in list(self.entries):
                if self.rng.rand() < c.noise:
                    m = list(self.entries[o]); p = self.rng.randint(len(m))
                    m[p] = int(self.rng.randint(self.vocab))
                    self.entries[o], self.succ[o] = tuple(m), 1

    def read(self):
        if not self.entries:
            return None, None
        objs = np.array(sorted(self.entries))
        return objs, np.array([self.entries[int(o)] for o in objs])

    def snapshot(self):
        return [[int(o), list(self.entries[o]), int(self.succ[o])] for o in sorted(self.entries)]


# =============================================================================
# 4. Training with extended logging
# =============================================================================
def make_agents(cfg, world, seed):
    torch.manual_seed(seed)
    if cfg.arch == "gumbel":
        return GumbelSender(world.dim, cfg.vocab, cfg.msg_len, cfg.hidden), GumbelReceiver(world.dim, cfg.vocab, cfg.msg_len, cfg.hidden)
    return Sender(world.dim, cfg.vocab, cfg.msg_len, cfg.hidden), Receiver(world.dim, cfg.vocab, cfg.hidden)


def teach_sender(cfg, world, child, objs, msgs):
    opt = torch.optim.Adam(child.parameters(), lr=cfg.lr * 3)
    x, target = world.encode(objs), torch.as_tensor(msgs, dtype=torch.long)
    for _ in range(cfg.transmit_steps):
        opt.zero_grad(); child.supervised_loss(x, target).backward(); opt.step()


def teach_receiver(cfg, world, child: Receiver, objs, msgs, rng):
    """The child receiver also 'reads the bone': learns to pick the recorded object from distractors."""
    opt = torch.optim.Adam(child.parameters(), lr=cfg.lr * 3)
    m = torch.as_tensor(msgs, dtype=torch.long)
    for _ in range(cfg.transmit_steps):
        cands, labels = world.candidates(objs, cfg.n_distractors, rng)
        logits = child(m, world.encode(cands.reshape(-1)).view(len(objs), -1, world.dim))
        opt.zero_grad(); F.cross_entropy(logits, torch.from_numpy(labels)).backward(); opt.step()


def snapshot(cfg, world, s, r, record, gen, step, gen_step, final: bool):
    msgs_t, ent = sender_language(s, world)
    lang = msgs_t.numpy()
    dec = receiver_decode(r, world, msgs_t)
    rec = dict(
        gen=gen, step=step, gen_step=gen_step,
        train_acc=accuracy(s, r, world, cfg.n_distractors, "train"),
        test_acc=accuracy(s, r, world, cfg.n_distractors, "test"),
        topsim=topsim(world.objects, lang),
        posdis=positional_disentanglement(world, lang),
        n_unique_msgs=int(len({tuple(m) for m in lang})),
        msg_entropy=ent,
        intelligibility=float((dec == np.arange(len(dec))).mean()),
        record_size=(len(record.entries) if record is not None else None),
        language=lang.tolist(),
        decode=dec.tolist(),
    )
    if final:
        pacc = per_object_accuracy(s, r, world, cfg.n_distractors)
        rec["per_obj_acc"] = pacc.round(4).tolist()
        rec["_pacc"] = pacc                      # stripped before saving
    return rec


def train_generation(cfg, world, senders, receivers, rng, record, log, gen, off, n_steps):
    params = [p for a in senders + receivers for p in a.parameters()]
    opt = torch.optim.Adam(params, lr=cfg.lr, foreach=True)
    baseline = 0.0
    for step in range(1, n_steps + 1):
        s = senders[rng.randint(len(senders))]; r = receivers[rng.randint(len(receivers))]
        t, cands, labels = world.sample_batch(cfg.batch, cfg.n_distractors, "train", rng)
        msgs, logp, ent = s(world.encode(t))
        feats = world.encode(cands.reshape(-1)).view(cfg.batch, -1, world.dim)
        logits = r(msgs, feats, onehot=s.onehot) if cfg.arch == "gumbel" else r(msgs, feats)
        labels_t = torch.from_numpy(labels)
        r_loss = F.cross_entropy(logits, labels_t)
        with torch.no_grad():
            reward = (logits.argmax(-1) == labels_t).float()
        if cfg.arch == "gumbel":
            opt.zero_grad(); r_loss.backward(); opt.step()          # gradient reaches the sender through the straight-through one-hot
        else:
            adv = reward - baseline
            baseline = 0.95 * baseline + 0.05 * reward.mean().item()
            s_loss = -(logp * adv).mean() - cfg.entropy_coef * ent.mean()
            opt.zero_grad(); (r_loss + s_loss).backward(); opt.step()
        if record is not None:
            record.observe(t, msgs.numpy(), reward.numpy().astype(bool))
        if step % cfg.eval_every == 0 or step == n_steps:
            log.append(snapshot(cfg, world, senders[0], receivers[0], record, gen, off + step, step, step == n_steps))
    return off + n_steps


def run_cell(cfg: RunCfg):
    """Returns (log, weights). Deterministic given cfg."""
    cell = cfg.cell
    rng = np.random.RandomState(cfg.seed); torch.manual_seed(cfg.seed)
    world = World(cfg.n_attrs, cfg.n_vals, cfg.holdout_frac, seed=cfg.seed); world.hard_frac = cfg.hard_frac
    log, weights = [], []

    def agents(seed):
        return make_agents(cfg, world, seed)

    if cell.mode in ("pair", "population"):
        n = 1 if cell.mode == "pair" else cfg.population
        ag = [agents(cfg.seed * 100 + i) for i in range(n)]
        train_generation(cfg, world, [a[0] for a in ag], [a[1] for a in ag], rng, None, log, 0, 0,
                         cfg.steps * cfg.generations)
        if cfg.save_weights:
            weights.append(dict(sender=ag[0][0].state_dict(), receiver=ag[0][1].state_dict()))
        return _strip(log), weights

    # the record gets its OWN rng stream so that the training stream (batches, pairings) is
    # identical across cells for a given seed -> generation 0 is bit-identical everywhere
    record = Record(cell, world, cfg.vocab, np.random.RandomState(cfg.seed + 7919)) if cell.select != "none" else None
    off = 0
    for g in range(cfg.generations):
        s, r = agents(cfg.seed * 100 + g)
        taught = None
        if g > 0 and record is not None:
            objs, msgs = record.read()
            if objs is not None:
                teach_sender(cfg, world, s, objs, msgs)
                if cell.reader == "both":
                    teach_receiver(cfg, world, r, objs, msgs, record.rng)
                taught = objs.tolist()
        off = train_generation(cfg, world, [s], [r], rng, record, log, g, off, cfg.steps)
        fin = log[-1]
        fin["transmitted_objs"] = taught
        if record is not None:
            record.end_of_generation(np.array(fin["language"]), fin["_pacc"])
            fin["record"] = record.snapshot()
            fin["slot_set"] = sorted(record.slot_set) if record.slot_set is not None else None
        if cfg.save_weights:
            weights.append(dict(sender=s.state_dict(), receiver=r.state_dict()))
    return _strip(log), weights


def _strip(log):
    for r in log:
        r.pop("_pacc", None)
    return log


def cfg_to_json(cfg: RunCfg):
    d = asdict(cfg); d["cell"] = asdict(cfg.cell); return d


def cfg_from_json(d):
    d = dict(d); d["cell"] = Cell(**d["cell"]); return RunCfg(**d)


# =============================================================================
# 5. Sweep
# =============================================================================
def _job(args):
    cell, seed, out, over = args
    torch.set_num_threads(1)
    cfg = make_cfg(cell, seed, **over)
    path = os.path.join(out, f"{cell.name()}_seed{seed}")
    if os.path.exists(path + ".json"):
        return f"skip   {os.path.basename(path)}"
    t0 = time.time()
    try:
        log, weights = run_cell(cfg)
    except Exception:
        return f"FAIL   {os.path.basename(path)}\n{traceback.format_exc()}"
    if weights:
        torch.save(weights, path + ".pt")
    with open(path + ".json.tmp", "w") as f:
        json.dump({"config": cfg_to_json(cfg), "log": log}, f)
    os.replace(path + ".json.tmp", path + ".json")        # atomic: no half-written files on Ctrl-C
    l = log[-1]
    return (f"done   {os.path.basename(path):70s} test={l['test_acc']:.2f} topsim={l['topsim']:.3f} "
            f"uniq={l['n_unique_msgs']:3d} intel={l['intelligibility']:.2f} ({time.time()-t0:.0f}s)")


def git_hash():
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
    except Exception:
        return "n/a"


def write_prereg(out, cells, seeds, over):
    p = os.path.join(out, "PREREG.md")
    if os.path.exists(p):
        return
    L = [f"# Pre-registration — v3 factorial sweep", "",
         f"Written {time.strftime('%Y-%m-%d %H:%M')} at commit `{git_hash()}` BEFORE any run in this directory.", "",
         f"Seeds: {seeds}. Cells: {len(cells)}. Overrides: {over or 'none'}.", "",
         "## Decision rule (fixed in advance)",
         f"A directional hypothesis is SUPPORTED if the paired-by-seed difference is in the predicted direction in at least "
         f"{int(SUPPORT_FRAC*100)}% of seeds AND the bootstrap 95% CI of the mean difference excludes 0. It is REFUTED if the "
         f"opposite direction meets the same bar. Otherwise INCONCLUSIVE. No verdict below {MIN_SEEDS} seeds. Pairing: each record cell is matched to the cell that "
         "differs only in the factor under test; per-seed differences are averaged over matched pairs before testing.", "",
         "## Hypotheses"]
    for h in HYPOTHESES:
        L.append(f"- **{h['id']}** ({h['metric']}): {h['title']}")
    L += ["", "## Cells", ""] + [f"- `{c.name()}`" for c in cells]
    open(p, "w").write("\n".join(L) + "\n")


def cmd_run(a):
    os.makedirs(a.out, exist_ok=True)
    cells = [c for w in a.worlds for c in build_grid(w, a.grid)]
    if a.cells:                                   # keep only cells whose name contains one of the substrings
        cells = [c for c in cells if any(sub in c.name() for sub in a.cells)]
        if not cells:
            sys.exit("no cells match --cells")
    over = {}
    if a.quick:
        over.update(steps=300, generations=2, eval_every=100, transmit_steps=20)
    if a.steps: over["steps"] = a.steps
    if a.no_weights: over["save_weights"] = False
    if a.entropy_coef is not None: over["entropy_coef"] = a.entropy_coef
    if a.hard_frac is not None: over["hard_frac"] = a.hard_frac
    if a.arch is not None: over["arch"] = a.arch
    write_prereg(a.out, cells, a.seeds, over)
    jobs = [(c, s, a.out, over) for s in a.seeds for c in cells]
    todo = [j for j in jobs if not os.path.exists(os.path.join(a.out, f"{j[0].name()}_seed{j[1]}.json"))]
    print(f"{len(jobs)} jobs, {len(todo)} to run, {a.workers} workers -> {a.out}/", flush=True)
    t0, n = time.time(), 0
    with Pool(a.workers) as pool:
        for msg in pool.imap_unordered(_job, todo):
            n += 1
            el = time.time() - t0
            eta = el / n * (len(todo) - n)
            print(f"[{n}/{len(todo)} eta {eta/60:.0f}m] {msg}", flush=True)


def cmd_named(a):
    """Run only the seven v2 conditions (as cells) — a quick replication check."""
    os.makedirs(a.out, exist_ok=True)
    over = dict(steps=300, generations=2, eval_every=100, transmit_steps=20) if a.quick else {}
    if a.no_weights: over["save_weights"] = False
    jobs = [(c, s, a.out, over) for s in a.seeds for w in a.worlds for c in named_cells(w).values()]
    with Pool(a.workers) as pool:
        for msg in pool.imap_unordered(_job, jobs):
            print(msg, flush=True)


def cmd_list(a):
    for w in a.worlds:
        cells = build_grid(w, a.grid)
        sec = a.sec_per_run * (1 if w == "small" else a.big_factor)
        hrs = len(cells) * len(a.seeds) * sec / a.workers / 3600
        print(f"{w}: {len(cells)} cells x {len(a.seeds)} seeds = {len(cells)*len(a.seeds)} runs "
              f"≈ {hrs:.1f} h with {a.workers} workers at {sec:.0f}s/run")
        for c in cells:
            print("   ", c.name())


# =============================================================================
# 6. Pre-registered analysis
# =============================================================================
SUPPORT_FRAC = 0.8
MIN_SEEDS = 8          # no verdict is issued below this: a 3-seed "trend" killed a v1 headline
HYPOTHESES = [
    dict(id="H1", metric="topsim", title="Selection: random slots beat success-selected slots (the v2 surprise is about WHAT gets recorded)",
         kind="factor", factor="select", a="random", b="success", direction=">"),
    dict(id="H2", metric="topsim", title="Capacity: a smaller record yields a more compositional language (bottleneck = structure)",
         kind="slope", factor="capacity", direction="<"),
    dict(id="H3", metric="topsim", title="Freshness: rewriting from the final language beats accumulating carved forms",
         kind="factor", factor="fresh", a="rewrite", b="accumulate", direction=">"),
    dict(id="H4", metric="topsim", title="Erosion repairs an accumulating record: noise raises topsim when forms accumulate",
         kind="factor", factor="noise", a=0.2, b=0.0, direction=">", restrict=dict(fresh="accumulate")),
    dict(id="H5", metric="test_acc", title="A record both agents read changes held-out accuracy (direction unknown)",
         kind="factor", factor="reader", a="both", b="sender", direction="?"),
    dict(id="H6", metric="n_unique_msgs", title="Every bottlenecked record compresses the lexicon vs no transmission",
         kind="control", direction="<"),
    dict(id="H7", metric="topsim", title="v2 replication: oral_fixed beats bone_edition",
         kind="named", a="oral_fixed", b="bone_edition", direction=">"),
    dict(id="H8", metric="test_acc", title="Recording the HARD objects helps held-out accuracy more than random objects",
         kind="factor", factor="select", a="hard", b="random", direction=">"),
    dict(id="H9", metric="intelligibility", title="Rewritten records are more mutually intelligible than accumulated ones",
         kind="factor", factor="fresh", a="rewrite", b="accumulate", direction=">"),
]
FACTORS = ["select", "fresh", "capacity", "noise", "reader"]
METRICS = ["topsim", "test_acc", "n_unique_msgs", "intelligibility", "train_acc"]


def sign_test(d):
    d = np.asarray(d); d = d[d != 0]
    n, k = len(d), int((d > 0).sum())
    if n == 0:
        return 1.0
    p1 = sum(comb(n, i) for i in range(max(k, n - k), n + 1)) / 2 ** n
    return min(1.0, 2 * p1)


def boot_ci(d, B=5000, seed=0):
    d = np.asarray(d, float); rng = np.random.RandomState(seed)
    m = np.array([rng.choice(d, len(d)).mean() for _ in range(B)])
    return float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))


def load_runs(out):
    runs = {}                                    # (cell, seed) -> final record (+ a few series)
    for p in sorted(glob.glob(os.path.join(out, "*_seed*.json"))):
        d = json.load(open(p)); cfg = cfg_from_json(d["config"])
        fin = dict(d["log"][-1]); fin["_series"] = [(r["gen"], r["topsim"]) for r in d["log"] if "per_obj_acc" in r]
        runs[(cfg.cell, cfg.seed)] = fin
    return runs


def stats_line(diffs, direction):
    d = np.asarray(diffs, float)
    lo, hi = boot_ci(d)
    wins = int((d > 0).sum()); n = len(d)
    verdict = ""
    if n < MIN_SEEDS:
        verdict = f"UNDERPOWERED (n<{MIN_SEEDS})"
    elif direction in (">", "<"):
        want = d if direction == ">" else -d
        frac = (want > 0).mean()
        ci_ok = (lo > 0) if direction == ">" else (hi < 0)
        ci_opp = (hi < 0) if direction == ">" else (lo > 0)
        if frac >= SUPPORT_FRAC and ci_ok: verdict = "SUPPORTED"
        elif (1 - frac) >= SUPPORT_FRAC and ci_opp: verdict = "REFUTED"
        else: verdict = "INCONCLUSIVE"
    else:
        verdict = "TWO-SIDED: " + ("A>B" if lo > 0 else "A<B" if hi < 0 else "no difference") + " (CI)"
    return dict(n=n, wins=wins, losses=int((d < 0).sum()), mean=float(d.mean()), lo=lo, hi=hi,
                p=sign_test(d), verdict=verdict)


def fmt(s):
    return f"| {s['n']} | {s['wins']}/{s['losses']} | {s['mean']:+.3f} | [{s['lo']:+.3f}, {s['hi']:+.3f}] | {s['p']:.3f} | {s['verdict']} |"


def factor_diffs(runs, world, metric, factor, a, b, restrict=None):
    """Per-seed mean of metric(cell with factor=a) − metric(matched cell with factor=b)."""
    def matches(c):
        return (c.world == world and c.is_record and c.slots != "redraw"
                and all(getattr(c, k) == v for k, v in (restrict or {}).items()))
    per_seed = defaultdict(list)
    for (c, s), fin in runs.items():
        if not matches(c) or getattr(c, factor) != a:
            continue
        kw = {factor: b}
        if factor == "select":                                        # slots is tied to select
            kw["slots"] = "fixed" if b == "random" else "dynamic"
        twin = replace(c, **kw)
        if (twin, s) in runs:
            per_seed[s].append(fin[metric] - runs[(twin, s)][metric])
    return {s: float(np.mean(v)) for s, v in per_seed.items()}


def capacity_slopes(runs, world, metric):
    """Per-seed mean slope of metric vs log2(capacity) over matched groups."""
    groups = defaultdict(dict)
    for (c, s), fin in runs.items():
        if c.world == world and c.is_record and c.slots != "redraw":
            groups[(s, replace(c, capacity=0))][c.capacity] = fin[metric]
    per_seed = defaultdict(list)
    for (s, _), d in groups.items():
        if len(d) >= 3:
            x = np.log2(sorted(d)); y = [d[k] for k in sorted(d)]
            per_seed[s].append(np.polyfit(x, y, 1)[0])
    return {s: float(np.mean(v)) for s, v in per_seed.items()}


def control_diffs(runs, world, metric):
    ctrl = Cell(world, "gens")
    per_seed = defaultdict(list)
    for (c, s), fin in runs.items():
        if c.world == world and c.is_record and (ctrl, s) in runs:
            per_seed[s].append(fin[metric] - runs[(ctrl, s)][metric])
    cells_neg = [d < 0 for v in per_seed.values() for d in v]
    return {s: float(np.mean(v)) for s, v in per_seed.items()}, (float(np.mean(cells_neg)) if cells_neg else float("nan"))


def analyze(out):
    runs = load_runs(out)
    if not runs:
        sys.exit("no runs found")
    worlds = sorted({c.world for c, _ in runs})
    L = ["# v3 factorial sweep — summary", "",
         f"Runs: {len(runs)}. Worlds: {worlds}. Seeds: {sorted({s for _, s in runs})}.",
         f"Pre-registered hypotheses and the decision rule are in `{os.path.join(out, 'PREREG.md')}`.", ""]

    for world in worlds:
        R = {k: v for k, v in runs.items() if k[0].world == world}
        seeds = sorted({s for _, s in R})
        L += [f"# World: {world}", ""]

        # ---- hypotheses -----------------------------------------------------------
        L += ["## Pre-registered hypotheses", "",
              "| id | hypothesis | metric | n seeds | wins/losses | mean diff | 95% CI | p | verdict |",
              "|---|---|---|---|---|---|---|---|---|"]
        for h in HYPOTHESES:
            if h["kind"] == "factor":
                d = factor_diffs(runs, world, h["metric"], h["factor"], h["a"], h["b"], h.get("restrict"))
            elif h["kind"] == "slope":
                d = capacity_slopes(runs, world, h["metric"])
            elif h["kind"] == "control":
                d, frac = control_diffs(runs, world, h["metric"])
            elif h["kind"] == "named":
                nc = named_cells(world); d = {}
                for s in seeds:
                    if (nc[h["a"]], s) in runs and (nc[h["b"]], s) in runs:
                        d[s] = runs[(nc[h["a"]], s)][h["metric"]] - runs[(nc[h["b"]], s)][h["metric"]]
            if len(d) < 2:
                L.append(f"| {h['id']} | {h['title']} | {h['metric']} | – | – | – | – | – | NOT TESTABLE (cells missing) |")
                continue
            st = stats_line(list(d.values()), h["direction"])
            extra = f" ({frac*100:.0f}% of cell×seed below control)" if h["kind"] == "control" else ""
            L.append(f"| {h['id']} | {h['title']}{extra} | {h['metric']} " + fmt(st))
        L.append("")

        # ---- main effects -----------------------------------------------------------
        L += ["## Main effects (paired by seed, averaged over all other factors; A − B)", ""]
        for metric in ["topsim", "test_acc", "n_unique_msgs", "intelligibility"]:
            L += [f"### {metric}", "", "| factor | A | B | n | wins/losses | mean diff | 95% CI | p | |", "|---|---|---|---|---|---|---|---|---|"]
            for f in FACTORS:
                levels = sorted({getattr(c, f) for c, _ in R if c.is_record and c.slots != "redraw"})
                for a, b in itertools.combinations(levels, 2):
                    d = factor_diffs(runs, world, metric, f, a, b)
                    if len(d) >= 2:
                        L.append(f"| {f} | {a} | {b} " + fmt(stats_line(list(d.values()), "?")))
            L.append("")

        # ---- interactions -------------------------------------------------------------
        L += ["## Interactions (cell means of topsim over seeds and remaining factors)", ""]
        for f1, f2 in [("select", "fresh"), ("select", "capacity"), ("fresh", "noise"), ("select", "reader"), ("fresh", "reader"), ("capacity", "noise")]:
            tab = defaultdict(list)
            for (c, s), fin in R.items():
                if c.is_record and c.slots != "redraw":
                    tab[(getattr(c, f1), getattr(c, f2))].append(fin["topsim"])
            if not tab:
                continue
            l1 = sorted({k[0] for k in tab}); l2 = sorted({k[1] for k in tab})
            L += [f"### {f1} × {f2}", "", "| " + f1 + " \\ " + f2 + " | " + " | ".join(map(str, l2)) + " |", "|---|" + "---|" * len(l2)]
            for x in l1:
                L.append(f"| {x} | " + " | ".join(f"{np.mean(tab[(x, y)]):.3f}" if (x, y) in tab else "–" for y in l2) + " |")
            L.append("")

        # ---- v2 named conditions --------------------------------------------------------
        nc = named_cells(world)
        present = [n for n, c in nc.items() if any(k[0] == c for k in R)]
        if present:
            L += ["## The v2 named conditions, as cells", "", "| condition | " + " | ".join(METRICS) + " |", "|---|" + "---|" * len(METRICS)]
            for n in present:
                vals = [R[(nc[n], s)] for s in seeds if (nc[n], s) in R]
                L.append(f"| {n} | " + " | ".join(f"{np.mean([v[m] for v in vals]):.3f} ± {np.std([v[m] for v in vals], ddof=1) if len(vals) > 1 else 0:.3f}" for m in METRICS) + " |")
            L += ["", "| A | B | metric | n | wins/losses | mean diff | 95% CI | p | |", "|---|---|---|---|---|---|---|---|---|"]
            for a, b, m in [("oral_fixed", "bone_edition", "topsim"), ("bone", "bone_edition", "topsim"), ("oral_fixed", "pair", "topsim"),
                            ("oral", "oral_fixed", "topsim"), ("oral_fixed", "bone", "topsim"), ("oral", "pair", "test_acc"), ("population", "pair", "topsim")]:
                if a in present and b in present:
                    d = [R[(nc[a], s)][m] - R[(nc[b], s)][m] for s in seeds if (nc[a], s) in R and (nc[b], s) in R]
                    if len(d) >= 2:
                        L.append(f"| {a} | {b} | {m} " + fmt(stats_line(d, "?")))
            L.append("")

        # ---- leaderboard ------------------------------------------------------------------
        cells = sorted({c for c, _ in R}, key=lambda c: -np.mean([R[(c, s)]["topsim"] for s in seeds if (c, s) in R]))
        L += ["## All cells ranked by topsim (mean ± sd over seeds)", "", "| cell | n | topsim | test_acc | n_unique | intelligibility |", "|---|---|---|---|---|---|"]
        for c in cells:
            v = [R[(c, s)] for s in seeds if (c, s) in R]
            L.append(f"| `{c.name().split('__', 1)[1]}` | {len(v)} | " + " | ".join(
                f"{np.mean([x[m] for x in v]):.3f} ± {np.std([x[m] for x in v], ddof=1) if len(v) > 1 else 0:.3f}"
                for m in ["topsim", "test_acc", "n_unique_msgs", "intelligibility"]) + " |")
        L.append("")

    path = os.path.join(out, "summary_v3.md")
    open(path, "w").write("\n".join(L) + "\n")
    print("\n".join(L)); print("wrote", path)
    _figure(runs, worlds, out)


def _figure(runs, worlds, out):
    try:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not installed; skipped figure"); return
    metrics = ["topsim", "test_acc", "n_unique_msgs", "intelligibility"]
    for world in worlds:
        fig, axes = plt.subplots(len(metrics), len(FACTORS), figsize=(3.2 * len(FACTORS), 2.6 * len(metrics)), squeeze=False)
        for i, m in enumerate(metrics):
            for j, f in enumerate(FACTORS):
                ax = axes[i, j]
                per = defaultdict(lambda: defaultdict(list))         # level -> seed -> values
                for (c, s), fin in runs.items():
                    if c.world == world and c.is_record and c.slots != "redraw":
                        per[getattr(c, f)][s].append(fin[m])
                levels = sorted(per)
                means = [np.mean([np.mean(v) for v in per[l].values()]) for l in levels]
                ses = [np.std([np.mean(v) for v in per[l].values()], ddof=1) / np.sqrt(len(per[l])) if len(per[l]) > 1 else 0 for l in levels]
                ax.errorbar(range(len(levels)), means, yerr=ses, fmt="o-", capsize=3)
                ax.set_xticks(range(len(levels))); ax.set_xticklabels([str(l) for l in levels], fontsize=8)
                if i == 0: ax.set_title(f, fontsize=10)
                if j == 0: ax.set_ylabel(m, fontsize=9)
        fig.suptitle(f"{world}: main effects (mean ± s.e. over seeds; other factors averaged)")
        plt.tight_layout(); p = os.path.join(out, f"main_effects_{world}.png"); plt.savefig(p, dpi=120); plt.close(fig)
        print("saved", p)


# ---- confirmation analysis (seeds 10-29, cells at cap 19 / noise 0 / reader sender) ----------
def confirm(out):
    runs = load_runs(out)
    world = "small"
    def cell(sel, fresh):
        return Cell(world, "gens", sel, "fixed" if sel == "random" else "dynamic", fresh, WORLDS[world]["mid"], 0.0, "sender")
    seeds = sorted({s for _, s in runs})
    def diff(a, b, m):
        return [runs[(a, s)][m] - runs[(b, s)][m] for s in seeds if (a, s) in runs and (b, s) in runs]
    H, R, S = cell("hard", "rewrite"), cell("random", "rewrite"), cell("success", "rewrite")
    G = Cell(world, "gens")
    tests = [
        ("C1", "hard+rewrite > random+rewrite", "topsim", diff(H, R, "topsim"), ">"),
        ("C2", "hard+rewrite > random+rewrite", "test_acc", diff(H, R, "test_acc"), ">"),
        ("C3", "hard+rewrite > success+rewrite (bone_edition)", "test_acc", diff(H, S, "test_acc"), ">"),
        ("C4", "bone_edition > bone (rewrite > accumulate, success slots)", "topsim", diff(S, cell("success", "accumulate"), "topsim"), ">"),
        ("C5", "oral_fixed vs bone_edition", "topsim", diff(R, S, "topsim"), "?"),
    ]
    for sel, fresh in itertools.product(SELECTS, FRESHES):
        tests.append((f"C6 {sel}+{fresh}", "record cell vs generations (no transmission)", "topsim", diff(cell(sel, fresh), G, "topsim"), "?"))
    L = [f"# Confirmation on seeds {seeds[0]}–{seeds[-1]} (n={len(seeds)}) — `{out}`", "",
         "| id | test | metric | n | wins/losses | mean diff | 95% CI | p | verdict |", "|---|---|---|---|---|---|---|---|---|"]
    for i, title, m, d, direction in tests:
        if len(d) < 2:
            L.append(f"| {i} | {title} | {m} | – | – | – | – | – | NOT TESTABLE |"); continue
        L.append(f"| {i} | {title} | {m} " + fmt(stats_line(d, direction)))
    L += ["", "| cell | " + " | ".join(METRICS) + " |", "|---|" + "---|" * len(METRICS)]
    for c in sorted({c for c, _ in runs}, key=lambda c: c.name()):
        v = [runs[(c, s)] for s in seeds if (c, s) in runs]
        L.append(f"| `{c.name().split('__', 1)[1]}` | " + " | ".join(
            f"{np.mean([x[m] for x in v]):.3f} ± {np.std([x[m] for x in v], ddof=1) if len(v) > 1 else 0:.3f}" for m in METRICS) + " |")
    path = os.path.join(out, "confirmation.md")
    open(path, "w").write("\n".join(L) + "\n"); print("\n".join(L)); print("wrote", path)


# =============================================================================
if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("run", "list", "named"):
        p = sub.add_parser(name)
        p.add_argument("--out", default="results_v3")
        p.add_argument("--worlds", nargs="+", default=["small"], choices=list(WORLDS))
        p.add_argument("--grid", default="full", choices=["full", "reduced"])
        p.add_argument("--seeds", nargs="+", type=int, default=list(range(10)))
        p.add_argument("--workers", type=int, default=4)
        p.add_argument("--quick", action="store_true", help="tiny smoke run (300 steps x 2 generations)")
        p.add_argument("--steps", type=int, default=None, help="override steps per generation")
        p.add_argument("--no_weights", action="store_true")
        p.add_argument("--entropy_coef", type=float, default=None, help="override the sender entropy bonus (default 0.02)")
        p.add_argument("--hard_frac", type=float, default=None, help="share of rounds whose distractors are Hamming-1 neighbours of the target")
        p.add_argument("--arch", default=None, choices=["gru", "gumbel"], help="agent architecture / learning rule")
        p.add_argument("--cells", nargs="+", default=None, help="(run) only cells whose name contains any of these substrings")
        p.add_argument("--sec_per_run", type=float, default=90.0, help="(list) calibration: seconds per small-world run")
        p.add_argument("--big_factor", type=float, default=6.0, help="(list) big-world runs are this much slower")
    p = sub.add_parser("analyze"); p.add_argument("out", nargs="?", default="results_v3")
    p = sub.add_parser("confirm"); p.add_argument("out", nargs="?", default="results_v3_confirm")
    a = ap.parse_args()
    {"run": cmd_run, "list": cmd_list, "named": cmd_named, "analyze": lambda a: analyze(a.out),
     "confirm": lambda a: confirm(a.out)}[a.cmd](a)
