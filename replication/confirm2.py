"""confirm2.py — evaluate K1–K9 (results_v3_confirm2/PREREG.md) on seeds 10–29, using results_v3_confirm for the
cap-19/noise-0/reader-sender partner cells.   python confirm2.py -> results_v3_confirm2/confirmation2.md"""
import glob, itertools, json, os
import numpy as np, torch
from collections import defaultdict
from scipy.optimize import linear_sum_assignment
from game import World, Sender, Receiver, GumbelSender, GumbelReceiver
from lab import Cell, spearman, stats_line, fmt, SELECTS, FRESHES, topsim
torch.set_num_threads(4)
LOGS, WPATH, ARCH = {}, {}, {}
import os as _os
_KS = _os.environ.get("K_SEEDS"); _KO = _os.environ.get("K_OUT", "results_v3_confirm2")
def _seeds(default):
    return list(range(int(_KS.split("..")[0]), int(_KS.split("..")[1]) + 1)) if _KS else default
for d in ("results_v3_confirm", _KO):
    for p in glob.glob(os.path.join(d, "*_seed*.json")):
        j = json.load(open(p)); k = (Cell(**j["config"]["cell"]), j["config"]["seed"]); LOGS[k] = j["log"]; ARCH[k] = j["config"].get("arch", "gru")
        if os.path.exists(p[:-5] + ".pt"): WPATH[k] = p[:-5] + ".pt"
worlds = {s: World(3, 4, 0.25, seed=s) for s in range(300)}; N = 64; IU = np.triu_indices(N, 1)
OD = {s: (worlds[s].objects[:, None, :] != worlds[s].objects[None, :, :]).sum(-1)[IU] for s in worlds}
SEEDS = _seeds(list(range(10, 30)))
def cell(sel, fresh, cap=19, noise=0.0, rd="sender"): return Cell("small", "gens", sel, "fixed" if sel == "random" else "dynamic", fresh, cap, noise, rd)
def tsd(s, lang):
    lang = np.asarray(lang); md = (lang[:, None, :] != lang[None, :, :]).sum(-1)[IU]; k = md > 0; return spearman(OD[s][k], md[k]) if k.sum() > 2 else np.nan
def cbm(lang, w):
    lang = np.asarray(lang); M = np.zeros((24, 12))
    for o in range(N):
        for p in range(3):
            for a in range(3): M[p * 8 + lang[o, p], a * 4 + w.objects[o, a]] += 1
    r, c = linear_sum_assignment(-M); return M[r, c].sum() / (N * 3)
def owners(r): return np.array(r["decode"]) == np.arange(N)
def own_ts(f, w): o = owners(f); return topsim(w.objects[o], np.array(f["language"])[o]) if o.sum() >= 4 else np.nan
def connected(w, idx):
    idx = list(idx)
    if len(idx) <= 1: return True
    seen = {idx[0]}; stack = [idx[0]]
    while stack:
        a = stack.pop()
        for b in idx:
            if b not in seen and (w.objects[a] != w.objects[b]).sum() == 1: seen.add(b); stack.append(b)
    return len(seen) == len(idx)
def convexity(lang, w):
    g = defaultdict(list)
    for o in range(N): g[tuple(lang[o])].append(o)
    v = [connected(w, x) for x in g.values() if len(x) >= 3]; return np.mean(v) if v else np.nan
_W = {}
def agents(c, s):
    if (c, s) not in _W:
        ws = torch.load(WPATH[(c, s)], weights_only=True); w = worlds[s]; out = []
        for d in ws:
            S_, R_ = (GumbelSender(w.dim, 8, 3, 64), GumbelReceiver(w.dim, 8, 3, 64)) if ARCH[(c, s)] == "gumbel" else (Sender(w.dim, 8, 3, 64), Receiver(w.dim, 8, 64)); S_.load_state_dict(d["sender"]); R_.load_state_dict(d["receiver"]); S_.eval(); R_.eval(); out.append((S_, R_))
        _W[(c, s)] = out
    return _W[(c, s)]
@torch.no_grad()
def cont(c, s):
    if (c, s) not in WPATH: return np.nan
    w = worlds[s]; S_, R_ = agents(c, s)[0][0], agents(c, s)[-1][1]; rng = np.random.RandomState(123); t, cc, lab = w.sample_batch(512, 4, "train", rng)
    return float((R_(S_(w.encode(t), greedy=True)[0], w.encode(cc.reshape(-1)).view(512, 5, w.dim)).argmax(-1).numpy() == lab).mean())
M = {"distinct": lambda c, s: tsd(s, LOGS[(c, s)][-1]["language"]), "CBM": lambda c, s: cbm(LOGS[(c, s)][-1]["language"], worlds[s]),
     "owners_topsim": lambda c, s: own_ts(LOGS[(c, s)][-1], worlds[s]), "continuity": cont, "n_owners": lambda c, s: float(owners(LOGS[(c, s)][-1]).sum()),
     "convexity": lambda c, s: convexity(np.array(LOGS[(c, s)][-1]["language"]), worlds[s]), "test_acc": lambda c, s: LOGS[(c, s)][-1]["test_acc"]}
