# Post-hoc probes — `results_v3` (770 runs, 10 seeds, world=small)

Exploratory. Paired-by-seed columns are wins/losses | mean diff | 95% CI | sign-test p.

## 1. Trajectory per generation (mean over seeds)

### topsim

| cell | gen 0 | gen 1 | gen 2 | gen 3 | gen 4 | gen 5 |
|---|---|---|---|---|---|---|
| generations | 0.313 | 0.362 | 0.356 | 0.308 | 0.322 | 0.356 |
| random+accumulate | 0.313 | 0.286 | 0.294 | 0.314 | 0.301 | 0.313 |
| random+rewrite | 0.313 | 0.342 | 0.353 | 0.363 | 0.359 | 0.362 |
| success+accumulate | 0.313 | 0.295 | 0.303 | 0.287 | 0.276 | 0.292 |
| success+rewrite | 0.313 | 0.326 | 0.363 | 0.370 | 0.346 | 0.376 |
| hard+accumulate | 0.313 | 0.347 | 0.346 | 0.354 | 0.355 | 0.358 |
| hard+rewrite | 0.313 | 0.347 | 0.353 | 0.384 | 0.388 | 0.401 |

### test_acc

| cell | gen 0 | gen 1 | gen 2 | gen 3 | gen 4 | gen 5 |
|---|---|---|---|---|---|---|
| generations | 0.611 | 0.632 | 0.615 | 0.606 | 0.603 | 0.626 |
| random+accumulate | 0.611 | 0.592 | 0.591 | 0.642 | 0.581 | 0.617 |
| random+rewrite | 0.611 | 0.577 | 0.593 | 0.592 | 0.605 | 0.596 |
| success+accumulate | 0.611 | 0.579 | 0.525 | 0.530 | 0.550 | 0.538 |
| success+rewrite | 0.611 | 0.559 | 0.606 | 0.606 | 0.545 | 0.579 |
| hard+accumulate | 0.611 | 0.623 | 0.633 | 0.616 | 0.625 | 0.588 |
| hard+rewrite | 0.611 | 0.623 | 0.639 | 0.649 | 0.651 | 0.684 |

### n_unique_msgs

| cell | gen 0 | gen 1 | gen 2 | gen 3 | gen 4 | gen 5 |
|---|---|---|---|---|---|---|
| generations | 44.700 | 43.100 | 40.400 | 42.300 | 37.900 | 44.100 |
| random+accumulate | 44.700 | 27.700 | 29.400 | 27.300 | 27.700 | 27.700 |
| random+rewrite | 44.700 | 33.100 | 35.600 | 34.600 | 33.600 | 34.500 |
| success+accumulate | 44.700 | 28.000 | 27.800 | 24.700 | 24.400 | 27.300 |
| success+rewrite | 44.700 | 32.800 | 28.900 | 24.300 | 21.300 | 21.500 |
| hard+accumulate | 44.700 | 31.600 | 26.200 | 22.400 | 19.300 | 20.600 |
| hard+rewrite | 44.700 | 31.600 | 25.200 | 24.900 | 21.000 | 20.000 |

Change in topsim from gen 0 to gen 1 (the first transmission), success slots: accumulate − rewrite: 2/8 | -0.030 | [-0.060, +0.001] | 0.109

## 2. Fidelity: share of the transmitted (object, message) pairs the child still uses at the end of its generation

| factor | level | fidelity | topsim |
|---|---|---|---|
| select | hard | 0.770 | 0.322 |
| select | random | 0.775 | 0.302 |
| select | success | 0.740 | 0.309 |
| fresh | accumulate | 0.722 | 0.291 |
| fresh | rewrite | 0.801 | 0.330 |
| capacity | 8 | 0.681 | 0.325 |
| capacity | 19 | 0.774 | 0.321 |
| capacity | 40 | 0.829 | 0.286 |
| noise | 0.0 | 0.755 | 0.330 |
| noise | 0.2 | 0.768 | 0.292 |
| reader | both | 0.783 | 0.304 |
| reader | sender | 0.740 | 0.317 |

Within-seed correlation between fidelity and final topsim across all 74 record cells: mean r = -0.06 (positive in 4/10 seeds).

- holding fresh=accumulate: mean r = -0.22 (positive in 1/10)
- holding fresh=rewrite: mean r = -0.13 (positive in 5/10)

## 3. 'Hard' slots: rotation and repair

