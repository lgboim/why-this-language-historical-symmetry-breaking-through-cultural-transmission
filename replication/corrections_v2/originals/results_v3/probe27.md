# probe27 — systematic (Hamming-1) emancipation vs random emancipation vs control (30 seeds)

| metric | control | emancipate (random) | emancipate_h1 | h1 − control | | | | | | random − control | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| topsim_distinct @2000 | 0.290 | 0.165 | 0.261 | 30 | 5/25 | -0.028 | [-0.040, -0.017] | 0.000 | TWO-SIDED: A<B (CI) | | 30 | 0/30 | -0.125 | [-0.142, -0.107] | 0.000 | TWO-SIDED: A<B (CI) |
| topsim_distinct @250 | 0.282 | 0.136 | 0.251 | 30 | 3/27 | -0.031 | [-0.042, -0.020] | 0.000 | TWO-SIDED: A<B (CI) | | 30 | 0/30 | -0.146 | [-0.162, -0.128] | 0.000 | TWO-SIDED: A<B (CI) |
| CBM @2000 | 0.486 | 0.392 | 0.448 | 30 | 4/25 | -0.039 | [-0.050, -0.028] | 0.000 | TWO-SIDED: A<B (CI) | | 30 | 2/28 | -0.094 | [-0.111, -0.077] | 0.000 | TWO-SIDED: A<B (CI) |
| n_owners train @2000 | 37.300 | 46.800 | 46.767 | 30 | 29/0 | +9.467 | [+7.367, +11.767] | 0.000 | TWO-SIDED: A>B (CI) | | 30 | 30/0 | +9.500 | [+7.467, +11.700] | 0.000 | TWO-SIDED: A>B (CI) |
| test_acc @2000 | 0.585 | 0.370 | 0.492 | 30 | 5/25 | -0.092 | [-0.123, -0.062] | 0.000 | TWO-SIDED: A<B (CI) | | 30 | 1/29 | -0.215 | [-0.251, -0.177] | 0.000 | TWO-SIDED: A<B (CI) |
| train_acc @2000 | 0.979 | 0.998 | 0.998 | 30 | 25/1 | +0.019 | [+0.013, +0.026] | 0.000 | TWO-SIDED: A>B (CI) | | 30 | 26/0 | +0.019 | [+0.013, +0.026] | 0.000 | TWO-SIDED: A>B (CI) |
| held-out sharing a train form @2000 | 0.660 | 0.271 | 0.306 | 30 | 2/28 | -0.354 | [-0.444, -0.267] | 0.000 | TWO-SIDED: A<B (CI) | | 30 | 1/28 | -0.390 | [-0.475, -0.302] | 0.000 | TWO-SIDED: A<B (CI) |
| drift/250, ex-orphans TRAIN | 0.087 | 0.046 | 0.039 | 29 | 4/24 | -0.048 | [-0.070, -0.026] | 0.000 | TWO-SIDED: A<B (CI) | | 29 | 6/23 | -0.042 | [-0.059, -0.024] | 0.002 | TWO-SIDED: A<B (CI) |
| drift/250, owners | 0.075 | 0.040 | 0.055 | 30 | 8/20 | -0.020 | [-0.033, -0.007] | 0.036 | TWO-SIDED: A<B (CI) | | 30 | 4/25 | -0.035 | [-0.048, -0.023] | 0.000 | TWO-SIDED: A<B (CI) |

## Train-objects-only structure (held-out objects were also emancipated in these arms, which mechanically removes borrowing; this restricts the metrics to the 48 train objects)

| metric | control | random | h1 | h1 − control | | | | | | random − control | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| topsim_distinct train @2000 | 0.341 | 0.226 | 0.322 | 30 | 12/18 | -0.019 | [-0.035, -0.003] | 0.362 | TWO-SIDED: A<B (CI) | | 30 | 3/27 | -0.115 | [-0.142, -0.089] | 0.000 | TWO-SIDED: A<B (CI) |
| CBM train @2000 | 0.514 | 0.437 | 0.485 | 30 | 3/24 | -0.029 | [-0.040, -0.017] | 0.000 | TWO-SIDED: A<B (CI) | | 30 | 2/27 | -0.077 | [-0.094, -0.059] | 0.000 | TWO-SIDED: A<B (CI) |