def pdiff(m, A, B):
    d = []
    for s in SEEDS:
        va = [M[m](c, s) for c in A if (c, s) in LOGS]; vb = [M[m](c, s) for c in B if (c, s) in LOGS]; va = [x for x in va if not np.isnan(x)]; vb = [x for x in vb if not np.isnan(x)]
        if va and vb: d.append(np.mean(va) - np.mean(vb))
    return np.array(d)
SF = list(itertools.product(SELECTS, FRESHES))
C = lambda cap=19, noise=0.0, rd="sender": [cell(sel, fr, cap, noise, rd) for sel, fr in SF]
O = [f"# K1–K9 on {_KO} (seeds {SEEDS[0]}–{SEEDS[-1]})", "", "| id | test | metric | " + "n | wins/losses | mean diff | 95% CI | p | verdict |", "|---|---|---|---|---|---|---|---|---|"]
tests = [("K1", "cap 8 − cap 19", "distinct", C(8), C(19), "<"), ("K2", "cap 19 − cap 40", "distinct", C(19), C(40), "?"), ("K3", "cap 19 − cap 40", "CBM", C(19), C(40), ">"), ("K3", "cap 19 − cap 40", "owners_topsim", C(19), C(40), ">"),
         ("K4", "cap 40 − cap 19", "continuity", C(40), C(19), ">"), ("K4", "cap 19 − cap 8", "continuity", C(19), C(8), ">"), ("K6", "noise 0.2 − noise 0", "distinct", C(noise=0.2), C(), "<"), ("K6", "noise 0.2 − noise 0", "CBM", C(noise=0.2), C(), "<"),
         ("K7", "noise 0.2 − noise 0", "n_owners", C(noise=0.2), C(), ">"), ("K8", "both − sender", "distinct", C(rd="both"), C(), "?"), ("K8", "both − sender", "CBM", C(rd="both"), C(), "?"), ("K8", "both − sender", "test_acc", C(rd="both"), C(), "?"),
         ("K9", "accumulate − rewrite", "convexity", [cell(sel, "accumulate") for sel in SELECTS], [cell(sel, "rewrite") for sel in SELECTS], ">"), ("K9", "cap 8 − cap 40", "convexity", C(8), C(40), ">")]
for i, t, m, A, B, d in tests:
    x = pdiff(m, A, B); O.append(f"| {i} | {t} | {m} " + (fmt(stats_line(x, d)) if len(x) >= 2 else "| NOT TESTABLE |"))
# K5: correlations across cells
cells = C(8) + C(19) + C(40) + C(noise=0.2) + C(rd="both"); cm = {}
for m in ("continuity", "distinct", "convexity", "CBM"):
    cm[m] = np.array([np.nanmean([M[m](c, s) for s in SEEDS if (c, s) in LOGS]) for c in cells])
ok = ~np.isnan(cm["continuity"])
O += ["", f"K5: across {ok.sum()} cells, corr(continuity, distinct) = {np.corrcoef(cm['continuity'][ok], cm['distinct'][ok])[0,1]:+.2f}; corr(continuity, convexity) = {np.corrcoef(cm['continuity'][ok], cm['convexity'][ok])[0,1]:+.2f}; corr(continuity, CBM) = {np.corrcoef(cm['continuity'][ok], cm['CBM'][ok])[0,1]:+.2f}", ""]
# K8 fidelity
fid = []; fid_seed = []
for s in SEEDS:
    per_cell = []
    for sel, fr in SF:
        v = {}
        for rd in ("both", "sender"):
            c = cell(sel, fr, rd=rd)
            if (c, s) not in LOGS: continue
            E = [r for r in LOGS[(c, s)] if "per_obj_acc" in r]; x = []
            for g in range(1, len(E)):
                rec = {o: tuple(mm) for o, mm, _ in E[g - 1]["record"]}; lang = np.array(E[g]["language"]); x.append(np.mean([tuple(lang[o]) == mm for o, mm in rec.items()]))
            v[rd] = np.mean(x)
        if len(v) == 2: fid.append(v["both"] - v["sender"]); per_cell.append(v["both"] - v["sender"])
    if per_cell: fid_seed.append(np.mean(per_cell))
O.append(f"K8 fidelity of taught forms, both − sender (SEED as the unit: matched-cell differences averaged within seed first; correction 2026-09-05): " + (fmt(stats_line(np.array(fid_seed), ">")) if len(fid_seed) >= 2 else "NOT TESTABLE"))
O.append(f"K8 fidelity, original pooled seed×cell line (dependent observations; kept for the changelog only): " + (fmt(stats_line(np.array(fid), ">")) if len(fid) >= 2 else "NOT TESTABLE"))
path = f"{_KO}/confirmation2.md"; open(path, "w").write("\n".join(O) + "\n"); print("\n".join(O)); print("wrote", path)
