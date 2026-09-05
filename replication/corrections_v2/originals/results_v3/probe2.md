# probe2 — `results_v3` (770 runs, 10 seeds)

Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## 1. Is 'structure' partly a compression artifact?

`topsim` counts pairs of objects that share a message (message distance 0). With a small lexicon many close objects share a message, which inflates the correlation for free. `topsim_distinct` uses only pairs with different messages.

Within-seed correlation of lexicon size with topsim: r = -0.15; with topsim_distinct: r = +0.43 (across all 77 cells).

| comparison (A − B) | metric | n | wins/losses | mean diff | 95% CI | p | |
|---|---|---|---|---|---|---|---|
| rewrite − accumulate (success slots) | topsim | 10 | 10/0 | +0.085 | [+0.046, +0.132] | 0.002 | TWO-SIDED: A>B (CI) |
| rewrite − accumulate (success slots) | topsim_distinct | 10 | 9/1 | +0.092 | [+0.037, +0.155] | 0.021 | TWO-SIDED: A>B (CI) |
| rewrite − accumulate (success slots) | n_unique | 10 | 4/6 | -5.800 | [-11.300, +0.000] | 0.754 | TWO-SIDED: no difference (CI) |
| rewrite − accumulate (random slots) | topsim | 10 | 7/3 | +0.050 | [+0.010, +0.089] | 0.344 | TWO-SIDED: A>B (CI) |
| rewrite − accumulate (random slots) | topsim_distinct | 10 | 8/2 | +0.078 | [+0.034, +0.118] | 0.109 | TWO-SIDED: A>B (CI) |
| rewrite − accumulate (random slots) | n_unique | 10 | 8/2 | +6.800 | [+1.800, +11.800] | 0.109 | TWO-SIDED: A>B (CI) |
| cap 19 − cap 40 (success+rewrite) | topsim | 10 | 5/5 | -0.009 | [-0.070, +0.044] | 1.000 | TWO-SIDED: no difference (CI) |
| cap 19 − cap 40 (success+rewrite) | topsim_distinct | 10 | 5/5 | -0.041 | [-0.105, +0.016] | 1.000 | TWO-SIDED: no difference (CI) |
| cap 19 − cap 40 (success+rewrite) | n_unique | 10 | 0/10 | -21.000 | [-24.800, -16.898] | 0.002 | TWO-SIDED: A<B (CI) |
| cap 8 − cap 19 (success+rewrite) | topsim | 10 | 3/7 | -0.047 | [-0.089, -0.012] | 0.344 | TWO-SIDED: A<B (CI) |
| cap 8 − cap 19 (success+rewrite) | topsim_distinct | 10 | 1/9 | -0.109 | [-0.162, -0.049] | 0.021 | TWO-SIDED: A<B (CI) |
| cap 8 − cap 19 (success+rewrite) | n_unique | 10 | 2/8 | -8.500 | [-14.000, -2.600] | 0.109 | TWO-SIDED: A<B (CI) |
| hard − random (rewrite) | topsim | 10 | 5/5 | +0.039 | [-0.002, +0.084] | 1.000 | TWO-SIDED: no difference (CI) |
| hard − random (rewrite) | topsim_distinct | 10 | 4/6 | -0.005 | [-0.044, +0.039] | 0.754 | TWO-SIDED: no difference (CI) |
| hard − random (rewrite) | n_unique | 10 | 0/10 | -14.500 | [-18.800, -11.200] | 0.002 | TWO-SIDED: A<B (CI) |
| hard+rewrite − generations | topsim | 10 | 7/3 | +0.046 | [+0.008, +0.083] | 0.344 | TWO-SIDED: A>B (CI) |
| hard+rewrite − generations | topsim_distinct | 10 | 5/5 | -0.012 | [-0.051, +0.026] | 1.000 | TWO-SIDED: no difference (CI) |
| hard+rewrite − generations | n_unique | 10 | 0/10 | -24.100 | [-28.800, -20.300] | 0.002 | TWO-SIDED: A<B (CI) |
| success+rewrite − generations | topsim | 10 | 6/4 | +0.021 | [-0.012, +0.059] | 0.754 | TWO-SIDED: no difference (CI) |
| success+rewrite − generations | topsim_distinct | 10 | 4/6 | -0.013 | [-0.057, +0.033] | 0.754 | TWO-SIDED: no difference (CI) |
| success+rewrite − generations | n_unique | 10 | 0/10 | -22.600 | [-26.200, -19.100] | 0.002 | TWO-SIDED: A<B (CI) |
| random+rewrite (oral_fixed) − generations | topsim | 10 | 6/4 | +0.007 | [-0.018, +0.032] | 0.754 | TWO-SIDED: no difference (CI) |
| random+rewrite (oral_fixed) − generations | topsim_distinct | 10 | 4/6 | -0.007 | [-0.037, +0.023] | 0.754 | TWO-SIDED: no difference (CI) |
| random+rewrite (oral_fixed) − generations | n_unique | 10 | 0/10 | -9.600 | [-12.700, -7.000] | 0.002 | TWO-SIDED: A<B (CI) |
| noise 0 − noise 0.2 (success+rewrite) | topsim | 10 | 7/3 | +0.030 | [-0.008, +0.068] | 0.344 | TWO-SIDED: no difference (CI) |
| noise 0 − noise 0.2 (success+rewrite) | topsim_distinct | 10 | 7/3 | +0.023 | [-0.034, +0.071] | 0.344 | TWO-SIDED: no difference (CI) |
| noise 0 − noise 0.2 (success+rewrite) | n_unique | 10 | 1/8 | -7.400 | [-11.200, -3.600] | 0.039 | TWO-SIDED: A<B (CI) |
| generations − pair | topsim | 10 | 10/0 | +0.060 | [+0.034, +0.087] | 0.002 | TWO-SIDED: A>B (CI) |
| generations − pair | topsim_distinct | 10 | 8/2 | +0.048 | [+0.019, +0.080] | 0.109 | TWO-SIDED: A>B (CI) |
| generations − pair | n_unique | 10 | 0/10 | -10.800 | [-13.800, -7.600] | 0.002 | TWO-SIDED: A<B (CI) |

