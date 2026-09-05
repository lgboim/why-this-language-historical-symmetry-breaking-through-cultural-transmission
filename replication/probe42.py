"""probe42.py — K16 on seeds 30-44 (parents from results_v3_confirm2/k14_raw.json).
"""
"""probe41.py — symmetry breaking: two independent children (different inits) of the same parent (end of gen 0):
   siblings taught the SAME 19 fresh forms vs siblings taught nothing vs siblings taught DIFFERENT random 19-sets.
   Partition similarity (ARI, train objects) between siblings; and between each sibling and the parent.   30 seeds.
   python probe41.py -> results_v3_confirm2/k16.md"""
import glob, json, os
import numpy as np, torch
from multiprocessing import Pool
from collections import Counter
from game import World, Sender, Receiver
from lab import Cell, make_cfg, teach_sender, train_generation, stats_line, fmt
GENS = Cell("small", "gens"); N = 64
_P = json.load(open("results_v3_confirm2/k14_raw.json"))[0]
def parent(s): return np.array(_P[str(s)][0]), np.array(_P[str(s)][1])
SEEDS = list(range(30, 45))
def job(args):
    s, arm, init = args; torch.set_num_threads(1); cfg = make_cfg(GENS, s, steps=2000, eval_every=2000, generations=1, save_weights=False)
    world = World(3, 4, 0.25, seed=s); lang, dec = parent(s); tr = np.array(world.train_idx)
    torch.manual_seed(s * 100 + 50 + init); S_, R_ = Sender(world.dim, 8, 3, 64), Receiver(world.dim, 8, 64)
    if arm == "same": objs = np.random.RandomState(3000 + s).choice(tr, 19, replace=False)
    elif arm == "different": objs = np.random.RandomState(3000 + s + 100 * init).choice(tr, 19, replace=False)
    else: objs = None
    if objs is not None: teach_sender(cfg, world, S_, np.sort(objs), lang[np.sort(objs)])
    log = []; train_generation(cfg, world, [S_], [R_], np.random.RandomState(s + 7 * init), None, log, 1, 0, 2000)
    return s, arm, init, log[-1]["language"]
from metrics import ari   # shared standard ARI (corrected 2026-09-05; the old local copy returned 0 for identical singleton partitions)
if __name__ == "__main__":
    raw = "results_v3_confirm2/k16_raw.json"
    if os.path.exists(raw): res = [tuple(x) for x in json.load(open(raw))]
    else:
        with Pool(8) as p: res = p.map(job, [(s, arm, i) for s in SEEDS for arm in ("same", "different", "none") for i in (1, 2)])
        json.dump(res, open(raw, "w"))
    R = {(s, arm, i): np.array(l) for s, arm, i, l in res}; worlds = {s: World(3, 4, 0.25, seed=s) for s in SEEDS}
    O = ["# K16 — sibling symmetry breaking on new seeds 30–44 (pre-registered)", "", "| arm | ARI sibling–sibling | ARI child–parent (mean of 2) | share of train forms shared by siblings |", "|---|---|---|---|"]
    V = {}
    for arm in ("same", "different", "none"):
        ss, cp, sh = [], [], []
        for s in SEEDS:
            tr = worlds[s].train_idx; lp = parent(s)[0]; a, b = R[(s, arm, 1)], R[(s, arm, 2)]; pa = [tuple(a[o]) for o in tr]; pb = [tuple(b[o]) for o in tr]; pp = [tuple(lp[o]) for o in tr]
            ss.append(ari(pa, pb)); cp.append((ari(pa, pp) + ari(pb, pp)) / 2); sh.append(np.mean([x == y for x, y in zip(pa, pb)]))
        V[arm] = np.array(ss); O.append(f"| {arm} | {np.mean(ss):.3f} | {np.mean(cp):.3f} | {np.mean(sh):.2f} |")
    O += ["", "same − none (sibling ARI): " + fmt(stats_line(V["same"] - V["none"], ">")), "same − different: " + fmt(stats_line(V["same"] - V["different"], ">")), "different − none: " + fmt(stats_line(V["different"] - V["none"], ">"))]
    open("results_v3_confirm2/k16.md", "w").write("\n".join(O) + "\n"); print("\n".join(O))
