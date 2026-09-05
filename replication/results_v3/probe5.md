# probe5 — probes on the saved weights

Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## A. Cross-generation intelligibility (5-candidate game accuracy on training objects)

receiver of generation g plays with the sender of generation g−k. own = same generation.

| cell | n | own | parent (k=1) | grandparent (k=2) | founder (gen 0) | parent's receiver on child's sender |
|---|---|---|---|---|---|---|
| generations | 30 | 0.971 | 0.221 | 0.220 | 0.216 | 0.220 |
| random+accumulate | 30 | 0.954 | 0.718 | 0.708 | 0.453 | 0.714 |
| random+rewrite | 30 | 0.965 | 0.851 | 0.824 | 0.768 | 0.851 |
| success+accumulate | 30 | 0.938 | 0.659 | 0.636 | 0.397 | 0.667 |
| success+rewrite | 30 | 0.943 | 0.780 | 0.682 | 0.633 | 0.784 |
| hard+accumulate | 30 | 0.926 | 0.793 | 0.710 | 0.666 | 0.790 |
| hard+rewrite | 30 | 0.933 | 0.812 | 0.715 | 0.663 | 0.810 |

Chance = 0.20. 'parent' measures how much of the parent's language the child's receiver can still use; 'founder' whether anything of generation 0 survives.

## B. Sender confidence: probability of its own greedy message, train vs held-out objects

| cell | n | p(greedy) train | held-out | held-out − train | | | | | corr(confidence, per-object acc) train | held-out | share of held-out objects with a UNIQUE message |
|---|---|---|---|---|---|---|---|---|---|---|---|
| generations | 30 | 0.673 | 0.527 | 30 | 0/30 | -0.146 | [-0.171, -0.121] | 0.000 | TWO-SIDED: A<B (CI) | -0.02 | +0.11 | 0.38 |
| random+accumulate | 30 | 0.954 | 0.755 | 30 | 0/30 | -0.199 | [-0.220, -0.178] | 0.000 | TWO-SIDED: A<B (CI) | -0.12 | +0.20 | 0.07 |
| random+rewrite | 30 | 0.951 | 0.790 | 30 | 0/30 | -0.160 | [-0.185, -0.136] | 0.000 | TWO-SIDED: A<B (CI) | -0.14 | +0.24 | 0.11 |
| success+accumulate | 30 | 0.946 | 0.774 | 30 | 0/30 | -0.172 | [-0.194, -0.150] | 0.000 | TWO-SIDED: A<B (CI) | -0.16 | +0.13 | 0.07 |
| success+rewrite | 30 | 0.969 | 0.873 | 30 | 1/29 | -0.096 | [-0.120, -0.074] | 0.000 | TWO-SIDED: A<B (CI) | -0.08 | +0.16 | 0.03 |
| hard+accumulate | 30 | 0.958 | 0.882 | 30 | 2/28 | -0.076 | [-0.102, -0.051] | 0.000 | TWO-SIDED: A<B (CI) | -0.06 | +0.22 | 0.03 |
| hard+rewrite | 30 | 0.967 | 0.889 | 30 | 0/30 | -0.078 | [-0.098, -0.061] | 0.000 | TWO-SIDED: A<B (CI) | -0.10 | +0.17 | 0.03 |
| pair | 30 | 0.661 | 0.603 | 30 | 5/25 | -0.058 | [-0.079, -0.039] | 0.000 | TWO-SIDED: A<B (CI) | +nan | +0.05 | 0.49 |

## C. Grammar inheritance: stability of positional roles across generations

role matrix = MI(position, attribute) normalised per position; stability = correlation between consecutive generations' matrices. Also: share of generations whose dominant attribute per position matches the parent's.

