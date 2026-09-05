# v3 factorial sweep — summary

Runs: 770. Worlds: ['small']. Seeds: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
Pre-registered hypotheses and the decision rule are in `results_v3/PREREG.md`.

# World: small

## Pre-registered hypotheses

| id | hypothesis | metric | n seeds | wins/losses | mean diff | 95% CI | p | verdict |
|---|---|---|---|---|---|---|---|---|
| H1 | Selection: random slots beat success-selected slots (the v2 surprise is about WHAT gets recorded) | topsim | 10 | 3/7 | -0.007 | [-0.013, -0.002] | 0.344 | INCONCLUSIVE |
| H2 | Capacity: a smaller record yields a more compositional language (bottleneck = structure) | topsim | 10 | 2/8 | -0.016 | [-0.024, -0.008] | 0.109 | SUPPORTED |
| H3 | Freshness: rewriting from the final language beats accumulating carved forms | topsim | 10 | 10/0 | +0.039 | [+0.033, +0.045] | 0.002 | SUPPORTED |
| H4 | Erosion repairs an accumulating record: noise raises topsim when forms accumulate | topsim | 10 | 1/9 | -0.039 | [-0.051, -0.025] | 0.021 | REFUTED |
| H5 | A record both agents read changes held-out accuracy (direction unknown) | test_acc | 10 | 4/6 | -0.004 | [-0.022, +0.014] | 0.754 | TWO-SIDED: no difference (CI) |
| H6 | Every bottlenecked record compresses the lexicon vs no transmission (86% of cell×seed below control) | n_unique_msgs | 10 | 0/10 | -16.181 | [-18.223, -14.158] | 0.002 | SUPPORTED |
| H7 | v2 replication: oral_fixed beats bone_edition | topsim | 10 | 5/5 | -0.014 | [-0.045, +0.016] | 1.000 | INCONCLUSIVE |
| H8 | Recording the HARD objects helps held-out accuracy more than random objects | test_acc | 10 | 1/9 | -0.044 | [-0.065, -0.019] | 0.021 | REFUTED |
| H9 | Rewritten records are more mutually intelligible than accumulated ones | intelligibility | 10 | 9/1 | +0.032 | [+0.018, +0.045] | 0.021 | SUPPORTED |

## Main effects (paired by seed, averaged over all other factors; A − B)

### topsim

| factor | A | B | n | wins/losses | mean diff | 95% CI | p | |
|---|---|---|---|---|---|---|---|---|
| select | hard | random | 10 | 7/3 | +0.021 | [+0.011, +0.031] | 0.344 | TWO-SIDED: A>B (CI) |
| select | hard | success | 10 | 8/2 | +0.014 | [+0.003, +0.025] | 0.109 | TWO-SIDED: A>B (CI) |
| select | random | success | 10 | 3/7 | -0.007 | [-0.013, -0.002] | 0.344 | TWO-SIDED: A<B (CI) |
| fresh | accumulate | rewrite | 10 | 0/10 | -0.039 | [-0.045, -0.033] | 0.002 | TWO-SIDED: A<B (CI) |
| capacity | 8 | 19 | 10 | 7/3 | +0.004 | [-0.007, +0.016] | 0.344 | TWO-SIDED: no difference (CI) |
| capacity | 8 | 40 | 10 | 8/2 | +0.039 | [+0.020, +0.057] | 0.109 | TWO-SIDED: A>B (CI) |
| capacity | 19 | 40 | 10 | 9/1 | +0.034 | [+0.019, +0.047] | 0.021 | TWO-SIDED: A>B (CI) |
| noise | 0.0 | 0.2 | 10 | 10/0 | +0.038 | [+0.027, +0.048] | 0.002 | TWO-SIDED: A>B (CI) |
| reader | both | sender | 10 | 0/10 | -0.013 | [-0.016, -0.010] | 0.002 | TWO-SIDED: A<B (CI) |

### test_acc

