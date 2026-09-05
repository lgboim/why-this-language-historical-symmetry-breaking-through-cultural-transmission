"""confirm3.py — K13 and K15 (results_v3_confirm2/PREREG.md) on seeds 10-29.   python confirm3.py -> results_v3_confirm2/confirmation3.md"""
import glob, itertools, json, os, numpy as np
from collections import Counter, defaultdict
from game import World
from lab import Cell, stats_line, fmt, SELECTS, FRESHES
N = 64; worlds = {s: World(3, 4, 0.25, seed=s) for s in range(300)}; TR = {s: np.isin(np.arange(N), worlds[s].train_idx) for s in range(300)}
SD = {s: (worlds[s].objects[:, None, :] != worlds[s].objects[None, :, :]).sum(-1) for s in range(300)}
LOGS = {}
import os as _os
_KS = _os.environ.get("K_SEEDS"); _KO = _os.environ.get("K_OUT", "results_v3_confirm2")
def _seeds(default):
    return list(range(int(_KS.split("..")[0]), int(_KS.split("..")[1]) + 1)) if _KS else default
for d in ("results_v3_confirm", _KO):
    for p in glob.glob(os.path.join(d, "*_seed*.json")):
        j = json.load(open(p)); LOGS[(Cell(**j["config"]["cell"]), j["config"]["seed"])] = j["log"]
def cell(sel, fr, cap=19, noise=0.0, rd="sender"): return Cell("small", "gens", sel, "fixed" if sel == "random" else "dynamic", fr, cap, noise, rd)
GENS = Cell("small", "gens"); SEEDS = _seeds(list(range(10, 30))); L = lambda r: np.array(r["language"])
def ends(c, s): return [r for r in LOGS[(c, s)] if "per_obj_acc" in r]
from metrics import ari   # shared standard ARI (corrected 2026-09-05; the old local copy returned 0 for identical singleton partitions)
def run_ari(c, s):
    E = ends(c, s); tr = np.where(TR[s])[0]; return np.mean([ari([tuple(L(E[g - 1])[o]) for o in tr], [tuple(L(E[g])[o]) for o in tr]) for g in range(1, len(E))])
def fam_ari(cs, s):
    v = [run_ari(c, s) for c in cs if (c, s) in LOGS]; return np.mean(v) if v else np.nan
def k15(cs, s):
    same, other = [], []
    for c in cs:
        if (c, s) not in LOGS: continue
        E = ends(c, s)
        for g in range(1, len(E)):
            lp, lc = L(E[g - 1]), L(E[g]); rec = {o: tuple(m) for o, m, _ in E[g - 1]["record"]}
            for o in np.where(TR[s])[0]:
                if o in rec: continue
                anc = [p for p in np.where(TR[s])[0] if p != o and SD[s][o, p] == 1 and p in rec and rec[p] == tuple(lp[p])]
                if not anc: continue
                (same if any(tuple(lp[p]) == tuple(lp[o]) for p in anc) else other).append((lc[o] == lp[o]).all())
    return (np.mean(same) if same else np.nan), (np.mean(other) if other else np.nan)
fams = {"cap 8": (8, 0.0, "sender"), "cap 40": (40, 0.0, "sender"), "noise 0.2": (19, 0.2, "sender"), "reader both": (19, 0.0, "both")}
O = [f"# K13 / K15 on {_KO} (seeds {SEEDS[0]}–{SEEDS[-1]}), per seed", "", "## K13a: ARI rewrite cells − no-record generations cell", "", "| family | n | wins/losses | mean | 95% CI | p | verdict |", "|---|---|---|---|---|---|---|"]
for lab, (cap, noise, rd) in fams.items():
    rw = [cell(sel, "rewrite", cap, noise, rd) for sel in SELECTS]; d = np.array([fam_ari(rw, s) - run_ari(GENS, s) for s in SEEDS if (GENS, s) in LOGS and not np.isnan(fam_ari(rw, s))])
    O.append(f"| {lab} " + fmt(stats_line(d, ">")))
O += ["", "## K13b: ARI rewrite − accumulate within results_v3_confirm2 (random/success selection; hard exempt, shown for information)", "", "| family | select | n | wins/losses | mean | 95% CI | p | verdict |", "|---|---|---|---|---|---|---|---|"]
for lab, (cap, noise, rd) in fams.items():
    for sel in SELECTS:
        a, b = cell(sel, "rewrite", cap, noise, rd), cell(sel, "accumulate", cap, noise, rd); d = np.array([run_ari(a, s) - run_ari(b, s) for s in SEEDS if (a, s) in LOGS and (b, s) in LOGS])
        O.append(f"| {lab} | {sel} " + fmt(stats_line(d, ">")))
O += ["", "## K15: retention with ≥1 same-form taught neighbour − with only other-form taught neighbours (predicted gap ≥ 0.15)", "", "| family | n | wins/losses | mean | 95% CI | p | verdict | same / other |", "|---|---|---|---|---|---|---|---|"]
for lab, (cap, noise, rd) in fams.items():
    cs = [cell(sel, fr, cap, noise, rd) for sel, fr in itertools.product(SELECTS, FRESHES)]; v = {s: k15(cs, s) for s in SEEDS}; d = np.array([v[s][0] - v[s][1] for s in SEEDS if not np.isnan(v[s][0] + v[s][1])])
    O.append(f"| {lab} " + fmt(stats_line(d, ">")) + f" {np.nanmean([v[s][0] for s in SEEDS]):.2f} / {np.nanmean([v[s][1] for s in SEEDS]):.2f} |")
open(f"{_KO}/confirmation3.md", "w").write("\n".join(O) + "\n"); print("\n".join(O))
