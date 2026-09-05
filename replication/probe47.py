"""probe47.py — experiment S: lineage after a ONE-SHOT immature vs mature snapshot (results_oneshot/PREREG.md).
   Gen 1 taught 19 objects with parent's step-500 or final forms; gens 2-5 use a rewritten success-selected record (cap 19).
   python probe47.py -> results_oneshot/s.md"""
import glob, json, os
import numpy as np, torch
from multiprocessing import Pool
from collections import Counter
from game import World, Sender, Receiver
from lab import Cell, make_cfg, teach_sender, train_generation, Record, stats_line, fmt
N = 64; SEEDS = list(range(30)); CELL = Cell("small", "gens", "success", "dynamic", "rewrite", 19, 0.0, "sender")
def gen0(s):
    f = glob.glob(f"results_v3/*_seed{s}.json") + glob.glob(f"results_v3_confirm/*_seed{s}.json"); j = json.load(open(f[0]))
    Lg = {r["gen_step"]: np.array(r["language"]) for r in j["log"] if r["gen"] == 0}; return Lg[500], Lg[2000]
from metrics import ari   # shared standard ARI (corrected 2026-09-05; the old local copy returned 0 for identical singleton partitions)
def job(args):
    s, arm = args; torch.set_num_threads(1); cfg = make_cfg(CELL, s, eval_every=2000, save_weights=False); world = World(3, 4, 0.25, seed=s)
    l500, lfin = gen0(s); objs = np.sort(np.random.RandomState(3000 + s).choice(np.array(world.train_idx), 19, replace=False)); lang1 = l500 if arm == "immature" else lfin
    record = Record(CELL, world, 8, np.random.RandomState(s + 7919)); rng = np.random.RandomState(s); langs = []; off = 2000
    for g in range(1, 6):
        torch.manual_seed(s * 100 + g); S_, R_ = Sender(world.dim, 8, 3, 64), Receiver(world.dim, 8, 64)
        if g == 1: teach_sender(cfg, world, S_, objs, lang1[objs])
        else:
            o_, m_ = record.read(); teach_sender(cfg, world, S_, o_, m_)
        log = []; off = train_generation(cfg, world, [S_], [R_], rng, record, log, g, off, 2000); fin = log[-1]
        record.end_of_generation(np.array(fin["language"]), fin["_pacc"]); langs.append(fin["language"])
    return s, arm, langs
if __name__ == "__main__":
    raw = "results_oneshot/s_raw.json"
    if os.path.exists(raw): res = [tuple(x) for x in json.load(open(raw))]
    else:
        with Pool(8) as p: res = p.map(job, [(s, arm) for s in SEEDS for arm in ("immature", "mature")])
        json.dump(res, open(raw, "w"))
    R = {(s, arm): [np.array(l) for l in langs] for s, arm, langs in res}; worlds = {s: World(3, 4, 0.25, seed=s) for s in SEEDS}
    def A(s, arm, g, ref):
        tr = worlds[s].train_idx; l = R[(s, arm)][g - 1]; return ari([tuple(l[o]) for o in tr], [tuple(ref[o]) for o in tr])
    O = ["# Experiment S — one-shot immature vs mature snapshot, lineage of 5 generations (30 seeds)", "", "| g | ARI to step-500: immature / mature | ARI to parent final: immature / mature | gap-1 ARI (g−1→g): immature / mature |", "|---|---|---|---|"]
    S1, S2, S3 = [], [], []
    for g in range(1, 6):
        i5 = [A(s, "immature", g, gen0(s)[0]) for s in SEEDS]; m5 = [A(s, "mature", g, gen0(s)[0]) for s in SEEDS]; iF = [A(s, "immature", g, gen0(s)[1]) for s in SEEDS]; mF = [A(s, "mature", g, gen0(s)[1]) for s in SEEDS]
        if g > 1:
            gi = [ari([tuple(R[(s, "immature")][g - 1][o]) for o in worlds[s].train_idx], [tuple(R[(s, "immature")][g - 2][o]) for o in worlds[s].train_idx]) for s in SEEDS]; gm = [ari([tuple(R[(s, "mature")][g - 1][o]) for o in worlds[s].train_idx], [tuple(R[(s, "mature")][g - 2][o]) for o in worlds[s].train_idx]) for s in SEEDS]
        else: gi = gm = [np.nan] * len(SEEDS)
        O.append(f"| {g} | {np.mean(i5):.3f} / {np.mean(m5):.3f} | {np.mean(iF):.3f} / {np.mean(mF):.3f} | {np.nanmean(gi):.3f} / {np.nanmean(gm):.3f} |")
        if g == 3: S1 = np.array(i5) - np.array(m5)
        if g == 5: S2 = np.array(mF) - np.array(iF)
        if g > 1: S3.append(np.array(gi) - np.array(gm))
    s3 = stats_line(np.concatenate(S3), "?")
    O += ["", "S1 (g=3) ARI to snapshot, immature − mature: " + fmt(stats_line(S1, ">")), "S2 (g=5) ARI to parent final, mature − immature: " + fmt(stats_line(S2, ">")),
          "S3 gap-1 ARI, immature − mature (equivalence |mean|<0.05, CI within ±0.08): " + fmt(s3) + (" → SUPPORTED" if abs(s3["mean"]) < 0.05 and s3["lo"] > -0.08 and s3["hi"] < 0.08 else " → FAILED")]
    open("results_oneshot/s.md", "w").write("\n".join(O) + "\n"); print("\n".join(O))