| factor | A | B | n | wins/losses | mean diff | 95% CI | p | |
|---|---|---|---|---|---|---|---|---|
| select | hard | random | 10 | 1/9 | -0.044 | [-0.065, -0.019] | 0.021 | TWO-SIDED: A<B (CI) |
| select | hard | success | 10 | 3/7 | -0.017 | [-0.038, +0.003] | 0.344 | TWO-SIDED: no difference (CI) |
| select | random | success | 10 | 8/2 | +0.027 | [+0.011, +0.043] | 0.109 | TWO-SIDED: A>B (CI) |
| fresh | accumulate | rewrite | 10 | 2/8 | -0.007 | [-0.020, +0.006] | 0.109 | TWO-SIDED: no difference (CI) |
| capacity | 8 | 19 | 10 | 1/9 | -0.061 | [-0.083, -0.037] | 0.021 | TWO-SIDED: A<B (CI) |
| capacity | 8 | 40 | 10 | 1/9 | -0.054 | [-0.088, -0.022] | 0.021 | TWO-SIDED: A<B (CI) |
| capacity | 19 | 40 | 10 | 5/5 | +0.007 | [-0.016, +0.033] | 1.000 | TWO-SIDED: no difference (CI) |
| noise | 0.0 | 0.2 | 10 | 4/6 | -0.006 | [-0.025, +0.012] | 0.754 | TWO-SIDED: no difference (CI) |
| reader | both | sender | 10 | 4/6 | -0.004 | [-0.022, +0.014] | 0.754 | TWO-SIDED: no difference (CI) |

### n_unique_msgs

| factor | A | B | n | wins/losses | mean diff | 95% CI | p | |
|---|---|---|---|---|---|---|---|---|
| select | hard | random | 10 | 0/10 | -6.233 | [-7.629, -5.062] | 0.002 | TWO-SIDED: A<B (CI) |
| select | hard | success | 10 | 1/9 | -2.542 | [-3.367, -1.596] | 0.021 | TWO-SIDED: A<B (CI) |
| select | random | success | 10 | 10/0 | +3.692 | [+2.567, +4.804] | 0.002 | TWO-SIDED: A>B (CI) |
| fresh | accumulate | rewrite | 10 | 1/9 | -2.292 | [-3.261, -1.200] | 0.021 | TWO-SIDED: A<B (CI) |
| capacity | 8 | 19 | 10 | 0/10 | -11.858 | [-13.179, -10.392] | 0.002 | TWO-SIDED: A<B (CI) |
| capacity | 8 | 40 | 10 | 0/10 | -26.867 | [-28.525, -24.904] | 0.002 | TWO-SIDED: A<B (CI) |
| capacity | 19 | 40 | 10 | 0/10 | -15.008 | [-16.254, -13.854] | 0.002 | TWO-SIDED: A<B (CI) |
| noise | 0.0 | 0.2 | 10 | 1/9 | -3.075 | [-4.428, -1.803] | 0.021 | TWO-SIDED: A<B (CI) |
| reader | both | sender | 10 | 5/5 | -0.003 | [-0.458, +0.456] | 1.000 | TWO-SIDED: no difference (CI) |

### intelligibility

| factor | A | B | n | wins/losses | mean diff | 95% CI | p | |
|---|---|---|---|---|---|---|---|---|
| select | hard | random | 10 | 0/10 | -0.093 | [-0.112, -0.078] | 0.002 | TWO-SIDED: A<B (CI) |
| select | hard | success | 10 | 0/10 | -0.039 | [-0.049, -0.028] | 0.002 | TWO-SIDED: A<B (CI) |
| select | random | success | 10 | 10/0 | +0.055 | [+0.040, +0.069] | 0.002 | TWO-SIDED: A>B (CI) |
| fresh | accumulate | rewrite | 10 | 1/9 | -0.032 | [-0.045, -0.018] | 0.021 | TWO-SIDED: A<B (CI) |
| capacity | 8 | 19 | 10 | 0/10 | -0.174 | [-0.192, -0.153] | 0.002 | TWO-SIDED: A<B (CI) |
| capacity | 8 | 40 | 10 | 0/10 | -0.385 | [-0.406, -0.359] | 0.002 | TWO-SIDED: A<B (CI) |
| capacity | 19 | 40 | 10 | 0/10 | -0.211 | [-0.230, -0.196] | 0.002 | TWO-SIDED: A<B (CI) |
| noise | 0.0 | 0.2 | 10 | 1/9 | -0.044 | [-0.064, -0.025] | 0.021 | TWO-SIDED: A<B (CI) |
| reader | both | sender | 10 | 6/4 | +0.003 | [-0.004, +0.010] | 0.754 | TWO-SIDED: no difference (CI) |

