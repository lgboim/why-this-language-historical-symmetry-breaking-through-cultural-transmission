"""figures.py — the four main figures, from stored results.   python figures.py -> figs/fig1..fig4 (.png, .pdf)"""
import glob, itertools, json, os
import numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from collections import Counter, defaultdict
from game import World
from lab import Cell, spearman, SELECTS, FRESHES
N = 64; IU = np.triu_indices(N, 1); plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False})
worlds = {s: World(3, 4, 0.25, seed=s) for s in range(160)}; TR = {s: np.isin(np.arange(N), worlds[s].train_idx) for s in worlds}
SD = {s: (worlds[s].objects[:, None, :] != worlds[s].objects[None, :, :]).sum(-1) for s in worlds}; OD = {s: SD[s][IU] for s in worlds}
LOGS = {}
for d in ("results_v3", "results_v3_confirm", "results_v3_confirm2"):
    for p in glob.glob(os.path.join(d, "*_seed*.json")):
        j = json.load(open(p)); LOGS[(Cell(**j["config"]["cell"]), j["config"]["seed"])] = j["log"]
def cell(sel, fr, cap=19): return Cell("small", "gens", sel, "fixed" if sel == "random" else "dynamic", fr, cap, 0.0, "sender")
GENS = Cell("small", "gens"); L = lambda r: np.array(r["language"])
def ends(c, s): return [r for r in LOGS[(c, s)] if "per_obj_acc" in r]
def tsd(s, lang): md = (lang[:, None, :] != lang[None, :, :]).sum(-1)[IU]; k = md > 0; return spearman(OD[s][k], md[k]) if k.sum() > 2 else np.nan
from metrics import ari   # shared standard ARI (corrected 2026-09-05; the old local copy returned 0 for identical singleton partitions)
def gen0_parent(s):
    """the generation-0 parent of the discovery seeds (0-29): the `small__generations` run only (a glob on *_seed{s}.json also matched long-generation files for seeds 4 and 24; corrected 2026-09-05). Returns {gen_step: language}."""
    f = glob.glob(f"results_v3/small__generations_seed{s}.json") + glob.glob(f"results_v3_confirm/small__generations_seed{s}.json"); j = json.load(open(f[0]))
    return {r["gen_step"]: np.array(r["language"]) for r in j["log"] if r["gen"] == 0}
def nbrs(s, o): return [p for p in np.where(TR[s])[0] if p != o and SD[s][o, p] == 1]
def sem(x): x = np.asarray(x, float); return x.std(ddof=1) / np.sqrt(len(x)) if len(x) > 1 else 0.0
def seed_stats(d):
    """d: dict seed -> list of observations; returns (mean of per-seed means, s.e.m. over seeds, n seeds). Seeds with no eligible observation are dropped and counted."""
    m = [np.mean(v) for v in d.values() if len(v)]; return (np.mean(m), sem(m), len(m)) if m else (np.nan, 0.0, 0)
STATS = {}   # statistics quoted in captions/changelog
OUTDIR = os.environ.get("FIG_OUT", "figs_v2"); os.makedirs(OUTDIR, exist_ok=True)
def save(fig, name): fig.savefig(f"{OUTDIR}/{name}.png", dpi=200, bbox_inches="tight"); fig.savefig(f"{OUTDIR}/{name}.pdf", bbox_inches="tight"); plt.close(fig); print("saved", name)

# ---------------- Fig 1: Snapshot Effect
fig, ax = plt.subplots(1, 4, figsize=(16, 3.4))
acc, rew = [], []
for s in range(30):
    a = [tsd(s, L(ends(cell(sel, "accumulate"), s)[-1])) for sel in ("random", "success") if (cell(sel, "accumulate"), s) in LOGS]
    r = [tsd(s, L(ends(cell(sel, "rewrite"), s)[-1])) for sel in ("random", "success") if (cell(sel, "rewrite"), s) in LOGS]
    if a and r: acc.append(np.mean(a)); rew.append(np.mean(r))
