# Symbol emergence — summary

Seeds per condition: pair=10, population=10, generations=10, oral=10, oral_fixed=10, bone=10, bone_edition=10

Final values (mean ± sd over seeds). test_acc = held-out attribute combinations (chance = 0.2). topsim = topographic similarity (tie-corrected Spearman). posdis = positional disentanglement. n_unique_msgs = distinct messages over the 64 objects.

| condition | train_acc | test_acc | topsim | posdis | n_unique_msgs |
|---|---|---|---|---|---|
| pair | 0.993 ± 0.007 | 0.615 ± 0.091 | 0.305 ± 0.035 | 0.079 ± 0.051 | 51.900 ± 5.646 |
| population | 0.986 ± 0.013 | 0.615 ± 0.066 | 0.336 ± 0.042 | 0.112 ± 0.041 | 48.200 ± 7.131 |
| generations | 0.979 ± 0.018 | 0.605 ± 0.131 | 0.327 ± 0.037 | 0.102 ± 0.054 | 44.600 ± 9.348 |
| oral | 0.940 ± 0.018 | 0.619 ± 0.110 | 0.345 ± 0.054 | 0.155 ± 0.077 | 22.800 ± 5.514 |
| oral_fixed | 0.957 ± 0.023 | 0.597 ± 0.103 | 0.381 ± 0.059 | 0.172 ± 0.089 | 31.500 ± 5.462 |
| bone | 0.935 ± 0.026 | 0.566 ± 0.083 | 0.314 ± 0.049 | 0.141 ± 0.099 | 22.300 ± 4.448 |
| bone_edition | 0.933 ± 0.036 | 0.567 ± 0.095 | 0.347 ± 0.046 | 0.146 ± 0.098 | 21.600 ± 5.481 |

## Paired-by-seed comparisons (A − B)

wins = seeds where A > B. p = two-sided exact sign test. CI = bootstrap 95% of mean difference.

### test_acc

| A | B | n | wins/ties/losses | mean diff | 95% CI | p |
|---|---|---|---|---|---|---|
| pair | population | 10 | 6/0/4 | +0.001 | [-0.054, +0.051] | 0.754 |
| pair | generations | 10 | 7/0/3 | +0.010 | [-0.069, +0.090] | 0.344 |
| pair | oral | 10 | 6/0/4 | -0.003 | [-0.086, +0.081] | 0.754 |
| pair | oral_fixed | 10 | 5/0/5 | +0.019 | [-0.041, +0.077] | 1.000 |
| pair | bone | 10 | 6/0/4 | +0.049 | [-0.031, +0.126] | 0.754 |
| pair | bone_edition | 10 | 6/0/4 | +0.049 | [-0.025, +0.125] | 0.754 |
| population | generations | 10 | 4/0/6 | +0.010 | [-0.060, +0.086] | 0.754 |
| population | oral | 10 | 4/0/6 | -0.004 | [-0.069, +0.065] | 0.754 |
| population | oral_fixed | 10 | 5/0/5 | +0.018 | [-0.056, +0.088] | 1.000 |
| population | bone | 10 | 7/0/3 | +0.049 | [+0.001, +0.104] | 0.344 |
| population | bone_edition | 10 | 7/0/3 | +0.048 | [-0.004, +0.101] | 0.344 |
| generations | oral | 10 | 5/0/5 | -0.013 | [-0.117, +0.091] | 1.000 |
| generations | oral_fixed | 10 | 5/0/5 | +0.008 | [-0.081, +0.108] | 1.000 |
| generations | bone | 10 | 6/1/3 | +0.039 | [-0.023, +0.109] | 0.508 |
| generations | bone_edition | 10 | 6/0/4 | +0.038 | [-0.037, +0.113] | 0.754 |
| oral | oral_fixed | 10 | 7/0/3 | +0.022 | [-0.062, +0.107] | 0.344 |
| oral | bone | 10 | 6/0/4 | +0.052 | [-0.036, +0.132] | 0.754 |
| oral | bone_edition | 10 | 7/0/3 | +0.052 | [-0.035, +0.131] | 0.344 |
| oral_fixed | bone | 10 | 5/0/5 | +0.030 | [-0.045, +0.106] | 1.000 |
| oral_fixed | bone_edition | 10 | 7/0/3 | +0.030 | [-0.065, +0.115] | 0.344 |
| bone | bone_edition | 10 | 5/0/5 | -0.000 | [-0.074, +0.072] | 1.000 |

