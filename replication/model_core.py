"""model_core.py — the toy model's definitions (world, energy, reconstruct, anchors, sibling design), copied verbatim from model.py
so that follow-up scripts can import them WITHOUT re-running the original simulation or rewriting results_model/toy_results.md.
model.py is left untouched as the record of the original run (2026-09-05)."""
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