for x, y in zip(acc, rew): ax[0].plot([0, 1], [x, y], color="grey", alpha=0.5, lw=0.8)
ax[0].plot([0, 1], [np.mean(acc), np.mean(rew)], "o-", color="black", lw=2); ax[0].set_xticks([0, 1]); ax[0].set_xticklabels(["accumulated\n(immature snapshot)", "rewritten\n(mature)"]); ax[0].set_ylabel("topsim_distinct, final generation"); d4a = np.array(rew) - np.array(acc); STATS["fig4a_rewrite_minus_accumulate"] = (float(d4a.mean()), float(sem(d4a)), len(d4a), int((d4a > 0).sum()))
ax[0].set_title(f"a  Snapshot effect (H3/C4), n={len(acc)}", loc="left", fontsize=9)
tr = {fr: defaultdict(lambda: defaultdict(list)) for fr in FRESHES}   # fr -> step -> seed -> obs
for fr in FRESHES:
    for sel in ("random", "success"):
        c = cell(sel, fr)
        for s in range(30):
            if (c, s) not in LOGS: continue
            by = defaultdict(dict)
            for r in LOGS[(c, s)]:
                if r["gen_step"] % 250 == 0 and r["gen_step"] > 0: by[r["gen"]][r["gen_step"]] = r
            E = ends(c, s)
            for g in range(1, len(E)):
                rec = {o: tuple(m) for o, m, _ in E[g - 1]["record"]}
                for k, r in by[g].items(): tr[fr][k][s].append(np.mean([tuple(L(r)[o]) == m for o, m in rec.items()]))
for fr, lab, col in (("rewrite", "mature anchors", "tab:blue"), ("accumulate", "immature anchors", "tab:red")):
    ks = sorted(tr[fr]); st = [seed_stats(tr[fr][k]) for k in ks]; ax[1].errorbar(ks, [a for a, b, n in st], yerr=[b for a, b, n in st], label=f"{lab} (n={st[0][2]} seeds)", color=col, marker="o", ms=3)
    STATS[f"fig4b_final_fidelity_{fr}"] = st[-1]
ax[1].set_xlabel("step within generation"); ax[1].set_ylabel("share of taught forms still produced"); ax[1].legend(frameon=False); ax[1].set_title("b  Erosion of the record", loc="left", fontsize=9)
caps, vals, errs = (8, 19, 40), [], []
for cap in caps:
    d = defaultdict(list)
    for sel in ("random", "success"):
        for s in range(10, 30):
            a, b = cell(sel, "rewrite", cap), cell(sel, "accumulate", cap)
            if (a, s) not in LOGS or (b, s) not in LOGS: continue
            def run_ari(c):
                E = ends(c, s); trn = np.where(TR[s])[0]; return np.mean([ari([tuple(L(E[g - 1])[o]) for o in trn], [tuple(L(E[g])[o]) for o in trn]) for g in range(1, len(E))])
            d[s].append(run_ari(a) - run_ari(b))
    m_, e_, n_ = seed_stats(d); vals.append(m_); errs.append(e_); STATS[f"fig4c_cap{cap}"] = (m_, e_, n_)
ax[2].bar(range(3), vals, yerr=errs, color=["tab:red", "grey", "tab:blue"]); ax[2].axhline(0, color="black", lw=0.8); ax[2].set_xticks(range(3)); ax[2].set_xticklabels([f"capacity {c}" for c in caps]); ax[2].set_ylabel("ARI(parent, child): mature − immature"); ax[2].set_title(f"c  Coverage boundary (K13b)", loc="left", fontsize=9)
# item-level: same objects, same parent, record form = step-500 snapshot vs final → child keeps parent's FINAL form (taught objects)
IT = {"fresh": defaultdict(list), "stale": defaultdict(list)}
for f in ("results_v3/probe44_raw.json", "results_v3_confirm2/k17_raw.json", "results_replicate/k14_k17_power_raw.json"):
    data = json.load(open(f)); PP = None
    if isinstance(data[0], dict): PP, data = data
    Rr = {(s, arm, i): np.array(l) for s, arm, i, l in data if arm in ("fresh", "stale")}
    for s in sorted({s for s, _, _ in Rr}):
        if PP: v = PP[str(s)]; lf = np.array(v[1] if len(v) == 2 else v[0])
        else:
            lf = gen0_parent(s)[2000]
        objs = np.sort(np.random.RandomState(3000 + s).choice(np.array(worlds[s].train_idx), 19, replace=False))
        for arm in IT:
            for i in (1, 2): IT[arm][s].append(np.mean([(Rr[(s, arm, i)][o] == lf[o]).all() for o in objs]))
