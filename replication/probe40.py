"""probe40.py — K14 on NEW seeds 30-44: train a fresh parent (gen 0, 2000 steps) per seed, then the five content rules of probe32.
   python probe40.py -> results_v3_confirm2/k14.md"""
import json, os, itertools
import numpy as np, torch
from multiprocessing import Pool
from collections import defaultdict
from scipy.optimize import linear_sum_assignment
from game import World, Sender, Receiver
from lab import Cell, make_cfg, teach_sender, train_generation, stats_line, fmt, spearman
GENS = Cell("small", "gens"); N = 64; IU = np.triu_indices(N, 1); ARMS = ("random19", "owners19", "orphans19", "classes19", "stable19"); SEEDS = list(range(30, 45))
def choose(arm, world, lang, dec, hist, rng):
    tr = np.array(world.train_idx); own = dec == np.arange(N); tro = tr[own[tr]]; trr = tr[~own[tr]]
    if arm == "random19": return rng.choice(tr, 19, replace=False)
    if arm == "owners19": return rng.choice(tro, 19, replace=False) if len(tro) >= 19 else np.concatenate([tro, rng.choice(trr, 19 - len(tro), replace=False)])
    if arm == "orphans19": return rng.choice(trr, 19, replace=False) if len(trr) >= 19 else np.concatenate([trr, rng.choice(tro, 19 - len(trr), replace=False)])
    if arm == "classes19":
        g = defaultdict(list)
        for o in tr: g[tuple(lang[o])].append(o)
        cls = [v for v in g.values() if len(v) >= 2]; rng.shuffle(cls); out = []
        for v in cls:
            if len(out) + len(v) <= 19: out += v
        rest = [o for o in tr if o not in out]; rng.shuffle(rest); return np.array(out + rest[: 19 - len(out)])
    if arm == "stable19":
        ch = np.array([sum((a[o] != b[o]).any() for a, b in zip(hist, hist[1:])) for o in range(N)], float) + rng.rand(N) * 0.1; return tr[np.argsort(ch[tr])[:19]]
def parent_job(s):
    torch.set_num_threads(1); cfg = make_cfg(GENS, s, steps=2000, eval_every=250, generations=1, save_weights=False); world = World(3, 4, 0.25, seed=s)
    torch.manual_seed(s * 100); S_, R_ = Sender(world.dim, 8, 3, 64), Receiver(world.dim, 8, 64); log = []
    train_generation(cfg, world, [S_], [R_], np.random.RandomState(s), None, log, 0, 0, 2000)
    from lab import receiver_decode, sender_language
    msgs, _ = sender_language(S_, world); dec = receiver_decode(R_, world, msgs)
    return s, msgs.numpy().tolist(), list(map(int, dec)), [r["language"] for r in log if r["gen_step"] in (1000, 1250, 1500, 1750, 2000)]
def child_job(args):
    s, arm, lang, dec, hist = args; torch.set_num_threads(1); lang, dec, hist = np.array(lang), np.array(dec), [np.array(h) for h in hist]
    cfg = make_cfg(GENS, s, steps=2000, eval_every=250, generations=1, save_weights=False); world = World(3, 4, 0.25, seed=s); rng = np.random.RandomState(2000 + s)
    objs = np.array(sorted(choose(arm, world, lang, dec, hist, rng))); torch.manual_seed(s * 100 + 1); S_, R_ = Sender(world.dim, 8, 3, 64), Receiver(world.dim, 8, 64)
    teach_sender(cfg, world, S_, objs, lang[objs]); log = []; train_generation(cfg, world, [S_], [R_], np.random.RandomState(s), None, log, 1, 0, 2000)
    return s, arm, objs.tolist(), log[-1]["language"], log[-1]["decode"], log[-1]["test_acc"]
if __name__ == "__main__":
    raw = "results_v3_confirm2/k14_raw.json"
    if os.path.exists(raw): P, res = json.load(open(raw))
    else:
        with Pool(6) as p: P = {s: (l, d, h) for s, l, d, h in p.map(parent_job, SEEDS)}
        with Pool(6) as p: res = p.map(child_job, [(s, arm, *P[s]) for s in SEEDS for arm in ARMS])
        json.dump([{str(k): v for k, v in P.items()}, res], open(raw, "w")); P = {str(k): v for k, v in P.items()}
    worlds = {s: World(3, 4, 0.25, seed=s) for s in SEEDS}; OD = {s: (worlds[s].objects[:, None, :] != worlds[s].objects[None, :, :]).sum(-1)[IU] for s in SEEDS}
    def tsd(s, lang): md = (lang[:, None, :] != lang[None, :, :]).sum(-1)[IU]; k = md > 0; return spearman(OD[s][k], md[k]) if k.sum() > 2 else np.nan
    def cbm(lang, w):
        M = np.zeros((24, 12))
        for o in range(N):
            for p in range(3):
                for a in range(3): M[p * 8 + lang[o, p], a * 4 + w.objects[o, a]] += 1
        r, c = linear_sum_assignment(-M); return M[r, c].sum() / (N * 3)
    R = {(s, arm): (np.array(l), np.array(d), ta) for s, arm, objs, l, d, ta in res}
    O = ["# K14 on new seeds 30–44 (pre-registered thresholds: |Δ topsim_distinct| < 0.03 AND |Δ CBM| < 0.02 → 'not materially different'; all |Δ topsim| < 0.05)", "", "| rule | Δ topsim_distinct vs random | | | | | | Δ CBM vs random | | | | | | verdict |", "|---|" + "---|" * 13]
    ok = 0
    for arm in ARMS[1:]:
        dt = np.array([tsd(s, R[(s, arm)][0]) - tsd(s, R[(s, "random19")][0]) for s in SEEDS]); dc = np.array([cbm(R[(s, arm)][0], worlds[s]) - cbm(R[(s, "random19")][0], worlds[s]) for s in SEEDS])
        v = abs(dt.mean()) < 0.03 and abs(dc.mean()) < 0.02; ok += v
        O.append(f"| {arm} " + fmt(stats_line(dt, "?")) + " " + fmt(stats_line(dc, "?")) + f" {'not different' if v else 'DIFFERENT'} (|Δt|<0.05: {abs(dt.mean()) < 0.05}) |")
    O += ["", f"K14: {ok}/4 rules not materially different from random (needs ≥3); test_acc by rule: " + ", ".join(f"{arm} {np.mean([R[(s, arm)][2] for s in SEEDS]):.3f}" for arm in ARMS)]
    open("results_v3_confirm2/k14.md", "w").write("\n".join(O) + "\n"); print("\n".join(O))
