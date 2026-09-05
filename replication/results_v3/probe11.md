# probe11 — object-level causal effects, forgetting curves, transparency

Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## A. Staleness at the object level (generation 0 → 1; the parent is identical across cells of a seed)

In the ACCUMULATE record after generation 0, an entry is STALE if its form ≠ the parent's final form for that object. Compare the child's treatment of stale vs fresh entries within the same run; and, across cells, the same object's fate when its recorded form was stale (accumulate) vs final (rewrite).

| cell | n runs | share of entries stale | child keeps: stale | fresh | child's final fit: stale | fresh | child owner: stale | fresh |
|---|---|---|---|---|---|---|---|---|
| random+accumulate | 30 | 0.91 | 0.69 | 0.56 | 0.297 | 0.370 | 0.60 | 0.48 |
| success+accumulate | 30 | 0.90 | 0.63 | 0.64 | 0.346 | 0.394 | 0.53 | 0.39 |
| hard+accumulate | 30 | 0.00 | nan | 0.79 | nan | 0.403 | nan | 0.53 |

Cross-cell, same object, same parent (random slots: the 19 slots are identical in accumulate and rewrite for a seed):

| object's recorded form | child fidelity | child fit | child owner | child's gen-1 topsim (run) |
|---|---|---|---|---|
| stale in accumulate → child via accumulate (n=518) | 0.69 | 0.297 | 0.60 | 0.295 |
| stale in accumulate → child via rewrite (n=518) | 0.80 | 0.385 | 0.64 | 0.340 |
| identical in both → child via accumulate (n=52) | 0.56 | 0.370 | 0.48 | 0.302 |
| identical in both → child via rewrite (n=52) | 0.79 | 0.443 | 0.44 | 0.339 |

## B. Carving time: when in generation 0 was each accumulated form carved? (first eval whose greedy language contains it)

| cell | entries | carved at step ≤500 | 750–1250 | ≥1500 | share stale by carving time: early | mid | late | child keeps: early | late |
|---|---|---|---|---|---|---|---|---|---|
| random+accumulate | 183 | 0.91 | 0.05 | 0.04 | 0.75 | 0.50 | 0.14 | 0.56 | 0.71 |
| success+accumulate | 236 | 0.96 | 0.03 | 0.01 | 0.77 | 0.50 | 0.50 | 0.60 | 0.00 |
| hard+accumulate | 570 | 0.42 | 0.30 | 0.28 | 0.00 | 0.00 | 0.00 | 0.82 | 0.76 |

## C. Forgetting curve: fidelity to the inherited form at each eval inside the child's generation (gens ≥ 1)

| cell | 250 | 500 | 1000 | 1500 | 2000 | share of drops that happen by step 250 |
|---|---|---|---|---|---|---|
| random+accumulate | 0.89 | 0.86 | 0.79 | 0.74 | 0.69 | 0.34 |
| random+rewrite | 0.93 | 0.91 | 0.87 | 0.85 | 0.83 | 0.40 |
| success+accumulate | 0.85 | 0.80 | 0.72 | 0.67 | 0.64 | 0.41 |
| success+rewrite | 0.92 | 0.91 | 0.86 | 0.84 | 0.80 | 0.40 |
| hard+accumulate | 0.93 | 0.90 | 0.86 | 0.82 | 0.78 | 0.33 |
| hard+rewrite | 0.94 | 0.92 | 0.87 | 0.83 | 0.80 | 0.28 |

## D. Morphological transparency: for Hamming-1 pairs of objects that are BOTH owners, how many message symbols differ?

| cell | pairs | 1 symbol | 2 symbols | 3 symbols | mean | random-language baseline mean |
|---|---|---|---|---|---|---|
| generations | 2878 | 0.32 | 0.43 | 0.25 | 1.92 | 2.63 |
| random+accumulate | 1373 | 0.31 | 0.38 | 0.31 | 2.00 | 2.63 |
| random+rewrite | 1852 | 0.41 | 0.38 | 0.21 | 1.80 | 2.63 |
| success+accumulate | 1173 | 0.32 | 0.38 | 0.31 | 1.99 | 2.63 |
| success+rewrite | 804 | 0.47 | 0.38 | 0.15 | 1.68 | 2.63 |
| hard+accumulate | 638 | 0.45 | 0.38 | 0.17 | 1.72 | 2.63 |
| hard+rewrite | 653 | 0.47 | 0.35 | 0.17 | 1.70 | 2.63 |
| pair | 4148 | 0.25 | 0.45 | 0.30 | 2.05 | 2.63 |

