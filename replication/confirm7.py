"""confirm7.py — M1–M4 (results_medium/PREREG.md)."""
import glob, itertools, json, os, numpy as np
from collections import Counter
from game import World
from lab import Cell, spearman, stats_line, fmt, SELECTS, FRESHES
worlds = {s: World(4, 4, 0.25, seed=s) for s in range(10)}; N = 256; IU = np.triu_indices(N, 1)
TR = {s: np.isin(np.arange(N), worlds[s].train_idx) for s in worlds}; SD = {s: (worlds[s].objects[:, None, :] != worlds[s].objects[None, :, :]).sum(-1) for s in worlds}; OD = {s: SD[s][IU] for s in worlds}
LOGS = {}
for p in glob.glob("results_medium/*_seed*.json"):
    j = json.load(open(p)); LOGS[(Cell(**j["config"]["cell"]), j["config"]["seed"])] = j["log"]
def cell(sel, fr): return Cell("medium", "gens", sel, "fixed" if sel == "random" else "dynamic", fr, 77, 0.0, "sender")
GENS = Cell("medium", "gens"); L = lambda r: np.array(r["language"]); FC = [cell(a, b) for a, b in itertools.product(SELECTS, FRESHES)]
def ends(c, s): return [r for r in LOGS[(c, s)] if "per_obj_acc" in r]
from metrics import ari   # shared standard ARI (corrected 2026-09-05; the old local copy returned 0 for identical singleton partitions)
def tsd(s, lang): md = (lang[:, None, :] != lang[None, :, :]).sum(-1)[IU]; k = md > 0; return spearman(OD[s][k], md[k]) if k.sum() > 2 else np.nan
def nbrs(s, o): return np.where((SD[s][o] == 1) & TR[s])[0]
def run_ari(c, s): E = ends(c, s); tr = worlds[s].train_idx; return np.mean([ari([tuple(L(E[g - 1])[o]) for o in tr], [tuple(L(E[g])[o]) for o in tr]) for g in range(1, len(E))])
seeds = sorted({s for c, s in LOGS if c == GENS}); O = [f"# M1–M4: medium world (256 objects, hard_frac 0.5), seeds {seeds[0]}–{seeds[-1]}", ""]
m1, m3, m4, acc, ts, own = [], [], [], [], [], []
for s in seeds:
    same, other = [], []
    for c in FC:
        if (c, s) not in LOGS: continue
        E = ends(c, s)
        for g in range(1, len(E)):
            lp, lc = L(E[g - 1]), L(E[g]); rec = {o: tuple(m) for o, m, _ in E[g - 1]["record"]}
            for o in np.where(TR[s])[0]:
                if o in rec: continue
                anc = [p for p in nbrs(s, o) if p in rec and rec[p] == tuple(lp[p])]
                if not anc: continue
                (same if any(tuple(lp[p]) == tuple(lp[o]) for p in anc) else other).append((lc[o] == lp[o]).all())
    if same and other: m1.append(np.mean(same) - np.mean(other))
    rw = [run_ari(cell(sel, "rewrite"), s) for sel in SELECTS if (cell(sel, "rewrite"), s) in LOGS]
    if rw and (GENS, s) in LOGS: m3.append(np.mean(rw) - run_ari(GENS, s))
    a = [tsd(s, L(ends(cell(sel, "rewrite"), s)[-1])) - tsd(s, L(ends(cell(sel, "accumulate"), s)[-1])) for sel in ("random", "success") if (cell(sel, "rewrite"), s) in LOGS and (cell(sel, "accumulate"), s) in LOGS]
    if a: m4.append(np.mean(a))
    for c in FC + [GENS]:
        if (c, s) in LOGS: r = ends(c, s)[-1]; acc.append(r["test_acc"]); ts.append(tsd(s, L(r))); own.append((np.array(r["decode"]) == np.arange(N)).mean())
O += ["M1 same − other anchors (≥ 0.15): " + fmt(stats_line(np.array(m1), ">")) + (" → magnitude below the registered 0.15 band: DIRECTION SUPPORTED, MAGNITUDE NOT" if np.mean(m1) < 0.15 else " → magnitude ≥ 0.15 met"), "M3 parent–child ARI, rewrite − generations: " + fmt(stats_line(np.array(m3), ">")), "M4 rewrite − accumulate topsim_distinct: " + fmt(stats_line(np.array(m4), ">")),
      f"descriptive: held-out acc {np.mean(acc):.3f}, topsim_distinct {np.mean(ts):.3f}, owner share {np.mean(own):.2f}"]
if os.path.exists("results_medium/m2_raw.json"):
    sib = {(s, arm, i): np.array(l) for s, arm, i, l in json.load(open("results_medium/m2_raw.json"))}; P, Sd = [], []
    for s in seeds:
        if (s, "same", 1) not in sib: continue
        tr = worlds[s].train_idx; Pt = lambda l: [tuple(l[o]) for o in tr]; a = lambda arm: ari(Pt(sib[(s, arm, 1)]), Pt(sib[(s, arm, 2)]))
        P.append(a("same") - a("different")); Sd.append(a("different") - a("none"))
    O += ["M2 sibling ARI same − different (primary): " + fmt(stats_line(np.array(P), ">")), "M2 different − none (secondary): " + fmt(stats_line(np.array(Sd), ">"))]
open("results_medium/confirmation7.md", "w").write("\n".join(O) + "\n"); print("\n".join(O))