S4d = {arm: seed_stats(IT[arm]) for arm in IT}; STATS["fig4d"] = S4d
ax[3].bar([0, 1], [S4d["fresh"][0], S4d["stale"][0]], yerr=[S4d["fresh"][1], S4d["stale"][1]], color=["tab:blue", "tab:red"]); ax[3].set_xticks([0, 1]); ax[3].set_xticklabels(["taught mature\nform", "taught step-500\nform"]); ax[3].set_ylabel("child ends with parent's final form (taught objects)"); ax[3].set_title(f"d  Item level: same objects, same parent (n={S4d['fresh'][2]} seeds, s.e.m. over seeds)", loc="left", fontsize=9)
save(fig, "fig4_snapshot")

# ---------------- Fig 2: anchoring mechanism
fig, ax = plt.subplots(1, 3, figsize=(12.5, 3.4)); FC = [cell(a, b) for a, b in itertools.product(SELECTS, FRESHES)]
R = defaultdict(lambda: defaultdict(list)); Q = defaultdict(list); CH = defaultdict(lambda: defaultdict(list))
for c in FC:
    for s in range(30):
        if (c, s) not in LOGS: continue
        E = ends(c, s)
        for g in range(1, len(E)):
            lp, lc = L(E[g - 1]), L(E[g]); rec = {o: tuple(m) for o, m, _ in E[g - 1]["record"]}
            for o in np.where(TR[s])[0]:
                if o in rec: continue
                anc = [p for p in nbrs(s, o) if p in rec and rec[p] == tuple(lp[p])]; k = len(anc); ret = (lc[o] == lp[o]).all()
                if k == 0: R[("none", 0)][s].append(ret)
                else:
                    same = any((lp[p] == lp[o]).all() for p in anc); R[("same" if same else "other", min(k, 3))][s].append(ret)
                forms = {tuple(lp[p]) for p in nbrs(s, o)}
                if tuple(lp[o]) in forms and len(forms) >= 2:
                    src = [p for p in nbrs(s, o) if tuple(lp[p]) == tuple(lp[o])]; taught = any(p in rec and rec[p] == tuple(lp[p]) for p in src); CH["taught" if taught else "untaught"][s].append(ret)
                    if not taught: CH["chance"][s].append(1 / len(forms))   # chance reference on the same untaught-source cases as the bar it is compared with (corrected 2026-09-05)
st0 = seed_stats(R[("none", 0)]); ax[0].errorbar([0], [st0[0]], yerr=[st0[1]], fmt="o", color="black", label="no anchor"); STATS["fig2a_none"] = st0
for lab, col in (("same", "tab:green"), ("other", "tab:orange")):
    ks = [k for k in (1, 2, 3) if R[(lab, k)]]; st = {k: seed_stats(R[(lab, k)]) for k in ks}; ax[0].errorbar(ks, [st[k][0] for k in ks], yerr=[st[k][1] for k in ks], marker="o", color=col, label=f"≥1 {lab}-form anchor" if lab == "same" else "other-form anchors only")
    for k in ks: STATS[f"fig2a_{lab}_{k}"] = st[k]
