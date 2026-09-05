# probe6 — sharpening: continuity, grammar inheritance, anatomy of mutation

Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## A. Continuity as a factorial result (seeds 0–9, all record cells)

founder = accuracy of the LAST generation's receiver with generation 0's sender (train objects, 5 candidates). roles = correlation of the position↔attribute role matrix between generation 0 and the last generation.

### founder intelligibility

| factor | A | B | n | wins/losses | mean diff | 95% CI | p | |
|---|---|---|---|---|---|---|---|---|
| select | hard | random | 10 | 1/9 | -0.034 | [-0.058, -0.012] | 0.021 | TWO-SIDED: A<B (CI) |
| select | hard | success | 10 | 10/0 | +0.052 | [+0.040, +0.065] | 0.002 | TWO-SIDED: A>B (CI) |
| select | random | success | 10 | 10/0 | +0.086 | [+0.071, +0.103] | 0.002 | TWO-SIDED: A>B (CI) |
| fresh | accumulate | rewrite | 10 | 0/10 | -0.130 | [-0.152, -0.110] | 0.002 | TWO-SIDED: A<B (CI) |
| capacity | 8 | 19 | 10 | 0/10 | -0.177 | [-0.206, -0.148] | 0.002 | TWO-SIDED: A<B (CI) |
| capacity | 8 | 40 | 10 | 0/10 | -0.398 | [-0.425, -0.366] | 0.002 | TWO-SIDED: A<B (CI) |
| capacity | 19 | 40 | 10 | 0/10 | -0.221 | [-0.240, -0.200] | 0.002 | TWO-SIDED: A<B (CI) |
| noise | 0.0 | 0.2 | 10 | 10/0 | +0.077 | [+0.064, +0.090] | 0.002 | TWO-SIDED: A>B (CI) |
| reader | both | sender | 10 | 8/2 | +0.016 | [+0.004, +0.027] | 0.109 | TWO-SIDED: A>B (CI) |

### role stability gen0→gen5

| factor | A | B | n | wins/losses | mean diff | 95% CI | p | |
|---|---|---|---|---|---|---|---|---|
| select | hard | random | 10 | 4/5 | +nan | [+nan, +nan] | 0.754 | TWO-SIDED: no difference (CI) |
| select | hard | success | 10 | 6/3 | +nan | [+nan, +nan] | 0.754 | TWO-SIDED: no difference (CI) |
| select | random | success | 10 | 8/2 | +0.142 | [+0.037, +0.257] | 0.109 | TWO-SIDED: A>B (CI) |
| fresh | accumulate | rewrite | 10 | 2/7 | +nan | [+nan, +nan] | 0.109 | TWO-SIDED: no difference (CI) |
| capacity | 8 | 19 | 10 | 1/8 | +nan | [+nan, +nan] | 0.021 | TWO-SIDED: no difference (CI) |
| capacity | 8 | 40 | 10 | 0/9 | +nan | [+nan, +nan] | 0.002 | TWO-SIDED: no difference (CI) |
| capacity | 19 | 40 | 10 | 0/10 | -0.290 | [-0.352, -0.229] | 0.002 | TWO-SIDED: A<B (CI) |
| noise | 0.0 | 0.2 | 10 | 9/0 | +nan | [+nan, +nan] | 0.021 | TWO-SIDED: no difference (CI) |
| reader | both | sender | 10 | 4/5 | +nan | [+nan, +nan] | 0.754 | TWO-SIDED: no difference (CI) |

No-transmission control: founder intelligibility 0.196, role stability +0.21. Across record cells: corr(founder intelligibility, final topsim) = +0.12; corr(role stability, final topsim) = +nan.

## B. Half-life of a language: intelligibility of receiver g with sender g−k (train objects), by k

| cell | k=0 | k=1 | k=2 | k=3 | k=4 | k=5 | half-life (generations, exp fit above chance) |
|---|---|---|---|---|---|---|---|
| generations | 0.97 | 0.22 | 0.22 | 0.21 | 0.23 | 0.22 | inf |
| random+accumulate | 0.96 | 0.72 | 0.71 | 0.67 | 0.62 | 0.46 | 4.4 |
| random+rewrite | 0.97 | 0.85 | 0.82 | 0.79 | 0.76 | 0.72 | 12.8 |
| success+accumulate | 0.94 | 0.66 | 0.64 | 0.61 | 0.55 | 0.40 | 3.7 |
| success+rewrite | 0.95 | 0.78 | 0.68 | 0.61 | 0.55 | 0.51 | 4.4 |
| hard+accumulate | 0.93 | 0.79 | 0.71 | 0.66 | 0.61 | 0.56 | 5.8 |
| hard+rewrite | 0.94 | 0.81 | 0.72 | 0.65 | 0.60 | 0.56 | 5.4 |

## C. Anatomy of a mutation (parent → child, train objects)

