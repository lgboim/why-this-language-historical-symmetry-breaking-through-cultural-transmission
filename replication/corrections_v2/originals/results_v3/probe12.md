# probe12 — two phases, the train-error law, required complexity, exposure vs structure

Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## A. Two phases in a single dyad (`pair`, 12,000 steps, 30 seeds): topsim and lexicon size over time

| step | 250 | 500 | 1000 | 2000 | 4000 | 6000 | 8000 | 10000 | 12000 |
|---|---|---|---|---|---|---|---|---|---|
| topsim | 0.280 | 0.343 | 0.343 | 0.313 | 0.306 | 0.296 | 0.293 | 0.291 | 0.285 |
| n_unique | 14.0 | 25.2 | 32.4 | 41.0 | 47.3 | 49.6 | 50.1 | 51.5 | 52.5 |
| train_acc | 0.610 | 0.843 | 0.934 | 0.969 | 0.983 | 0.986 | 0.989 | 0.991 | 0.993 |

Step of peak topsim per seed: median 750, IQR 500–1000; peak topsim 0.364 vs final 0.285.
Within a fresh generation (2000 steps, `generations`, gen 5): 250: 0.279, 500: 0.337, 1000: 0.341, 1500: 0.339, 2000: 0.340

## B. The train-error law: is every training error an orphan target with its owner among the candidates?

Final agents, 4000 training trials per run. same-word = a candidate that shares the target's message.

| cell | n | train acc | share of errors with a same-word candidate present | acc when same-word present | acc when absent | share of trials with same-word present |
|---|---|---|---|---|---|---|
| generations | 30 | 0.979 | 0.76 | 0.68 | 0.994 | 0.05 |
| random+accumulate | 30 | 0.952 | 0.99 | 0.65 | 0.999 | 0.13 |
| random+rewrite | 30 | 0.962 | 0.98 | 0.66 | 0.999 | 0.11 |
| success+accumulate | 30 | 0.939 | 0.98 | 0.64 | 0.999 | 0.17 |
| success+rewrite | 30 | 0.928 | 0.99 | 0.63 | 0.999 | 0.19 |
| hard+accumulate | 30 | 0.905 | 0.98 | 0.63 | 0.997 | 0.24 |
| hard+rewrite | 30 | 0.917 | 0.99 | 0.63 | 0.999 | 0.22 |
| pair | 30 | 0.993 | 0.91 | 0.80 | 1.000 | 0.03 |

## C. Required complexity (Zhang): how many attributes are needed to separate the target from the 4 distractors, and accuracy by that number

| cell | split | share of trials needing 1 attr | 2 | 3 | acc needing 1 | 2 | 3 |
|---|---|---|---|---|---|---|---|
| generations | train | 0.71 | 0.29 | 0.00 | 0.99 | 0.97 | 0.96 |
| generations | test | 0.71 | 0.29 | 0.00 | 0.67 | 0.54 | 0.31 |
| success+rewrite | train | 0.71 | 0.29 | 0.00 | 0.94 | 0.88 | 0.80 |
| success+rewrite | test | 0.71 | 0.29 | 0.00 | 0.63 | 0.47 | 0.19 |
| hard+rewrite | train | 0.71 | 0.29 | 0.00 | 0.94 | 0.86 | 0.65 |
| hard+rewrite | test | 0.71 | 0.29 | 0.00 | 0.70 | 0.51 | 0.22 |
| pair | train | 0.71 | 0.29 | 0.00 | 1.00 | 0.99 | 0.99 |
| pair | test | 0.71 | 0.29 | 0.00 | 0.59 | 0.45 | 0.34 |

## D. Exposure → structure at the object level: in the child's final language, are UNTAUGHT training objects more regular than TAUGHT ones?

local fit = per-object Spearman fit inside the child's final language. Taught = in the record the child read.

| cell | fit: taught | untaught train | untaught − taught | | | | | held-out |
|---|---|---|---|---|---|---|---|---|
| random+accumulate | 0.306 | 0.323 | 30 | 22/8 | +0.017 | [+0.003, +0.030] | 0.016 | TWO-SIDED: A>B (CI) | 0.270 |
| random+rewrite | 0.406 | 0.365 | 30 | 5/25 | -0.041 | [-0.056, -0.026] | 0.000 | TWO-SIDED: A<B (CI) | 0.282 |
| success+accumulate | 0.352 | 0.308 | 30 | 4/26 | -0.044 | [-0.062, -0.028] | 0.000 | TWO-SIDED: A<B (CI) | 0.272 |
| success+rewrite | 0.441 | 0.372 | 30 | 0/30 | -0.069 | [-0.078, -0.058] | 0.000 | TWO-SIDED: A<B (CI) | 0.303 |
| hard+accumulate | 0.397 | 0.379 | 30 | 6/24 | -0.018 | [-0.024, -0.011] | 0.001 | TWO-SIDED: A<B (CI) | 0.314 |
| hard+rewrite | 0.409 | 0.393 | 30 | 5/25 | -0.016 | [-0.024, -0.008] | 0.000 | TWO-SIDED: A<B (CI) | 0.322 |

## E. Fate of taught vs untaught training objects at the end of the child's generation

| cell | per-object acc: taught | untaught | owner share: taught | untaught | fidelity to inherited form: taught |
|---|---|---|---|---|---|
| random+accumulate | 0.957 | 0.951 | 0.57 | 0.53 | 0.69 |
| random+rewrite | 0.969 | 0.962 | 0.64 | 0.60 | 0.83 |
| success+accumulate | 0.938 | 0.940 | 0.50 | 0.49 | 0.64 |
| success+rewrite | 0.950 | 0.943 | 0.53 | 0.48 | 0.80 |
| hard+accumulate | 0.912 | 0.936 | 0.38 | 0.45 | 0.78 |
| hard+rewrite | 0.918 | 0.944 | 0.39 | 0.47 | 0.80 |

