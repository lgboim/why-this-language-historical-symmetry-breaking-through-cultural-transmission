# probe13 — is erosion real? expressivity, shared grammar, fossil geometry

Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## A. Is the late decline of structure in `pair` real, or just de-inflation? (30 seeds)

| metric | 500 | 1000 | 2000 | 4000 | 8000 | 12000 | paired 1000 → 12000 |
|---|---|---|---|---|---|---|---|
| topsim | 0.343 | 0.343 | 0.313 | 0.306 | 0.293 | 0.285 | 30 | 2/28 | -0.058 | [-0.073, -0.045] | 0.000 | TWO-SIDED: A<B (CI) | |
| topsim_distinct | 0.277 | 0.297 | 0.281 | 0.287 | 0.278 | 0.275 | 30 | 9/21 | -0.022 | [-0.039, -0.005] | 0.043 | TWO-SIDED: A<B (CI) | |
| owners-only topsim | 0.524 | 0.405 | 0.346 | 0.334 | 0.320 | 0.316 | 30 | 2/28 | -0.089 | [-0.111, -0.066] | 0.000 | TWO-SIDED: A<B (CI) | |
| CBM | 0.500 | 0.493 | 0.484 | 0.475 | 0.463 | 0.458 | 30 | 5/24 | -0.034 | [-0.046, -0.023] | 0.001 | TWO-SIDED: A<B (CI) | |
| n_owners | 10.400 | 21.467 | 32.600 | 39.867 | 42.733 | 44.233 | 30 | 30/0 | +22.767 | [+21.267, +24.200] | 0.000 | TWO-SIDED: A>B (CI) | |
| n_unique | 25.233 | 32.400 | 41.033 | 47.267 | 50.067 | 52.533 | 30 | 30/0 | +20.133 | [+18.167, +22.133] | 0.000 | TWO-SIDED: A>B (CI) | |

## B. Expressivity by transfer (Guo et al. 2022): a fresh listener learns 90% of the final language's (object, message) pairs, tested on the other 10%, in games of different size

| cell | n | |C|=2 | |C|=5 | |C|=10 | |C|=20 | mean |
|---|---|---|---|---|---|---|
| generations | 10 | 0.918 | 0.752 | 0.557 | 0.344 | 0.643 |
| random+accumulate | 10 | 0.877 | 0.658 | 0.472 | 0.239 | 0.562 |
| random+rewrite | 10 | 0.905 | 0.715 | 0.491 | 0.285 | 0.599 |
| success+accumulate | 10 | 0.891 | 0.681 | 0.455 | 0.253 | 0.570 |
| success+rewrite | 10 | 0.888 | 0.677 | 0.483 | 0.287 | 0.584 |
| hard+accumulate | 10 | 0.892 | 0.663 | 0.442 | 0.215 | 0.553 |
| hard+rewrite | 10 | 0.929 | 0.739 | 0.516 | 0.294 | 0.620 |
| pair | 10 | 0.845 | 0.601 | 0.417 | 0.239 | 0.526 |

chance = 1/|C|. Within-seed rank of channels is what matters; absolute values depend on the 58/6 split.

## C. Shared grammar: does the receiver rely on the positions that carry the sender's information?

receiver reliance on position p = share of the 64 messages whose decode (over all 64) changes when the symbol at p is replaced by a random other symbol (mean of 8 draws). sender information at p = total MI(position p, attributes). Reported: correlation across the 3 positions, per run, then averaged; and the share of runs where the receiver's most-relied-on position is the sender's most informative one.

| cell | n | corr(reliance, information) | argmax agreement | chance |
|---|---|---|---|---|
| generations | 30 | +0.77 | 0.93 | 0.33 |
| random+accumulate | 30 | +0.38 | 0.37 | 0.33 |
| random+rewrite | 30 | -0.15 | 0.30 | 0.33 |
| success+accumulate | 30 | +0.18 | 0.33 | 0.33 |
| success+rewrite | 30 | +0.06 | 0.30 | 0.33 |
| hard+accumulate | 30 | +0.18 | 0.47 | 0.33 |
| hard+rewrite | 30 | +0.55 | 0.47 | 0.33 |
| pair | 30 | +0.74 | 0.87 | 0.33 |

## D. Fossil geometry: are the objects whose message survived gen 0 → 5 clustered in attribute space?

| cell | n | mean pairwise Hamming among fossils | among random sets of the same size | fossils' share of held-out objects |
|---|---|---|---|---|
| random+accumulate | 21 | 2.10 | 2.28 | 0.10 |
| random+rewrite | 30 | 2.23 | 2.28 | 0.13 |
| success+accumulate | 10 | 1.88 | 2.29 | 0.06 |
| success+rewrite | 24 | 2.02 | 2.29 | 0.15 |
| hard+accumulate | 30 | 2.09 | 2.29 | 0.10 |
| hard+rewrite | 28 | 2.05 | 2.29 | 0.16 |

(held-out objects are 25% of all objects)

## E. Anatomy of the late phase in `pair` (step 1000 → 12000): who changes?

| quantity | value |
|---|---|
| orphans at 1000 promoted to owners by 12000 (of 64) | 24.3 |
| owners at 1000 demoted by 12000 | 1.5 |
| share of step-1000 owners whose form changed | 0.69 |
| share of step-1000 orphans whose form changed | 0.80 |
| owners at 1000 still owners with the SAME form at 12000 | 5.7 |

