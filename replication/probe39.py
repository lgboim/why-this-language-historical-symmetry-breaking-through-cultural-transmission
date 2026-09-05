"""probe39.py — stress-testing the distilled claim.   python probe39.py -> results_v3/probe39.md
 A 'not how many': structure at gen end by capacity (rewrite cells; seeds 0-9 + completed confirm2 seeds)
 B 'reconstruction from anchors' literally: predict the child's form for untaught objects from taught anchors + geometry; compare with 'copy parent'
 C 'same structure, different forms': partition similarity (ARI) parent vs child, no-record vs record cells vs random baseline
 D 'developmental state' literally: maturity of a record entry (earliest step in the parent's generation at which that form held) vs its fidelity and pull"""
import glob, itertools, json, os
import numpy as np
from collections import defaultdict, Counter
from scipy.optimize import linear_sum_assignment
from game import World
from lab import Cell, spearman, stats_line, fmt, SELECTS, FRESHES
N = 64; IU = np.triu_indices(N, 1)
worlds = {s: World(3, 4, 0.25, seed=s) for s in range(30)}; TR = {s: np.isin(np.arange(N), worlds[s].train_idx) for s in range(30)}
SD = {s: (worlds[s].objects[:, None, :] != worlds[s].objects[None, :, :]).sum(-1) for s in range(30)}; OD = {s: SD[s][IU] for s in range(30)}
LOGS = {}
for d in ("results_v3", "results_v3_confirm", "results_v3_confirm2"):
    for p in glob.glob(os.path.join(d, "*_seed*.json")):
        j = json.load(open(p)); LOGS[(Cell(**j["config"]["cell"]), j["config"]["seed"])] = j["log"]
def cell(sel, fr, cap=19): return Cell("small", "gens", sel, "fixed" if sel == "random" else "dynamic", fr, cap, 0.0, "sender")
GENS = Cell("small", "gens"); FOCUS = [(f"{s}+{f}", cell(s, f)) for s, f in itertools.product(SELECTS, FRESHES)]
def ends(c, s): return [r for r in LOGS[(c, s)] if "per_obj_acc" in r]
L = lambda r: np.array(r["language"]); D = lambda r: np.array(r["decode"])
def tsd(s, lang): md = (lang[:, None, :] != lang[None, :, :]).sum(-1)[IU]; k = md > 0; return spearman(OD[s][k], md[k]) if k.sum() > 2 else np.nan
def cbm(lang, w):
    M = np.zeros((24, 12))
    for o in range(N):
        for p in range(3):
            for a in range(3): M[p * 8 + lang[o, p], a * 4 + w.objects[o, a]] += 1
    r, c = linear_sum_assignment(-M); return M[r, c].sum() / (N * 3)
def paired(a, b):
    ks = sorted(k for k in set(a) & set(b) if not np.isnan(a[k] + b[k])); return fmt(stats_line(np.array([a[k] - b[k] for k in ks]), "?"))
O = ["# probe39 — stress-testing the distilled claim", ""]
# A
O += ["## A. 'Not how many': final-generation structure by capacity, rewrite cells (select pooled), paired by seed where both exist", "", "| capacity | seeds | topsim_distinct | CBM | n_owners | continuity proxy: parent form kept (untaught) |", "|---|---|---|---|---|---|"]
V = {}
for cap in (8, 19, 40):
    v = defaultdict(dict)
    for s in range(30):
        vals = []
        for sel in SELECTS:
            c = cell(sel, "rewrite", cap)
            if (c, s) not in LOGS: continue
            E = ends(c, s); l = L(E[-1]); lp = L(E[-2]); rec = {o for o, _, _ in E[-2]["record"]}; un = [o for o in np.where(TR[s])[0] if o not in rec]
            vals.append((tsd(s, l), cbm(l, worlds[s]), (D(E[-1]) == np.arange(N)).sum(), np.mean([(l[o] == lp[o]).all() for o in un])))
        if vals:
            m = np.mean(vals, 0)
            for i, k in enumerate(("t", "c", "o", "k")): v[k][s] = m[i]
    V[cap] = v; O.append(f"| {cap} | {len(v['t'])} | {np.mean(list(v['t'].values())):.3f} | {np.mean(list(v['c'].values())):.3f} | {np.mean(list(v['o'].values())):.1f} | {np.mean(list(v['k'].values())):.3f} |")
O += ["", "cap 8 − cap 19, topsim_distinct: " + paired(V[8]["t"], V[19]["t"]), "cap 40 − cap 19, topsim_distinct: " + paired(V[40]["t"], V[19]["t"]), "cap 8 − cap 19, CBM: " + paired(V[8]["c"], V[19]["c"]), "cap 40 − cap 19, CBM: " + paired(V[40]["c"], V[19]["c"]), ""]
# B
O += ["## B. Literal reconstruction: for each untaught train object, predict the child's final form. Predictors: (i) copy parent's form; (ii) nearest same-class anchor's form if any, else nearest taught neighbour's form (Hamming distance, ties by parent's form); (iii) anchor-or-parent: same-class anchor's form if any, else parent's form. Accuracy = exact match with the child's form", "",
      "| cell | n | copy parent | nearest anchor | anchor-or-parent | child form ∈ {any taught neighbour's form} |", "|---|---|---|---|---|---|"]
