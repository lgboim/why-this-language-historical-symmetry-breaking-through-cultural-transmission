"""confirm5.py — E1–E4 (results_entropy/PREREG.md): entropy-bonus scan vs the default 0.02 (results_v3, seeds 0-9)."""
import glob, itertools, json, os, numpy as np
from collections import defaultdict
from game import World
from lab import Cell, spearman, stats_line, fmt, SELECTS, FRESHES
N = 64; IU = np.triu_indices(N, 1); worlds = {s: World(3, 4, 0.25, seed=s) for s in range(30)}; TR = {s: np.isin(np.arange(N), worlds[s].train_idx) for s in worlds}
SD = {s: (worlds[s].objects[:, None, :] != worlds[s].objects[None, :, :]).sum(-1) for s in worlds}; OD = {s: SD[s][IU] for s in worlds}
def load(d):
    L = {}
    for p in glob.glob(f"{d}/*_seed*.json"):
        j = json.load(open(p)); L[(Cell(**j["config"]["cell"]), j["config"]["seed"])] = j["log"]
    return L
LOGS = {0.005: load("results_entropy/coef_0.005"), 0.02: load("results_v3"), 0.08: load("results_entropy/coef_0.08")}
def cell(sel, fr): return Cell("small", "gens", sel, "fixed" if sel == "random" else "dynamic", fr, 19, 0.0, "sender")
GENS = Cell("small", "gens"); L = lambda r: np.array(r["language"])
def tsd(s, lang): md = (lang[:, None, :] != lang[None, :, :]).sum(-1)[IU]; k = md > 0; return spearman(OD[s][k], md[k]) if k.sum() > 2 else np.nan
def ends(LG, c, s): return [r for r in LG[(c, s)] if "per_obj_acc" in r]
def nbrs(s, o): return [p for p in np.where(TR[s])[0] if p != o and SD[s][o, p] == 1]
O = ["# E1–E4: entropy-bonus scan (seeds 0–9)", ""]
for coef, LG in LOGS.items():
    d1, e2, gap = [], [], []
    for s in sorted({ss for _, ss in LG}):
        rw = [tsd(s, L(ends(LG, cell(sel, "rewrite"), s)[-1])) for sel in ("random", "success") if (cell(sel, "rewrite"), s) in LG]
        ac = [tsd(s, L(ends(LG, cell(sel, "accumulate"), s)[-1])) for sel in ("random", "success") if (cell(sel, "accumulate"), s) in LG]
        if rw and ac: d1.append(np.mean(rw) - np.mean(ac))
        if (GENS, s) in LG:
            g0 = [r["msg_entropy"] for r in LG[(GENS, s)] if r["gen"] == 0 and r["gen_step"] == 250][0]
            ch = [r["msg_entropy"] for sel, fr in itertools.product(SELECTS, FRESHES) if (cell(sel, fr), s) in LG for r in LG[(cell(sel, fr), s)] if r["gen"] >= 1 and r["gen_step"] == 250]
            if ch: e2.append(np.mean(ch) < 0.5 * g0)
        same, other = [], []
        for sel, fr in itertools.product(SELECTS, FRESHES):
            c = cell(sel, fr)
            if (c, s) not in LG: continue
            E = ends(LG, c, s)
            for g in range(1, len(E)):
                lp, lc = L(E[g - 1]), L(E[g]); rec = {o: tuple(m) for o, m, _ in E[g - 1]["record"]}
                for o in np.where(TR[s])[0]:
                    if o in rec: continue
                    anc = [p for p in nbrs(s, o) if p in rec and rec[p] == tuple(lp[p])]
                    if not anc: continue
                    (same if any(tuple(lp[p]) == tuple(lp[o]) for p in anc) else other).append((lc[o] == lp[o]).all())
        if same and other: gap.append(np.mean(same) - np.mean(other))
    O.append(f"## coef {coef}: n runs = {len(LG)}, seeds = {len({ss for _, ss in LG})}"); O.append("E1 rewrite − accumulate topsim_distinct: " + fmt(stats_line(np.array(d1), ">")) if len(d1) >= 2 else "E1: n/a")
    O.append(f"E2 child entropy@250 < 0.5 × gen-0 entropy@250: {np.mean(e2):.2f} of seeds" if e2 else "E2: n/a"); O.append("E4 same − other anchors: " + fmt(stats_line(np.array(gap), ">")) if len(gap) >= 2 else "E4: n/a"); O.append("")
# E3 drift monotone in coef
def drift(LG, s):
    v = []
    for sel, fr in itertools.product(SELECTS, FRESHES):
        c = cell(sel, fr)
        if (c, s) not in LG: continue
        by = defaultdict(dict)
        for r in LG[(c, s)]:
            if r["gen_step"] % 250 == 0 and r["gen_step"] > 0: by[r["gen"]][r["gen_step"]] = r
        for g in sorted(by)[1:]:
            st = sorted(by[g]); v += [(L(by[g][a]) != L(by[g][b])).any(1).mean() for a, b in zip(st, st[1:])]
    return np.mean(v) if v else np.nan
D = {coef: np.array([drift(LG, s) for s in range(10)]) for coef, LG in LOGS.items()}
O += ["## E3 within-generation form change per 250 steps (inheriting generations)", "", " | ".join(f"coef {c}: {np.nanmean(D[c]):.3f}" for c in D), "0.02 − 0.005: " + fmt(stats_line(D[0.02] - D[0.005], ">")), "0.08 − 0.02: " + fmt(stats_line(D[0.08] - D[0.02], ">"))]
open("results_entropy/confirmation5.md", "w").write("\n".join(O) + "\n"); print("\n".join(O))
