# Confirmation on seeds 10–29 (n=20) — `results_v3_confirm`

| id | test | metric | n | wins/losses | mean diff | 95% CI | p | verdict |
|---|---|---|---|---|---|---|---|---|
| C1 | hard+rewrite > random+rewrite | topsim | 20 | 14/6 | +0.027 | [-0.004, +0.054] | 0.115 | INCONCLUSIVE |
| C2 | hard+rewrite > random+rewrite | test_acc | 20 | 12/8 | +0.019 | [-0.035, +0.068] | 0.503 | INCONCLUSIVE |
| C3 | hard+rewrite > success+rewrite (bone_edition) | test_acc | 20 | 9/11 | +0.010 | [-0.048, +0.071] | 0.824 | INCONCLUSIVE |
| C4 | bone_edition > bone (rewrite > accumulate, success slots) | topsim | 20 | 17/3 | +0.071 | [+0.045, +0.096] | 0.003 | SUPPORTED |
| C5 | oral_fixed vs bone_edition | topsim | 20 | 9/11 | -0.020 | [-0.047, +0.005] | 0.824 | TWO-SIDED: no difference (CI) |
| C6 random+accumulate | record cell vs generations (no transmission) | topsim | 20 | 2/18 | -0.049 | [-0.068, -0.031] | 0.000 | TWO-SIDED: A<B (CI) |
| C6 random+rewrite | record cell vs generations (no transmission) | topsim | 20 | 12/8 | +0.016 | [-0.011, +0.045] | 0.503 | TWO-SIDED: no difference (CI) |
| C6 success+accumulate | record cell vs generations (no transmission) | topsim | 20 | 6/14 | -0.035 | [-0.063, -0.010] | 0.115 | TWO-SIDED: A<B (CI) |
| C6 success+rewrite | record cell vs generations (no transmission) | topsim | 20 | 16/4 | +0.036 | [+0.010, +0.060] | 0.012 | TWO-SIDED: A>B (CI) |
| C6 hard+accumulate | record cell vs generations (no transmission) | topsim | 20 | 15/5 | +0.035 | [+0.007, +0.060] | 0.041 | TWO-SIDED: A>B (CI) |
| C6 hard+rewrite | record cell vs generations (no transmission) | topsim | 20 | 15/5 | +0.043 | [+0.015, +0.069] | 0.041 | TWO-SIDED: A>B (CI) |

| cell | topsim | test_acc | n_unique_msgs | intelligibility | train_acc |
|---|---|---|---|---|---|
| `generations` | 0.332 ± 0.044 | 0.611 ± 0.112 | 45.400 ± 7.708 | 0.566 ± 0.105 | 0.977 ± 0.019 |
| `pair` | 0.279 ± 0.031 | 0.537 ± 0.079 | 51.350 ± 5.489 | 0.680 ± 0.054 | 0.993 ± 0.008 |
| `sel-hard_slots-dynamic_fresh-accumulate_cap-19_noise-0.0_rd-sender` | 0.367 ± 0.034 | 0.603 ± 0.086 | 15.950 ± 7.236 | 0.236 ± 0.104 | 0.900 ± 0.053 |
| `sel-hard_slots-dynamic_fresh-rewrite_cap-19_noise-0.0_rd-sender` | 0.375 ± 0.046 | 0.606 ± 0.088 | 17.100 ± 4.291 | 0.258 ± 0.064 | 0.912 ± 0.039 |
| `sel-random_slots-fixed_fresh-accumulate_cap-19_noise-0.0_rd-sender` | 0.283 ± 0.029 | 0.569 ± 0.088 | 26.750 ± 4.204 | 0.395 ± 0.061 | 0.952 ± 0.018 |
| `sel-random_slots-fixed_fresh-rewrite_cap-19_noise-0.0_rd-sender` | 0.348 ± 0.050 | 0.587 ± 0.073 | 29.050 ± 8.185 | 0.427 ± 0.110 | 0.961 ± 0.026 |
| `sel-random_slots-redraw_fresh-accumulate_cap-19_noise-0.0_rd-sender` | 0.327 ± 0.049 | 0.646 ± 0.072 | 21.200 ± 4.980 | 0.322 ± 0.074 | 0.937 ± 0.023 |
| `sel-random_slots-redraw_fresh-rewrite_cap-19_noise-0.0_rd-sender` | 0.362 ± 0.054 | 0.607 ± 0.095 | 23.400 ± 3.393 | 0.355 ± 0.049 | 0.940 ± 0.014 |
| `sel-success_slots-dynamic_fresh-accumulate_cap-19_noise-0.0_rd-sender` | 0.297 ± 0.036 | 0.548 ± 0.085 | 23.400 ± 5.623 | 0.345 ± 0.079 | 0.933 ± 0.024 |
| `sel-success_slots-dynamic_fresh-rewrite_cap-19_noise-0.0_rd-sender` | 0.368 ± 0.039 | 0.596 ± 0.098 | 19.900 ± 6.198 | 0.298 ± 0.085 | 0.921 ± 0.040 |
