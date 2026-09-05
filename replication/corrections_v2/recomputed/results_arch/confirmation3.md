# K13 / K15 on results_arch (seeds 100–119), per seed

## K13a: ARI rewrite cells − no-record generations cell

| family | n | wins/losses | mean | 95% CI | p | verdict |
|---|---|---|---|---|---|---|
| cap 8 | 20 | 19/1 | +0.165 | [+0.116, +0.211] | 0.000 | SUPPORTED |
| cap 40 | 20 | 20/0 | +0.685 | [+0.646, +0.723] | 0.000 | SUPPORTED |
| noise 0.2 | 20 | 20/0 | +0.398 | [+0.315, +0.480] | 0.000 | SUPPORTED |
| reader both | 20 | 20/0 | +0.442 | [+0.364, +0.524] | 0.000 | SUPPORTED |

## K13b: ARI rewrite − accumulate within results_v3_confirm2 (random/success selection; hard exempt, shown for information)

| family | select | n | wins/losses | mean | 95% CI | p | verdict |
|---|---|---|---|---|---|---|---|
| cap 8 | random | 20 | 13/7 | +0.061 | [-0.042, +0.157] | 0.263 | INCONCLUSIVE |
| cap 8 | success | 20 | 8/12 | -0.025 | [-0.091, +0.044] | 0.503 | INCONCLUSIVE |
| cap 8 | hard | 20 | 8/11 | -0.003 | [-0.059, +0.059] | 0.648 | INCONCLUSIVE |
| cap 40 | random | 20 | 19/1 | +0.461 | [+0.311, +0.597] | 0.000 | SUPPORTED |
| cap 40 | success | 20 | 18/0 | +0.420 | [+0.314, +0.526] | 0.000 | SUPPORTED |
| cap 40 | hard | 20 | 10/1 | +0.156 | [+0.067, +0.251] | 0.012 | INCONCLUSIVE |
| noise 0.2 | random | 20 | 15/5 | +0.264 | [+0.123, +0.417] | 0.041 | INCONCLUSIVE |
| noise 0.2 | success | 20 | 20/0 | +0.441 | [+0.351, +0.530] | 0.000 | SUPPORTED |
| noise 0.2 | hard | 20 | 13/5 | +0.106 | [-0.013, +0.229] | 0.096 | INCONCLUSIVE |
| reader both | random | 20 | 14/6 | +0.206 | [+0.062, +0.345] | 0.115 | INCONCLUSIVE |
| reader both | success | 20 | 17/3 | +0.342 | [+0.219, +0.465] | 0.003 | SUPPORTED |
| reader both | hard | 20 | 9/7 | +0.044 | [-0.071, +0.159] | 0.804 | INCONCLUSIVE |

## K15: retention with ≥1 same-form taught neighbour − with only other-form taught neighbours (predicted gap ≥ 0.15)

| family | n | wins/losses | mean | 95% CI | p | verdict | same / other |
|---|---|---|---|---|---|---|---|
| cap 8 | 20 | 18/2 | +0.203 | [+0.147, +0.254] | 0.000 | SUPPORTED | 0.37 / 0.17 |
| cap 40 | 19 | 7/12 | -0.076 | [-0.197, +0.043] | 0.359 | INCONCLUSIVE | 0.40 / 0.48 |
| noise 0.2 | 20 | 11/9 | +0.015 | [-0.054, +0.080] | 0.824 | INCONCLUSIVE | 0.31 / 0.29 |
| reader both | 20 | 11/9 | +0.057 | [-0.006, +0.126] | 0.824 | INCONCLUSIVE | 0.46 / 0.41 |
