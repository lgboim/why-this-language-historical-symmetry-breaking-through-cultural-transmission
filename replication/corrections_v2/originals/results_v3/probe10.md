# probe10 — is ownership in the language?

Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## A. Main effects on the owners' language (seeds 0–9, all record cells; paired by seed, other factors averaged)

### own_topsim

| factor | A | B | n | wins/losses | mean diff | 95% CI | p | |
|---|---|---|---|---|---|---|---|---|
| select | hard | random | 10 | 3/4 | +nan | [+nan, +nan] | 0.344 | TWO-SIDED: no difference (CI) |
| select | hard | success | 10 | 2/5 | +nan | [+nan, +nan] | 0.109 | TWO-SIDED: no difference (CI) |
| select | random | success | 10 | 3/7 | -0.020 | [-0.032, -0.007] | 0.344 | TWO-SIDED: A<B (CI) |
| fresh | accumulate | rewrite | 10 | 0/7 | +nan | [+nan, +nan] | 0.002 | TWO-SIDED: no difference (CI) |
| capacity | 8 | 19 | 10 | 3/4 | +nan | [+nan, +nan] | 0.344 | TWO-SIDED: no difference (CI) |
| capacity | 8 | 40 | 10 | 5/2 | +nan | [+nan, +nan] | 1.000 | TWO-SIDED: no difference (CI) |
| capacity | 19 | 40 | 10 | 10/0 | +0.041 | [+0.025, +0.057] | 0.002 | TWO-SIDED: A>B (CI) |
| noise | 0.0 | 0.2 | 10 | 6/1 | +nan | [+nan, +nan] | 0.754 | TWO-SIDED: no difference (CI) |
| reader | both | sender | 10 | 1/6 | +nan | [+nan, +nan] | 0.021 | TWO-SIDED: no difference (CI) |

### n_owners

| factor | A | B | n | wins/losses | mean diff | 95% CI | p | |
|---|---|---|---|---|---|---|---|---|
| select | hard | random | 10 | 0/10 | -5.979 | [-7.146, -4.979] | 0.002 | TWO-SIDED: A<B (CI) |
| select | hard | success | 10 | 0/10 | -2.487 | [-3.163, -1.788] | 0.002 | TWO-SIDED: A<B (CI) |
| select | random | success | 10 | 10/0 | +3.492 | [+2.579, +4.421] | 0.002 | TWO-SIDED: A>B (CI) |
| fresh | accumulate | rewrite | 10 | 1/9 | -2.075 | [-2.878, -1.167] | 0.021 | TWO-SIDED: A<B (CI) |
| capacity | 8 | 19 | 10 | 0/10 | -11.108 | [-12.312, -9.767] | 0.002 | TWO-SIDED: A<B (CI) |
| capacity | 8 | 40 | 10 | 0/10 | -24.621 | [-25.996, -22.992] | 0.002 | TWO-SIDED: A<B (CI) |
| capacity | 19 | 40 | 10 | 0/10 | -13.512 | [-14.712, -12.537] | 0.002 | TWO-SIDED: A<B (CI) |
| noise | 0.0 | 0.2 | 10 | 1/9 | -2.792 | [-4.103, -1.575] | 0.021 | TWO-SIDED: A<B (CI) |
| reader | both | sender | 10 | 6/4 | +0.175 | [-0.261, +0.608] | 0.754 | TWO-SIDED: no difference (CI) |

Record cells vs no-transmission control on own_topsim (paired, seeds 0–9):

- random+accumulate: | 10 | 3/7 | -0.062 | [-0.115, -0.002] | 0.344 | TWO-SIDED: A<B (CI) |
- random+rewrite: | 10 | 6/4 | +0.024 | [-0.044, +0.091] | 0.754 | TWO-SIDED: no difference (CI) |
- success+accumulate: | 10 | 2/8 | -0.076 | [-0.124, -0.025] | 0.109 | TWO-SIDED: A<B (CI) |
- success+rewrite: | 10 | 6/4 | +0.043 | [-0.024, +0.116] | 0.754 | TWO-SIDED: no difference (CI) |
- hard+accumulate: | 10 | 7/3 | +0.035 | [-0.034, +0.101] | 0.344 | TWO-SIDED: no difference (CI) |
- hard+rewrite: | 10 | 5/5 | +0.017 | [-0.050, +0.080] | 1.000 | TWO-SIDED: no difference (CI) |

