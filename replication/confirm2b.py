"""confirm2b.py — per-seed evaluation of K10-K12 (results_v3_confirm2/PREREG.md) on seeds 10-29.  python confirm2b.py"""
import glob, itertools, json, os, numpy as np
from collections import defaultdict
from game import World
from lab import Cell, stats_line, fmt, SELECTS, FRESHES
N = 64; worlds = {s: World(3, 4, 0.25, seed=s) for s in range(300)}; TR = {s: np.isin(np.arange(N), worlds[s].train_idx) for s in range(300)}
SD = {s: (worlds[s].objects[:, None, :] != worlds[s].objects[None, :, :]).sum(-1) for s in range(300)}
LOGS = {}
import os as _os
_KS = _os.environ.get("K_SEEDS"); _KO = _os.environ.get("K_OUT", "results_v3_confirm2")
def _seeds(default):
    return list(range(int(_KS.split("..")[0]), int(_KS.split("..")[1]) + 1)) if _KS else default
for p in glob.glob(f"{_KO}/*_seed*.json"):
    j = json.load(open(p)); LOGS[(Cell(**j["config"]["cell"]), j["config"]["seed"])] = j["log"]
def cell(sel, fr, cap=19, noise=0.0, rd="sender"): return Cell("small", "gens", sel, "fixed" if sel == "random" else "dynamic", fr, cap, noise, rd)
L = lambda r: np.array(r["language"]); nb = lambda s, o: [p for p in np.where(TR[s])[0] if p != o and SD[s][o, p] == 1]
def per_seed(cs, s):
    rt, ru, ch, chu, R, R2 = [], [], [], [], defaultdict(list), defaultdict(list)   # R: 0/1/2/3+ anchors; R2: 0/1/>=2 (the registered K12 bins)
    for c in cs:
        if (c, s) not in LOGS: continue
        E = [r for r in LOGS[(c, s)] if "per_obj_acc" in r]
        for g in range(1, len(E)):
            lp, lc = L(E[g - 1]), L(E[g]); rec = {o: tuple(m) for o, m, _ in E[g - 1]["record"]}
            for o in np.where(TR[s])[0]:
                if o in rec: continue
                n_ = nb(s, o); k = sum(p in rec and rec[p] == tuple(lp[p]) for p in n_); R[min(k, 3)].append((lc[o] == lp[o]).all()); R2[min(k, 2)].append((lc[o] == lp[o]).all()); forms = {tuple(lp[p]) for p in n_}
                if tuple(lp[o]) in forms and len(forms) >= 2:
                    src = [p for p in n_ if tuple(lp[p]) == tuple(lp[o])]; a = (lc[o] == lp[o]).all(); ch.append(1 / len(forms)); taught = any(p in rec and rec[p] == tuple(lp[p]) for p in src); (rt if taught else ru).append(a)
                    if not taught: chu.append(1 / len(forms))   # chance reference restricted to the untaught cases it is compared with (correction 2026-09-05)
    return (np.mean(rt) if rt else np.nan, np.mean(ru) if ru else np.nan, np.mean(ch) if ch else np.nan, [np.mean(R[k]) if R[k] else np.nan for k in range(4)], [np.mean(R2[k]) if R2[k] else np.nan for k in range(3)], np.mean(chu) if chu else np.nan)
fams = {"cap 8": [cell(a, b, 8) for a, b in itertools.product(SELECTS, FRESHES)], "cap 40": [cell(a, b, 40) for a, b in itertools.product(SELECTS, FRESHES)], "noise 0.2": [cell(a, b, 19, 0.2) for a, b in itertools.product(SELECTS, FRESHES)], "reader both": [cell(a, b, 19, 0.0, "both") for a, b in itertools.product(SELECTS, FRESHES)]}
O = [f"# K10–K12 per seed ({_KO}, seeds {_seeds(list(range(10, 30)))[0]}–{_seeds(list(range(10, 30)))[-1]})", "", "| family | n | K10 gap taught−untaught | | | | | | K10 untaught−chance mean | K11 corr(anchors, retention) per seed | | | | | |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
PS = {}
for lab, cs in fams.items():
    PS[lab] = {s: per_seed(cs, s) for s in _seeds(list(range(10, 30))) if any((c, s) in LOGS for c in cs)}
    gap = np.array([v[0] - v[1] for v in PS[lab].values() if not np.isnan(v[0] + v[1])]); uc = np.nanmean([v[1] - v[2] for v in PS[lab].values()])
    slope = np.array([np.polyfit(range(4), v[3], 1)[0] for v in PS[lab].values() if not np.isnan(v[3]).any()])
    O.append(f"| {lab} | {len(gap)} " + fmt(stats_line(gap, ">")) + f" {uc:+.3f} " + fmt(stats_line(slope, ">")))
if PS.get("cap 8") and PS.get("cap 40"):
    ks = sorted(set(PS["cap 8"]) & set(PS["cap 40"]))
    for k, lab in [(0, "0 anchors"), (3, "3+ anchors (additional, non-registered subgroup)")]:
        d = np.array([PS["cap 40"][s][3][k] - PS["cap 8"][s][3][k] for s in ks if not np.isnan(PS["cap 40"][s][3][k] + PS["cap 8"][s][3][k])])
        O.append(f"\nK12 retention | {lab}: cap 40 − cap 8 " + fmt(stats_line(d, "?")) + f" (equivalence needs |mean| < 0.05, CI within ±0.08)")
    d2 = np.array([PS["cap 40"][s][4][2] - PS["cap 8"][s][4][2] for s in ks if not np.isnan(PS["cap 40"][s][4][2] + PS["cap 8"][s][4][2])])
    O.append(f"\nK12 retention | >=2 anchors (the REGISTERED subgroup, '0 vs >=2'): cap 40 − cap 8 " + fmt(stats_line(d2, "?")) + f" (equivalence needs |mean| < 0.05, CI within ±0.08)")
# K11 adjacent-step contrasts, family-pooled per seed (the registration asked for monotonicity in every cell; these are the closest per-seed checks)
for lab in fams:
    if not PS.get(lab): continue
    for a, b, name in ((0, 1, "1 vs 0"), (1, 2, "2 vs 1"), (2, 3, "3+ vs 2")):
        d = np.array([v[3][b] - v[3][a] for v in PS[lab].values() if not np.isnan(v[3][a] + v[3][b])])
        if len(d) >= 2: O.append(f"K11 adjacent step {name}, {lab}: " + fmt(stats_line(d, ">")))
for lab in fams:
    if not PS.get(lab): continue
    ucu = np.nanmean([v[1] - v[5] for v in PS[lab].values()]); O.append(f"K10 untaught − chance (chance on untaught cases only), {lab}: {ucu:+.3f} (registered band ±0.10)")
open(f"{_KO}/confirmation2b.md", "w").write("\n".join(O) + "\n"); print("\n".join(O))
