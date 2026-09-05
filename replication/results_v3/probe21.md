# probe21 — adoption curves, convexity over time, the origin of grammar, Zipf and inventory over generations, new forms

## A. Adoption curves: forms absent at step 250 that reach ≥ 3 objects by step 2000 (all generations)

| cell | such forms | mean size at each eval 250→2000 | share reaching final size in ONE eval step (sudden) | mean number of evals with growth |
|---|---|---|---|---|
| generations | 467 | 0.0 1.7 2.1 2.2 2.4 2.5 2.7 3.4 | 0.54 | 2.7 |
| random+accumulate | 245 | 0.0 0.9 1.4 1.9 2.2 2.5 2.7 3.5 | 0.39 | 2.5 |
| random+rewrite | 185 | 0.0 0.9 1.7 1.9 2.2 2.4 2.5 3.3 | 0.40 | 2.6 |
| success+accumulate | 281 | 0.0 0.8 1.4 2.1 2.4 2.6 2.8 3.5 | 0.46 | 2.4 |
| success+rewrite | 217 | 0.0 0.9 1.7 2.0 2.2 2.5 2.7 3.5 | 0.50 | 2.5 |
| hard+accumulate | 288 | 0.0 1.0 1.6 2.1 2.4 2.9 3.0 3.8 | 0.52 | 2.3 |
| hard+rewrite | 293 | 0.0 0.9 1.5 1.9 2.2 2.7 2.9 3.7 | 0.48 | 2.3 |
| pair | 68 | 0.0 1.2 2.0 2.2 2.2 2.3 2.4 3.3 | 0.51 | 2.6 |

## B. Convexity over time: share of homonym classes (size ≥ 3) that are connected, at each eval (gens ≥ 1; gen 0 for control)

| cell | 250 | 500 | 750 | 1000 | 1250 | 1500 | 1750 | 2000 |
|---|---|---|---|---|---|---|---|---|
| generations | 0.60 | 0.69 | 0.76 | 0.78 | 0.80 | 0.79 | 0.76 | 0.74 |
| random+accumulate | 0.76 | 0.77 | 0.78 | 0.78 | 0.79 | 0.78 | 0.77 | 0.77 |
| random+rewrite | 0.68 | 0.71 | 0.70 | 0.71 | 0.71 | 0.70 | 0.68 | 0.68 |
| success+accumulate | 0.73 | 0.76 | 0.76 | 0.77 | 0.75 | 0.76 | 0.76 | 0.76 |
| success+rewrite | 0.70 | 0.74 | 0.75 | 0.75 | 0.75 | 0.75 | 0.74 | 0.73 |
| hard+accumulate | 0.80 | 0.81 | 0.81 | 0.82 | 0.83 | 0.84 | 0.83 | 0.83 |
| hard+rewrite | 0.81 | 0.82 | 0.84 | 0.84 | 0.85 | 0.84 | 0.84 | 0.83 |
| pair | 0.57 | 0.67 | 0.76 | 0.73 | 0.78 | 0.80 | 0.75 | 0.70 |

## C. Where does the grammar come from? Role-matrix correlation between final languages

| comparison | n pairs | mean corr |
|---|---|---|
| different channels, same seed (rewrite cells) | 30 | +0.24 |
| same channel, different seeds | 135 | -0.01 |
| independent generations, same seed (no transmission) | 150 | +0.01 |

(parent → child within a lineage: 0.5–0.8). If same-seed/different-channel ≈ different-seed, the grammar is a property of the lineage, not of the split.

## D. Class-size distribution over generations: Zipf slope and largest class

| cell | slope gen 0 | 1 | 2 | 3 | 4 | 5 | largest class gen 0 → 5 |
|---|---|---|---|---|---|---|---|
| generations | -0.48 | -0.47 | -0.47 | -0.49 | -0.49 | -0.41 | 4.9 → 3.8 |
| random+accumulate | -0.48 | -0.66 | -0.66 | -0.66 | -0.66 | -0.65 | 4.9 → 6.7 |
| random+rewrite | -0.48 | -0.59 | -0.57 | -0.57 | -0.58 | -0.58 | 4.9 → 6.1 |
| success+accumulate | -0.48 | -0.71 | -0.71 | -0.70 | -0.73 | -0.74 | 4.9 → 8.0 |
| success+rewrite | -0.48 | -0.57 | -0.59 | -0.65 | -0.63 | -0.65 | 4.9 → 7.9 |
| hard+accumulate | -0.48 | -0.63 | -0.65 | -0.66 | -0.71 | -0.69 | 4.9 → 9.4 |
| hard+rewrite | -0.48 | -0.63 | -0.65 | -0.63 | -0.64 | -0.66 | 4.9 → 9.0 |

## E. Symbol inventory: distinct symbols used per position (of 8), by generation; and the least-used position's inventory

| cell | mean inventory gen 0 | 1 | 2 | 3 | 4 | 5 | smallest-position inventory gen 5 | positions with ≤ 3 symbols at gen 5 (share) |
|---|---|---|---|---|---|---|---|---|
| generations | 5.83 | 6.03 | 5.80 | 5.74 | 5.77 | 6.04 | 5.80 | 0.00 |
| random+accumulate | 5.83 | 6.74 | 6.70 | 6.69 | 6.62 | 6.66 | 5.83 | 0.00 |
| random+rewrite | 5.83 | 5.61 | 5.60 | 5.59 | 5.61 | 5.61 | 5.17 | 0.01 |
| success+accumulate | 5.83 | 6.38 | 6.43 | 6.31 | 6.42 | 6.36 | 5.63 | 0.03 |
| success+rewrite | 5.83 | 5.40 | 5.26 | 5.06 | 4.91 | 4.77 | 3.93 | 0.11 |
| hard+accumulate | 5.83 | 5.48 | 5.14 | 5.00 | 4.87 | 4.69 | 4.07 | 0.16 |
| hard+rewrite | 5.83 | 5.48 | 5.18 | 4.99 | 4.84 | 4.71 | 3.93 | 0.14 |

## F. Forms the child invents (absent from the parent's pool): how many, are they owned, are they regular?

| cell | new forms per transition (of the child's distinct forms) | share of new forms that are OWNED in the child | owned share of inherited forms | fit of objects with new forms | with inherited forms |
|---|---|---|---|---|---|
| random+accumulate | 0.43 | 0.51 | 0.36 | 0.304 | 0.305 |
| random+rewrite | 0.28 | 0.59 | 0.43 | 0.346 | 0.359 |
| success+accumulate | 0.45 | 0.47 | 0.32 | 0.311 | 0.313 |
| success+rewrite | 0.26 | 0.51 | 0.34 | 0.372 | 0.376 |
| hard+accumulate | 0.28 | 0.46 | 0.28 | 0.373 | 0.367 |
| hard+rewrite | 0.27 | 0.48 | 0.29 | 0.375 | 0.381 |

