# probe24 — punctuated vs continuous change after inheritance

## A. Within-generation change of the canonical form per 250 steps (gens ≥ 1): owners vs orphans (status at the start of the window)

| cell | owners | orphans | paired (owner − orphan) | | | | | |
|---|---|---|---|---|---|---|---|---|
| generations | 0.357 | 0.515 | 30 | 0/30 | -0.159 | [-0.169, -0.148] | 0.000 | TWO-SIDED: A<B (CI) | |
| random+accumulate | 0.055 | 0.169 | 30 | 0/30 | -0.114 | [-0.122, -0.105] | 0.000 | TWO-SIDED: A<B (CI) | |
| random+rewrite | 0.060 | 0.192 | 30 | 0/30 | -0.132 | [-0.143, -0.121] | 0.000 | TWO-SIDED: A<B (CI) | |
| success+accumulate | 0.065 | 0.159 | 30 | 0/30 | -0.094 | [-0.102, -0.086] | 0.000 | TWO-SIDED: A<B (CI) | |
| success+rewrite | 0.051 | 0.156 | 30 | 0/30 | -0.105 | [-0.116, -0.094] | 0.000 | TWO-SIDED: A<B (CI) | |
| hard+accumulate | 0.052 | 0.138 | 30 | 0/30 | -0.087 | [-0.100, -0.074] | 0.000 | TWO-SIDED: A<B (CI) | |
| hard+rewrite | 0.054 | 0.134 | 30 | 0/30 | -0.080 | [-0.090, -0.070] | 0.000 | TWO-SIDED: A<B (CI) | |

## B. Change at transfer (end of gen g → step 250 of gen g+1): taught vs untaught objects; and of the changed forms, share that are inventions (not in parent's language) vs borrowed (parent's form of another object)

| cell | taught change | untaught change | paired (taught − untaught) | | | | | | invention share | borrowed share |
|---|---|---|---|---|---|---|---|---|---|---|
| random+accumulate | 0.464 | 0.732 | 30 | 0/30 | -0.268 | [-0.296, -0.238] | 0.000 | TWO-SIDED: A<B (CI) | 0.30 | 0.70 |
| random+rewrite | 0.068 | 0.705 | 30 | 0/30 | -0.637 | [-0.668, -0.603] | 0.000 | TWO-SIDED: A<B (CI) | 0.16 | 0.84 |
| success+accumulate | 0.484 | 0.756 | 30 | 0/30 | -0.272 | [-0.301, -0.240] | 0.000 | TWO-SIDED: A<B (CI) | 0.30 | 0.70 |
| success+rewrite | 0.076 | 0.738 | 30 | 0/30 | -0.662 | [-0.689, -0.634] | 0.000 | TWO-SIDED: A<B (CI) | 0.15 | 0.85 |
| hard+accumulate | 0.122 | 0.638 | 30 | 0/30 | -0.516 | [-0.542, -0.490] | 0.000 | TWO-SIDED: A<B (CI) | 0.16 | 0.84 |
| hard+rewrite | 0.057 | 0.615 | 30 | 0/30 | -0.558 | [-0.585, -0.530] | 0.000 | TWO-SIDED: A<B (CI) | 0.11 | 0.89 |

## C. Sender entropy trajectory within a generation (mean over seeds and gens ≥ 1)

| cell | 250 | 500 | 750 | 1000 | 1250 | 1500 | 1750 | 2000 |
|---|---|---|---|---|---|---|---|---|
| generations | 1.31 | 0.89 | 0.69 | 0.57 | 0.49 | 0.45 | 0.41 | 0.38 |
| random+accumulate | 0.16 | 0.13 | 0.12 | 0.12 | 0.11 | 0.11 | 0.11 | 0.11 |
| random+rewrite | 0.16 | 0.14 | 0.12 | 0.12 | 0.11 | 0.11 | 0.10 | 0.10 |
| success+accumulate | 0.16 | 0.13 | 0.12 | 0.11 | 0.11 | 0.10 | 0.10 | 0.10 |
| success+rewrite | 0.13 | 0.11 | 0.10 | 0.09 | 0.09 | 0.08 | 0.08 | 0.08 |
| hard+accumulate | 0.11 | 0.10 | 0.08 | 0.08 | 0.07 | 0.07 | 0.07 | 0.07 |
| hard+rewrite | 0.11 | 0.09 | 0.08 | 0.08 | 0.08 | 0.07 | 0.07 | 0.07 |

## D. Per-object variant rate of the sender at the end of a generation (from weights) vs whether that object's canonical form changed in the last window (1750→2000), gens ≥ 1