Partial correlation of fresh=rewrite with topsim_distinct after removing lexicon size (within seed): r = +0.31 (positive in 10/10 seeds).

## 2. Are the 'hard' objects the homonym-bearing ones?

At each generation end, share of selected slot objects whose message is shared with another object, vs the share among all training objects.

| cell | slot objects that are homonyms | all train objects | n | wins/losses | mean diff | 95% CI | p | |
|---|---|---|---|---|---|---|---|---|
| hard+rewrite | 0.88 | 0.77 | 10 | 10/0 | +0.116 | [+0.094, +0.138] | 0.002 | TWO-SIDED: A>B (CI) |
| hard+accumulate | 0.89 | 0.77 | 10 | 10/0 | +0.116 | [+0.103, +0.128] | 0.002 | TWO-SIDED: A>B (CI) |
| success+rewrite | 0.77 | 0.74 | 10 | 6/4 | +0.027 | [-0.001, +0.053] | 0.754 | TWO-SIDED: no difference (CI) |

Sanity (generations control): per-object accuracy of homonyms minus non-homonyms = -0.076 (negative in 9/10 seeds).

## 3. When the child changes an inherited form, does the new form fit the language better?

For each taught object the child re-formed: local fit = Spearman(object distance, message distance) from that object to all others, computed in the child's final language with (a) the child's new form vs (b) the inherited form substituted in.