## Interactions (cell means of topsim over seeds and remaining factors)

### select × fresh

| select \ fresh | accumulate | rewrite |
|---|---|---|
| hard | 0.317 | 0.327 |
| random | 0.276 | 0.327 |
| success | 0.281 | 0.337 |

### select × capacity

| select \ capacity | 8 | 19 | 40 |
|---|---|---|---|
| hard | 0.319 | 0.334 | 0.315 |
| random | 0.334 | 0.310 | 0.261 |
| success | 0.323 | 0.319 | 0.284 |

### fresh × noise

| fresh \ noise | 0.0 | 0.2 |
|---|---|---|
| accumulate | 0.311 | 0.272 |
| rewrite | 0.349 | 0.312 |

### select × reader

| select \ reader | both | sender |
|---|---|---|
| hard | 0.319 | 0.326 |
| random | 0.295 | 0.309 |
| success | 0.300 | 0.318 |

### fresh × reader

| fresh \ reader | both | sender |
|---|---|---|
| accumulate | 0.285 | 0.298 |
| rewrite | 0.324 | 0.337 |

### capacity × noise

| capacity \ noise | 0.0 | 0.2 |
|---|---|---|
| 8 | 0.336 | 0.315 |
| 19 | 0.338 | 0.304 |
| 40 | 0.315 | 0.258 |

## The v2 named conditions, as cells

| condition | topsim | test_acc | n_unique_msgs | intelligibility | train_acc |
|---|---|---|---|---|---|
| pair | 0.296 ± 0.035 | 0.554 ± 0.086 | 54.900 ± 4.771 | 0.714 ± 0.048 | 0.994 ± 0.012 |
| population | 0.322 ± 0.034 | 0.578 ± 0.080 | 48.200 ± 8.351 | 0.613 ± 0.106 | 0.982 ± 0.017 |
| generations | 0.356 ± 0.032 | 0.626 ± 0.140 | 44.100 ± 3.784 | 0.577 ± 0.053 | 0.981 ± 0.008 |
| oral | 0.376 ± 0.044 | 0.610 ± 0.087 | 28.900 ± 7.838 | 0.420 ± 0.106 | 0.959 ± 0.020 |
| oral_fixed | 0.362 ± 0.038 | 0.596 ± 0.107 | 34.500 ± 5.855 | 0.505 ± 0.077 | 0.971 ± 0.013 |
| bone | 0.292 ± 0.041 | 0.538 ± 0.071 | 27.300 ± 5.964 | 0.397 ± 0.083 | 0.944 ± 0.022 |
| bone_edition | 0.376 ± 0.057 | 0.579 ± 0.137 | 21.500 ± 5.442 | 0.322 ± 0.074 | 0.929 ± 0.043 |