ax[0].set_xticks([0, 1, 2, 3]); ax[0].set_xticklabels(["0", "1", "2", "3+"]); ax[0].set_xlabel("taught neighbours of an untaught object"); ax[0].set_ylabel("parent's form retained by child"); ax[0].legend(frameon=False, fontsize=8); ax[0].set_title(f"a  Class-matched anchoring (K11, K15); s.e.m. over {st0[2]} seeds", loc="left", fontsize=9)
S2b = {k: seed_stats(CH[k]) for k in ("taught", "untaught", "chance")}; STATS["fig2b"] = S2b
ax[1].bar([0, 1, 2], [S2b[k][0] for k in ("taught", "untaught", "chance")], yerr=[S2b[k][1] for k in ("taught", "untaught", "chance")], color=["tab:green", "tab:orange", "lightgrey"]); ax[1].set_xticks([0, 1, 2]); ax[1].set_xticklabels(["source\ntaught", "source\nuntaught", "chance"]); ax[1].set_ylabel("child repeats parent's choice of neighbour"); ax[1].set_title("b  Anchored choice (K10)", loc="left", fontsize=9)
for cap, col in ((8, "tab:red"), (19, "grey"), (40, "tab:blue")):
    Rk = defaultdict(lambda: defaultdict(list)); cov = []
    for sel, fr in itertools.product(SELECTS, FRESHES):
        c = cell(sel, fr, cap)
        for s in range(30):
            if (c, s) not in LOGS: continue
            E = ends(c, s)
            for g in range(1, len(E)):
                lp, lc = L(E[g - 1]), L(E[g]); rec = {o: tuple(m) for o, m, _ in E[g - 1]["record"]}
                for o in np.where(TR[s])[0]:
                    if o in rec: continue
                    k = sum(p in rec and rec[p] == tuple(lp[p]) for p in nbrs(s, o)); Rk[min(k, 3)][s].append((lc[o] == lp[o]).all()); cov.append(k)
    ks = [k for k in range(4) if sum(len(v) for v in Rk[k].values()) >= 30]; st = {k: seed_stats(Rk[k]) for k in ks}; ax[2].errorbar(ks, [st[k][0] for k in ks], yerr=[st[k][1] for k in ks], marker="o", color=col, label=f"capacity {cap} (mean anchors {np.mean(cov):.1f}; n={min(st[k][2] for k in ks)}–{max(st[k][2] for k in ks)} seeds)")
    for k in ks: STATS[f"fig2c_cap{cap}_{k}"] = st[k]
ax[2].set_xticks([0, 1, 2, 3]); ax[2].set_xticklabels(["0", "1", "2", "3+"]); ax[2].set_xlabel("taught neighbours"); ax[2].set_ylabel("parent's form retained"); ax[2].legend(frameon=False, fontsize=8); ax[2].set_title("c  Capacity and coverage (K1, K12); s.e.m. over seeds", loc="left", fontsize=9)
save(fig, "fig2_anchors")

# ---------------- Fig 3: siblings (symmetry breaking)
sib = {}
for f in ("results_v3/probe41_raw.json", "results_v3_confirm2/k16_raw.json"):
    for s, arm, i, l in json.load(open(f)): sib[(s, arm, i)] = np.array(l)
_P = json.load(open("results_v3_confirm2/k14_raw.json"))[0]
def parent(s):
    if s >= 30: return np.array(_P[str(s)][0])
    return gen0_parent(s)[2000]
seeds = sorted({s for s, _, _ in sib}); ss, cp = defaultdict(list), defaultdict(list)
for arm in ("same", "different", "none"):
    for s in seeds:
        trn = worlds[s].train_idx; a, b, lp = sib[(s, arm, 1)], sib[(s, arm, 2)], parent(s); P = lambda l: [tuple(l[o]) for o in trn]
        ss[arm].append(ari(P(a), P(b))); cp[arm].append((ari(P(a), P(lp)) + ari(P(b), P(lp))) / 2)
fig, ax = plt.subplots(1, 3, figsize=(13.5, 3.4), gridspec_kw={"wspace": 0.3}); arms = ("same", "different", "none"); labs = ["same\nrecord", "different\nrecords", "no\nrecord"]
ax[0].bar(range(3), [np.mean(ss[a]) for a in arms], yerr=[sem(ss[a]) for a in arms], color=["tab:blue", "tab:orange", "lightgrey"]); ax[0].set_xticks(range(3)); ax[0].set_xticklabels(labs); ax[0].set_ylabel("ARI between two independent siblings"); ax[0].set_title(f"a  Symmetry breaking (K16), n={len(seeds)}", loc="left", fontsize=9)
w = 0.38; x = np.arange(3)
ax[1].bar(x - w / 2, [np.mean(ss[a]) for a in arms], w, yerr=[sem(ss[a]) for a in arms], label="sibling–sibling", color="tab:blue"); ax[1].bar(x + w / 2, [np.mean(cp[a]) for a in arms], w, yerr=[sem(cp[a]) for a in arms], label="sibling–parent", color="tab:purple")
ax[1].set_xticks(x); ax[1].set_xticklabels(labs); ax[1].legend(frameon=False, fontsize=8); ax[1].set_title("b  Siblings converge on each other, not the parent", loc="left", fontsize=9)
# panel c: form-level agreement, GRU (seeds 0-29) vs Gumbel MLP (seeds 120-159)
FA = {"GRU": defaultdict(list), "Gumbel MLP": defaultdict(list)}
for s in range(30):
    trn = worlds[s].train_idx
    for arm in arms: FA["GRU"][arm].append(np.mean([(sib[(s, arm, 1)][o] == sib[(s, arm, 2)][o]).all() for o in trn]))