| cell | variant rate, changed objects | variant rate, unchanged | paired (changed − unchanged) | | | | | | owners: changed − unchanged |
|---|---|---|---|---|---|---|---|---|---|
| random+accumulate | 0.326 | 0.068 | 30 | 30/0 | +0.258 | [+0.245, +0.271] | 0.000 | TWO-SIDED: A>B (CI) | +0.205 (1.00) |
| random+rewrite | 0.317 | 0.067 | 30 | 30/0 | +0.250 | [+0.232, +0.269] | 0.000 | TWO-SIDED: A>B (CI) | +0.193 (1.00) |
| success+accumulate | 0.330 | 0.066 | 30 | 30/0 | +0.264 | [+0.247, +0.283] | 0.000 | TWO-SIDED: A>B (CI) | +0.239 (1.00) |
| success+rewrite | 0.282 | 0.055 | 30 | 30/0 | +0.227 | [+0.203, +0.251] | 0.000 | TWO-SIDED: A>B (CI) | +0.188 (0.93) |
| hard+accumulate | 0.265 | 0.049 | 30 | 30/0 | +0.215 | [+0.193, +0.237] | 0.000 | TWO-SIDED: A>B (CI) | +0.186 (0.97) |
| hard+rewrite | 0.268 | 0.051 | 30 | 30/0 | +0.217 | [+0.197, +0.240] | 0.000 | TWO-SIDED: A>B (CI) | +0.190 (0.93) |

## E. Does it settle? within-gen total change and transfer change by generation (mean over 30 seeds, 6 focus cells pooled)

| gen | within-gen (250→2000) | at transfer into this gen | entropy @250 | n_owners @2000 |
|---|---|---|---|---|
| 0 | 0.878 | nan | 1.33 | 32.6 |
| 1 | 0.376 | 0.715 | 0.16 | 27.1 |
| 2 | 0.361 | 0.548 | 0.14 | 25.1 |
| 3 | 0.338 | 0.514 | 0.14 | 23.9 |
| 4 | 0.331 | 0.497 | 0.13 | 22.9 |
| 5 | 0.322 | 0.493 | 0.13 | 21.9 |

within-gen change, gen 5 − gen 1, paired over (cell, seed): | 180 | 52/122 | -0.053 | [-0.074, -0.033] | 0.000 | TWO-SIDED: A<B (CI) |

## F. Reversion: of objects whose form changed at some window within a gen ≥ 1, share whose form at step 2000 equals the form at step 250 (oscillation) vs a new form

| cell | changed at least once | of those, back to the step-250 form at 2000 | ended on a form seen earlier in the gen (any) |
|---|---|---|---|
| generations | 0.922 | 0.04 | 0.83 |
| random+accumulate | 0.451 | 0.15 | 0.86 |
| random+rewrite | 0.434 | 0.22 | 0.89 |
| success+accumulate | 0.458 | 0.14 | 0.87 |
| success+rewrite | 0.414 | 0.20 | 0.89 |
| hard+accumulate | 0.389 | 0.19 | 0.88 |
| hard+rewrite | 0.387 | 0.18 | 0.87 |

## G. Fidelity trajectory: share of the record's taught forms the child still produces, by step within the generation (gens ≥ 1)

| cell | 250 | 500 | 750 | 1000 | 1250 | 1500 | 1750 | 2000 | 250→2000 paired |
|---|---|---|---|---|---|---|---|---|---|
| random+accumulate | 0.89 | 0.86 | 0.83 | 0.79 | 0.77 | 0.74 | 0.71 | 0.69 | 30 | 0/30 | -0.206 | [-0.229, -0.185] | 0.000 | TWO-SIDED: A<B (CI) | |
| random+rewrite | 0.93 | 0.91 | 0.89 | 0.87 | 0.87 | 0.85 | 0.83 | 0.83 | 30 | 0/29 | -0.103 | [-0.119, -0.086] | 0.000 | TWO-SIDED: A<B (CI) | |
| success+accumulate | 0.85 | 0.80 | 0.75 | 0.72 | 0.69 | 0.67 | 0.65 | 0.64 | 30 | 0/30 | -0.213 | [-0.238, -0.188] | 0.000 | TWO-SIDED: A<B (CI) | |
| success+rewrite | 0.92 | 0.91 | 0.88 | 0.86 | 0.85 | 0.84 | 0.82 | 0.80 | 30 | 0/30 | -0.121 | [-0.136, -0.104] | 0.000 | TWO-SIDED: A<B (CI) | |
| hard+accumulate | 0.93 | 0.90 | 0.88 | 0.86 | 0.84 | 0.82 | 0.80 | 0.78 | 30 | 0/30 | -0.149 | [-0.170, -0.128] | 0.000 | TWO-SIDED: A<B (CI) | |
| hard+rewrite | 0.94 | 0.92 | 0.90 | 0.87 | 0.85 | 0.83 | 0.81 | 0.80 | 30 | 0/30 | -0.144 | [-0.166, -0.122] | 0.000 | TWO-SIDED: A<B (CI) | |

## H. Starting-state explanation: across seeds within each cell, corr(entropy @250, within-gen change) and corr(entropy mean over gen, within-gen change), gens ≥ 1 pooled