| cell | slots kept gen→gen | Δacc on taught objects (child − parent) | Δacc on untaught train objects |
|---|---|---|---|
| random+accumulate | 1.00 | -0.002 | -0.005 |
| random+rewrite | 1.00 | +0.000 | -0.001 |
| success+accumulate | 1.00 | -0.005 | -0.006 |
| success+rewrite | 0.52 | -0.005 | -0.009 |
| hard+accumulate | 0.46 | +0.041 | -0.046 |
| hard+rewrite | 0.47 | +0.041 | -0.042 |

Are 'hard' objects intrinsically hard? Correlation of per-object accuracy between consecutive generations (if the same objects are hard every time, hard slots would be stable):

- generations: mean r = +0.03
- hard+rewrite: mean r = +0.22
- random+rewrite: mean r = +0.14

## 4. Held-out objects: solvable when a recorded object sits next to them?

| cell | held-out acc, dist 1 to a recorded object | dist ≥ 2 | paired diff (wins/losses, mean, CI, p) | share of held-out objects with acc ≥ 0.8 | share ≤ 0.2 |
|---|---|---|---|---|---|
| random+accumulate | 0.596 | 0.641 | 2/3 | -0.045 | [-0.120, +0.031] | 1.000 | 0.35 | 0.09 |
| random+rewrite | 0.602 | 0.434 | 3/2 | +0.168 | [-0.021, +0.356] | 1.000 | 0.31 | 0.11 |
| success+accumulate | 0.512 | 0.538 | 2/3 | -0.026 | [-0.205, +0.152] | 1.000 | 0.19 | 0.15 |
| success+rewrite | 0.581 | 0.486 | 6/4 | +0.095 | [+0.019, +0.176] | 0.754 | 0.29 | 0.13 |
| hard+accumulate | 0.614 | 0.526 | 5/4 | +0.088 | [-0.037, +0.219] | 1.000 | 0.23 | 0.09 |
| hard+rewrite | 0.655 | 0.608 | 5/4 | +0.047 | [-0.088, +0.182] | 1.000 | 0.35 | 0.05 |

Control (generations): share of held-out objects with acc ≥ 0.8 = 0.34, ≤ 0.2 = 0.12. Bimodality = generalisation is per-object all-or-nothing.

## 5. Sender–receiver agreement

| cell | sender topsim | receiver-side topsim | intelligibility | synonymy (messages per decoded object) |
|---|---|---|---|---|
| pair | 0.296 | 0.648 | 0.714 | 1.20 |
| population | 0.322 | 0.594 | 0.613 | 1.19 |
| generations | 0.356 | 0.596 | 0.577 | 1.16 |
| random+accumulate | 0.313 | 0.496 | 0.412 | 1.04 |
| random+rewrite | 0.362 | 0.542 | 0.505 | 1.06 |
| success+accumulate | 0.292 | 0.443 | 0.397 | 1.05 |
| success+rewrite | 0.376 | 0.444 | 0.322 | 1.02 |
| hard+accumulate | 0.358 | 0.449 | 0.305 | 1.03 |
| hard+rewrite | 0.401 | 0.472 | 0.300 | 1.02 |

Across all 770 runs: corr(sender topsim, intelligibility) = -0.15.

## 6. Inside a generation (generations ≥ 1, mean over seeds and generations)

### n_unique_msgs

| cell | 250 | 500 | 750 | 1000 | 1250 | 1500 | 1750 | 2000 |
|---|---|---|---|---|---|---|---|---|
| generations | 13.4 | 25.2 | 30.0 | 32.1 | 36.0 | 38.0 | 39.9 | 41.6 |
| random+accumulate | 18.0 | 20.0 | 21.7 | 23.5 | 24.4 | 26.0 | 26.9 | 28.0 |
| random+rewrite | 24.7 | 27.0 | 28.4 | 30.0 | 31.7 | 32.4 | 33.0 | 34.3 |
| success+accumulate | 16.6 | 18.6 | 20.0 | 21.8 | 23.4 | 24.5 | 25.3 | 26.4 |
| success+rewrite | 18.4 | 19.7 | 21.2 | 22.4 | 23.1 | 24.1 | 25.2 | 25.8 |
| hard+accumulate | 15.7 | 17.3 | 19.0 | 20.0 | 21.2 | 22.1 | 23.4 | 24.0 |
| hard+rewrite | 16.4 | 18.1 | 19.3 | 20.5 | 21.8 | 22.6 | 23.8 | 24.5 |

### topsim

