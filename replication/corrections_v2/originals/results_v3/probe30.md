# probe30 — emancipation of TRAIN orphans only (held-out untouched): control vs random vs Hamming-1 (30 seeds)

| metric | control | emancipate (random) | emancipate_h1 | h1 − control | | | | | | random − control | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| topsim_distinct @2000 | 0.290 | 0.208 | 0.281 | 30 | 14/15 | -0.009 | [-0.021, +0.002] | 1.000 | TWO-SIDED: no difference (CI) | | 30 | 2/27 | -0.082 | [-0.101, -0.061] | 0.000 | TWO-SIDED: A<B (CI) |
| topsim_distinct @250 | 0.282 | 0.200 | 0.278 | 30 | 12/17 | -0.004 | [-0.013, +0.007] | 0.458 | TWO-SIDED: no difference (CI) | | 30 | 0/29 | -0.082 | [-0.099, -0.065] | 0.000 | TWO-SIDED: A<B (CI) |
| CBM @2000 | 0.486 | 0.430 | 0.460 | 30 | 4/22 | -0.026 | [-0.037, -0.016] | 0.001 | TWO-SIDED: A<B (CI) | | 30 | 3/26 | -0.057 | [-0.072, -0.040] | 0.000 | TWO-SIDED: A<B (CI) |
| n_owners train @2000 | 37.300 | 46.267 | 46.267 | 30 | 29/0 | +8.967 | [+6.833, +11.167] | 0.000 | TWO-SIDED: A>B (CI) | | 30 | 28/0 | +8.967 | [+6.767, +11.234] | 0.000 | TWO-SIDED: A>B (CI) |
| test_acc @2000 | 0.585 | 0.552 | 0.557 | 30 | 6/22 | -0.027 | [-0.045, -0.009] | 0.004 | TWO-SIDED: A<B (CI) | | 30 | 8/20 | -0.032 | [-0.059, -0.005] | 0.036 | TWO-SIDED: A<B (CI) |
| train_acc @2000 | 0.979 | 0.998 | 0.997 | 30 | 23/1 | +0.018 | [+0.012, +0.024] | 0.000 | TWO-SIDED: A>B (CI) | | 30 | 24/3 | +0.019 | [+0.013, +0.025] | 0.000 | TWO-SIDED: A>B (CI) |
| held-out sharing a train form @2000 | 0.660 | 0.619 | 0.600 | 30 | 7/15 | -0.060 | [-0.119, -0.004] | 0.134 | TWO-SIDED: A<B (CI) | | 30 | 6/15 | -0.042 | [-0.090, +0.004] | 0.078 | TWO-SIDED: no difference (CI) |
| drift/250, ex-orphans TRAIN | 0.087 | 0.037 | 0.053 | 29 | 8/21 | -0.034 | [-0.061, -0.006] | 0.024 | TWO-SIDED: A<B (CI) | | 29 | 3/25 | -0.051 | [-0.068, -0.033] | 0.000 | TWO-SIDED: A<B (CI) |
| drift/250, owners | 0.075 | 0.054 | 0.069 | 30 | 12/15 | -0.006 | [-0.018, +0.005] | 0.701 | TWO-SIDED: no difference (CI) | | 30 | 5/21 | -0.021 | [-0.032, -0.010] | 0.002 | TWO-SIDED: A<B (CI) |