| cell | n | corr(ent@250, change) | corr(mean ent, change) | corr(ent@250, transfer change into gen) |
|---|---|---|---|---|
| random+accumulate | 150 | +0.21 | +0.49 | -0.00 |
| random+rewrite | 150 | +0.46 | +0.66 | +0.45 |
| success+accumulate | 150 | +0.40 | +0.66 | +0.11 |
| success+rewrite | 150 | +0.54 | +0.67 | +0.48 |
| hard+accumulate | 150 | +0.56 | +0.73 | +0.64 |
| hard+rewrite | 150 | +0.52 | +0.68 | +0.64 |

## I. Capacity and noise vs the split of change (seeds 0–9, select ∈ {random,success,hard} × fresh pooled)

| cell | within-gen (250→2000) | at transfer | share at transfer | entropy @250 |
|---|---|---|---|---|
| cap 8 | 0.420 | 0.662 | 0.61 | 0.12 |
| cap 19 | 0.363 | 0.563 | 0.61 | 0.14 |
| cap 40 | 0.281 | 0.400 | 0.59 | 0.15 |
| noise 0.2 | 0.375 | 0.687 | 0.65 | 0.16 |

## J. Reconciling A with §3.5. (1) Within-gen orphan changes: was the orphan's form before the change identical to its owner's (a true homonym)? after? (2) Transfer change (end g → 250 of g+1) by owner status at end of g, taught vs untaught

| cell | orphan changes: homonym before | homonym after | owner changed in same window | transfer: owners taught | owners untaught | orphans taught | orphans untaught | owner − orphan (untaught) |
|---|---|---|---|---|---|---|---|---|
| random+accumulate | 0.86 | 0.08 | 0.13 | 0.50 | 0.78 | 0.40 | 0.71 | 30 | 25/5 | +0.078 | [+0.057, +0.097] | 0.000 | TWO-SIDED: A>B (CI) | |
| random+rewrite | 0.84 | 0.08 | 0.13 | 0.08 | 0.76 | 0.06 | 0.68 | 30 | 27/3 | +0.079 | [+0.054, +0.104] | 0.000 | TWO-SIDED: A>B (CI) | |
| success+accumulate | 0.87 | 0.10 | 0.14 | 0.53 | 0.82 | 0.43 | 0.73 | 30 | 29/1 | +0.097 | [+0.077, +0.116] | 0.000 | TWO-SIDED: A>B (CI) | |
| success+rewrite | 0.87 | 0.10 | 0.15 | 0.08 | 0.79 | 0.07 | 0.71 | 30 | 27/3 | +0.083 | [+0.063, +0.103] | 0.000 | TWO-SIDED: A>B (CI) | |
| hard+accumulate | 0.88 | 0.13 | 0.17 | 0.09 | 0.62 | 0.12 | 0.66 | 30 | 7/23 | -0.046 | [-0.066, -0.024] | 0.005 | TWO-SIDED: A<B (CI) | |
| hard+rewrite | 0.89 | 0.13 | 0.17 | 0.05 | 0.59 | 0.06 | 0.64 | 30 | 9/21 | -0.047 | [-0.072, -0.021] | 0.043 | TWO-SIDED: A<B (CI) | |

## K. A revisited with the held-out confound removed: within-gen change per 250 steps (gens ≥ 1), TRAIN objects only, owners vs orphans; and held-out objects

| cell | train owners | train orphans | paired (train orphan − train owner) | | | | | | held-out (all orphans) | share of orphans that are held-out |
|---|---|---|---|---|---|---|---|---|---|---|
| generations | 0.355 | 0.475 | 30 | 30/0 | +0.120 | [+0.108, +0.131] | 0.000 | TWO-SIDED: A>B (CI) | 0.579 | 0.38 |
| random+accumulate | 0.053 | 0.099 | 30 | 30/0 | +0.046 | [+0.041, +0.052] | 0.000 | TWO-SIDED: A>B (CI) | 0.284 | 0.38 |
| random+rewrite | 0.058 | 0.109 | 30 | 30/0 | +0.051 | [+0.044, +0.058] | 0.000 | TWO-SIDED: A>B (CI) | 0.302 | 0.42 |
| success+accumulate | 0.064 | 0.101 | 30 | 30/0 | +0.038 | [+0.034, +0.042] | 0.000 | TWO-SIDED: A>B (CI) | 0.261 | 0.35 |
| success+rewrite | 0.050 | 0.098 | 30 | 30/0 | +0.047 | [+0.041, +0.054] | 0.000 | TWO-SIDED: A>B (CI) | 0.250 | 0.37 |
| hard+accumulate | 0.051 | 0.089 | 30 | 30/0 | +0.038 | [+0.030, +0.047] | 0.000 | TWO-SIDED: A>B (CI) | 0.228 | 0.34 |
| hard+rewrite | 0.052 | 0.086 | 30 | 30/0 | +0.034 | [+0.028, +0.041] | 0.000 | TWO-SIDED: A>B (CI) | 0.216 | 0.35 |