| cell | 250 | 500 | 750 | 1000 | 1250 | 1500 | 1750 | 2000 |
|---|---|---|---|---|---|---|---|---|
| generations | 0.281 | 0.340 | 0.340 | 0.346 | 0.344 | 0.343 | 0.345 | 0.341 |
| random+accumulate | 0.274 | 0.284 | 0.291 | 0.293 | 0.294 | 0.298 | 0.299 | 0.301 |
| random+rewrite | 0.338 | 0.345 | 0.345 | 0.348 | 0.351 | 0.350 | 0.352 | 0.356 |
| success+accumulate | 0.259 | 0.266 | 0.270 | 0.277 | 0.285 | 0.288 | 0.289 | 0.290 |
| success+rewrite | 0.341 | 0.347 | 0.353 | 0.351 | 0.351 | 0.354 | 0.358 | 0.356 |
| hard+accumulate | 0.337 | 0.338 | 0.344 | 0.350 | 0.348 | 0.353 | 0.353 | 0.352 |
| hard+rewrite | 0.354 | 0.359 | 0.363 | 0.364 | 0.369 | 0.372 | 0.374 | 0.375 |

### train_acc

| cell | 250 | 500 | 750 | 1000 | 1250 | 1500 | 1750 | 2000 |
|---|---|---|---|---|---|---|---|---|
| generations | 0.619 | 0.831 | 0.903 | 0.930 | 0.948 | 0.958 | 0.966 | 0.968 |
| random+accumulate | 0.888 | 0.914 | 0.926 | 0.935 | 0.941 | 0.946 | 0.950 | 0.951 |
| random+rewrite | 0.929 | 0.944 | 0.950 | 0.959 | 0.962 | 0.964 | 0.968 | 0.970 |
| success+accumulate | 0.856 | 0.889 | 0.906 | 0.918 | 0.926 | 0.933 | 0.936 | 0.941 |
| success+rewrite | 0.890 | 0.909 | 0.918 | 0.926 | 0.928 | 0.933 | 0.937 | 0.941 |
| hard+accumulate | 0.880 | 0.900 | 0.912 | 0.915 | 0.922 | 0.925 | 0.931 | 0.933 |
| hard+rewrite | 0.891 | 0.907 | 0.917 | 0.924 | 0.928 | 0.932 | 0.937 | 0.940 |

## 7. Ease of learning: a fresh sender imitates each final language (64 objects, 150 supervised steps)

ease = mean reproduction accuracy over the 150 steps (area under the learning curve). Li & Bowling 2019: compositional languages should be easier to teach.

| cell | ease | topsim | paired vs generations (wins/losses, mean, CI, p) |
|---|---|---|---|
| pair | 0.748 | 0.296 | 4/6 | -0.012 | [-0.025, -0.001] | 0.754 |
| generations | 0.760 | 0.356 | – |
| random+accumulate | 0.766 | 0.313 | 5/5 | +0.005 | [-0.017, +0.029] | 1.000 |
| random+rewrite | 0.785 | 0.362 | 10/0 | +0.025 | [+0.014, +0.035] | 0.002 |
| success+accumulate | 0.773 | 0.292 | 6/4 | +0.012 | [-0.006, +0.030] | 0.754 |
| success+rewrite | 0.797 | 0.376 | 9/1 | +0.037 | [+0.019, +0.053] | 0.021 |
| hard+accumulate | 0.802 | 0.358 | 10/0 | +0.041 | [+0.027, +0.060] | 0.002 |
| hard+rewrite | 0.797 | 0.401 | 9/1 | +0.036 | [+0.016, +0.058] | 0.021 |

corr(ease, topsim) across these 8 cells: +0.74

## 8. What compression drops: homonym pairs that differ in exactly one attribute

concentration = share of those pairs falling on the single most-dropped attribute within a seed (1/n_attrs = no preference).

| cell | n pairs | concentration | most-dropped attribute is the same across seeds? |
|---|---|---|---|
| pair | 61 | 0.71 | 0.56 of seeds agree |
| generations | 181 | 0.71 | 0.70 of seeds agree |
| random+accumulate | 474 | 0.63 | 0.70 of seeds agree |
| random+rewrite | 315 | 0.56 | 0.50 of seeds agree |
| success+accumulate | 474 | 0.51 | 0.40 of seeds agree |
| success+rewrite | 553 | 0.53 | 0.50 of seeds agree |
| hard+accumulate | 722 | 0.56 | 0.50 of seeds agree |
| hard+rewrite | 703 | 0.65 | 0.40 of seeds agree |