for fpath in glob.glob("results_arch*/k14_k17_power_raw.json"):
    Pp, res = json.load(open(fpath)); G = {(s, arm, i): np.array(l) for s, arm, i, l in res if s >= 120}
    for s in sorted({s for s, _, _ in G}):
        trn = worlds[s].train_idx
        for arm, key in (("same", "fresh"), ("different", "different"), ("none", "none")):
            if (s, key, 1) in G: FA["Gumbel MLP"][arm].append(np.mean([(G[(s, key, 1)][o] == G[(s, key, 2)][o]).all() for o in trn]))
for i, (lab, col) in enumerate((("GRU", "tab:blue"), ("Gumbel MLP", "tab:green"))):
    ax[2].bar(x + (i - 0.5) * w, [np.mean(FA[lab][a]) for a in arms], w, yerr=[sem(FA[lab][a]) for a in arms], label=lab, color=col)
ax[2].set_xticks(x); ax[2].set_xticklabels(labs); ax[2].set_ylabel("share of objects with identical forms (siblings)"); ax[2].legend(frameon=False, fontsize=8); ax[2].set_title("c  Same pattern in a second learner (A3′; form level)", loc="left", fontsize=9)
save(fig, "fig1_siblings")

# ---------------- Fig 4: dissociation (K17)
V = {arm: {"ss": [], "cp": [], "c5": []} for arm in ("fresh", "stale")}
for f in ("results_v3/probe44_raw.json", "results_v3_confirm2/k17_raw.json"):
    data = json.load(open(f)); P17 = None
    if isinstance(data[0], dict): P17, data = data
    R44 = {(s, arm, i): np.array(l) for s, arm, i, l in data}
    for s in sorted({s for s, _, _ in R44}):
        if P17: l5, lf = np.array(P17[str(s)][0]), np.array(P17[str(s)][1])
        else:
            Lg = gen0_parent(s); l5, lf = Lg[500], Lg[2000]
        trn = worlds[s].train_idx; P = lambda l: [tuple(l[o]) for o in trn]
        for arm in V:
            a, b = R44[(s, arm, 1)], R44[(s, arm, 2)]; V[arm]["ss"].append(ari(P(a), P(b))); V[arm]["cp"].append((ari(P(a), P(lf)) + ari(P(b), P(lf))) / 2); V[arm]["c5"].append((ari(P(a), P(l5)) + ari(P(b), P(l5))) / 2)
fig, ax = plt.subplots(figsize=(6, 3.3)); x = np.arange(3); w = 0.38; keys = ("ss", "cp", "c5"); labs = ["sibling–sibling\n(coordination)", "to parent's final\nlanguage", "to parent's\nstep-500 snapshot"]
for i, (arm, col, lab) in enumerate((("fresh", "tab:blue", "mature anchors"), ("stale", "tab:red", "immature anchors"))):
    ax.bar(x + (i - 0.5) * w, [np.mean(V[arm][k]) for k in keys], w, yerr=[sem(V[arm][k]) for k in keys], label=lab, color=col)
ax.set_xticks(x); ax.set_xticklabels(labs); ax.set_ylabel("adjusted Rand index"); ax.legend(frameon=False); ax.set_title(f"Coordination strength vs target (K17a/K17c); n={len(V['fresh']['ss'])}: 30 discovery + 15 pre-registered", loc="left", fontsize=8)
save(fig, "fig3_dissociation")

json.dump({k: (list(v) if not isinstance(v, dict) else {kk: list(vv) for kk, vv in v.items()}) for k, v in STATS.items()}, open(f"{OUTDIR}/figure_stats.json", "w"), indent=1); print(json.dumps({k: (list(np.round(v, 4)) if not isinstance(v, dict) else {kk: list(np.round(vv, 4)) for kk, vv in v.items()}) for k, v in STATS.items()}, indent=1))
