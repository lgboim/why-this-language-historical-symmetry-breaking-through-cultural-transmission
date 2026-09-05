# K13 / K15 on results_arch (seeds 100–119), per seed

## K13a: ARI rewrite cells − no-record generations cell

| family | n | wins/losses | mean | 95% CI | p | verdict |
|---|---|---|---|---|---|---|
| cap 8 | 20 | 20/0 | +0.152 | [+0.113, +0.193] | 0.000 | SUPPORTED |
| cap 40 | 20 | 12/8 | +0.035 | [-0.012, +0.089] | 0.503 | INCONCLUSIVE |
| noise 0.2 | 20 | 15/5 | +0.028 | [-0.002, +0.063] | 0.041 | INCONCLUSIVE |
| reader both | 20 | 18/2 | +0.126 | [+0.078, +0.177] | 0.000 | SUPPORTED |

## K13b: ARI rewrite − accumulate within results_v3_confirm2 (random/success selection; hard exempt, shown for information)

| family | select | n | wins/losses | mean | 95% CI | p | verdict |
|---|---|---|---|---|---|---|---|
| cap 8 | random | 20 | 11/9 | +0.011 | [-0.084, +0.100] | 0.824 | INCONCLUSIVE |
| cap 8 | success | 20 | 7/13 | -0.035 | [-0.099, +0.030] | 0.263 | INCONCLUSIVE |
| cap 8 | hard | 20 | 8/11 | -0.003 | [-0.059, +0.059] | 0.648 | INCONCLUSIVE |
| cap 40 | random | 20 | 15/2 | +0.091 | [+0.010, +0.207] | 0.002 | INCONCLUSIVE |
| cap 40 | success | 20 | 9/4 | +0.010 | [-0.043, +0.073] | 0.267 | INCONCLUSIVE |
| cap 40 | hard | 20 | 4/2 | -0.034 | [-0.130, +0.024] | 0.688 | INCONCLUSIVE |
| noise 0.2 | random | 20 | 10/9 | +0.014 | [-0.021, +0.050] | 1.000 | INCONCLUSIVE |
| noise 0.2 | success | 20 | 10/9 | +0.031 | [-0.018, +0.092] | 1.000 | INCONCLUSIVE |
| noise 0.2 | hard | 20 | 8/9 | -0.004 | [-0.059, +0.060] | 1.000 | INCONCLUSIVE |
| reader both | random | 20 | 11/8 | +0.036 | [-0.060, +0.132] | 0.648 | INCONCLUSIVE |
| reader both | success | 20 | 9/10 | -0.048 | [-0.116, +0.013] | 1.000 | INCONCLUSIVE |
| reader both | hard | 20 | 5/10 | +0.044 | [-0.029, +0.128] | 0.302 | INCONCLUSIVE |

## K15: retention with ≥1 same-form taught neighbour − with only other-form taught neighbours (predicted gap ≥ 0.15)

| family | n | wins/losses | mean | 95% CI | p | verdict | same / other |
|---|---|---|---|---|---|---|---|
| cap 8 | 20 | 18/2 | +0.203 | [+0.147, +0.254] | 0.000 | SUPPORTED | 0.37 / 0.17 |
| cap 40 | 19 | 7/12 | -0.076 | [-0.197, +0.043] | 0.359 | INCONCLUSIVE | 0.40 / 0.48 |
| noise 0.2 | 20 | 11/9 | +0.015 | [-0.054, +0.080] | 0.824 | INCONCLUSIVE | 0.31 / 0.29 |
| reader both | 20 | 11/9 | +0.057 | [-0.006, +0.126] | 0.824 | INCONCLUSIVE | 0.46 / 0.41 |
