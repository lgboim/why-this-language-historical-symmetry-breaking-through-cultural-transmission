# probe29 — the derivation mechanism

## A/B. Distance-1 derivations where the orphan differs from its old owner in exactly ONE attribute a. A: is the changed position the CBM position of a (chance 1/3)? B: is the new symbol the one most used for value (a, v) at that position among other objects (chance ~1/8), and among the orphan's semantic neighbours sharing that value?

| cell | events (1-attr) | changed pos = CBM pos of a | new symbol = modal symbol for (a,v) at that pos | new symbol appears at that pos in ≥1 other object with value v | chance |
|---|---|---|---|---|---|
| random+accumulate | 376 | 0.30 | 0.30 | 0.84 | 0.33 / 0.13 |
| random+rewrite | 406 | 0.37 | 0.31 | 0.90 | 0.33 / 0.13 |
| success+accumulate | 356 | 0.42 | 0.26 | 0.79 | 0.33 / 0.13 |
| success+rewrite | 272 | 0.39 | 0.32 | 0.86 | 0.33 / 0.13 |
| hard+accumulate | 242 | 0.38 | 0.31 | 0.89 | 0.33 / 0.13 |
| hard+rewrite | 275 | 0.42 | 0.31 | 0.87 | 0.33 / 0.13 |

## C. Propagation: after a derivation (o gets new form f1 at window i), share of o's semantic H1 neighbours (train, not o) that by gen end hold a form at message-distance ≤1 from f1, vs the same quantity for a matched random train owner that did not change in that window

| cell | events | neighbours near f1 at gen end | matched control | paired diff over seeds | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| random+accumulate | 0 | 0.36 | 0.39 | 30 | 8/22 | -0.029 | [-0.057, +0.001] | 0.016 | TWO-SIDED: no difference (CI) | |
| random+rewrite | 0 | 0.44 | 0.46 | 30 | 15/15 | -0.024 | [-0.058, +0.007] | 1.000 | TWO-SIDED: no difference (CI) | |
| success+accumulate | 0 | 0.38 | 0.42 | 30 | 9/21 | -0.045 | [-0.084, -0.010] | 0.043 | TWO-SIDED: A<B (CI) | |
| success+rewrite | 0 | 0.45 | 0.51 | 28 | 7/21 | -0.060 | [-0.094, -0.027] | 0.013 | TWO-SIDED: A<B (CI) | |
| hard+accumulate | 0 | 0.42 | 0.50 | 30 | 5/25 | -0.085 | [-0.116, -0.055] | 0.000 | TWO-SIDED: A<B (CI) | |
| hard+rewrite | 0 | 0.46 | 0.50 | 30 | 7/23 | -0.039 | [-0.068, -0.010] | 0.005 | TWO-SIDED: A<B (CI) | |

## D. Transmission of derived forms: forms created by a distance-1 derivation in gen g (and still held at gen end) vs other new forms held at gen end (created within the gen, not by derivation): share present in the child's language at gen g+1 end (same object)

| cell | derived forms | survive to child end | other new forms | survive | paired diff | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|
| random+accumulate | 289 | 0.12 | 1664 | 0.16 | 30 | 9/21 | -0.045 | [-0.092, +0.006] | 0.043 | TWO-SIDED: no difference (CI) | |
| random+rewrite | 282 | 0.28 | 1344 | 0.38 | 30 | 7/23 | -0.099 | [-0.168, -0.029] | 0.005 | TWO-SIDED: A<B (CI) | |
| success+accumulate | 259 | 0.09 | 1782 | 0.15 | 30 | 11/19 | -0.057 | [-0.103, -0.012] | 0.200 | TWO-SIDED: A<B (CI) | |
| success+rewrite | 208 | 0.39 | 1506 | 0.43 | 28 | 11/17 | -0.036 | [-0.142, +0.069] | 0.345 | TWO-SIDED: no difference (CI) | |
| hard+accumulate | 176 | 0.16 | 1428 | 0.34 | 30 | 5/25 | -0.181 | [-0.249, -0.100] | 0.000 | TWO-SIDED: A<B (CI) | |
| hard+rewrite | 205 | 0.18 | 1454 | 0.46 | 30 | 4/26 | -0.274 | [-0.345, -0.204] | 0.000 | TWO-SIDED: A<B (CI) | |

## E. Structure growth within a gen (250→2000) vs number of successful distance-1 derivations in that gen, across (seed, gen ≥ 1)

| cell | n | corr(derivations, Δtopsim_distinct) | corr(derivations, ΔCBM) | corr(derivations, Δn_owners) |
|---|---|---|---|---|
| random+accumulate | 150 | +0.41 | +0.13 | +0.56 |
| random+rewrite | 150 | +0.13 | +0.13 | +0.57 |
| success+accumulate | 150 | +0.27 | -0.01 | +0.56 |
| success+rewrite | 150 | +0.27 | +0.08 | +0.64 |
| hard+accumulate | 150 | +0.28 | -0.08 | +0.67 |
| hard+rewrite | 150 | +0.16 | -0.09 | +0.62 |

## F. Class stability by number of attributes shared by ALL members (train classes at step 250, size ≥ 2 → intact at 2000); G. when an intact class changed its shared form, size of the change

| cell | shared attrs 0: n, intact | 1: n, intact | 2: n, intact | intact classes that changed form | of those: 1 symbol / 2 / 3 |
|---|---|---|---|---|---|
| generations | 539, 0.00 | 316, 0.01 | 144, 0.23 | 0.53 | 0.50 / 0.25 / 0.25 |
| random+accumulate | 336, 0.12 | 812, 0.31 | 695, 0.57 | 0.03 | 0.76 / 0.24 / 0.00 |
| random+rewrite | 173, 0.20 | 839, 0.33 | 1042, 0.58 | 0.02 | 0.75 / 0.25 / 0.00 |
| success+accumulate | 438, 0.13 | 769, 0.30 | 447, 0.56 | 0.03 | 0.88 / 0.06 / 0.06 |
| success+rewrite | 274, 0.19 | 876, 0.36 | 767, 0.65 | 0.03 | 0.79 / 0.21 / 0.00 |
| hard+accumulate | 236, 0.24 | 866, 0.44 | 658, 0.67 | 0.05 | 0.78 / 0.22 / 0.00 |
| hard+rewrite | 221, 0.28 | 879, 0.39 | 715, 0.67 | 0.04 | 0.83 / 0.17 / 0.00 |
