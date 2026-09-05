# K1–K9 on results_replicate (seeds 100–119)

| id | test | metric | n | wins/losses | mean diff | 95% CI | p | verdict |
|---|---|---|---|---|---|---|---|---|
| K1 | cap 8 − cap 19 | distinct | 20 | 1/19 | -0.075 | [-0.092, -0.057] | 0.000 | SUPPORTED |
| K2 | cap 19 − cap 40 | distinct | 20 | 6/14 | -0.027 | [-0.044, -0.010] | 0.115 | TWO-SIDED: A<B (CI) |
| K3 | cap 19 − cap 40 | CBM | 20 | 13/7 | +0.015 | [+0.003, +0.027] | 0.263 | INCONCLUSIVE |
| K3 | cap 19 − cap 40 | owners_topsim | 20 | 14/6 | +0.019 | [-0.002, +0.038] | 0.115 | INCONCLUSIVE |
| K4 | cap 40 − cap 19 | continuity | 20 | 20/0 | +0.228 | [+0.208, +0.246] | 0.000 | SUPPORTED |
| K4 | cap 19 − cap 8 | continuity | 20 | 20/0 | +0.194 | [+0.176, +0.213] | 0.000 | SUPPORTED |
| K6 | noise 0.2 − noise 0 | distinct | 20 | 8/12 | -0.013 | [-0.022, -0.004] | 0.503 | INCONCLUSIVE |
| K6 | noise 0.2 − noise 0 | CBM | 20 | 3/17 | -0.020 | [-0.026, -0.013] | 0.003 | SUPPORTED |
| K7 | noise 0.2 − noise 0 | n_owners | 20 | 19/1 | +4.400 | [+3.358, +5.458] | 0.000 | SUPPORTED |
| K8 | both − sender | distinct | 20 | 6/14 | -0.011 | [-0.024, +0.002] | 0.115 | TWO-SIDED: no difference (CI) |
| K8 | both − sender | CBM | 20 | 7/13 | -0.004 | [-0.010, +0.003] | 0.263 | TWO-SIDED: no difference (CI) |
| K8 | both − sender | test_acc | 20 | 9/11 | -0.004 | [-0.019, +0.013] | 0.824 | TWO-SIDED: no difference (CI) |
| K9 | accumulate − rewrite | convexity | 20 | 9/11 | -0.011 | [-0.059, +0.038] | 0.824 | INCONCLUSIVE |
| K9 | cap 8 − cap 40 | convexity | 20 | 17/3 | +0.152 | [+0.095, +0.209] | 0.003 | SUPPORTED |

K5: across 30 cells, corr(continuity, distinct) = +0.88; corr(continuity, convexity) = -0.67; corr(continuity, CBM) = +0.50

K8 fidelity of taught forms, both − sender: | 120 | 96/19 | +0.053 | [+0.041, +0.064] | 0.000 | SUPPORTED |