## E. Zipf: rank–frequency of words (class size = number of objects using the word), pooled over seeds

| cell | slope of log(size) vs log(rank) | largest class | share of objects covered by the top 5 words |
|---|---|---|---|
| generations | -0.41 | 3.8 | 0.23 |
| random+accumulate | -0.65 | 6.7 | 0.38 |
| random+rewrite | -0.58 | 6.1 | 0.35 |
| success+accumulate | -0.74 | 8.0 | 0.45 |
| success+rewrite | -0.65 | 7.9 | 0.46 |
| hard+accumulate | -0.69 | 9.4 | 0.54 |
| hard+rewrite | -0.66 | 9.0 | 0.49 |
| pair | -0.30 | 3.5 | 0.20 |

## F. Entrenchment: the record's success counter vs the child's fidelity (accumulate cells)

| cell | entries | counter median | fidelity: counter ≤ 2 | 3–10 | > 10 | corr(log counter, kept) |
|---|---|---|---|---|---|---|
| random+accumulate | 2850 | 3678 | 0.76 | 0.70 | 0.68 | +0.07 |
| success+accumulate | 2850 | 3014 | 0.73 | 0.68 | 0.63 | +0.11 |
| hard+accumulate | 2850 | 1 | 0.78 | 0.40 | 0.79 | +0.02 |

## G. When the receiver also reads the record, do the record's objects become owners? (seeds 0–9, cap 19, noise 0)

| cell | owners among record objects: reader=both | reader=sender | paired | | | | | owners among non-record train objects: both | sender |
|---|---|---|---|---|---|---|---|---|---|
| random+accumulate | 0.58 | 0.59 | 10 | 4/6 | -0.011 | [-0.038, +0.019] | 0.754 | TWO-SIDED: no difference (CI) | 0.53 | 0.52 |
| random+rewrite | 0.69 | 0.71 | 10 | 4/6 | -0.018 | [-0.068, +0.027] | 0.754 | TWO-SIDED: no difference (CI) | 0.62 | 0.64 |
| success+accumulate | 0.51 | 0.53 | 10 | 4/6 | -0.017 | [-0.054, +0.023] | 0.754 | TWO-SIDED: no difference (CI) | 0.50 | 0.51 |
| success+rewrite | 0.57 | 0.52 | 10 | 7/3 | +0.051 | [-0.011, +0.109] | 0.344 | TWO-SIDED: no difference (CI) | 0.54 | 0.50 |
| hard+accumulate | 0.44 | 0.42 | 10 | 4/5 | +0.015 | [-0.046, +0.081] | 1.000 | TWO-SIDED: no difference (CI) | 0.47 | 0.51 |
| hard+rewrite | 0.45 | 0.43 | 10 | 6/2 | +0.021 | [-0.037, +0.077] | 0.289 | TWO-SIDED: no difference (CI) | 0.46 | 0.52 |

## H. Divergence between channels from an identical generation 0 (same seed): relabel-invariant language similarity, by generation

| pair of cells | gen 0 | gen 1 | gen 2 | gen 3 | gen 4 | gen 5 |
|---|---|---|---|---|---|---|
| random+rewrite vs random+accumulate | 1.00 | 0.07 | 0.07 | 0.07 | 0.07 | 0.07 |
| random+rewrite vs success+rewrite | 1.00 | 0.20 | 0.14 | 0.11 | 0.10 | 0.10 |
| random+rewrite vs hard+rewrite | 1.00 | 0.22 | 0.16 | 0.13 | 0.12 | 0.11 |
| random+rewrite vs generations | 1.00 | 0.05 | 0.05 | 0.05 | 0.06 | 0.05 |