### topsim

| A | B | n | wins/ties/losses | mean diff | 95% CI | p |
|---|---|---|---|---|---|---|
| pair | population | 10 | 3/0/7 | -0.031 | [-0.060, -0.002] | 0.344 |
| pair | generations | 10 | 3/0/7 | -0.023 | [-0.049, +0.009] | 0.344 |
| pair | oral | 10 | 3/0/7 | -0.040 | [-0.077, +0.005] | 0.344 |
| pair | oral_fixed | 10 | 0/0/10 | -0.076 | [-0.110, -0.046] | 0.002 |
| pair | bone | 10 | 4/0/6 | -0.009 | [-0.046, +0.024] | 0.754 |
| pair | bone_edition | 10 | 1/0/9 | -0.042 | [-0.067, -0.018] | 0.021 |
| population | generations | 10 | 5/0/5 | +0.008 | [-0.033, +0.049] | 1.000 |
| population | oral | 10 | 3/0/7 | -0.009 | [-0.054, +0.038] | 0.344 |
| population | oral_fixed | 10 | 3/0/7 | -0.046 | [-0.082, -0.009] | 0.344 |
| population | bone | 10 | 5/0/5 | +0.022 | [-0.020, +0.069] | 1.000 |
| population | bone_edition | 10 | 5/0/5 | -0.012 | [-0.053, +0.027] | 1.000 |
| generations | oral | 10 | 3/0/7 | -0.017 | [-0.039, +0.009] | 0.344 |
| generations | oral_fixed | 10 | 2/0/8 | -0.054 | [-0.091, -0.015] | 0.109 |
| generations | bone | 10 | 7/0/3 | +0.014 | [-0.012, +0.039] | 0.344 |
| generations | bone_edition | 10 | 3/0/7 | -0.020 | [-0.049, +0.012] | 0.344 |
| oral | oral_fixed | 10 | 3/0/7 | -0.037 | [-0.080, +0.010] | 0.344 |
| oral | bone | 10 | 7/0/3 | +0.031 | [-0.013, +0.068] | 0.344 |
| oral | bone_edition | 10 | 4/0/6 | -0.003 | [-0.044, +0.038] | 0.754 |
| oral_fixed | bone | 10 | 7/0/3 | +0.068 | [+0.014, +0.121] | 0.344 |
| oral_fixed | bone_edition | 10 | 9/0/1 | +0.034 | [+0.014, +0.056] | 0.021 |
| bone | bone_edition | 10 | 4/0/6 | -0.034 | [-0.074, +0.011] | 0.754 |

### n_unique_msgs

