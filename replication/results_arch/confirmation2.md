# K1–K9 on results_arch (seeds 100–119)

| id | test | metric | n | wins/losses | mean diff | 95% CI | p | verdict |
|---|---|---|---|---|---|---|---|---|
| K1 | cap 8 − cap 19 | distinct | 20 | 4/16 | -0.106 | [-0.145, -0.069] | 0.012 | SUPPORTED |
| K2 | cap 19 − cap 40 | distinct | 20 | 20/0 | +0.068 | [+0.051, +0.084] | 0.000 | TWO-SIDED: A>B (CI) |
| K3 | cap 19 − cap 40 | CBM | 20 | 20/0 | +0.081 | [+0.062, +0.100] | 0.000 | SUPPORTED |
| K3 | cap 19 − cap 40 | owners_topsim | 20 | 20/0 | +0.069 | [+0.053, +0.086] | 0.000 | SUPPORTED |
| K4 | cap 40 − cap 19 | continuity | 20 | 20/0 | +0.189 | [+0.170, +0.206] | 0.000 | SUPPORTED |
| K4 | cap 19 − cap 8 | continuity | 20 | 20/0 | +0.229 | [+0.198, +0.260] | 0.000 | SUPPORTED |
| K6 | noise 0.2 − noise 0 | distinct | 20 | 4/16 | -0.035 | [-0.051, -0.020] | 0.012 | SUPPORTED |
| K6 | noise 0.2 − noise 0 | CBM | 20 | 5/14 | -0.029 | [-0.046, -0.013] | 0.064 | INCONCLUSIVE |
| K7 | noise 0.2 − noise 0 | n_owners | 20 | 6/14 | -1.300 | [-2.109, -0.467] | 0.115 | INCONCLUSIVE |
| K8 | both − sender | distinct | 20 | 1/19 | -0.064 | [-0.080, -0.048] | 0.000 | TWO-SIDED: A<B (CI) |
| K8 | both − sender | CBM | 20 | 2/18 | -0.054 | [-0.068, -0.038] | 0.000 | TWO-SIDED: A<B (CI) |
| K8 | both − sender | test_acc | 20 | 1/19 | -0.024 | [-0.033, -0.014] | 0.000 | TWO-SIDED: A<B (CI) |
| K9 | accumulate − rewrite | convexity | 3 | 0/1 | -0.083 | [-0.250, +0.000] | 1.000 | UNDERPOWERED (n<8) |
| K9 | cap 8 − cap 40 | convexity | 13 | 3/8 | +0.015 | [-0.114, +0.158] | 0.227 | INCONCLUSIVE |

K5: across 30 cells, corr(continuity, distinct) = +0.30; corr(continuity, convexity) = +nan; corr(continuity, CBM) = +0.13

K8 fidelity of taught forms, both − sender: | 120 | 112/5 | +0.097 | [+0.086, +0.109] | 0.000 | SUPPORTED |