for name, c in FOCUS:
    a1, a2, a3, a4 = [], [], [], []
    for s in range(30):
        if (c, s) not in LOGS: continue
        E = ends(c, s)
        for g in range(1, len(E)):
            lp, lc = L(E[g - 1]), L(E[g]); rec = {o: tuple(m) for o, m, _ in E[g - 1]["record"]}; taught = [o for o, m in rec.items() if m == tuple(lp[o])]
            for o in np.where(TR[s])[0]:
                if o in rec: continue
                cf = tuple(lc[o]); a1.append(cf == tuple(lp[o]))
                h1 = [p for p in taught if SD[s][o, p] == 1]; same = [p for p in h1 if tuple(lp[p]) == tuple(lp[o])]
                if same: pred = tuple(lp[same[0]])
                elif taught: d = [SD[s][o, p] for p in taught]; pred = tuple(lp[taught[int(np.argmin(d))]])
                else: pred = tuple(lp[o])
                a2.append(cf == pred); a3.append(cf == (tuple(lp[same[0]]) if same else tuple(lp[o]))); a4.append(cf in {tuple(lp[p]) for p in h1})
    O.append(f"| {name} | {len(a1)} | {np.mean(a1):.3f} | {np.mean(a2):.3f} | {np.mean(a3):.3f} | {np.mean(a4):.3f} |")
# C
from metrics import ari   # shared standard ARI (corrected 2026-09-05; the old local copy returned 0 for identical singleton partitions)
O += ["", "## C. 'Same structure, different forms': adjusted Rand index between the parent's and the child's partition of train objects into form-classes, at generation ends; baseline = child partition vs a random permutation of the parent's partition; and share of forms shared", "",
      "| cell | ARI parent→child | baseline ARI | share of train objects keeping parent's form | ARI among objects that CHANGED form |", "|---|---|---|---|---|"]
rng = np.random.RandomState(0)
for name, c in [("generations (no record)", GENS)] + FOCUS:
    A_, B_, K_, C_ = [], [], [], []
    for s in range(30):
        if (c, s) not in LOGS: continue
        E = ends(c, s)
        for g in range(1, len(E)):
            lp, lc = L(E[g - 1]), L(E[g]); tr = np.where(TR[s])[0]; pa = [tuple(lp[o]) for o in tr]; ch = [tuple(lc[o]) for o in tr]
            A_.append(ari(pa, ch)); B_.append(ari([pa[i] for i in rng.permutation(len(pa))], ch)); K_.append(np.mean([p == q for p, q in zip(pa, ch)]))
            idx = [i for i, (p, q) in enumerate(zip(pa, ch)) if p != q]
            if len(idx) > 5: C_.append(ari([pa[i] for i in idx], [ch[i] for i in idx]))
    O.append(f"| {name} | {np.mean(A_):.3f} | {np.mean(B_):.3f} | {np.mean(K_):.2f} | {np.mean(C_):.3f} |")
# D
O += ["", "## D. 'Developmental state' literally (accumulate cells, gen 1 children of gen 0): maturity of a record entry = earliest step (250..2000) at which the parent's language held that form for that object continuously until... (first step it appeared). Child fidelity and pull by maturity", "",
      "| first step the form appeared in parent | entries | form == parent's final | child holds it @2000 | untaught H1 nbrs adopt it | untaught H1 nbrs keep parent's form |", "|---|---|---|---|---|---|"]
Rm = defaultdict(lambda: defaultdict(list))
for name, c in [(n, c) for n, c in FOCUS if c.fresh == "accumulate"]:
    for s in range(30):
        if (c, s) not in LOGS: continue
        log = LOGS[(c, s)]; g0 = {r["gen_step"]: L(r) for r in log if r["gen"] == 0 and r["gen_step"] % 250 == 0 and r["gen_step"] > 0}; E = ends(c, s)
        if len(E) < 2: continue
        lp, lc = L(E[0]), L(E[1]); rec = {o: tuple(m) for o, m, _ in E[0]["record"]}
        for o, m in rec.items():
            steps = [k for k in sorted(g0) if tuple(g0[k][o]) == m]
            if not steps: continue
            first = steps[0]; b = "≤500" if first <= 500 else ("750-1250" if first <= 1250 else "≥1500"); Rm[b]["n"].append(1); Rm[b]["fresh"].append(m == tuple(lp[o])); Rm[b]["hold"].append(tuple(lc[o]) == m)
            un = [p for p in np.where(TR[s])[0] if p != o and SD[s][o, p] == 1 and p not in rec]
            if un: Rm[b]["pull"].append(np.mean([tuple(lc[p]) == m and not (lc[p] == lp[p]).all() for p in un])); Rm[b]["keep"].append(np.mean([(lc[p] == lp[p]).all() for p in un]))
for b in ("≤500", "750-1250", "≥1500"): O.append(f"| {b} | {len(Rm[b]['n'])} | {np.mean(Rm[b]['fresh']):.2f} | {np.mean(Rm[b]['hold']):.2f} | {np.mean(Rm[b]['pull']):.3f} | {np.mean(Rm[b]['keep']):.3f} |")
path = "results_v3/probe39.md"; open(path, "w").write("\n".join(O) + "\n"); print("\n".join(O)); print("wrote", path)
