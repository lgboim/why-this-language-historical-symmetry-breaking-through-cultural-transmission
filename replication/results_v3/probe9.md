# probe9 — the sociology of words: owners and orphans

owner = the receiver decodes the object's own message back to it (over all 64). Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## A. Who owns a word? (final generation, training objects)

| cell | n | owners among train (of 48) | # training neighbours: owners | orphans | in the record: owners | orphans | per-object acc: owners | orphans | owners among held-out (of 16) |
|---|---|---|---|---|---|---|---|---|---|
| generations | 30 | 35.9 | 6.70 | 6.78 | nan | nan | 1.000 | 0.923 | 0.5 |
| random+accumulate | 30 | 25.5 | 6.75 | 6.69 | 0.41 | 0.38 | 1.000 | 0.894 | 0.1 |
| random+rewrite | 30 | 28.8 | 6.78 | 6.64 | 0.42 | 0.36 | 1.000 | 0.907 | 0.2 |
| success+accumulate | 30 | 23.1 | 6.86 | 6.59 | 0.38 | 0.41 | 1.000 | 0.880 | 0.0 |
| success+rewrite | 30 | 19.6 | 6.75 | 6.70 | 0.44 | 0.36 | 1.000 | 0.878 | 0.0 |
| hard+accumulate | 30 | 16.6 | 6.91 | 6.62 | 0.32 | 0.44 | 1.000 | 0.849 | 0.0 |
| hard+rewrite | 30 | 17.3 | 6.81 | 6.67 | 0.34 | 0.43 | 1.000 | 0.867 | 0.1 |
| pair | 30 | 44.1 | 6.71 | 6.81 | nan | nan | 1.000 | 0.915 | 0.1 |

## B. Is ownership inherited? (parent status → child status, training objects)

| cell | transitions | P(child owner | parent owner) | P(child owner | parent orphan) | difference | | | | |
|---|---|---|---|---|---|---|---|---|
| random+accumulate | 150 | 0.58 | 0.50 | 30 | 23/7 | +0.084 | [+0.050, +0.116] | 0.005 | TWO-SIDED: A>B (CI) | |
| random+rewrite | 150 | 0.66 | 0.55 | 30 | 29/1 | +0.116 | [+0.090, +0.141] | 0.000 | TWO-SIDED: A>B (CI) | |
| success+accumulate | 150 | 0.52 | 0.46 | 30 | 24/5 | +0.066 | [+0.042, +0.089] | 0.001 | TWO-SIDED: A>B (CI) | |
| success+rewrite | 150 | 0.56 | 0.43 | 30 | 27/3 | +0.129 | [+0.096, +0.164] | 0.000 | TWO-SIDED: A>B (CI) | |
| hard+accumulate | 150 | 0.49 | 0.35 | 30 | 29/1 | +0.135 | [+0.111, +0.161] | 0.000 | TWO-SIDED: A>B (CI) | |
| hard+rewrite | 150 | 0.51 | 0.37 | 30 | 28/2 | +0.138 | [+0.112, +0.162] | 0.000 | TWO-SIDED: A>B (CI) | |

## C. Precedence: is the owner the member of its class that got the word first in the generation?

For each final homonym class of size ≥ 2 (train objects), find at which eval each member first carried the final word; owner = earliest? chance = 1/class size.

| cell | classes | owner was first (share) | chance | owner was last |
|---|---|---|---|---|
| generations | 236 | 0.22 | 0.47 | 0.16 |
| random+accumulate | 401 | 0.11 | 0.42 | 0.10 |
| random+rewrite | 382 | 0.10 | 0.43 | 0.07 |
| success+accumulate | 362 | 0.10 | 0.38 | 0.10 |
| success+rewrite | 416 | 0.07 | 0.38 | 0.06 |
| hard+accumulate | 356 | 0.07 | 0.34 | 0.06 |
| hard+rewrite | 406 | 0.07 | 0.36 | 0.04 |
| pair | 80 | 0.21 | 0.45 | 0.15 |

## D. Centrality: is the owner the member closest (Hamming) to the other members of its class?

