"""probe49.py — experiment D (results_degeneracy/PREREG.md): sibling gaps vs hard_frac, GRU, seeds 0-19.  -> results_degeneracy/d.md"""
import json, os
import numpy as np, torch
from multiprocessing import Pool
from collections import Counter
from game import World, Sender, Receiver
from lab import Cell, make_cfg, teach_sender, train_generation, stats_line, fmt
GENS = Cell("small", "gens"); N = 64; SEEDS = list(range(20)); HF = (0.0, 0.5, 1.0)
from metrics import ari   # shared standard ARI (corrected 2026-09-05; the old local copy returned 0 for identical singleton partitions)
def parent_job(args):
    s, hf = args; torch.set_num_threads(1); cfg = make_cfg(GENS, s, steps=2000, eval_every=2000, generations=1, save_weights=False, hard_frac=hf); w = World(3, 4, 0.25, seed=s); w.hard_frac = hf
    torch.manual_seed(s * 100); S_, R_ = Sender(w.dim, 8, 3, 64), Receiver(w.dim, 8, 64); log = []; train_generation(cfg, w, [S_], [R_], np.random.RandomState(s), None, log, 0, 0, 2000)
    return s, hf, log[-1]["language"], log[-1]["decode"]
def child_job(args):
    s, hf, arm, init, lang = args; torch.set_num_threads(1); cfg = make_cfg(GENS, s, steps=2000, eval_every=2000, generations=1, save_weights=False, hard_frac=hf); w = World(3, 4, 0.25, seed=s); w.hard_frac = hf; lang = np.array(lang); tr = np.array(w.train_idx)
    if arm == "same": objs = np.random.RandomState(3000 + s).choice(tr, 19, replace=False)
    elif arm == "different": objs = np.random.RandomState(3000 + s + 100 * init).choice(tr, 19, replace=False)
    else: objs = None
    torch.manual_seed(s * 100 + 50 + init); S_, R_ = Sender(w.dim, 8, 3, 64), Receiver(w.dim, 8, 64)
    if objs is not None: teach_sender(cfg, w, S_, np.sort(objs), lang[np.sort(objs)])
    log = []; train_generation(cfg, w, [S_], [R_], np.random.RandomState(s + 7 * init), None, log, 1, 0, 2000); return s, hf, arm, init, log[-1]["language"]
if __name__ == "__main__":
    raw = "results_degeneracy/d_raw.json"
    if os.path.exists(raw): P, res = json.load(open(raw)); P = {(int(k.split("_")[0]), float(k.split("_")[1])): v for k, v in P.items()}
    else:
        with Pool(6) as p: P = {(s, hf): (l, d) for s, hf, l, d in p.map(parent_job, [(s, hf) for s in SEEDS for hf in HF])}
        with Pool(6) as p: res = p.map(child_job, [(s, hf, arm, i, P[(s, hf)][0]) for s in SEEDS for hf in HF for arm in ("same", "different", "none") for i in (1, 2)])
        json.dump([{f"{s}_{hf}": v for (s, hf), v in P.items()}, res], open(raw, "w"))
    sib = {(s, hf, arm, i): np.array(l) for s, hf, arm, i, l in res}; worlds = {s: World(3, 4, 0.25, seed=s) for s in SEEDS}
    O = ["# Experiment D — sibling gaps vs hard_frac (GRU, 20 seeds)", "", "| hard_frac | distinct msgs (parent) | owner share | ARI same / different / none | form agreement same / different / none | ARI gap | form gap |", "|---|---|---|---|---|---|---|"]
    G = {hf: {"ari": {}, "form": {}} for hf in HF}
    for hf in HF:
        dm, ow, A, F = [], [], {"same": [], "different": [], "none": []}, {"same": [], "different": [], "none": []}
        for s in SEEDS:
            lp, dp = np.array(P[(s, hf)][0]), np.array(P[(s, hf)][1]); dm.append(len({tuple(m) for m in lp})); ow.append((dp == np.arange(N)).mean()); tr = worlds[s].train_idx; Pt = lambda l: [tuple(l[o]) for o in tr]
            for arm in A:
                a, b = sib[(s, hf, arm, 1)], sib[(s, hf, arm, 2)]; A[arm].append(ari(Pt(a), Pt(b))); F[arm].append(np.mean([(a[o] == b[o]).all() for o in tr]))
            G[hf]["ari"][s] = A["same"][-1] - A["different"][-1]; G[hf]["form"][s] = F["same"][-1] - F["different"][-1]
        O.append(f"| {hf} | {np.mean(dm):.1f} | {np.mean(ow):.2f} | {np.mean(A['same']):.3f} / {np.mean(A['different']):.3f} / {np.mean(A['none']):.3f} | {np.mean(F['same']):.2f} / {np.mean(F['different']):.2f} / {np.mean(F['none']):.2f} | {np.mean(list(G[hf]['ari'].values())):.3f} | {np.mean(list(G[hf]['form'].values())):.3f} |")
    O += ["", "D1 ARI gap 0.0 − 0.5: " + fmt(stats_line(np.array([G[0.0]["ari"][s] - G[0.5]["ari"][s] for s in SEEDS]), ">")), "D1 ARI gap 0.5 − 1.0: " + fmt(stats_line(np.array([G[0.5]["ari"][s] - G[1.0]["ari"][s] for s in SEEDS]), ">"))]
    st = stats_line(np.array([G[1.0]["form"][s] - G[0.0]["form"][s] for s in SEEDS]), "?")
    O.append("D2 form gap 1.0 − 0.0 (equivalence |mean|<0.10, CI within ±0.15): " + fmt(st) + (" → SUPPORTED" if abs(st["mean"]) < 0.10 and st["lo"] > -0.15 and st["hi"] < 0.15 else " → FAILED"))
    open("results_degeneracy/d.md", "w").write("\n".join(O) + "\n"); print("\n".join(O))