| A | B | metric | n | wins/losses | mean diff | 95% CI | p | |
|---|---|---|---|---|---|---|---|---|
| oral_fixed | bone_edition | topsim | 10 | 5/5 | -0.014 | [-0.045, +0.016] | 1.000 | TWO-SIDED: no difference (CI) |
| bone | bone_edition | topsim | 10 | 0/10 | -0.085 | [-0.132, -0.046] | 0.002 | TWO-SIDED: A<B (CI) |
| oral_fixed | pair | topsim | 10 | 9/1 | +0.067 | [+0.047, +0.084] | 0.021 | TWO-SIDED: A>B (CI) |
| oral | oral_fixed | topsim | 10 | 6/4 | +0.013 | [-0.013, +0.042] | 0.754 | TWO-SIDED: no difference (CI) |
| oral_fixed | bone | topsim | 10 | 10/0 | +0.071 | [+0.044, +0.099] | 0.002 | TWO-SIDED: A>B (CI) |
| oral | pair | test_acc | 10 | 8/2 | +0.057 | [+0.012, +0.096] | 0.109 | TWO-SIDED: A>B (CI) |
| population | pair | topsim | 10 | 8/2 | +0.027 | [-0.006, +0.059] | 0.109 | TWO-SIDED: no difference (CI) |

## All cells ranked by topsim (mean ± sd over seeds)