## B. Do independently trained receivers agree on who owns each word? (seeds 0–9, final languages)

Two fresh receivers (different inits, 400 steps on training objects only) decode the sender's messages over all 64 objects.

| cell | n | owner agreement: fresh1 vs original | fresh1 vs fresh2 | chance (share of owners) | agreement on ORPHANS' assigned owner (fresh1 vs original) |
|---|---|---|---|---|---|
| generations | 10 | 0.78 | 0.85 | 0.64 | 0.37 |
| random+accumulate | 10 | 0.74 | 0.71 | 0.53 | 0.50 |
| random+rewrite | 10 | 0.75 | 0.72 | 0.57 | 0.48 |
| success+accumulate | 10 | 0.77 | 0.70 | 0.52 | 0.52 |
| success+rewrite | 10 | 0.66 | 0.65 | 0.53 | 0.44 |
| hard+accumulate | 10 | 0.74 | 0.73 | 0.56 | 0.40 |
| hard+rewrite | 10 | 0.73 | 0.67 | 0.54 | 0.49 |
| pair | 10 | 0.96 | 0.96 | 0.91 | 0.30 |

## C. Does the sender know who owns the word?

| cell | n | p(greedy): owners | orphans | paired | | | | | owner = most confident member of its class (share) | chance |
|---|---|---|---|---|---|---|---|---|---|---|
| generations | 30 | 0.668 | 0.683 | 30 | 11/19 | -0.015 | [-0.047, +0.019] | 0.200 | TWO-SIDED: no difference (CI) | 0.61 | 0.47 |
| random+accumulate | 30 | 0.941 | 0.970 | 30 | 5/25 | -0.029 | [-0.039, -0.019] | 0.000 | TWO-SIDED: A<B (CI) | 0.46 | 0.42 |
| random+rewrite | 30 | 0.938 | 0.975 | 30 | 1/29 | -0.037 | [-0.047, -0.026] | 0.000 | TWO-SIDED: A<B (CI) | 0.43 | 0.43 |
| success+accumulate | 30 | 0.924 | 0.970 | 30 | 3/27 | -0.046 | [-0.059, -0.034] | 0.000 | TWO-SIDED: A<B (CI) | 0.44 | 0.38 |
| success+rewrite | 30 | 0.967 | 0.971 | 30 | 9/21 | -0.005 | [-0.011, +0.003] | 0.043 | TWO-SIDED: no difference (CI) | 0.48 | 0.38 |
| hard+accumulate | 30 | 0.949 | 0.966 | 30 | 9/21 | -0.017 | [-0.028, -0.007] | 0.043 | TWO-SIDED: A<B (CI) | 0.37 | 0.34 |
| hard+rewrite | 30 | 0.959 | 0.973 | 30 | 11/19 | -0.014 | [-0.024, -0.003] | 0.200 | TWO-SIDED: A<B (CI) | 0.46 | 0.36 |
| pair | 30 | 0.637 | 0.944 | 27 | 0/27 | -0.302 | [-0.341, -0.262] | 0.000 | TWO-SIDED: A<B (CI) | 0.40 | 0.45 |

## D. Does the lexicon abandon whole attribute VALUES? (final generation, training objects)

For each (attribute, value): share of its training objects that are orphans. Gap = a value whose objects are ≥ 80% orphans. Concentration = max over values of orphan share within the most-dropped attribute.

