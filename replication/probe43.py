"""probe43.py — anatomy of the basin (sibling symmetry breaking).   python probe43.py -> results_v3/probe43.md
 A siblings vs parent restricted to UNTAUGHT train objects (ARI and exact-form agreement)
 B what siblings jointly invent: forms agreed by both siblings but != parent — anchor's form / 1 symbol from an anchor / other
 C 'different records' arm: sibling agreement by anchoring stratum (anchored in both records / one / neither)
 D decay of partition similarity along a lineage (sweep): ARI at generation gaps 1..5, by cell"""
import glob, itertools, json, os
import numpy as np
from collections import Counter, defaultdict
from game import World
from lab import Cell, SELECTS, FRESHES
N = 64
from metrics import ari as _ari_std   # shared standard ARI (corrected 2026-09-05)
def ari(a, b): return np.nan if len(a) < 4 else _ari_std(a, b)
# siblings data: seeds 0-29 (probe41) + 30-44 (k16)
_P = json.load(open("results_v3_confirm2/k14_raw.json"))[0]
def parent(s):
    if s >= 30: return np.array(_P[str(s)][0])
    f = glob.glob(f"results_v3/*_seed{s}.json") + glob.glob(f"results_v3_confirm/*_seed{s}.json"); j = json.load(open(f[0])); r = [x for x in j["log"] if x["gen"] == 0][-1]; return np.array(r["language"])
R = {}
for f in ("results_v3/probe41_raw.json", "results_v3_confirm2/k16_raw.json"):
    for s, arm, i, l in json.load(open(f)): R[(s, arm, i)] = np.array(l)
SEEDS = sorted({s for s, _, _ in R}); worlds = {s: World(3, 4, 0.25, seed=s) for s in SEEDS}; TR = {s: np.isin(np.arange(N), worlds[s].train_idx) for s in SEEDS}
SD = {s: (worlds[s].objects[:, None, :] != worlds[s].objects[None, :, :]).sum(-1) for s in SEEDS}
def taught(s, arm, i):
    tr = np.array(worlds[s].train_idx)
    if arm == "none": return set()
    rng = np.random.RandomState(3000 + s) if arm == "same" else np.random.RandomState(3000 + s + 100 * i); return set(rng.choice(tr, 19, replace=False).tolist())
O = ["# probe43 — anatomy of the basin", ""]
# A
O += [f"## A. Restricted to objects UNTAUGHT in both siblings' records ({len(SEEDS)} seeds): ARI sibling–sibling vs child–parent; exact-form agreement", "",
      "| arm | untaught objs | ARI sib–sib | ARI child–parent | form agreement sib–sib | child–parent | sib−parent ARI: seeds > 0 |", "|---|---|---|---|---|---|---|"]
for arm in ("same", "different", "none"):
    ss, cp, fs, fp, n_, w = [], [], [], [], [], 0
    for s in SEEDS:
        lp = parent(s); a, b = R[(s, arm, 1)], R[(s, arm, 2)]; un = [o for o in worlds[s].train_idx if o not in taught(s, arm, 1) and o not in taught(s, arm, 2)]; n_.append(len(un))
        pa, pb, pp = [tuple(a[o]) for o in un], [tuple(b[o]) for o in un], [tuple(lp[o]) for o in un]
        x = ari(pa, pb); y = (ari(pa, pp) + ari(pb, pp)) / 2; ss.append(x); cp.append(y); w += x > y; fs.append(np.mean([p == q for p, q in zip(pa, pb)])); fp.append(np.mean([p == q for p, q in zip(pa, pp)] + [p == q for p, q in zip(pb, pp)]))
    O.append(f"| {arm} | {np.mean(n_):.0f} | {np.nanmean(ss):.3f} | {np.nanmean(cp):.3f} | {np.mean(fs):.2f} | {np.mean(fp):.2f} | {w}/{len(SEEDS)} |")
# B
O += ["", "## B. What siblings jointly invent (same-record arm): untaught objects where both siblings hold the SAME form ≠ parent's form. That form is: a taught anchor's form (H1 taught neighbour) / 1 symbol from an anchor's form / parent's form of some other H1 neighbour (untaught) / other", "", "| count | anchor's form | 1 symbol from anchor | untaught neighbour's parent form | other | (share of untaught objects that are joint inventions) |", "|---|---|---|---|---|---|"]
K = Counter(); tot_un = 0
for s in SEEDS:
    lp = parent(s); a, b = R[(s, "same", 1)], R[(s, "same", 2)]; T = taught(s, "same", 1)
    for o in worlds[s].train_idx:
        if o in T: continue
        tot_un += 1
        if not (a[o] == b[o]).all() or (a[o] == lp[o]).all(): continue
        f = a[o]; nb = [p for p in worlds[s].train_idx if p != o and SD[s][o, p] == 1]; anc = [p for p in nb if p in T]
        if any((lp[p] == f).all() for p in anc): K["anchor"] += 1
        elif any((lp[p] != f).sum() == 1 for p in anc): K["anchor1"] += 1
        elif any((lp[p] == f).all() for p in nb if p not in T): K["untaught_nb"] += 1
        else: K["other"] += 1