| cell | classes (size ≥ 3) | owner is the most central | chance | owner is least central |
|---|---|---|---|---|
| generations | 41 | 0.34 | 0.31 | 0.00 |
| random+accumulate | 159 | 0.40 | 0.29 | 0.03 |
| random+rewrite | 126 | 0.42 | 0.30 | 0.02 |
| success+accumulate | 189 | 0.39 | 0.27 | 0.01 |
| success+rewrite | 222 | 0.41 | 0.28 | 0.03 |
| hard+accumulate | 232 | 0.33 | 0.25 | 0.00 |
| hard+rewrite | 239 | 0.33 | 0.27 | 0.01 |
| pair | 21 | 0.14 | 0.30 | 0.00 |

## E. Do orphans' forms mutate more than owners' forms? (parent status; parent→child, training objects)

| cell | mutation rate: parent owners | parent orphans | difference | | | | |
|---|---|---|---|---|---|---|---|
| random+accumulate | 0.70 | 0.61 | 30 | 1/29 | -0.086 | [-0.107, -0.066] | 0.000 | TWO-SIDED: A<B (CI) | |
| random+rewrite | 0.49 | 0.46 | 30 | 8/22 | -0.031 | [-0.055, -0.005] | 0.016 | TWO-SIDED: A<B (CI) | |
| success+accumulate | 0.74 | 0.65 | 30 | 3/27 | -0.088 | [-0.114, -0.064] | 0.000 | TWO-SIDED: A<B (CI) | |
| success+rewrite | 0.54 | 0.50 | 30 | 7/23 | -0.045 | [-0.070, -0.020] | 0.005 | TWO-SIDED: A<B (CI) | |
| hard+accumulate | 0.63 | 0.35 | 30 | 0/30 | -0.273 | [-0.293, -0.253] | 0.000 | TWO-SIDED: A<B (CI) | |
| hard+rewrite | 0.61 | 0.29 | 30 | 0/30 | -0.318 | [-0.345, -0.290] | 0.000 | TWO-SIDED: A<B (CI) | |

## F. The owners' language: topsim computed over owners only

| cell | n | topsim (all 64) | topsim_distinct | topsim over owners only | owners' language size |
|---|---|---|---|---|---|
| generations | 30 | 0.340 | 0.321 | 0.378 | 36.5 |
| random+accumulate | 30 | 0.293 | 0.235 | 0.309 | 25.6 |
| random+rewrite | 30 | 0.353 | 0.312 | 0.395 | 29.0 |
| success+accumulate | 30 | 0.295 | 0.232 | 0.302 | 23.2 |
| success+rewrite | 30 | 0.371 | 0.304 | 0.403 | 19.6 |
| hard+accumulate | 30 | 0.364 | 0.268 | 0.417 | 16.6 |
| hard+rewrite | 30 | 0.384 | 0.303 | 0.392 | 17.4 |
| pair | 30 | 0.285 | 0.275 | 0.316 | 44.2 |

## G. Are the 'hard' slots the orphans?

| cell | slots that are orphans (at selection time) | orphan share among all train objects | slots that are orphans whose OWNER is also a slot |
|---|---|---|---|
| hard+rewrite | 0.91 | 0.50 | 0.06 |
| hard+accumulate | 0.91 | 0.51 | 0.06 |
| success+rewrite | 0.44 | 0.45 | 0.58 |
| random+rewrite | 0.35 | 0.37 | 0.32 |

## H. Ownership churn inside a generation: share of training objects whose owner status flips between consecutive evals (250 steps)

| cell | early (≤ 1000) | late (> 1000) | owner → orphan | orphan → owner (late) |
|---|---|---|---|---|
| generations | 0.25 | 0.27 | 0.20 | 0.39 |
| random+accumulate | 0.22 | 0.26 | 0.25 | 0.28 |
| random+rewrite | 0.25 | 0.26 | 0.23 | 0.35 |
| success+accumulate | 0.20 | 0.24 | 0.26 | 0.25 |
| success+rewrite | 0.24 | 0.27 | 0.30 | 0.28 |
| hard+accumulate | 0.23 | 0.25 | 0.34 | 0.24 |
| hard+rewrite | 0.23 | 0.26 | 0.33 | 0.25 |
| pair | 0.14 | 0.13 | 0.09 | 0.43 |

## I. Number of owners per cell and what it predicts (final generation, all 970 runs)

- corr(#owners, n_unique) = +0.99; corr(#owners, test_acc) = +0.23; corr(#owners, topsim) = -0.17; corr(#owners, topsim_distinct) = +0.41
- owners are 94% of distinct messages on average (the rest are messages the receiver decodes to some other object).