| cell | mutated objects | parent's receiver decodes the CHILD's message correctly: mutated | unmutated | mutation rate at the most informative position | least informative position |
|---|---|---|---|---|---|
| random+accumulate | 0.66 | 0.59 | 0.95 | 0.42 | 0.42 |
| random+rewrite | 0.48 | 0.73 | 0.96 | 0.23 | 0.35 |
| success+accumulate | 0.69 | 0.54 | 0.93 | 0.43 | 0.44 |
| success+rewrite | 0.52 | 0.64 | 0.94 | 0.31 | 0.34 |
| hard+accumulate | 0.49 | 0.65 | 0.92 | 0.25 | 0.34 |
| hard+rewrite | 0.45 | 0.67 | 0.93 | 0.23 | 0.30 |

## D. Do children preferentially replace ill-fitting inherited forms? (taught objects)

| cell | fit of forms the child KEPT | fit of forms the child CHANGED | changed − kept | | | | |
|---|---|---|---|---|---|---|---|
| random+accumulate | 0.270 | 0.267 | 30 | 16/14 | -0.003 | [-0.021, +0.015] | 0.856 | TWO-SIDED: no difference (CI) | |
| random+rewrite | 0.395 | 0.390 | 30 | 14/16 | -0.005 | [-0.022, +0.013] | 0.856 | TWO-SIDED: no difference (CI) | |
| success+accumulate | 0.321 | 0.279 | 30 | 7/23 | -0.041 | [-0.059, -0.024] | 0.005 | TWO-SIDED: A<B (CI) | |
| success+rewrite | 0.418 | 0.394 | 30 | 6/24 | -0.024 | [-0.039, -0.009] | 0.001 | TWO-SIDED: A<B (CI) | |
| hard+accumulate | 0.378 | 0.363 | 30 | 12/18 | -0.014 | [-0.028, -0.002] | 0.362 | TWO-SIDED: A<B (CI) | |
| hard+rewrite | 0.388 | 0.364 | 30 | 7/23 | -0.024 | [-0.035, -0.013] | 0.005 | TWO-SIDED: A<B (CI) | |

## E. Parent–child agreement on HELD-OUT objects (never taught, never trained) vs untaught training objects

| cell | held-out agreement | untaught-train agreement | held-out − untaught | | | | |
|---|---|---|---|---|---|---|---|
| random+accumulate | 0.20 | 0.25 | 30 | 9/21 | -0.053 | [-0.075, -0.032] | 0.043 | TWO-SIDED: A<B (CI) | |
| random+rewrite | 0.25 | 0.32 | 30 | 5/25 | -0.074 | [-0.100, -0.049] | 0.000 | TWO-SIDED: A<B (CI) | |
| success+accumulate | 0.20 | 0.22 | 30 | 12/18 | -0.019 | [-0.036, -0.002] | 0.362 | TWO-SIDED: A<B (CI) | |
| success+rewrite | 0.24 | 0.27 | 30 | 8/22 | -0.029 | [-0.048, -0.011] | 0.016 | TWO-SIDED: A<B (CI) | |
| hard+accumulate | 0.31 | 0.36 | 30 | 7/23 | -0.050 | [-0.079, -0.021] | 0.005 | TWO-SIDED: A<B (CI) | |
| hard+rewrite | 0.33 | 0.38 | 30 | 6/24 | -0.053 | [-0.080, -0.026] | 0.001 | TWO-SIDED: A<B (CI) | |

## F. Does the lineage settle? Mutation rate (share of 64 messages changed parent→child) by generation

| cell | g1 | g2 | g3 | g4 | g5 |
|---|---|---|---|---|---|
| random+accumulate | 0.96 | 0.65 | 0.63 | 0.63 | 0.62 |
| random+rewrite | 0.64 | 0.55 | 0.53 | 0.51 | 0.52 |
| success+accumulate | 0.96 | 0.68 | 0.64 | 0.65 | 0.68 |
| success+rewrite | 0.64 | 0.61 | 0.57 | 0.56 | 0.53 |
| hard+accumulate | 0.62 | 0.55 | 0.51 | 0.51 | 0.51 |
| hard+rewrite | 0.62 | 0.54 | 0.48 | 0.46 | 0.44 |

## G. Persistence inside one run (`pair`, 12k steps): share of objects keeping the same message over Δ steps, from step 6000

| Δ steps | 250 | 500 | 1000 | 2000 | 4000 | 6000 |
|---|---|---|---|---|---|---|
| pair | 0.69 | 0.64 | 0.62 | 0.56 | 0.54 | 0.46 |

## H. Rank of a held-out object under its own message, among all 64 (final agents)

| cell | n | median rank of held-out target | share ranked 1st | share ranked ≤ 5 | median rank of train targets |
|---|---|---|---|---|---|
| generations | 30 | 6 | 0.03 | 0.42 | 1 |
| random+accumulate | 30 | 8 | 0.01 | 0.34 | 1 |
| random+rewrite | 30 | 7 | 0.01 | 0.39 | 1 |
| success+accumulate | 30 | 9 | 0.00 | 0.29 | 2 |
| success+rewrite | 30 | 7 | 0.00 | 0.36 | 2 |
| hard+accumulate | 30 | 7 | 0.00 | 0.26 | 2 |
| hard+rewrite | 30 | 7 | 0.01 | 0.38 | 2 |
| pair | 30 | 9 | 0.01 | 0.30 | 1 |