| A | B | n | wins/ties/losses | mean diff | 95% CI | p |
|---|---|---|---|---|---|---|
| pair | population | 10 | 7/0/3 | +3.700 | [-1.300, +8.600] | 0.344 |
| pair | generations | 10 | 8/0/2 | +7.300 | [+2.200, +14.200] | 0.109 |
| pair | oral | 10 | 10/0/0 | +29.100 | [+24.000, +33.800] | 0.002 |
| pair | oral_fixed | 10 | 9/0/1 | +20.400 | [+14.300, +25.100] | 0.021 |
| pair | bone | 10 | 10/0/0 | +29.600 | [+25.300, +33.800] | 0.002 |
| pair | bone_edition | 10 | 10/0/0 | +30.300 | [+25.600, +34.900] | 0.002 |
| population | generations | 10 | 6/0/4 | +3.600 | [-2.000, +9.600] | 0.754 |
| population | oral | 10 | 10/0/0 | +25.400 | [+20.200, +31.300] | 0.002 |
| population | oral_fixed | 10 | 10/0/0 | +16.700 | [+11.600, +22.400] | 0.002 |
| population | bone | 10 | 10/0/0 | +25.900 | [+21.100, +31.000] | 0.002 |
| population | bone_edition | 10 | 10/0/0 | +26.600 | [+22.300, +31.500] | 0.002 |
| generations | oral | 10 | 10/0/0 | +21.800 | [+15.800, +27.400] | 0.002 |
| generations | oral_fixed | 10 | 8/0/2 | +13.100 | [+6.398, +18.700] | 0.109 |
| generations | bone | 10 | 9/0/1 | +22.300 | [+15.400, +28.700] | 0.021 |
| generations | bone_edition | 10 | 10/0/0 | +23.000 | [+17.200, +27.400] | 0.002 |
| oral | oral_fixed | 10 | 0/0/10 | -8.700 | [-11.500, -6.100] | 0.002 |
| oral | bone | 10 | 6/0/4 | +0.500 | [-2.300, +3.400] | 0.754 |
| oral | bone_edition | 10 | 6/0/4 | +1.200 | [-2.100, +4.500] | 0.754 |
| oral_fixed | bone | 10 | 10/0/0 | +9.200 | [+6.100, +12.600] | 0.002 |
| oral_fixed | bone_edition | 10 | 10/0/0 | +9.900 | [+7.100, +12.900] | 0.002 |
| bone | bone_edition | 10 | 6/1/3 | +0.700 | [-3.900, +4.700] | 0.508 |

## Per-generation (end of each generation; mean ± sd over seeds)

### generations
| gen | test_acc | topsim | posdis | n_unique_msgs |
|---|---|---|---|---|
| 0 | 0.577 ± 0.056 | 0.336 ± 0.081 | 0.139 ± 0.067 | 37.900 ± 9.597 |
| 1 | 0.579 ± 0.075 | 0.334 ± 0.026 | 0.128 ± 0.078 | 40.600 ± 8.003 |
| 2 | 0.604 ± 0.107 | 0.328 ± 0.035 | 0.132 ± 0.074 | 39.100 ± 5.486 |
| 3 | 0.576 ± 0.130 | 0.318 ± 0.045 | 0.110 ± 0.088 | 41.300 ± 8.220 |
| 4 | 0.588 ± 0.096 | 0.328 ± 0.051 | 0.134 ± 0.059 | 36.900 ± 8.346 |
| 5 | 0.605 ± 0.131 | 0.327 ± 0.037 | 0.102 ± 0.054 | 44.600 ± 9.348 |

topsim slope per generation: -0.0020 (positive in 7/10 seeds, sign-test p=0.344)

### oral
| gen | test_acc | topsim | posdis | n_unique_msgs |
|---|---|---|---|---|
| 0 | 0.577 ± 0.056 | 0.336 ± 0.081 | 0.139 ± 0.067 | 37.900 ± 9.597 |
| 1 | 0.586 ± 0.105 | 0.332 ± 0.075 | 0.150 ± 0.080 | 33.000 ± 11.055 |
| 2 | 0.584 ± 0.160 | 0.346 ± 0.074 | 0.152 ± 0.069 | 28.000 ± 6.307 |
| 3 | 0.603 ± 0.075 | 0.358 ± 0.062 | 0.156 ± 0.086 | 27.000 ± 7.364 |
| 4 | 0.589 ± 0.059 | 0.346 ± 0.050 | 0.133 ± 0.094 | 25.100 ± 8.359 |
| 5 | 0.619 ± 0.110 | 0.345 ± 0.054 | 0.155 ± 0.077 | 22.800 ± 5.514 |