| cell | n | values that are gaps (of 12) | orphan share, worst value | orphan share, best value | expected worst if orphans were random (same count) |
|---|---|---|---|---|---|
| generations | 30 | 0.07 | 0.49 | 0.07 | 0.44 |
| random+accumulate | 30 | 0.37 | 0.70 | 0.27 | 0.68 |
| random+rewrite | 30 | 0.37 | 0.63 | 0.21 | 0.61 |
| success+accumulate | 30 | 0.47 | 0.73 | 0.31 | 0.73 |
| success+rewrite | 30 | 1.10 | 0.78 | 0.39 | 0.79 |
| hard+accumulate | 30 | 2.97 | 0.83 | 0.47 | 0.84 |
| hard+rewrite | 30 | 1.77 | 0.82 | 0.45 | 0.84 |
| pair | 30 | 0.00 | 0.24 | 0.00 | 0.19 |

## E. Affiliation: does an orphan keep borrowing from the same owner?

| cell | across consecutive evals (250 steps) | across generations (parent→child) | chance (same owner by luck, ≈ 1/#owners) |
|---|---|---|---|
| generations | 0.60 | 0.16 | 0.08 |
| random+accumulate | 0.69 | 0.27 | 0.06 |
| random+rewrite | 0.72 | 0.45 | 0.05 |
| success+accumulate | 0.67 | 0.24 | 0.06 |
| success+rewrite | 0.66 | 0.36 | 0.06 |
| hard+accumulate | 0.65 | 0.42 | 0.07 |
| hard+rewrite | 0.66 | 0.44 | 0.07 |
| pair | 0.67 | nan | 0.04 |

## F. Promotion: which orphans become owners between consecutive evals inside a generation?

| cell | promotions | Hamming distance to former owner: promoted | not promoted | promoted got a brand-new word (share) |
|---|---|---|---|---|
| generations | 10443 | 1.17 | 1.28 | 0.44 |
| random+accumulate | 8652 | 1.15 | 1.21 | 0.20 |
| random+rewrite | 9016 | 1.12 | 1.17 | 0.19 |
| success+accumulate | 8153 | 1.17 | 1.24 | 0.21 |
| success+rewrite | 8832 | 1.15 | 1.21 | 0.18 |
| hard+accumulate | 8318 | 1.14 | 1.21 | 0.18 |
| hard+rewrite | 8536 | 1.13 | 1.20 | 0.18 |
| pair | 5184 | 1.14 | 1.24 | 0.31 |

## G. Noise creates new owners (seeds 0–9, cap 19, reader sender): #owners, own_topsim, topsim_distinct by noise level

| cell | noise 0: #owners | noise 0.2 | own_topsim: 0 | 0.2 | paired own_topsim (0 − 0.2) | | | | |
|---|---|---|---|---|---|---|---|---|---|
| random+accumulate | 26.4 | 30.3 | 0.320 | 0.262 | 10 | 8/2 | +0.058 | [-0.010, +0.114] | 0.109 | TWO-SIDED: no difference (CI) | |
| random+rewrite | 32.3 | 35.3 | 0.407 | 0.378 | 10 | 7/3 | +0.029 | [-0.008, +0.065] | 0.344 | TWO-SIDED: no difference (CI) | |
| success+accumulate | 25.4 | 24.2 | 0.306 | 0.277 | 10 | 5/5 | +0.029 | [-0.028, +0.086] | 1.000 | TWO-SIDED: no difference (CI) | |
| success+rewrite | 20.6 | 27.1 | 0.425 | 0.356 | 10 | 5/5 | +0.070 | [-0.007, +0.147] | 1.000 | TWO-SIDED: no difference (CI) | |
| hard+accumulate | 19.5 | 24.8 | 0.418 | 0.334 | 10 | 8/2 | +0.084 | [-0.016, +0.166] | 0.109 | TWO-SIDED: no difference (CI) | |
| hard+rewrite | 19.2 | 24.3 | 0.400 | 0.322 | 10 | 7/3 | +0.078 | [+0.008, +0.149] | 0.344 | TWO-SIDED: A>B (CI) | |