| cell | share of taught forms changed | fit(new) − fit(inherited) | n | wins/losses | mean diff | 95% CI | p | |
|---|---|---|---|---|---|---|---|---|
| random+accumulate | 0.35 | +0.084 | 10 | 10/0 | +0.084 | [+0.059, +0.110] | 0.002 | TWO-SIDED: A>B (CI) |
| random+rewrite | 0.18 | +0.053 | 10 | 10/0 | +0.053 | [+0.035, +0.071] | 0.002 | TWO-SIDED: A>B (CI) |
| success+accumulate | 0.35 | +0.101 | 10 | 10/0 | +0.101 | [+0.079, +0.126] | 0.002 | TWO-SIDED: A>B (CI) |
| success+rewrite | 0.19 | +0.052 | 10 | 10/0 | +0.052 | [+0.033, +0.072] | 0.002 | TWO-SIDED: A>B (CI) |
| hard+accumulate | 0.24 | +0.037 | 10 | 7/3 | +0.037 | [+0.008, +0.070] | 0.344 | TWO-SIDED: A>B (CI) |
| hard+rewrite | 0.22 | +0.056 | 10 | 10/0 | +0.056 | [+0.041, +0.071] | 0.002 | TWO-SIDED: A>B (CI) |

## 4. Why do seeds agree on which attribute gets dropped? Positional bias in the sender

Per message position: entropy of the symbol used (bits), and which attribute it carries most information about.

### pair

| position | entropy (bits, max 3.00) | MI with attr 0 | MI with attr 1 | MI with attr 2 | seeds where this position is mostly about attr 0/1/2 |
|---|---|---|---|---|---|
| 0 | 2.44 | 0.66 | 0.49 | 0.74 | 2/2/6 |
| 1 | 2.63 | 0.54 | 0.46 | 0.51 | 4/2/4 |
| 2 | 2.69 | 0.45 | 0.44 | 0.44 | 3/3/4 |

### generations

| position | entropy (bits, max 3.00) | MI with attr 0 | MI with attr 1 | MI with attr 2 | seeds where this position is mostly about attr 0/1/2 |
|---|---|---|---|---|---|
| 0 | 2.34 | 0.73 | 0.69 | 0.52 | 4/4/2 |
| 1 | 2.47 | 0.69 | 0.51 | 0.40 | 5/4/1 |
| 2 | 2.49 | 0.70 | 0.46 | 0.45 | 5/2/3 |

### success+rewrite

| position | entropy (bits, max 3.00) | MI with attr 0 | MI with attr 1 | MI with attr 2 | seeds where this position is mostly about attr 0/1/2 |
|---|---|---|---|---|---|
| 0 | 1.77 | 0.48 | 0.38 | 0.66 | 4/2/4 |
| 1 | 2.27 | 0.54 | 0.64 | 0.59 | 2/4/4 |
| 2 | 2.11 | 0.33 | 0.54 | 0.72 | 1/4/5 |

### hard+rewrite

| position | entropy (bits, max 3.00) | MI with attr 0 | MI with attr 1 | MI with attr 2 | seeds where this position is mostly about attr 0/1/2 |
|---|---|---|---|---|---|
| 0 | 1.78 | 0.62 | 0.44 | 0.51 | 3/2/5 |
| 1 | 2.18 | 0.50 | 0.59 | 0.72 | 1/5/4 |
| 2 | 2.23 | 0.64 | 0.47 | 0.81 | 3/2/5 |

Total MI carried per attribute (generations, summed over positions): attr 0: 2.12, attr 1: 1.66, attr 2: 1.38
Attributes are symmetric in the world (the split is random per seed), so any asymmetry here is an artefact of the encoder's input ordering or of the recurrent decoder — not of the language.

## 5. On a homonym, which object does the receiver pick?

For every group of objects sharing a message: does the receiver's decode land inside the group (consistent) and, if so, on a training object, and on the member with the highest per-object accuracy?

