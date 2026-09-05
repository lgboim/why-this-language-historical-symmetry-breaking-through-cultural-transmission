# probe28 — homonym classes as units of inheritance

## A. Class vs owner persistence across a generation boundary (parent's final train homonym classes, size ≥ 2 → child's final language)

| cell | classes | pair-level: still share a form @child end | class fully intact | intact with the SAME form | owner unchanged (given ≥2 still share) | owner unchanged, chance |
|---|---|---|---|---|---|---|
| generations | 1402 | 0.08 | 0.08 | 0.00 | 0.49 | 0.49 |
| random+accumulate | 1816 | 0.36 | 0.30 | 0.18 | 0.39 | 0.46 |
| random+rewrite | 1742 | 0.49 | 0.42 | 0.34 | 0.45 | 0.46 |
| success+accumulate | 1745 | 0.34 | 0.25 | 0.14 | 0.38 | 0.44 |
| success+rewrite | 1871 | 0.54 | 0.44 | 0.32 | 0.41 | 0.44 |
| hard+accumulate | 1863 | 0.65 | 0.53 | 0.38 | 0.42 | 0.41 |
| hard+rewrite | 1899 | 0.67 | 0.55 | 0.44 | 0.42 | 0.41 |

## B. Where a successfully emancipated TRAIN orphan goes (sweep, gens ≥ 1; success = owner at the next snapshot with a unique form). Form distance old→new; semantic distance to its nearest form-neighbour (Hamming-1 in message space) before vs after; and to a random unused form (chance)

| cell | events | form dist 1 / 2 / 3 | nearest form-neighbour is a semantic H1 neighbour: before | after | chance (random unused form) | still owner at gen end |
|---|---|---|---|---|---|---|
| random+accumulate | 648 | 0.66 / 0.23 / 0.10 | 0.29 | 0.48 | 0.18 | 0.94 |
| random+rewrite | 682 | 0.65 / 0.29 / 0.06 | 0.31 | 0.47 | 0.16 | 0.94 |
| success+accumulate | 618 | 0.66 / 0.27 / 0.07 | 0.27 | 0.48 | 0.18 | 0.93 |
| success+rewrite | 465 | 0.66 / 0.28 / 0.06 | 0.28 | 0.46 | 0.13 | 0.93 |
| hard+accumulate | 398 | 0.66 / 0.28 / 0.06 | 0.31 | 0.47 | 0.16 | 0.90 |
| hard+rewrite | 433 | 0.70 / 0.26 / 0.04 | 0.28 | 0.47 | 0.14 | 0.91 |

## C. Collision repair vs semantic distance: train homonym PAIRS at step 250 of a gen ≥ 1, share still homonyms at 2000, by attribute distance of the pair

| cell | pairs d=1 | survive | pairs d=2 | survive | pairs d=3 | survive |
|---|---|---|---|---|---|---|
| generations | 9321 | 0.17 | 14584 | 0.03 | 5581 | 0.00 |
| random+accumulate | 5621 | 0.54 | 4443 | 0.32 | 767 | 0.15 |
| random+rewrite | 4470 | 0.58 | 2419 | 0.36 | 270 | 0.23 |
| success+accumulate | 6178 | 0.55 | 6065 | 0.36 | 1233 | 0.25 |
| success+rewrite | 5673 | 0.64 | 3982 | 0.45 | 488 | 0.34 |
| hard+accumulate | 7121 | 0.70 | 5049 | 0.51 | 590 | 0.33 |
| hard+rewrite | 6910 | 0.68 | 4555 | 0.48 | 478 | 0.38 |

Forced collisions (probe25 collide arm), still homonyms at 2000 by semantic distance: d=1: 0.31 (n=83), d=2: 0.10 (n=200), d=3: 0.05 (n=215)

## D. Predicting class stability (train classes at step 250, gens ≥ 1, size ≥ 2): intact at 2000 by convexity, local density tercile, size; and point-biserial correlations

| cell | classes | convex: intact | non-convex: intact | density low / mid / high: intact | size 2 / 3 / 4+ : intact | corr(density, intact) | corr(size, intact) | corr(convex, intact) |
|---|---|---|---|---|---|---|---|---|
| generations | 999 | 0.06 | 0.00 | 0.00 / 0.01 / 0.11 | 0.10 / 0.05 / 0.01 | +0.35 | -0.16 | +0.15 |
| random+accumulate | 1843 | 0.37 | 0.37 | 0.25 / 0.44 / nan | 0.59 / 0.37 / 0.16 | +0.21 | -0.35 | +0.00 |
| random+rewrite | 2054 | 0.47 | 0.32 | 0.31 / 0.58 / nan | 0.59 / 0.36 / 0.24 | +0.21 | -0.26 | +0.12 |
| success+accumulate | 1654 | 0.34 | 0.27 | 0.23 / 0.24 / 0.55 | 0.59 / 0.35 / 0.16 | +0.24 | -0.33 | +0.06 |
| success+rewrite | 1917 | 0.48 | 0.34 | 0.29 / 0.55 / nan | 0.66 / 0.41 / 0.27 | +0.25 | -0.27 | +0.11 |
| hard+accumulate | 1760 | 0.52 | 0.31 | 0.34 / 0.59 / nan | 0.71 / 0.50 / 0.39 | +0.27 | -0.22 | +0.14 |
| hard+rewrite | 1815 | 0.51 | 0.34 | 0.33 / 0.58 / nan | 0.72 / 0.49 / 0.35 | +0.27 | -0.26 | +0.10 |