topsim slope per generation: +0.0027 (positive in 7/10 seeds, sign-test p=0.344)

### oral_fixed
| gen | test_acc | topsim | posdis | n_unique_msgs |
|---|---|---|---|---|
| 0 | 0.577 ± 0.056 | 0.336 ± 0.081 | 0.139 ± 0.067 | 37.900 ± 9.597 |
| 1 | 0.535 ± 0.085 | 0.366 ± 0.069 | 0.167 ± 0.071 | 30.700 ± 7.379 |
| 2 | 0.553 ± 0.101 | 0.368 ± 0.069 | 0.162 ± 0.080 | 31.300 ± 7.088 |
| 3 | 0.553 ± 0.110 | 0.377 ± 0.066 | 0.145 ± 0.088 | 29.400 ± 5.892 |
| 4 | 0.589 ± 0.100 | 0.384 ± 0.057 | 0.156 ± 0.086 | 28.700 ± 5.272 |
| 5 | 0.597 ± 0.103 | 0.381 ± 0.059 | 0.172 ± 0.089 | 31.500 ± 5.462 |

topsim slope per generation: +0.0083 (positive in 8/10 seeds, sign-test p=0.109)

### bone
| gen | test_acc | topsim | posdis | n_unique_msgs |
|---|---|---|---|---|
| 0 | 0.577 ± 0.056 | 0.336 ± 0.081 | 0.139 ± 0.067 | 37.900 ± 9.597 |
| 1 | 0.538 ± 0.091 | 0.310 ± 0.039 | 0.152 ± 0.136 | 22.300 ± 6.075 |
| 2 | 0.556 ± 0.070 | 0.299 ± 0.048 | 0.133 ± 0.085 | 22.500 ± 5.798 |
| 3 | 0.542 ± 0.073 | 0.318 ± 0.036 | 0.154 ± 0.131 | 23.900 ± 5.934 |
| 4 | 0.536 ± 0.054 | 0.305 ± 0.048 | 0.137 ± 0.079 | 22.600 ± 5.147 |
| 5 | 0.566 ± 0.083 | 0.314 ± 0.049 | 0.141 ± 0.099 | 22.300 ± 4.448 |

topsim slope per generation: -0.0030 (positive in 6/10 seeds, sign-test p=0.754)

### bone_edition
| gen | test_acc | topsim | posdis | n_unique_msgs |
|---|---|---|---|---|
| 0 | 0.577 ± 0.056 | 0.336 ± 0.081 | 0.139 ± 0.067 | 37.900 ± 9.597 |
| 1 | 0.557 ± 0.133 | 0.331 ± 0.056 | 0.171 ± 0.095 | 28.200 ± 9.601 |
| 2 | 0.589 ± 0.102 | 0.365 ± 0.058 | 0.187 ± 0.123 | 28.100 ± 7.047 |
| 3 | 0.543 ± 0.130 | 0.352 ± 0.059 | 0.171 ± 0.056 | 25.700 ± 5.716 |
| 4 | 0.583 ± 0.096 | 0.364 ± 0.054 | 0.186 ± 0.084 | 24.000 ± 4.216 |
| 5 | 0.567 ± 0.095 | 0.347 ± 0.046 | 0.146 ± 0.098 | 21.600 ± 5.481 |

topsim slope per generation: +0.0041 (positive in 6/10 seeds, sign-test p=0.754)

## Steps to train_acc ≥ 0.9 in the last generation

- pair: median 875 steps (reached in 10/10 seeds)
- population: median 3250 steps (reached in 10/10 seeds)
- generations: median 750 steps (reached in 10/10 seeds)
- oral: median 375 steps (reached in 10/10 seeds)
- oral_fixed: median 250 steps (reached in 10/10 seeds)
- bone: median 750 steps (reached in 9/10 seeds)
- bone_edition: median 500 steps (reached in 9/10 seeds)