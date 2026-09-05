# probe7 — frontier, forgetting, elimination, the founder's carvings

Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## A. Continuity vs structure: the Pareto frontier over all cells (seeds 0–9)

continuity = founder intelligibility (last receiver with gen-0 sender); structure = topsim_distinct (collision-free). Cell means.

| cell | continuity | topsim_distinct | topsim | test_acc |
|---|---|---|---|---|
| `sel-random_slots-fixed_fresh-rewrite_cap-40_noise-0.0_rd-both` | 0.93 | 0.307 | 0.323 | 0.57 |
| `sel-random_slots-fixed_fresh-rewrite_cap-40_noise-0.0_rd-sender` | 0.90 | 0.318 | 0.336 | 0.58 |
| `sel-hard_slots-dynamic_fresh-accumulate_cap-40_noise-0.0_rd-sender` | 0.89 | 0.338 | 0.359 | 0.60 |
| `sel-success_slots-dynamic_fresh-rewrite_cap-40_noise-0.0_rd-sender` | 0.81 | 0.365 | 0.385 | 0.57 |

Across 75 cells: corr(continuity, topsim_distinct) = +0.67; corr(continuity, test_acc) = +0.43.

## B. Within a lineage: does structure rise as the founder is forgotten?

Per run, over generations 1–5: corr(topsim_g, intelligibility of receiver g with the gen-0 sender). Negative = structure rises as the founder fades.

| cell | n runs | mean within-run corr | runs with corr < 0 | topsim gen1→gen5 | founder intelligibility gen1→gen5 |
|---|---|---|---|---|---|
| random+accumulate | 30 | +0.09 | 0.40 | -0.003 | +0.012 |
| random+rewrite | 30 | -0.10 | 0.63 | +0.013 | -0.095 |
| success+accumulate | 30 | +0.00 | 0.37 | -0.001 | +0.007 |
| success+rewrite | 30 | -0.27 | 0.70 | +0.037 | -0.277 |
| hard+accumulate | 30 | -0.14 | 0.60 | +0.016 | -0.252 |
| hard+rewrite | 30 | -0.35 | 0.73 | +0.036 | -0.252 |

## C. Direct elimination test (final agents): held-out accuracy with vs without an absorbing training object among the distractors

For every held-out object that shares its message with ≥1 training object: 200 trials with the absorber forced into the distractors, 200 without any absorber.

| cell | n | held-out objects with an absorber | acc, absorber present | acc, absorber absent | acc of held-out objects with NO absorber at all |
|---|---|---|---|---|---|
| generations | 30 | 0.55 | 0.00 | 0.67 | 0.63 |
| random+accumulate | 30 | 0.90 | 0.00 | 0.68 | 0.60 |
| random+rewrite | 30 | 0.87 | 0.00 | 0.67 | 0.63 |
| success+accumulate | 30 | 0.91 | 0.01 | 0.65 | 0.58 |
| success+rewrite | 30 | 0.95 | 0.00 | 0.73 | 0.57 |
| hard+accumulate | 30 | 0.97 | 0.00 | 0.79 | 0.60 |
| hard+rewrite | 30 | 0.95 | 0.00 | 0.80 | 0.74 |
| pair | 30 | 0.46 | 0.00 | 0.57 | 0.57 |

## D. When a held-out object reuses a training word, whose word is it?

| cell | absorbed held-out objects | share whose absorber is a Hamming-1 neighbour | expected if random among training objects |
|---|---|---|---|
| generations | 263 | 0.64 | 0.14 |
| random+accumulate | 433 | 0.78 | 0.14 |
| random+rewrite | 417 | 0.74 | 0.14 |
| success+accumulate | 437 | 0.80 | 0.14 |
| success+rewrite | 456 | 0.83 | 0.14 |
| hard+accumulate | 464 | 0.91 | 0.14 |
| hard+rewrite | 457 | 0.91 | 0.14 |
| pair | 221 | 0.48 | 0.14 |

## E. Which objects does a success-selected record carve in generation 0?

| cell | per-object accuracy at gen-0 end: carved | not carved | # training neighbours: carved | not carved | share of carved objects that are homonyms at gen-0 end | all train |
|---|---|---|---|---|---|---|
| success+accumulate | 0.968 | 0.970 | 6.95 | 6.57 | 0.60 | 0.57 |
| success+rewrite | 0.968 | 0.970 | 6.95 | 6.57 | 0.60 | 0.57 |
| success+accumulate cap40 | 0.972 | 0.980 | 6.81 | 6.11 | 0.51 | 0.48 |

## F. Does a more diverse record (attribute-value coverage of the 19 slots) give the child more structure or continuity?

diversity = mean entropy over attributes of the recorded objects' values (bits, max 2). Within-seed correlations across the 4 fixed-slot cells × generations.

- over 900 transmissions: corr(diversity, child topsim) = +0.12; corr(diversity, child test_acc) = +0.13; corr(diversity, child lexicon size) = +0.18
- mean diversity by cell: random+accumulate 1.91, random+rewrite 1.91, success+accumulate 1.85, success+rewrite 1.86, hard+accumulate 1.91, hard+rewrite 1.91

## G. Receiver lineage: agreement of parent's and child's decode maps (over all 64 messages of the CHILD's language)

child receiver vs parent receiver, both decoding the child's final messages; agreement = share of the 64 objects decoded to the same object.

| cell | n | agreement | agreement on objects the child decodes CORRECTLY | on objects it decodes wrongly |
|---|---|---|---|---|
| generations | 30 | 0.02 | 0.02 | 0.02 |
| random+accumulate | 30 | 0.25 | 0.26 | 0.24 |
| random+rewrite | 30 | 0.41 | 0.44 | 0.38 |
| success+accumulate | 30 | 0.21 | 0.23 | 0.20 |
| success+rewrite | 30 | 0.34 | 0.35 | 0.33 |
| hard+accumulate | 30 | 0.28 | 0.27 | 0.29 |
| hard+rewrite | 30 | 0.30 | 0.28 | 0.31 |

## H. Oral transmission proper (random subset REDRAWN each generation) vs a fixed subset (seeds 0–9)

| cell | founder intelligibility | half-life proxy: parent intelligibility | topsim | topsim_distinct | test_acc | objects ever transmitted over 5 generations |
|---|---|---|---|---|---|---|
| random+rewrite (fixed) | 0.74 | 0.86 | 0.362 | 0.330 | 0.60 | 19.0 |
| oral: random+rewrite (redraw) | 0.58 | 0.81 | 0.376 | 0.336 | 0.61 | 41.3 |
| random+accumulate (fixed) | 0.44 | 0.73 | 0.313 | 0.253 | 0.62 | 19.0 |
| oral: random+accumulate (redraw) | 0.47 | 0.76 | 0.348 | 0.307 | 0.55 | 41.3 |

