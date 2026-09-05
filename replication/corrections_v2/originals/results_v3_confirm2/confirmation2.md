# Second confirmation (seeds 10–29) — K1–K9

| id | test | metric | n | wins/losses | mean diff | 95% CI | p | verdict |
|---|---|---|---|---|---|---|---|---|
| K1 | cap 8 − cap 19 | distinct | 20 | 0/20 | -0.072 | [-0.089, -0.055] | 0.000 | SUPPORTED |
| K2 | cap 19 − cap 40 | distinct | 20 | 6/14 | -0.017 | [-0.033, -0.003] | 0.115 | TWO-SIDED: A<B (CI) |
| K3 | cap 19 − cap 40 | CBM | 20 | 17/3 | +0.024 | [+0.015, +0.034] | 0.003 | SUPPORTED |
| K3 | cap 19 − cap 40 | owners_topsim | 20 | 14/6 | +0.028 | [+0.005, +0.049] | 0.115 | INCONCLUSIVE |
| K4 | cap 40 − cap 19 | continuity | 20 | 20/0 | +0.195 | [+0.177, +0.212] | 0.000 | SUPPORTED |
| K4 | cap 19 − cap 8 | continuity | 20 | 20/0 | +0.205 | [+0.186, +0.226] | 0.000 | SUPPORTED |
| K6 | noise 0.2 − noise 0 | distinct | 20 | 5/15 | -0.010 | [-0.025, +0.006] | 0.041 | INCONCLUSIVE |
| K6 | noise 0.2 − noise 0 | CBM | 20 | 3/17 | -0.023 | [-0.030, -0.015] | 0.003 | SUPPORTED |
| K7 | noise 0.2 − noise 0 | n_owners | 20 | 19/1 | +4.792 | [+3.567, +5.908] | 0.000 | SUPPORTED |
| K8 | both − sender | distinct | 20 | 7/13 | -0.007 | [-0.021, +0.007] | 0.263 | TWO-SIDED: no difference (CI) |
| K8 | both − sender | CBM | 20 | 6/14 | -0.008 | [-0.014, -0.001] | 0.115 | TWO-SIDED: A<B (CI) |
| K8 | both − sender | test_acc | 20 | 9/11 | -0.007 | [-0.023, +0.008] | 0.824 | TWO-SIDED: no difference (CI) |
| K9 | accumulate − rewrite | convexity | 20 | 9/11 | +0.010 | [-0.052, +0.076] | 0.824 | INCONCLUSIVE |
| K9 | cap 8 − cap 40 | convexity | 20 | 20/0 | +0.216 | [+0.165, +0.266] | 0.000 | SUPPORTED |

K5: across 30 cells, corr(continuity, distinct) = +0.86; corr(continuity, convexity) = -0.68; corr(continuity, CBM) = +0.35

K8 fidelity of taught forms, both − sender: | 120 | 91/24 | +0.052 | [+0.040, +0.064] | 0.000 | INCONCLUSIVE |