| cell | n | role stability (r) | dominant-attribute match | within-run drift of roles in `pair` (first vs last eval) |
|---|---|---|---|---|
| generations | 30 | +0.03 | 0.38 | +0.78 (pair, mid-run vs end) |
| random+accumulate | 30 | +0.55 | 0.60 | +0.78 (pair, mid-run vs end) |
| random+rewrite | 30 | +0.74 | 0.70 | +0.78 (pair, mid-run vs end) |
| success+accumulate | 30 | +0.48 | 0.55 | +0.78 (pair, mid-run vs end) |
| success+rewrite | 30 | +0.71 | 0.70 | +0.78 (pair, mid-run vs end) |
| hard+accumulate | 30 | +0.78 | 0.72 | +0.78 (pair, mid-run vs end) |
| hard+rewrite | 30 | +0.82 | 0.80 | +0.78 (pair, mid-run vs end) |

## D. Spillover: parent–child agreement on UNTAUGHT training objects, by distance to the nearest taught object

| cell | n | dist 1 | dist 2 | dist 3 | taught objects (reference) |
|---|---|---|---|---|---|
| random+accumulate | 30 | 0.25 (4200) | 0.15 (150) | – | 0.47 |
| random+rewrite | 30 | 0.32 (4200) | 0.22 (150) | – | 0.83 |
| success+accumulate | 30 | 0.22 (4110) | 0.15 (240) | – | 0.44 |
| success+rewrite | 30 | 0.28 (4115) | 0.09 (235) | – | 0.80 |
| hard+accumulate | 30 | 0.37 (4198) | 0.12 (152) | – | 0.75 |
| hard+rewrite | 30 | 0.39 (4211) | 0.10 (139) | – | 0.80 |

## E. Homonym class sizes (final language)

| cell | n | classes | largest class | share of objects in classes ≥ 4 | entropy of message distribution (bits, max 6) |
|---|---|---|---|---|---|
| generations | 30 | 45.0 | 3.8 | 0.08 | 5.33 |
| random+accumulate | 30 | 27.1 | 6.7 | 0.41 | 4.48 |
| random+rewrite | 30 | 30.9 | 6.1 | 0.32 | 4.68 |
| success+accumulate | 30 | 24.7 | 8.0 | 0.53 | 4.27 |
| success+rewrite | 30 | 20.4 | 7.9 | 0.60 | 4.07 |
| hard+accumulate | 30 | 17.5 | 9.4 | 0.72 | 3.78 |
| hard+rewrite | 30 | 18.1 | 9.0 | 0.68 | 3.90 |
| pair | 30 | 52.5 | 3.5 | 0.04 | 5.59 |

## F. Receiver range when decoding over all 64 objects (final receiver)

| cell | n | distinct objects ever chosen | share of held-out objects ever chosen (of 16) | held-out objects decoded correctly |
|---|---|---|---|---|
| generations | 30 | 37.9 | 0.04 | 0.03 |
| random+accumulate | 30 | 26.0 | 0.01 | 0.01 |
| random+rewrite | 30 | 29.2 | 0.01 | 0.01 |
| success+accumulate | 30 | 23.7 | 0.01 | 0.00 |
| success+rewrite | 30 | 19.9 | 0.00 | 0.00 |
| hard+accumulate | 30 | 16.9 | 0.00 | 0.00 |
| hard+rewrite | 30 | 17.6 | 0.01 | 0.01 |
| pair | 30 | 44.3 | 0.01 | 0.01 |

## G. Symbol usage per position (final language): entropy in bits (max 3) and its within-seed correlation with topsim across all 77 cells

- corr(symbol entropy, topsim) within seed = -0.21

## H. Within a generation: receiver decode accuracy over all 64 (intelligibility) at each eval, generations ≥ 1

| cell | 250 | 500 | 1000 | 1500 | 2000 |
|---|---|---|---|---|---|
| generations | 0.07 | 0.17 | 0.34 | 0.45 | 0.52 |
| random+accumulate | 0.25 | 0.29 | 0.34 | 0.38 | 0.41 |
| random+rewrite | 0.31 | 0.35 | 0.41 | 0.44 | 0.46 |
| success+accumulate | 0.20 | 0.25 | 0.30 | 0.34 | 0.37 |
| success+rewrite | 0.24 | 0.28 | 0.33 | 0.36 | 0.37 |
| hard+accumulate | 0.21 | 0.24 | 0.27 | 0.29 | 0.32 |
| hard+rewrite | 0.21 | 0.25 | 0.28 | 0.31 | 0.33 |

