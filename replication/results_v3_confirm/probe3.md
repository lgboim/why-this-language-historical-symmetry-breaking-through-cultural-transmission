# probe3 — after confirmation

discovery = seeds 0–9 (`results_v3`), confirm = seeds 10–29 (`results_v3_confirm`). Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## A. The confirmation verdicts under three metrics

| set | comparison | topsim | topsim_distinct | CBM |
|---|---|---|---|---|
| discovery | rewrite − accumulate (success) | 10/0 +0.085 * | 9/1 +0.092 * | 10/0 +0.044 * |
| discovery | rewrite − accumulate (random) | 7/3 +0.050 * | 8/2 +0.078 * | 9/1 +0.035 * |
| discovery | rewrite − accumulate (hard) | 8/2 +0.043 * | 9/1 +0.059 * | 7/3 +0.026 * |
| discovery | hard − random (rewrite) | 5/5 +0.039  | 4/6 -0.005  | 7/3 +0.026 * |
| discovery | success+rewrite − generations | 6/4 +0.021  | 4/6 -0.013  | 7/3 +0.042 * |
| discovery | hard+rewrite − generations | 7/3 +0.046 * | 5/5 -0.012  | 9/1 +0.061 * |
| discovery | success+accumulate − generations | 2/8 -0.064 * | 1/9 -0.105 * | 5/5 -0.002  |
| discovery | generations − pair | 10/0 +0.060 * | 8/2 +0.048 * | 8/2 +0.033  |
| confirm | rewrite − accumulate (success) | 17/3 +0.071 * | 14/6 +0.062 * | 18/2 +0.058 * |
| confirm | rewrite − accumulate (random) | 18/2 +0.065 * | 18/2 +0.076 * | 19/0 +0.055 * |
| confirm | rewrite − accumulate (hard) | 10/10 +0.008  | 14/6 +0.023  | 12/8 +0.015  |
| confirm | hard − random (rewrite) | 14/6 +0.027  | 9/11 -0.010  | 11/7 +0.018 * |
| confirm | success+rewrite − generations | 16/4 +0.036 * | 9/11 -0.019  | 19/1 +0.070 * |
| confirm | hard+rewrite − generations | 15/5 +0.043 * | 10/10 -0.021  | 19/1 +0.066 * |
| confirm | success+accumulate − generations | 6/14 -0.035 * | 3/17 -0.081 * | 11/9 +0.012  |
| confirm | generations − pair | 17/3 +0.053 * | 17/3 +0.045 * | 15/5 +0.026 * |

`*` = bootstrap 95% CI excludes 0.

## B. The absorption bound as a law

bound = share of held-out objects whose message is NOT shared with any training object (final language). Claim: test_acc ≈ chance·(1−bound) + bound, i.e. an absorbed held-out object is decoded as the training object.

- discovery (770 runs): corr(predicted, observed test_acc) = +0.17; observed − predicted: mean +0.271, sd 0.142; runs above the bound by > 0.1: 89%
- confirm (200 runs): corr(predicted, observed test_acc) = -0.11; observed − predicted: mean +0.269, sd 0.196; runs above the bound by > 0.1: 80%

## C. Age of a carved form vs its regularity (accumulate cells, both sets)

For every entry the last child reads: age = generations since that (object, message) first appeared in the record; fit = local Spearman fit of that form inside the parent's final language; kept = child still uses it at the end.

| set | cell | n entries | fit: age 0 | age ≥ 2 | kept: age 0 | age ≥ 2 | corr(age, fit) |
|---|---|---|---|---|---|---|---|
| discovery | random+accumulate | 190 | nan | 0.284 | nan | 0.69 | +nan |
| discovery | success+accumulate | 190 | nan | 0.297 | nan | 0.64 | +nan |
| discovery | hard+accumulate | 190 | 0.355 | 0.424 | 0.69 | 0.81 | +0.22 |
| confirm | random+accumulate | 380 | nan | 0.281 | nan | 0.75 | +nan |
| confirm | success+accumulate | 380 | nan | 0.305 | nan | 0.62 | +nan |
| confirm | hard+accumulate | 380 | 0.358 | 0.396 | 0.80 | 0.83 | +0.12 |

## D. Post-hoc mechanisms from seeds 0–9, re-tested on seeds 10–29

### D1. When the child changes an inherited form, the new form fits better

| cell | share changed | fit(new) − fit(inherited) | n | wins/losses | mean | CI | p | |
|---|---|---|---|---|---|---|---|
| random+accumulate | 0.29 | +0.075 | 20 | 20/0 | +0.075 | [+0.055, +0.094] | 0.000 | SUPPORTED |
| random+rewrite | 0.16 | +0.044 | 20 | 19/1 | +0.044 | [+0.032, +0.056] | 0.000 | SUPPORTED |
| success+accumulate | 0.37 | +0.093 | 20 | 19/1 | +0.093 | [+0.061, +0.126] | 0.000 | SUPPORTED |
| success+rewrite | 0.20 | +0.063 | 20 | 18/2 | +0.063 | [+0.049, +0.077] | 0.000 | SUPPORTED |
| hard+accumulate | 0.21 | +0.061 | 20 | 19/1 | +0.061 | [+0.042, +0.080] | 0.000 | SUPPORTED |
| hard+rewrite | 0.19 | +0.068 | 20 | 18/2 | +0.068 | [+0.051, +0.085] | 0.000 | SUPPORTED |

### D2. The child inherits which attribute gets dropped (share of transitions keeping the parent's most-dropped attribute)

| cell | share |
|---|---|
| generations | 0.32 |
| random+accumulate | 0.57 |
| random+rewrite | 0.79 |
| success+accumulate | 0.61 |
| success+rewrite | 0.66 |
| hard+accumulate | 0.81 |
| hard+rewrite | 0.84 |

### D3. Semantic consistency of homonym classes (gain over class-size-matched random)

| cell | gain | vs generations |
|---|---|---|
| generations | +0.127 | – |
| pair | +0.066 | | 20 | 3/17 | -0.061 | [-0.090, -0.035] | 0.003 | TWO-SIDED: A<B (CI) | |
| random+accumulate | +0.222 | | 20 | 18/2 | +0.095 | [+0.062, +0.126] | 0.000 | TWO-SIDED: A>B (CI) | |
| random+rewrite | +0.216 | | 20 | 18/2 | +0.089 | [+0.054, +0.118] | 0.000 | TWO-SIDED: A>B (CI) | |
| success+accumulate | +0.221 | | 20 | 19/1 | +0.094 | [+0.069, +0.121] | 0.000 | TWO-SIDED: A>B (CI) | |
| success+rewrite | +0.263 | | 20 | 20/0 | +0.136 | [+0.108, +0.162] | 0.000 | TWO-SIDED: A>B (CI) | |
| hard+accumulate | +0.280 | | 20 | 19/1 | +0.153 | [+0.122, +0.183] | 0.000 | TWO-SIDED: A>B (CI) | |
| hard+rewrite | +0.282 | | 20 | 19/1 | +0.155 | [+0.118, +0.188] | 0.000 | TWO-SIDED: A>B (CI) | |

## E. Who decides generalisation: the held-out split (seed) or the channel (cell)?

- discovery, test_acc: seed explains 13% of variance, cell 22%, residual 65% (77 cells × 10 seeds)
- discovery, topsim: seed explains 4% of variance, cell 45%, residual 51% (77 cells × 10 seeds)
- confirm, test_acc: seed explains 14% of variance, cell 11%, residual 74% (10 cells × 20 seeds)
- confirm, topsim: seed explains 7% of variance, cell 42%, residual 51% (10 cells × 20 seeds)

