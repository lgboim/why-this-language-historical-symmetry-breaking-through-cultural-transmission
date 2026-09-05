"""model.py — formal toy model of anchored reconstruction on the Hamming graph (results_model/PREREG.md).   python model.py"""
import itertools, numpy as np
from collections import Counter
ATT, VAL = 3, 4; OBJ = np.array(list(itertools.product(range(VAL), repeat=ATT))); N = len(OBJ)
D = (OBJ[:, None, :] != OBJ[None, :, :]).sum(-1); NB = [np.where(D[i] == 1)[0] for i in range(N)]
C, LAM, W = 1.0, 6.0, 1.0      # collision cost, simplicity, smoothness (chosen so minimisers have ~10-25 classes; not tuned to outcomes)
def energy(P):
    cnt = Counter(P); within = sum(v * (v - 1) / 2 for v in cnt.values()); cut = sum(P[i] != P[j] for i in range(N) for j in NB[i] if j > i)
    return C * within + LAM * len(cnt) + W * cut
def reconstruct(anchors, rng, sweeps=30):
    """anchors: dict node -> fixed label. Greedy local search from a random init; anchored nodes never move."""
    P = rng.randint(0, N, N)
    for o, lab in anchors.items(): P[o] = lab
    for _ in range(sweeps):
        changed = False
        for i in rng.permutation(N):
            if i in anchors: continue
            cands = list({P[j] for j in NB[i]} | {P[i], max(P) + 1}); best, bestE = P[i], None
            for c in cands:
                old = P[i]; P[i] = c; e = energy(P); P[i] = old
                if bestE is None or e < bestE - 1e-9: best, bestE = c, e
            if best != P[i]: P[i] = best; changed = True
        if not changed: break
    return P
from metrics import ari   # shared standard ARI (corrected 2026-09-05; the old local copy returned 0 for identical singleton partitions)
def forms_of(P, rng):
    """surface forms: one random code per class (learner-specific)"""
    codes = {c: tuple(rng.randint(0, 8, 3)) for c in set(P)}; return [codes[c] for c in P]
def anchors_from(parentP, objs):
    """record = (object, form) pairs; objects with the same parent class share a label"""
    return {int(o): int(parentP[o]) for o in objs}
def sib(parentP, mode, s, k=19):
    rng = np.random.RandomState(s); tr = np.arange(N)
    if mode == "same": A1 = A2 = anchors_from(parentP, rng.choice(tr, k, replace=False))
    elif mode == "different": A1 = anchors_from(parentP, rng.choice(tr, k, replace=False)); A2 = anchors_from(parentP, rng.choice(tr, k, replace=False))
    else: A1 = A2 = {}
    return reconstruct(A1, np.random.RandomState(10 * s + 1)), reconstruct(A2, np.random.RandomState(10 * s + 2))
SEEDS = range(20); O = ["# Toy model — simulation results (20 seeds)", ""]
parents = {s: reconstruct({}, np.random.RandomState(1000 + s)) for s in SEEDS}
O.append(f"parents: {np.mean([len(set(P)) for P in parents.values()]):.1f} classes on average; energy minimisers are non-unique (ARI between two no-anchor learners of the same world = {np.mean([ari(reconstruct({}, np.random.RandomState(5*s+1)), reconstruct({}, np.random.RandomState(5*s+2))) for s in SEEDS]):.2f})")
# T1
res = {m: [] for m in ("same", "different", "none")}; cp = {m: [] for m in res}
for s in SEEDS:
    for m in res:
        a, b = sib(parents[s], m, s); res[m].append(ari(a, b)); cp[m].append((ari(a, parents[s]) + ari(b, parents[s])) / 2)
O += ["", "## T1 siblings", "| anchors | ARI sib–sib | ARI sib–parent |", "|---|---|---|"] + [f"| {m} | {np.mean(res[m]):.3f} | {np.mean(cp[m]):.3f} |" for m in res]
# T2 class-matched anchoring (emergent). Common outcome for every untaught object: does the child keep o with its parent classmates
# (o shares a child class with ≥1 Hamming-1 neighbour that was its classmate in the parent)? Compared across anchor situations.
keep = {"same-class anchor": [], "other-class anchors only": [], "no anchor": []}
for s in SEEDS:
    P = parents[s]; rng = np.random.RandomState(s); objs = rng.choice(N, 19, replace=False); A = anchors_from(P, objs); child = reconstruct(A, np.random.RandomState(77 + s))
    for o in range(N):
        if o in A: continue
        mates = [p for p in NB[o] if P[p] == P[o]]
        if not mates: continue
        anc = [p for p in NB[o] if p in A]; kept = any(child[o] == child[p] for p in mates)
        k = "same-class anchor" if any(P[p] == P[o] for p in anc) else ("other-class anchors only" if anc else "no anchor"); keep[k].append(kept)
O += ["", "## T2 class-matched anchoring (emergent): untaught object keeps its parent classmates", "| anchor situation | n | kept |", "|---|---|---|"] + [f"| {k} | {len(v)} | {np.mean(v):.2f} |" for k, v in keep.items()]
# T3 strength/target: early partition = a shallow search (few sweeps) from the parent's init
early = {s: reconstruct({}, np.random.RandomState(1000 + s), sweeps=1) for s in SEEDS}
ss_e, ss_f, tp_e, tp_f, te_e, te_f = [], [], [], [], [], []
for s in SEEDS:
    rng = np.random.RandomState(s); objs = rng.choice(N, 19, replace=False)
    for src, ss, tp, te in ((parents[s], ss_f, tp_f, te_f), (early[s], ss_e, tp_e, te_e)):
        A = anchors_from(src, objs); a, b = reconstruct(A, np.random.RandomState(10 * s + 1)), reconstruct(A, np.random.RandomState(10 * s + 2))
        ss.append(ari(a, b)); tp.append((ari(a, parents[s]) + ari(b, parents[s])) / 2); te.append((ari(a, early[s]) + ari(b, early[s])) / 2)
O += ["", "## T3 strength vs target", "| anchors from | ARI sib–sib | ARI to parent final | ARI to parent early |", "|---|---|---|---|", f"| final | {np.mean(ss_f):.3f} | {np.mean(tp_f):.3f} | {np.mean(te_f):.3f} |", f"| early | {np.mean(ss_e):.3f} | {np.mean(tp_e):.3f} | {np.mean(te_e):.3f} |",
      f"(early vs final partitions of the same parent: ARI {np.mean([ari(early[s], parents[s]) for s in SEEDS]):.2f})"]
# T4 persistence: 5 generations; rewrite = anchors from parent's final; accumulate = anchors from parent's early (frozen developmental state)
dec = {"rewrite": [], "accumulate": []}
for s in SEEDS:
    for mode in dec:
        P = parents[s]; founder = P; rng = np.random.RandomState(500 + s); traj = []
        for g in range(1, 6):
            src = P if mode == "rewrite" else reconstruct({}, np.random.RandomState(2000 + 10 * s + g), sweeps=1)   # accumulate: each generation's record is an early, immature partition
            A = anchors_from(src, rng.choice(N, 19, replace=False)); P = reconstruct(A, np.random.RandomState(300 + 10 * s + g)); traj.append(ari(P, founder))
        dec[mode].append(traj)
O += ["", "## T4 persistence (ARI to founder by generation)", "| record | g1 | g2 | g3 | g4 | g5 |", "|---|---|---|---|---|---|"] + [f"| {m} | " + " | ".join(f"{v:.3f}" for v in np.mean(dec[m], 0)) + " |" for m in dec]
open("results_model/toy_results.md", "w").write("\n".join(O) + "\n"); print("\n".join(O))
