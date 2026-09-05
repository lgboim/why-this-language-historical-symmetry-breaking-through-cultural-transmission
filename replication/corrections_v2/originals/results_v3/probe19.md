# probe19 — locality of drift, regular sound change, layers by capacity, morpheme frequency law

Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## A. Locality of semantic drift: consecutive generations, forms present in both

| cell | form-pairs | Jaccard(old, new extension) | new extension touches the old one (some Hamming-1 pair, or overlap) | if DISJOINT: adjacent to old | random set of same size adjacent |
|---|---|---|---|---|---|
| random+accumulate | 2354 | 0.36 | 0.91 | 0.69 | 0.39 |
| random+rewrite | 3391 | 0.49 | 0.94 | 0.67 | 0.29 |
| success+accumulate | 2019 | 0.32 | 0.90 | 0.68 | 0.39 |
| success+rewrite | 2714 | 0.43 | 0.93 | 0.65 | 0.35 |
| hard+accumulate | 2213 | 0.45 | 0.94 | 0.70 | 0.35 |
| hard+rewrite | 2367 | 0.48 | 0.94 | 0.68 | 0.34 |

## B. When an extension GROWS by one object (consecutive generations), along which attribute does the newcomer differ from the old members?

| cell | growth events | newcomer differs from some old member in exactly one attribute | that attribute = the parent's drop axis | expected if uniform |
|---|---|---|---|---|
| random+accumulate | 3427 | 0.67 | 0.40 | 0.33 |
| random+rewrite | 3271 | 0.70 | 0.46 | 0.33 |
| success+accumulate | 3572 | 0.66 | 0.36 | 0.33 |
| success+rewrite | 3688 | 0.70 | 0.40 | 0.33 |
| hard+accumulate | 3239 | 0.77 | 0.49 | 0.33 |
| hard+rewrite | 3041 | 0.75 | 0.49 | 0.33 |

## C. Regular sound change: among words whose symbol at position p changed between parent and child, is the substitution old→new systematic?

concentration = share of changed words at position p that follow the single most common substitution (old symbol → new symbol) in that transition; compared with shuffled new symbols.

| cell | transitions | changed symbols per transition & position | concentration | shuffled baseline | transitions where one substitution covers ≥ 50% |
|---|---|---|---|---|---|
| random+accumulate | 449 | 27.5 | 0.21 | 0.17 | 0.02 |
| random+rewrite | 447 | 19.6 | 0.25 | 0.22 | 0.06 |
| success+accumulate | 448 | 28.9 | 0.22 | 0.18 | 0.03 |
| success+rewrite | 444 | 21.6 | 0.28 | 0.23 | 0.08 |
| hard+accumulate | 444 | 19.6 | 0.30 | 0.24 | 0.12 |
| hard+rewrite | 436 | 18.5 | 0.30 | 0.25 | 0.11 |

## D. Which layer does a record transmit? Inheritance of roles / morphemes / words at capacity 8, 19, 40 (success+rewrite, seeds 0–9)

| capacity | n transitions | role stability (r) | morphemes conserved | words conserved (of 64) | held-out words conserved |
|---|---|---|---|---|---|
| 8 | 50 | +0.40 | 0.25 | 0.24 | 0.16 |
| 19 | 50 | +0.67 | 0.45 | 0.41 | 0.22 |
| 40 | 50 | +0.86 | 0.60 | 0.66 | 0.33 |

## E. Morpheme frequency law: associations supported by more objects survive to the child more often?

| cell | associations | support 4–6: survival | 7–10 | ≥ 11 | corr(support, survival) |
|---|---|---|---|---|---|
| random+accumulate | 1698 | 0.18 | 0.31 | 0.49 | +0.28 |
| random+rewrite | 1708 | 0.24 | 0.45 | 0.70 | +0.36 |
| success+accumulate | 1684 | 0.16 | 0.31 | 0.45 | +0.25 |
| success+rewrite | 1681 | 0.25 | 0.45 | 0.69 | +0.37 |
| hard+accumulate | 1627 | 0.20 | 0.42 | 0.65 | +0.37 |
| hard+rewrite | 1625 | 0.20 | 0.43 | 0.70 | +0.42 |

## F. Succession within a form: consecutive generations, a form that keeps existing but changes OWNER — was the new owner a former orphan of that form?

| cell | owner changes under a surviving form | new owner was in the old extension | new owner Hamming-1 to old owner |
|---|---|---|---|
| random+accumulate | 1460 | 0.34 | 0.61 |
| random+rewrite | 1549 | 0.41 | 0.71 |
| success+accumulate | 1327 | 0.32 | 0.55 |
| success+rewrite | 1480 | 0.40 | 0.69 |
| hard+accumulate | 1376 | 0.52 | 0.70 |
| hard+rewrite | 1439 | 0.55 | 0.72 |

## G. Cross-position mutual information vs held-out accuracy and structure (all 970 final languages)

- corr(cross-position MI, test_acc) = +0.17; corr(cross-position MI, topsim_distinct) = -0.16 (n = 970)

