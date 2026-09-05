"""probe45.py — K17a-c on seeds 30-44.   python probe45.py -> results_v3_confirm2/k17.md"""
import json, os
import numpy as np, torch
from multiprocessing import Pool
from collections import Counter
from game import World, Sender, Receiver
from lab import Cell, make_cfg, teach_sender, train_generation, stats_line, fmt
GENS = Cell("small", "gens"); N = 64; SEEDS = list(range(30, 45))
from metrics import ari   # shared standard ARI (corrected 2026-09-05; the old local copy returned 0 for identical singleton partitions)
def parent_job(s):
    torch.set_num_threads(1); cfg = make_cfg(GENS, s, steps=2000, eval_every=250, generations=1, save_weights=False); world = World(3, 4, 0.25, seed=s)
    torch.manual_seed(s * 100); S_, R_ = Sender(world.dim, 8, 3, 64), Receiver(world.dim, 8, 64); log = []
    train_generation(cfg, world, [S_], [R_], np.random.RandomState(s), None, log, 0, 0, 2000)
    L = {r["gen_step"]: r["language"] for r in log}; return s, L[500], L[2000]
def child_job(args):
    s, arm, init, l500, lfin = args; torch.set_num_threads(1); cfg = make_cfg(GENS, s, steps=2000, eval_every=2000, generations=1, save_weights=False)
    world = World(3, 4, 0.25, seed=s); lang = np.array(l500 if arm == "stale" else lfin); objs = np.sort(np.random.RandomState(3000 + s).choice(np.array(world.train_idx), 19, replace=False))
    torch.manual_seed(s * 100 + 50 + init); S_, R_ = Sender(world.dim, 8, 3, 64), Receiver(world.dim, 8, 64); teach_sender(cfg, world, S_, objs, lang[objs])
    log = []; train_generation(cfg, world, [S_], [R_], np.random.RandomState(s + 7 * init), None, log, 1, 0, 2000); return s, arm, init, log[-1]["language"]
if __name__ == "__main__":
    raw = "results_v3_confirm2/k17_raw.json"
    if os.path.exists(raw): P, res = json.load(open(raw)); P = {int(k): v for k, v in P.items()}
    else:
        with Pool(8) as p: P = {s: (l5, lf) for s, l5, lf in p.map(parent_job, SEEDS)}
        with Pool(8) as p: res = p.map(child_job, [(s, arm, i, *P[s]) for s in SEEDS for arm in ("stale", "fresh") for i in (1, 2)])
        json.dump([{str(k): v for k, v in P.items()}, res], open(raw, "w"))
    K14 = json.load(open("results_v3_confirm2/k14_raw.json"))[0]; match = np.mean([np.array_equal(np.array(P[s][1]), np.array(K14[str(s)][0])) for s in SEEDS])
    worlds = {s: World(3, 4, 0.25, seed=s) for s in SEEDS}; R = {(s, arm, i): np.array(l) for s, arm, i, l in res}
    V = {arm: {"ss": [], "cp": [], "c5": []} for arm in ("fresh", "stale")}
    for arm in V:
        for s in SEEDS:
            tr = worlds[s].train_idx; l5, lf = np.array(P[s][0]), np.array(P[s][1]); a, b = R[(s, arm, 1)], R[(s, arm, 2)]; Pt = lambda l: [tuple(l[o]) for o in tr]
            V[arm]["ss"].append(ari(Pt(a), Pt(b))); V[arm]["cp"].append((ari(Pt(a), Pt(lf)) + ari(Pt(b), Pt(lf))) / 2); V[arm]["c5"].append((ari(Pt(a), Pt(l5)) + ari(Pt(b), Pt(l5))) / 2)
    ss = np.array(V["stale"]["ss"]) - np.array(V["fresh"]["ss"]); cp = np.array(V["fresh"]["cp"]) - np.array(V["stale"]["cp"]); c5 = np.array(V["stale"]["c5"]) - np.array(V["fresh"]["c5"])
    st = stats_line(ss, "?"); k17a = st["mean"] >= -0.05 and st["lo"] >= -0.10
    O = [f"# K17 on seeds 30–44 (parents retrained; final language identical to k14 parents in {match:.0%} of seeds)", "",
         "| arm | ARI sib–sib | ARI child–parent final | ARI child–step-500 |", "|---|---|---|---|"] + [f"| {arm} | {np.mean(V[arm]['ss']):.3f} | {np.mean(V[arm]['cp']):.3f} | {np.mean(V[arm]['c5']):.3f} |" for arm in ("fresh", "stale")] + ["",
         f"K17a sibling ARI stale − fresh: {fmt(st)} → {'SUPPORTED' if k17a else 'FAILED'} (needs mean ≥ −0.05 and CI lower ≥ −0.10)",
         "K17b child–parent ARI fresh − stale: " + fmt(stats_line(cp, ">")), "K17c child–step-500 ARI stale − fresh: " + fmt(stats_line(c5, ">"))]
    open("results_v3_confirm2/k17.md", "w").write("\n".join(O) + "\n"); print("\n".join(O))