| cell | groups | decode inside group | picks a train object (share of train in group) | picks the most-accurate member (chance) |
|---|---|---|---|---|
| pair | 7.0/seed | 0.93 | 1.00 (0.59) | 0.98 (0.46) |
| generations | 14.6/seed | 0.97 | 1.00 (0.72) | 0.92 (0.45) |
| random+accumulate | 16.7/seed | 0.99 | 1.00 (0.75) | 0.95 (0.37) |
| random+rewrite | 17.0/seed | 0.98 | 0.99 (0.73) | 0.95 (0.41) |
| success+accumulate | 15.4/seed | 0.99 | 1.00 (0.74) | 0.95 (0.36) |
| success+rewrite | 17.6/seed | 0.99 | 1.00 (0.78) | 0.93 (0.35) |
| hard+accumulate | 14.8/seed | 0.97 | 1.00 (0.75) | 0.94 (0.33) |
| hard+rewrite | 16.0/seed | 0.99 | 1.00 (0.78) | 0.92 (0.33) |

## 6. Would the verdicts change with 1000-step generations?

Same comparisons, using the eval at gen_step 1000 of the LAST generation instead of the end.

| comparison (A − B) | metric | at 2000 steps | at 1000 steps |
|---|---|---|---|
| rewrite − accumulate (success slots) | topsim | 10/0 +0.085 A>B (CI) | 10/0 +0.090 A>B (CI) |
| rewrite − accumulate (success slots) | test_acc | 6/4 +0.041 no difference (CI) | 8/2 +0.037 no difference (CI) |
| rewrite − accumulate (random slots) | topsim | 7/3 +0.050 A>B (CI) | 7/3 +0.061 A>B (CI) |
| rewrite − accumulate (random slots) | test_acc | 6/4 -0.021 no difference (CI) | 4/6 -0.012 no difference (CI) |
| cap 19 − cap 40 (success+rewrite) | topsim | 5/5 -0.009 no difference (CI) | 4/6 -0.008 no difference (CI) |
| cap 19 − cap 40 (success+rewrite) | test_acc | 5/5 +0.007 no difference (CI) | 6/4 -0.041 no difference (CI) |
| cap 8 − cap 19 (success+rewrite) | topsim | 3/7 -0.047 A<B (CI) | 1/9 -0.060 A<B (CI) |
| cap 8 − cap 19 (success+rewrite) | test_acc | 4/6 -0.055 no difference (CI) | 4/6 -0.088 no difference (CI) |
| hard − random (rewrite) | topsim | 5/5 +0.039 no difference (CI) | 5/5 +0.023 no difference (CI) |
| hard − random (rewrite) | test_acc | 9/1 +0.088 A>B (CI) | 8/2 +0.077 A>B (CI) |
| hard+rewrite − generations | topsim | 7/3 +0.046 A>B (CI) | 9/1 +0.052 A>B (CI) |
| hard+rewrite − generations | test_acc | 7/3 +0.058 no difference (CI) | 7/3 +0.064 no difference (CI) |
| success+rewrite − generations | topsim | 6/4 +0.021 no difference (CI) | 8/2 +0.044 A>B (CI) |
| success+rewrite − generations | test_acc | 3/7 -0.047 no difference (CI) | 3/7 -0.020 no difference (CI) |
| random+rewrite (oral_fixed) − generations | topsim | 6/4 +0.007 no difference (CI) | 6/4 +0.029 A>B (CI) |
| random+rewrite (oral_fixed) − generations | test_acc | 4/6 -0.031 no difference (CI) | 5/5 -0.013 no difference (CI) |
| noise 0 − noise 0.2 (success+rewrite) | topsim | 7/3 +0.030 no difference (CI) | 6/4 +0.033 A>B (CI) |
| noise 0 − noise 0.2 (success+rewrite) | test_acc | 4/6 -0.063 no difference (CI) | 4/6 -0.050 no difference (CI) |
| generations − pair | topsim | 8/2 +0.042 A>B (CI) | 5/5 -0.016 no difference (CI) |
| generations − pair | test_acc | 5/5 +0.015 no difference (CI) | 5/4 -0.030 no difference (CI) |

