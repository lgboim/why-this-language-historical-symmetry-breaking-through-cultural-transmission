# probe22 — checks prompted by organising the report

## A. Main effects of the five knobs under the clean metrics (seeds 0–9; paired by seed; wins/losses and mean diff; * = CI excludes 0)

| factor | A − B | distinct | CBM | owners_topsim | convexity | n_owners | continuity | test_acc |
|---|---|---|---|---|---|---|---|---|
| select | hard − random | 4/5 -0.007 | 7/3 +0.005 | 3/4 -0.012 | 7/1 +0.034* | 0/10 -5.979* | 1/9 -0.034* | 1/9 -0.044* |
| select | hard − success | 4/5 -0.005 | 5/5 -0.003 | 2/5 -0.029 | 5/4 +0.026 | 0/10 -2.487* | 10/0 +0.052* | 3/7 -0.017 |
| select | random − success | 5/5 +0.002 | 2/8 -0.008* | 3/7 -0.020* | 5/4 +0.001 | 10/0 +3.492* | 10/0 +0.086* | 8/2 +0.027* |
| fresh | accumulate − rewrite | 0/9 -0.047* | 0/10 -0.021* | 0/7 -0.062* | 6/2 +0.034* | 1/9 -2.075* | 0/10 -0.130* | 2/8 -0.007 |
| capacity | 8 − 19 | 1/8 -0.051* | 4/6 +0.001 | 3/4 -0.017 | 9/1 +0.075* | 0/10 -11.108* | 0/10 -0.177* | 1/9 -0.061* |
| capacity | 8 − 40 | 1/8 -0.051* | 10/0 +0.041* | 5/2 +0.024 | 8/0 +0.182* | 0/10 -24.621* | 0/10 -0.398* | 1/9 -0.054* |
| capacity | 19 − 40 | 6/4 +0.002 | 10/0 +0.039* | 10/0 +0.041* | 8/0 +0.113* | 0/10 -13.512* | 0/10 -0.221* | 5/5 +0.007 |
| noise | 0.0 − 0.2 | 7/2 +0.024* | 10/0 +0.022* | 6/1 +0.050* | 5/3 +0.039 | 1/9 -2.792* | 10/0 +0.077* | 4/6 -0.006 |
| reader | both − sender | 0/9 -0.015* | 2/8 -0.005 | 1/6 -0.021* | 2/6 -0.023* | 6/4 +0.175 | 8/2 +0.016* | 4/6 -0.004 |

## B. Where the ratchet acts: topsim_distinct restricted to TAUGHT objects vs UNTAUGHT training objects, by generation (mean over 30 seeds)

| cell | subset | gen 1 | gen 2 | gen 3 | gen 4 | gen 5 | gen1→gen5 paired |
|---|---|---|---|---|---|---|---|
| random+accumulate | taught | 0.224 | 0.225 | 0.216 | 0.217 | 0.201 | 30 | 10/20 | -0.024 | [-0.048, -0.000] | 0.099 | TWO-SIDED: A<B (CI) | |
| random+accumulate | untaught | 0.267 | 0.255 | 0.261 | 0.279 | 0.270 | 30 | 12/18 | +0.003 | [-0.022, +0.030] | 0.362 | TWO-SIDED: no difference (CI) | |
| random+rewrite | taught | 0.374 | 0.392 | 0.401 | 0.399 | 0.410 | 30 | 19/11 | +0.035 | [+0.008, +0.062] | 0.200 | TWO-SIDED: A>B (CI) | |
| random+rewrite | untaught | 0.328 | 0.310 | 0.316 | 0.317 | 0.324 | 30 | 15/15 | -0.004 | [-0.032, +0.023] | 1.000 | TWO-SIDED: no difference (CI) | |
| success+accumulate | taught | 0.339 | 0.358 | 0.327 | 0.325 | 0.337 | 30 | 15/15 | -0.003 | [-0.030, +0.023] | 1.000 | TWO-SIDED: no difference (CI) | |
| success+accumulate | untaught | 0.241 | 0.248 | 0.230 | 0.230 | 0.237 | 30 | 17/13 | -0.004 | [-0.039, +0.029] | 0.585 | TWO-SIDED: no difference (CI) | |
| success+rewrite | taught | 0.467 | 0.472 | 0.460 | 0.437 | 0.438 | 30 | 11/19 | -0.029 | [-0.065, +0.009] | 0.200 | TWO-SIDED: no difference (CI) | |
| success+rewrite | untaught | 0.299 | 0.325 | 0.296 | 0.304 | 0.293 | 30 | 14/16 | -0.006 | [-0.039, +0.027] | 0.856 | TWO-SIDED: no difference (CI) | |
| hard+accumulate | taught | 0.353 | 0.299 | 0.289 | 0.308 | 0.283 | 30 | 9/21 | -0.070 | [-0.116, -0.021] | 0.043 | TWO-SIDED: A<B (CI) | |
| hard+accumulate | untaught | 0.314 | 0.296 | 0.309 | 0.296 | 0.295 | 30 | 12/18 | -0.020 | [-0.064, +0.024] | 0.362 | TWO-SIDED: no difference (CI) | |
| hard+rewrite | taught | 0.353 | 0.315 | 0.321 | 0.337 | 0.324 | 30 | 11/19 | -0.029 | [-0.076, +0.021] | 0.200 | TWO-SIDED: no difference (CI) | |
| hard+rewrite | untaught | 0.314 | 0.320 | 0.318 | 0.334 | 0.348 | 30 | 19/11 | +0.033 | [-0.002, +0.067] | 0.200 | TWO-SIDED: no difference (CI) | |

Whole-language topsim_distinct over generations (probe6 B): +0.01 to +0.04 in rewrite cells.

## C. Continuity (founder intelligibility) vs each clean metric across the 74 record cells (cell means, seeds 0–9)

| metric | corr with continuity |
|---|---|
| distinct | +0.72 |
| CBM | -0.08 |
| owners_topsim | +0.28 |
| convexity | -0.68 |
| n_owners | +0.83 |
| test_acc | +0.46 |

## D. What does convexity of word meanings go with? (within-seed correlations across the 77 cells, seeds 0–9)

| quantity | mean within-seed corr with convexity |
|---|---|
| test_acc | +0.21 |
| intelligibility | -0.43 |
| distinct | -0.16 |
| CBM | +0.21 |
| n_owners | -0.43 |
| continuity | -0.30 |

Classes (size ≥ 3): connected classes have 3.75 orphans on their owner vs 3.41 for disconnected ones (n = 1692).

