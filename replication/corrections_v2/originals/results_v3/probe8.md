# probe8 — omission grammar, word ownership, fossils

Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## A. Omission grammar: when a held-out object borrows a Hamming-1 neighbour's word, which attribute is dropped?

| cell | borrowings | dropped attribute = the lexicon's most-dropped attribute | expected (share of that attribute among train homonym pairs) | expected if uniform |
|---|---|---|---|---|
| generations | 208 | 0.71 | 0.73 | 0.33 |
| random+accumulate | 522 | 0.60 | 0.58 | 0.33 |
| random+rewrite | 462 | 0.61 | 0.60 | 0.33 |
| success+accumulate | 588 | 0.54 | 0.52 | 0.33 |
| success+rewrite | 704 | 0.62 | 0.61 | 0.33 |
| hard+accumulate | 922 | 0.61 | 0.62 | 0.33 |
| hard+rewrite | 866 | 0.64 | 0.64 | 0.33 |
| pair | 128 | 0.72 | 0.71 | 0.33 |

## B. Word ownership: two TRAINING objects share a word; each is the target with the other among the distractors (200 trials each)

| cell | pairs | acc of the stronger member | of the weaker member | pairs with a strict owner (one ≥ 0.9, other ≤ 0.1) | pairs shared (both 0.3–0.7) |
|---|---|---|---|---|---|
| generations | 363 | 1.00 | 0.00 | 1.00 | 0.00 |
| random+accumulate | 1108 | 1.00 | 0.00 | 1.00 | 0.00 |
| random+rewrite | 862 | 1.00 | 0.00 | 1.00 | 0.00 |
| success+accumulate | 1455 | 1.00 | 0.00 | 1.00 | 0.00 |
| success+rewrite | 1718 | 1.00 | 0.00 | 1.00 | 0.00 |
| hard+accumulate | 2292 | 1.00 | 0.00 | 1.00 | 0.00 |
| hard+rewrite | 1990 | 1.00 | 0.00 | 1.00 | 0.00 |
| pair | 163 | 1.00 | 0.00 | 1.00 | 0.00 |

## C. Productive variation: the sender's non-greedy alternatives (200 samples per training object)

| cell | n | share of samples ≠ greedy | of those: equals the greedy word of a Hamming-1 neighbour | of any other object | a word used by nobody |
|---|---|---|---|---|---|
| generations | 30 | 0.33 | 0.22 | 0.04 | 0.74 |
| random+accumulate | 30 | 0.05 | 0.50 | 0.05 | 0.45 |
| random+rewrite | 30 | 0.05 | 0.45 | 0.05 | 0.51 |
| success+accumulate | 30 | 0.05 | 0.43 | 0.06 | 0.51 |
| success+rewrite | 30 | 0.03 | 0.46 | 0.07 | 0.46 |
| hard+accumulate | 30 | 0.04 | 0.52 | 0.04 | 0.44 |
| hard+rewrite | 30 | 0.03 | 0.48 | 0.04 | 0.48 |
| pair | 30 | 0.34 | 0.05 | 0.02 | 0.93 |

## D. Capacity anatomy (success+rewrite, seeds 0–9): fidelity per taught object, and spillover to untaught objects

| capacity | taught objects | fidelity on taught | parent–child agreement on untaught train objects | founder intelligibility |
|---|---|---|---|---|
| 8 | 8 | 0.69 | 0.19 | 0.25 |
| 19 | 19 | 0.81 | 0.25 | 0.50 |
| 40 | 40 | 0.86 | 0.31 | 0.81 |

## E. Mechanism link: per transition, regularisation activity vs structure gain

activity = Σ over changed taught forms of (fit(new) − fit(inherited)); gain = child topsim − parent topsim. Correlation across transitions, within cell.

| cell | transitions | corr(activity, Δtopsim) | corr(share changed, Δtopsim) | corr(activity, Δtopsim_distinct) |
|---|---|---|---|---|
| random+accumulate | 150 | +0.42 | +0.21 | +0.41 |
| random+rewrite | 150 | +0.17 | -0.01 | +0.22 |
| success+accumulate | 150 | +0.36 | +0.21 | +0.31 |
| success+rewrite | 150 | +0.23 | +0.09 | +0.19 |
| hard+accumulate | 150 | +0.35 | +0.03 | +0.43 |
| hard+rewrite | 150 | +0.29 | +0.14 | +0.38 |

## F. Absorption timing: share of held-out objects whose message equals a training object's, by step inside a generation (gens ≥ 1)

| cell | 250 | 500 | 1000 | 1500 | 2000 |
|---|---|---|---|---|---|
| generations | 0.86 | 0.70 | 0.63 | 0.61 | 0.58 |
| random+accumulate | 0.94 | 0.94 | 0.93 | 0.91 | 0.90 |
| random+rewrite | 0.90 | 0.90 | 0.89 | 0.89 | 0.87 |
| success+accumulate | 0.96 | 0.96 | 0.95 | 0.93 | 0.91 |
| success+rewrite | 0.94 | 0.95 | 0.94 | 0.93 | 0.92 |
| hard+accumulate | 0.96 | 0.96 | 0.95 | 0.95 | 0.94 |
| hard+rewrite | 0.96 | 0.96 | 0.95 | 0.94 | 0.93 |
| pair | 0.87 | 0.72 | 0.65 | 0.61 | 0.59 |

## G. Fossils: objects whose message is identical in generation 0 and generation 5

expected = product of per-generation survival rates (independent mutation). Which objects fossilise: recorded slots vs others; homonym class size.

| cell | n | fossils (of 64) | expected under independent mutation | fossils among recorded (gen-0 slots) | among unrecorded | mean class size of fossil words | of non-fossil words |
|---|---|---|---|---|---|---|---|
| random+accumulate | 30 | 3.2 | 0.1 | 0.07 | 0.04 | 3.3 | 2.2 |
| random+rewrite | 30 | 15.6 | 1.4 | 0.49 | 0.14 | 2.8 | 2.1 |
| success+accumulate | 30 | 2.3 | 0.1 | 0.08 | 0.02 | 3.4 | 2.2 |
| success+rewrite | 30 | 6.5 | 0.9 | 0.17 | 0.07 | 3.6 | 2.1 |
| hard+accumulate | 30 | 9.8 | 1.6 | 0.29 | 0.10 | 3.8 | 2.0 |
| hard+rewrite | 30 | 9.0 | 2.0 | 0.24 | 0.10 | 3.7 | 2.0 |

## H. Homonym geometry: share of training homonym pairs at Hamming distance 1 (random pair of training objects: ≈ 0.14)

| cell | homonym pairs | share at distance 1 | at distance 3 |
|---|---|---|---|
| generations | 363 | 0.85 | 0.00 |
| random+accumulate | 1108 | 0.69 | 0.02 |
| random+rewrite | 862 | 0.74 | 0.02 |
| success+accumulate | 1455 | 0.60 | 0.04 |
| success+rewrite | 1718 | 0.63 | 0.04 |
| hard+accumulate | 2292 | 0.59 | 0.04 |
| hard+rewrite | 1990 | 0.62 | 0.05 |
| pair | 163 | 0.77 | 0.01 |

