"""metrics.py — shared, dependency-free partition metric.

ari(a, b): adjusted Rand index (Hubert & Arabie 1985) between two labelings of the same items, from the contingency table.
Conventions (the standard ones, as in scikit-learn's adjusted_rand_score):
  * identical partitions up to relabelling score 1.0, INCLUDING the degenerate cases where both partitions are all singletons or
    both are a single class (the earlier project copies returned 0.0 there; corrected 2026-09-05, see CORRECTIONS_PLAN_2026_09_05.md);
  * if the two partitions differ but the expected index equals the maximum index (e.g. one all-singletons, the other one class),
    the index is 0.0 (no information, no agreement above chance);
  * fewer than two items: 1.0 if identical labelings (trivially), else 0.0, by declared policy.
"""
from collections import Counter

def _comb2(x): return x * (x - 1) / 2.0

def ari(a, b):
    a, b = list(a), list(b)
    if len(a) != len(b): raise ValueError("ari: labelings must have the same length")
    n = len(a)
    if n < 2: return 1.0 if a == b else 0.0
    ct = Counter(zip(a, b)); A = Counter(a); B = Counter(b)
    sij = sum(_comb2(v) for v in ct.values()); sa = sum(_comb2(v) for v in A.values()); sb = sum(_comb2(v) for v in B.values())
    e = sa * sb / _comb2(n); mx = (sa + sb) / 2.0
    if mx == e:                      # both all-singletons, both one class, or one of each
        return 1.0 if len(A) == len(B) == len(ct) else 0.0   # identical partitions iff the contingency table is a permutation
    return (sij - e) / (mx - e)