n = sum(K.values()); O.append(f"| {n} | {K['anchor']/n:.2f} | {K['anchor1']/n:.2f} | {K['untaught_nb']/n:.2f} | {K['other']/n:.2f} | {n/tot_un:.2f} |")
# C
O += ["", "## C. Different-records arm: sibling exact-form agreement and ARI by anchoring stratum of untaught objects (same-class anchor present in both records / in one / in neither)", "", "| stratum | objs | form agreement sib–sib | ARI sib–sib | (same-record arm, untaught with ≥1 same-class anchor) |", "|---|---|---|---|---|"]
S = defaultdict(lambda: defaultdict(list)); ref = []
for s in SEEDS:
    lp = parent(s); a, b = R[(s, "different", 1)], R[(s, "different", 2)]; T1, T2 = taught(s, "different", 1), taught(s, "different", 2)
    def sc(o, T): return any(p in T and (lp[p] == lp[o]).all() for p in worlds[s].train_idx if p != o and SD[s][o, p] == 1)
    groups = defaultdict(list)
    for o in worlds[s].train_idx:
        if o in T1 or o in T2: continue
        k = sc(o, T1) + sc(o, T2); groups["both" if k == 2 else ("one" if k == 1 else "neither")].append(o)
    for g, objs in groups.items():
        S[g]["n"].append(len(objs)); S[g]["agree"].append(np.mean([(a[o] == b[o]).all() for o in objs])); S[g]["ari"].append(ari([tuple(a[o]) for o in objs], [tuple(b[o]) for o in objs]))
    a2, b2 = R[(s, "same", 1)], R[(s, "same", 2)]; T = taught(s, "same", 1); objs = [o for o in worlds[s].train_idx if o not in T and sc(o, T)]
    if objs: ref.append(np.mean([(a2[o] == b2[o]).all() for o in objs]))
for g in ("both", "one", "neither"): O.append(f"| {g} | {np.mean(S[g]['n']):.1f} | {np.mean(S[g]['agree']):.2f} | {np.nanmean(S[g]['ari']):.3f} | {np.mean(ref):.2f} |")
# D
LOGS = {}
for d in ("results_v3", "results_v3_confirm"):
    for p in glob.glob(os.path.join(d, "*_seed*.json")):
        j = json.load(open(p)); LOGS[(Cell(**j["config"]["cell"]), j["config"]["seed"])] = j["log"]
def cell(sel, fr): return Cell("small", "gens", sel, "fixed" if sel == "random" else "dynamic", fr, 19, 0.0, "sender")
W30 = {s: World(3, 4, 0.25, seed=s) for s in range(30)}
O += ["", "## D. Decay of partition similarity along a lineage (sweep, 30 seeds): mean ARI between generations at gap 1..5, train objects; and ARI(gen 0, gen 5) vs product of consecutive ARIs (Markov expectation)", "", "| cell | gap 1 | gap 2 | gap 3 | gap 4 | gap 5 | ARI(0,5) / Π consecutive |", "|---|---|---|---|---|---|---|"]
for name, c in [("generations", Cell("small", "gens"))] + [(f"{a}+{b}", cell(a, b)) for a, b in itertools.product(SELECTS, FRESHES)]:
    G = defaultdict(list); ratio = []
    for s in range(30):
        if (c, s) not in LOGS: continue
        E = [r for r in LOGS[(c, s)] if "per_obj_acc" in r]; tr = W30[s].train_idx; P = [[tuple(np.array(r["language"])[o]) for o in tr] for r in E]
        for i, j in itertools.combinations(range(len(P)), 2): G[j - i].append(ari(P[i], P[j]))
        cons = [ari(P[i], P[i + 1]) for i in range(len(P) - 1)]; pr = np.prod(cons)
        if pr > 0.001: ratio.append(ari(P[0], P[-1]) / pr)
    O.append(f"| {name} | " + " | ".join(f"{np.mean(G[k]):.3f}" for k in range(1, 6)) + f" | {np.median(ratio) if ratio else float('nan'):.1f} |")
path = "results_v3/probe43.md"; open(path, "w").write("\n".join(O) + "\n"); print("\n".join(O)); print("wrote", path)