| cell | n | topsim | test_acc | n_unique | intelligibility |
|---|---|---|---|---|---|
| `sel-hard_slots-dynamic_fresh-rewrite_cap-19_noise-0.0_rd-sender` | 10 | 0.401 ± 0.055 | 0.684 ± 0.103 | 20.000 ± 5.099 | 0.300 ± 0.072 |
| `sel-success_slots-dynamic_fresh-rewrite_cap-40_noise-0.0_rd-sender` | 10 | 0.385 ± 0.071 | 0.573 ± 0.100 | 42.500 ± 8.410 | 0.609 ± 0.107 |
| `sel-success_slots-dynamic_fresh-rewrite_cap-19_noise-0.0_rd-sender` | 10 | 0.376 ± 0.057 | 0.579 ± 0.137 | 21.500 ± 5.442 | 0.322 ± 0.074 |
| `sel-random_slots-redraw_fresh-rewrite_cap-19_noise-0.0_rd-sender` | 10 | 0.376 ± 0.044 | 0.610 ± 0.087 | 28.900 ± 7.838 | 0.420 ± 0.106 |
| `sel-success_slots-dynamic_fresh-rewrite_cap-19_noise-0.0_rd-both` | 10 | 0.364 ± 0.032 | 0.619 ± 0.080 | 26.600 ± 7.734 | 0.405 ± 0.110 |
| `sel-random_slots-fixed_fresh-rewrite_cap-19_noise-0.0_rd-sender` | 10 | 0.362 ± 0.038 | 0.596 ± 0.107 | 34.500 ± 5.855 | 0.505 ± 0.077 |
| `sel-random_slots-fixed_fresh-rewrite_cap-19_noise-0.0_rd-both` | 10 | 0.362 ± 0.052 | 0.589 ± 0.085 | 32.100 ± 4.725 | 0.477 ± 0.068 |
| `sel-hard_slots-dynamic_fresh-accumulate_cap-40_noise-0.0_rd-sender` | 10 | 0.359 ± 0.054 | 0.599 ± 0.126 | 40.400 ± 7.589 | 0.584 ± 0.100 |
| `sel-random_slots-fixed_fresh-rewrite_cap-8_noise-0.2_rd-sender` | 10 | 0.359 ± 0.040 | 0.621 ± 0.070 | 18.500 ± 6.096 | 0.281 ± 0.093 |
| `sel-hard_slots-dynamic_fresh-accumulate_cap-19_noise-0.0_rd-sender` | 10 | 0.358 ± 0.036 | 0.588 ± 0.103 | 20.600 ± 7.589 | 0.305 ± 0.110 |
| `generations` | 10 | 0.356 ± 0.032 | 0.626 ± 0.140 | 44.100 ± 3.784 | 0.577 ± 0.053 |
| `sel-hard_slots-dynamic_fresh-rewrite_cap-40_noise-0.0_rd-sender` | 10 | 0.355 ± 0.063 | 0.585 ± 0.087 | 43.100 ± 6.385 | 0.623 ± 0.078 |
| `sel-random_slots-redraw_fresh-accumulate_cap-19_noise-0.0_rd-sender` | 10 | 0.348 ± 0.037 | 0.551 ± 0.093 | 26.800 ± 3.259 | 0.403 ± 0.045 |
| `sel-success_slots-dynamic_fresh-rewrite_cap-19_noise-0.2_rd-sender` | 10 | 0.347 ± 0.040 | 0.642 ± 0.085 | 28.900 ± 4.886 | 0.423 ± 0.060 |
| `sel-hard_slots-dynamic_fresh-accumulate_cap-8_noise-0.0_rd-sender` | 10 | 0.346 ± 0.060 | 0.437 ± 0.096 | 8.000 ± 5.055 | 0.117 ± 0.070 |
| `sel-hard_slots-dynamic_fresh-accumulate_cap-8_noise-0.0_rd-both` | 10 | 0.344 ± 0.056 | 0.442 ± 0.126 | 8.000 ± 4.761 | 0.119 ± 0.063 |
| `sel-random_slots-fixed_fresh-accumulate_cap-8_noise-0.0_rd-sender` | 10 | 0.343 ± 0.052 | 0.576 ± 0.106 | 19.000 ± 7.102 | 0.281 ± 0.092 |
| `sel-hard_slots-dynamic_fresh-rewrite_cap-40_noise-0.0_rd-both` | 10 | 0.342 ± 0.065 | 0.596 ± 0.101 | 42.200 ± 5.203 | 0.617 ± 0.077 |
| `sel-random_slots-fixed_fresh-rewrite_cap-8_noise-0.0_rd-sender` | 10 | 0.338 ± 0.033 | 0.593 ± 0.068 | 17.400 ± 3.950 | 0.259 ± 0.055 |
| `sel-success_slots-dynamic_fresh-rewrite_cap-8_noise-0.0_rd-both` | 10 | 0.338 ± 0.039 | 0.487 ± 0.091 | 12.200 ± 5.453 | 0.184 ± 0.078 |
| `sel-random_slots-fixed_fresh-accumulate_cap-8_noise-0.0_rd-both` | 10 | 0.337 ± 0.046 | 0.579 ± 0.112 | 20.700 ± 6.395 | 0.308 ± 0.090 |
| `sel-success_slots-dynamic_fresh-accumulate_cap-8_noise-0.0_rd-sender` | 10 | 0.336 ± 0.054 | 0.596 ± 0.070 | 19.000 ± 6.429 | 0.275 ± 0.086 |
| `sel-random_slots-fixed_fresh-rewrite_cap-40_noise-0.0_rd-sender` | 10 | 0.336 ± 0.031 | 0.579 ± 0.081 | 44.800 ± 6.697 | 0.650 ± 0.091 |
| `sel-hard_slots-dynamic_fresh-rewrite_cap-8_noise-0.0_rd-sender` | 10 | 0.335 ± 0.073 | 0.464 ± 0.178 | 9.600 ± 3.978 | 0.142 ± 0.057 |
| `sel-hard_slots-dynamic_fresh-rewrite_cap-8_noise-0.0_rd-both` | 10 | 0.335 ± 0.045 | 0.460 ± 0.103 | 7.200 ± 3.259 | 0.106 ± 0.042 |
| `sel-success_slots-dynamic_fresh-rewrite_cap-19_noise-0.2_rd-both` | 10 | 0.335 ± 0.053 | 0.559 ± 0.071 | 30.400 ± 2.797 | 0.445 ± 0.028 |
| `sel-success_slots-dynamic_fresh-rewrite_cap-40_noise-0.0_rd-both` | 10 | 0.335 ± 0.054 | 0.588 ± 0.109 | 42.900 ± 4.358 | 0.634 ± 0.064 |
| `sel-hard_slots-dynamic_fresh-accumulate_cap-40_noise-0.0_rd-both` | 10 | 0.332 ± 0.042 | 0.582 ± 0.116 | 38.700 ± 5.376 | 0.559 ± 0.074 |
| `sel-success_slots-dynamic_fresh-rewrite_cap-8_noise-0.2_rd-both` | 10 | 0.331 ± 0.033 | 0.507 ± 0.071 | 16.900 ± 5.425 | 0.255 ± 0.077 |
| `sel-random_slots-fixed_fresh-rewrite_cap-8_noise-0.0_rd-both` | 10 | 0.330 ± 0.027 | 0.581 ± 0.090 | 20.000 ± 4.000 | 0.306 ± 0.057 |
| `sel-hard_slots-dynamic_fresh-rewrite_cap-19_noise-0.0_rd-both` | 10 | 0.329 ± 0.042 | 0.565 ± 0.124 | 16.500 ± 6.258 | 0.247 ± 0.095 |
| `sel-success_slots-dynamic_fresh-rewrite_cap-8_noise-0.0_rd-sender` | 10 | 0.329 ± 0.032 | 0.524 ± 0.082 | 13.000 ± 4.876 | 0.197 ± 0.073 |
| `sel-random_slots-fixed_fresh-accumulate_cap-8_noise-0.2_rd-sender` | 10 | 0.328 ± 0.040 | 0.618 ± 0.097 | 18.900 ± 7.460 | 0.273 ± 0.108 |
| `sel-random_slots-fixed_fresh-rewrite_cap-8_noise-0.2_rd-both` | 10 | 0.328 ± 0.055 | 0.563 ± 0.092 | 18.600 ± 4.671 | 0.281 ± 0.069 |
| `sel-hard_slots-dynamic_fresh-rewrite_cap-19_noise-0.2_rd-sender` | 10 | 0.328 ± 0.049 | 0.606 ± 0.118 | 25.600 ± 5.190 | 0.380 ± 0.075 |
| `sel-hard_slots-dynamic_fresh-accumulate_cap-19_noise-0.0_rd-both` | 10 | 0.327 ± 0.072 | 0.596 ± 0.089 | 15.700 ± 5.334 | 0.237 ± 0.079 |
| `sel-hard_slots-dynamic_fresh-rewrite_cap-8_noise-0.2_rd-both` | 10 | 0.326 ± 0.069 | 0.574 ± 0.110 | 13.900 ± 5.666 | 0.205 ± 0.082 |
| `sel-success_slots-dynamic_fresh-rewrite_cap-8_noise-0.2_rd-sender` | 10 | 0.325 ± 0.027 | 0.535 ± 0.080 | 12.900 ± 3.381 | 0.195 ± 0.049 |
| `sel-random_slots-fixed_fresh-rewrite_cap-19_noise-0.2_rd-sender` | 10 | 0.325 ± 0.045 | 0.567 ± 0.048 | 38.500 ± 6.884 | 0.552 ± 0.082 |
| `sel-random_slots-fixed_fresh-rewrite_cap-40_noise-0.0_rd-both` | 10 | 0.323 ± 0.037 | 0.570 ± 0.074 | 45.900 ± 4.358 | 0.656 ± 0.072 |
| `population` | 10 | 0.322 ± 0.034 | 0.578 ± 0.080 | 48.200 ± 8.351 | 0.613 ± 0.106 |
| `sel-hard_slots-dynamic_fresh-accumulate_cap-8_noise-0.2_rd-both` | 10 | 0.321 ± 0.047 | 0.496 ± 0.122 | 12.700 ± 6.750 | 0.191 ± 0.094 |
| `sel-success_slots-dynamic_fresh-accumulate_cap-8_noise-0.0_rd-both` | 10 | 0.319 ± 0.057 | 0.596 ± 0.096 | 17.400 ± 4.551 | 0.256 ± 0.062 |
| `sel-random_slots-fixed_fresh-rewrite_cap-19_noise-0.2_rd-both` | 10 | 0.319 ± 0.046 | 0.636 ± 0.100 | 37.100 ± 3.784 | 0.544 ± 0.064 |
| `sel-hard_slots-dynamic_fresh-accumulate_cap-19_noise-0.2_rd-sender` | 10 | 0.317 ± 0.054 | 0.592 ± 0.097 | 26.400 ± 6.979 | 0.388 ± 0.087 |
| `sel-hard_slots-dynamic_fresh-rewrite_cap-19_noise-0.2_rd-both` | 10 | 0.316 ± 0.031 | 0.588 ± 0.127 | 23.200 ± 7.021 | 0.350 ± 0.104 |
| `sel-random_slots-fixed_fresh-accumulate_cap-19_noise-0.0_rd-sender` | 10 | 0.313 ± 0.045 | 0.617 ± 0.088 | 27.700 ± 6.750 | 0.412 ± 0.097 |
| `sel-success_slots-dynamic_fresh-rewrite_cap-40_noise-0.2_rd-sender` | 10 | 0.308 ± 0.033 | 0.629 ± 0.073 | 44.700 ± 2.214 | 0.639 ± 0.025 |
| `sel-random_slots-fixed_fresh-accumulate_cap-8_noise-0.2_rd-both` | 10 | 0.306 ± 0.049 | 0.585 ± 0.079 | 18.700 ± 7.917 | 0.280 ± 0.110 |
| `sel-success_slots-dynamic_fresh-accumulate_cap-8_noise-0.2_rd-sender` | 10 | 0.303 ± 0.051 | 0.548 ± 0.079 | 14.300 ± 4.270 | 0.212 ± 0.063 |
| `sel-success_slots-dynamic_fresh-accumulate_cap-8_noise-0.2_rd-both` | 10 | 0.302 ± 0.047 | 0.551 ± 0.101 | 16.600 ± 2.875 | 0.250 ± 0.035 |
| `sel-hard_slots-dynamic_fresh-rewrite_cap-40_noise-0.2_rd-sender` | 10 | 0.299 ± 0.037 | 0.591 ± 0.093 | 45.700 ± 2.214 | 0.659 ± 0.034 |
| `pair` | 10 | 0.296 ± 0.035 | 0.554 ± 0.086 | 54.900 ± 4.771 | 0.714 ± 0.048 |
| `sel-random_slots-fixed_fresh-accumulate_cap-19_noise-0.0_rd-both` | 10 | 0.294 ± 0.037 | 0.589 ± 0.069 | 28.900 ± 4.095 | 0.427 ± 0.057 |
| `sel-hard_slots-dynamic_fresh-accumulate_cap-19_noise-0.2_rd-both` | 10 | 0.293 ± 0.068 | 0.607 ± 0.111 | 23.100 ± 6.540 | 0.342 ± 0.096 |
| `sel-success_slots-dynamic_fresh-accumulate_cap-19_noise-0.0_rd-sender` | 10 | 0.292 ± 0.041 | 0.538 ± 0.071 | 27.300 ± 5.964 | 0.397 ± 0.083 |
| `sel-success_slots-dynamic_fresh-accumulate_cap-19_noise-0.2_rd-sender` | 10 | 0.285 ± 0.031 | 0.560 ± 0.067 | 25.500 ± 5.442 | 0.378 ± 0.075 |
| `sel-hard_slots-dynamic_fresh-rewrite_cap-40_noise-0.2_rd-both` | 10 | 0.284 ± 0.038 | 0.588 ± 0.081 | 44.600 ± 5.211 | 0.648 ± 0.065 |
| `sel-hard_slots-dynamic_fresh-rewrite_cap-8_noise-0.2_rd-sender` | 10 | 0.279 ± 0.127 | 0.426 ± 0.223 | 12.700 ± 7.072 | 0.184 ± 0.100 |
| `sel-hard_slots-dynamic_fresh-accumulate_cap-40_noise-0.2_rd-both` | 10 | 0.278 ± 0.044 | 0.566 ± 0.063 | 45.100 ± 4.954 | 0.650 ± 0.063 |
| `sel-success_slots-dynamic_fresh-accumulate_cap-19_noise-0.2_rd-both` | 10 | 0.277 ± 0.051 | 0.573 ± 0.077 | 27.000 ± 3.916 | 0.400 ± 0.048 |
| `sel-success_slots-dynamic_fresh-accumulate_cap-19_noise-0.0_rd-both` | 10 | 0.277 ± 0.044 | 0.534 ± 0.102 | 25.900 ± 6.999 | 0.384 ± 0.092 |
| `sel-random_slots-fixed_fresh-rewrite_cap-40_noise-0.2_rd-sender` | 10 | 0.272 ± 0.028 | 0.596 ± 0.098 | 47.500 ± 2.461 | 0.692 ± 0.030 |
| `sel-success_slots-dynamic_fresh-accumulate_cap-40_noise-0.0_rd-sender` | 10 | 0.271 ± 0.048 | 0.560 ± 0.081 | 34.600 ± 5.502 | 0.506 ± 0.070 |
| `sel-hard_slots-dynamic_fresh-accumulate_cap-40_noise-0.2_rd-sender` | 10 | 0.269 ± 0.053 | 0.561 ± 0.104 | 42.800 ± 3.938 | 0.613 ± 0.055 |
| `sel-random_slots-fixed_fresh-accumulate_cap-40_noise-0.0_rd-sender` | 10 | 0.268 ± 0.046 | 0.600 ± 0.077 | 34.500 ± 4.378 | 0.512 ± 0.071 |
| `sel-random_slots-fixed_fresh-rewrite_cap-40_noise-0.2_rd-both` | 10 | 0.267 ± 0.049 | 0.618 ± 0.071 | 46.800 ± 4.158 | 0.678 ± 0.054 |
| `sel-success_slots-dynamic_fresh-rewrite_cap-40_noise-0.2_rd-both` | 10 | 0.266 ± 0.043 | 0.562 ± 0.081 | 47.900 ± 2.998 | 0.683 ± 0.031 |
| `sel-hard_slots-dynamic_fresh-accumulate_cap-8_noise-0.2_rd-sender` | 10 | 0.266 ± 0.103 | 0.394 ± 0.188 | 14.100 ± 7.880 | 0.209 ± 0.116 |
| `sel-random_slots-fixed_fresh-accumulate_cap-19_noise-0.2_rd-sender` | 10 | 0.256 ± 0.034 | 0.602 ± 0.128 | 31.900 ± 3.784 | 0.473 ± 0.056 |
| `sel-success_slots-dynamic_fresh-accumulate_cap-40_noise-0.2_rd-sender` | 10 | 0.254 ± 0.043 | 0.586 ± 0.078 | 37.900 ± 3.957 | 0.555 ± 0.039 |
| `sel-random_slots-fixed_fresh-accumulate_cap-19_noise-0.2_rd-both` | 10 | 0.246 ± 0.036 | 0.591 ± 0.087 | 30.000 ± 4.269 | 0.442 ± 0.056 |
| `sel-success_slots-dynamic_fresh-accumulate_cap-40_noise-0.0_rd-both` | 10 | 0.244 ± 0.037 | 0.573 ± 0.109 | 35.700 ± 5.034 | 0.527 ± 0.068 |
| `sel-random_slots-fixed_fresh-accumulate_cap-40_noise-0.0_rd-both` | 10 | 0.232 ± 0.049 | 0.568 ± 0.085 | 35.700 ± 2.908 | 0.519 ± 0.040 |
| `sel-success_slots-dynamic_fresh-accumulate_cap-40_noise-0.2_rd-both` | 10 | 0.207 ± 0.035 | 0.567 ± 0.089 | 39.300 ± 3.683 | 0.577 ± 0.051 |
| `sel-random_slots-fixed_fresh-accumulate_cap-40_noise-0.2_rd-sender` | 10 | 0.201 ± 0.036 | 0.609 ± 0.100 | 40.900 ± 5.131 | 0.597 ± 0.063 |
| `sel-random_slots-fixed_fresh-accumulate_cap-40_noise-0.2_rd-both` | 10 | 0.190 ± 0.032 | 0.597 ± 0.068 | 40.900 ± 3.446 | 0.613 ± 0.042 |

