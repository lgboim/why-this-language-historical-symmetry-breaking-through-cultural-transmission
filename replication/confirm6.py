"""confirm6.py — L1–L3 (results_long/PREREG.md): 6,000-step generations, seeds 0-9, vs the default 2,000 (results_v3)."""
import glob, itertools, json, os, numpy as np
from collections import defaultdict
from game import World
from lab import Cell, spearman, stats_line, fmt, SELECTS, FRESHES
N = 64; IU = np.triu_indices(N, 1); worlds = {s: World(3, 4, 0.25, seed=s) for s in range(30)}; TR = {s: np.isin(np.arange(N), worlds[s].train_idx) for s in worlds}
SD = {s: (worlds[s].objects[:, None, :] != worlds[s].objects[None, :, :]).sum(-1) for s in worlds}; OD = {s: SD[s][IU] for s in worlds}
LOGS = {}
for p in glob.glob("results_long/*_seed*.json"):
    j = json.load(open(p)); LOGS[(Cell(**j["config"]["cell"]), j["config"]["seed"])] = j["log"]
def cell(sel, fr): return Cell("small", "gens", sel, "fixed" if sel == "random" else "dynamic", fr, 19, 0.0, "sender")
L = lambda r: np.array(r["language"])
def tsd(s, lang): md = (lang[:, None, :] != lang[None, :, :]).sum(-1)[IU]; k = md > 0; return spearman(OD[s][k], md[k]) if k.sum() > 2 else np.nan
def ends(c, s): return [r for r in LOGS[(c, s)] if "per_obj_acc" in r]
def nbrs(s, o): return [p for p in np.where(TR[s])[0] if p != o and SD[s][o, p] == 1]
d1, fid, gap, fixed = [], [], [], []
for s in sorted({ss for _, ss in LOGS}):
    rw = [tsd(s, L(ends(cell(sel, "rewrite"), s)[-1])) for sel in ("random", "success") if (cell(sel, "rewrite"), s) in LOGS]
    ac = [tsd(s, L(ends(cell(sel, "accumulate"), s)[-1])) for sel in ("random", "success") if (cell(sel, "accumulate"), s) in LOGS]
    if rw and ac: d1.append(np.mean(rw) - np.mean(ac))
    f2, f6, same, other = [], [], [], []
    for sel, fr in itertools.product(SELECTS, FRESHES):
        c = cell(sel, fr)
        if (c, s) not in LOGS: continue
        by = defaultdict(dict)
        for r in LOGS[(c, s)]: by[r["gen"]][r["gen_step"]] = r
        E = ends(c, s)
        for g in range(1, len(E)):
            rec = {o: tuple(m) for o, m, _ in E[g - 1]["record"]}
            if 2000 in by[g] and 6000 in by[g]:
                f2.append(np.mean([tuple(L(by[g][2000])[o]) == m for o, m in rec.items()])); f6.append(np.mean([tuple(L(by[g][6000])[o]) == m for o, m in rec.items()]))
            lp, lc = L(E[g - 1]), L(E[g])
            for o in np.where(TR[s])[0]:
                if o in rec: continue
                anc = [p for p in nbrs(s, o) if p in rec and rec[p] == tuple(lp[p])]
                if not anc: continue
                (same if any(tuple(lp[p]) == tuple(lp[o]) for p in anc) else other).append((lc[o] == lp[o]).all())
        if fr == "accumulate":
            for g in range(len(E)):
                lang = L(E[g]); fixed.append(np.mean([tuple(m) != tuple(lang[o]) for o, m, _ in E[g]["record"]]))
    if f2 and f6: fid.append(np.mean(f2) - np.mean(f6))
    if same and other: gap.append(np.mean(same) - np.mean(other))
O = [f"# L1–L3: 6,000-step generations (n runs = {len(LOGS)}, seeds = {len({ss for _, ss in LOGS})})", "", "L1 rewrite − accumulate topsim_distinct at generation end: " + fmt(stats_line(np.array(d1), ">")),
     "L2 fidelity to record at step 2,000 − at step 6,000 (same generation): " + fmt(stats_line(np.array(fid), ">")), "L3 same − other anchors gap (≥ 0.15): " + fmt(stats_line(np.array(gap), ">")),
     f"staleness of accumulated entries at generation end (share ≠ parent final): {np.mean(fixed):.2f} (default 2,000-step regime: 0.35)"]
open("results_long/confirmation6.md", "w").write("\n".join(O) + "\n"); print("\n".join(O))
