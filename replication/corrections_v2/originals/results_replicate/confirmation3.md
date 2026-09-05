# K13 / K15 on results_replicate (seeds 100–119), per seed

## K13a: ARI rewrite cells − no-record generations cell

| family | n | wins/losses | mean | 95% CI | p | verdict |
|---|---|---|---|---|---|---|
| cap 8 | 20 | 20/0 | +0.196 | [+0.170, +0.223] | 0.000 | SUPPORTED |
| cap 40 | 20 | 20/0 | +0.610 | [+0.569, +0.650] | 0.000 | SUPPORTED |
| noise 0.2 | 20 | 20/0 | +0.251 | [+0.226, +0.277] | 0.000 | SUPPORTED |
| reader both | 20 | 20/0 | +0.394 | [+0.354, +0.434] | 0.000 | SUPPORTED |

## K13b: ARI rewrite − accumulate within results_v3_confirm2 (random/success selection; hard exempt, shown for information)

| family | select | n | wins/losses | mean | 95% CI | p | verdict |
|---|---|---|---|---|---|---|---|
| cap 8 | random | 20 | 9/11 | -0.013 | [-0.059, +0.030] | 0.824 | INCONCLUSIVE |
| cap 8 | success | 20 | 6/14 | -0.061 | [-0.107, -0.015] | 0.115 | INCONCLUSIVE |
| cap 8 | hard | 20 | 4/5 | -0.010 | [-0.031, +0.008] | 1.000 | INCONCLUSIVE |
| cap 40 | random | 20 | 19/1 | +0.375 | [+0.288, +0.457] | 0.000 | SUPPORTED |
| cap 40 | success | 20 | 20/0 | +0.389 | [+0.329, +0.447] | 0.000 | SUPPORTED |
| cap 40 | hard | 20 | 14/6 | +0.060 | [+0.016, +0.104] | 0.115 | INCONCLUSIVE |
| noise 0.2 | random | 20 | 16/4 | +0.088 | [+0.056, +0.118] | 0.012 | SUPPORTED |
| noise 0.2 | success | 20 | 16/4 | +0.065 | [+0.033, +0.096] | 0.012 | SUPPORTED |
| noise 0.2 | hard | 20 | 11/9 | +0.022 | [-0.018, +0.063] | 0.824 | INCONCLUSIVE |
| reader both | random | 20 | 15/5 | +0.112 | [+0.051, +0.171] | 0.041 | INCONCLUSIVE |
| reader both | success | 20 | 13/7 | +0.064 | [+0.007, +0.118] | 0.263 | INCONCLUSIVE |
| reader both | hard | 20 | 11/7 | +0.033 | [+0.002, +0.066] | 0.481 | INCONCLUSIVE |

## K15: retention with ≥1 same-form taught neighbour − with only other-form taught neighbours (predicted gap ≥ 0.15)

| family | n | wins/losses | mean | 95% CI | p | verdict | same / other |
|---|---|---|---|---|---|---|---|
| cap 8 | 20 | 20/0 | +0.425 | [+0.406, +0.444] | 0.000 | SUPPORTED | 0.54 / 0.11 |
| cap 40 | 20 | 19/1 | +0.210 | [+0.140, +0.285] | 0.000 | SUPPORTED | 0.51 / 0.30 |
| noise 0.2 | 20 | 20/0 | +0.362 | [+0.341, +0.379] | 0.000 | SUPPORTED | 0.46 / 0.10 |
| reader both | 20 | 20/0 | +0.409 | [+0.382, +0.437] | 0.000 | SUPPORTED | 0.60 / 0.19 |
