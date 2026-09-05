# probe4 — eleven fast probes (discovery seeds 0–9 + confirm seeds 10–29)

Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## 1. Fresh receiver: is the language generalisable?

A new receiver is trained (400 steps, 5 candidates) ONLY on training objects, from the sender's final language, then tested on held-out objects. If it beats the co-adapted receiver, the failure was co-adaptation, not the language.

| cell | n | co-adapted test_acc | fresh test_acc | fresh − co-adapted | | | | | fresh train_acc |
|---|---|---|---|---|---|---|---|---|---|
| generations | 30 | 0.616 | 0.578 | 30 | 7/22 | -0.039 | [-0.057, -0.021] | 0.008 | TWO-SIDED: A<B (CI) | 0.983 |
| pair | 30 | 0.542 | 0.508 | 30 | 9/21 | -0.035 | [-0.054, -0.016] | 0.043 | TWO-SIDED: A<B (CI) | 0.992 |
| random+accumulate | 30 | 0.585 | 0.582 | 30 | 15/15 | -0.003 | [-0.018, +0.012] | 1.000 | TWO-SIDED: no difference (CI) | 0.951 |
| random+rewrite | 30 | 0.590 | 0.591 | 30 | 15/15 | +0.001 | [-0.012, +0.015] | 1.000 | TWO-SIDED: no difference (CI) | 0.964 |
| success+accumulate | 30 | 0.545 | 0.545 | 30 | 17/12 | +0.000 | [-0.015, +0.017] | 0.458 | TWO-SIDED: no difference (CI) | 0.930 |
| success+rewrite | 30 | 0.590 | 0.595 | 30 | 17/12 | +0.005 | [-0.008, +0.018] | 0.458 | TWO-SIDED: no difference (CI) | 0.925 |
| hard+accumulate | 30 | 0.598 | 0.611 | 30 | 21/8 | +0.013 | [-0.002, +0.028] | 0.024 | TWO-SIDED: no difference (CI) | 0.903 |
| hard+rewrite | 30 | 0.632 | 0.633 | 30 | 18/11 | +0.001 | [-0.015, +0.016] | 0.265 | TWO-SIDED: no difference (CI) | 0.915 |

## 2. Sender rule test: do held-out messages follow the rule fitted on training objects?

Fit the best (position, symbol) ↔ (attribute, value) matching on TRAINING objects only; predict the symbol at each position for every object; consistency = share of predictable positions where the actual symbol matches.

| cell | n | consistency on train | on held-out | held-out − train | | | | |
|---|---|---|---|---|---|---|---|---|
| generations | 30 | 0.511 | 0.349 | 30 | 1/29 | -0.163 | [-0.188, -0.137] | 0.000 | TWO-SIDED: A<B (CI) | |
| pair | 30 | 0.484 | 0.317 | 30 | 2/28 | -0.168 | [-0.197, -0.138] | 0.000 | TWO-SIDED: A<B (CI) | |
| random+accumulate | 30 | 0.506 | 0.361 | 30 | 0/30 | -0.145 | [-0.162, -0.128] | 0.000 | TWO-SIDED: A<B (CI) | |
| random+rewrite | 30 | 0.564 | 0.396 | 30 | 0/30 | -0.167 | [-0.191, -0.143] | 0.000 | TWO-SIDED: A<B (CI) | |
| success+accumulate | 30 | 0.520 | 0.379 | 30 | 1/29 | -0.141 | [-0.162, -0.121] | 0.000 | TWO-SIDED: A<B (CI) | |
| success+rewrite | 30 | 0.590 | 0.421 | 30 | 0/30 | -0.169 | [-0.198, -0.142] | 0.000 | TWO-SIDED: A<B (CI) | |
| hard+accumulate | 30 | 0.582 | 0.425 | 30 | 0/30 | -0.157 | [-0.179, -0.137] | 0.000 | TWO-SIDED: A<B (CI) | |
| hard+rewrite | 30 | 0.596 | 0.445 | 30 | 0/30 | -0.151 | [-0.168, -0.134] | 0.000 | TWO-SIDED: A<B (CI) | |

## 3. Error correction: what does the child do with a corrupted inherited form? (rewrite + noise 0.2 cells, seeds 0–9)

corrupted = record form ≠ parent's final form (one symbol flipped). Child outcome at the end of its generation.

| cell | corrupted entries | kept corrupted | reverted to parent's form | other | intact entries kept | fit(parent form) − fit(corrupted) |
|---|---|---|---|---|---|---|
| random+rewrite+noise | 180 | 0.74 | 0.07 | 0.19 | 0.79 | +0.103 |
| success+rewrite+noise | 173 | 0.79 | 0.06 | 0.16 | 0.75 | +0.119 |
| hard+rewrite+noise | 179 | 0.69 | 0.07 | 0.24 | 0.77 | +0.107 |

## 4. Speed of the child: first eval step with train_acc ≥ 0.9 (generations ≥ 1, mean over gens)

| cell | n | steps | vs generations | | | | |
|---|---|---|---|---|---|---|---|
| generations | 30 | 872 | – | |
| random+accumulate | 30 | 538 | 30 | 4/25 | -333.333 | [-435.000, -221.667] | 0.000 | TWO-SIDED: A<B (CI) | |
| random+rewrite | 30 | 315 | 30 | 1/29 | -556.667 | [-621.667, -465.000] | 0.000 | TWO-SIDED: A<B (CI) | |
| success+accumulate | 30 | 858 | 30 | 10/18 | -13.333 | [-170.000, +170.000] | 0.185 | TWO-SIDED: no difference (CI) | |
| success+rewrite | 30 | 602 | 30 | 5/25 | -270.000 | [-401.667, -108.292] | 0.000 | TWO-SIDED: A<B (CI) | |
| hard+accumulate | 30 | 923 | 30 | 13/17 | +51.667 | [-133.375, +260.000] | 0.585 | TWO-SIDED: no difference (CI) | |
| hard+rewrite | 30 | 820 | 30 | 11/19 | -51.667 | [-236.667, +151.667] | 0.200 | TWO-SIDED: no difference (CI) | |

## 5. Attractor: does the split or the channel decide the language?

Similarity of two final languages = share of objects with identical messages after the best per-position symbol relabeling. Compared: same seed, different rewrite cells (split fixed, channel varies) vs same cell, different seeds (channel fixed, split varies).

- same seed, different channels: 0.090 (n=30)
- same channel, different seeds: 0.063 (n=135)
- generations (no transmission), different seeds: 0.055
- chance for a random pair of languages with this lexicon size ≈ 0.031

## 6. Convention drift inside a generation: share of objects whose message changed between consecutive evals (250 steps)

| cell | early (steps ≤ 1000) | late (> 1000) |
|---|---|---|
| pair (12k steps; early = first 1000 of 12k, late = last 6000) | 0.576 | 0.357 |
| generations, gen 5 | 0.637 | 0.395 |

## 7. Parent→child mutation rate vs change in structure

| cell | n transitions | mutation rate (share of 64 messages changed) | corr(mutation, Δtopsim) | corr(mutation, Δn_unique) |
|---|---|---|---|---|
| random+accumulate | 150 | 0.70 | -0.18 | -0.56 |
| random+rewrite | 150 | 0.55 | +0.11 | -0.31 |
| success+accumulate | 150 | 0.72 | -0.13 | -0.58 |
| success+rewrite | 150 | 0.58 | +0.07 | -0.25 |
| hard+accumulate | 150 | 0.54 | +0.07 | -0.31 |
| hard+rewrite | 150 | 0.51 | +0.16 | -0.42 |

## 8. Held-out accuracy vs number of TRAINING neighbours at Hamming distance 1 (0–9 possible)

| cell | 4 nb | 5 nb | 6 nb | 7 nb | 8 nb | 9 nb | corr |
|---|---|---|---|---|---|---|---|
| generations | 0.41 (18) | 0.51 (45) | 0.52 (109) | 0.65 (158) | 0.71 (113) | 0.78 (35) | +0.35 |
| pair | 0.22 (18) | 0.48 (45) | 0.45 (109) | 0.57 (158) | 0.61 (113) | 0.77 (35) | +0.37 |
| random+accumulate | 0.43 (18) | 0.50 (45) | 0.59 (109) | 0.60 (158) | 0.61 (113) | 0.68 (35) | +0.18 |
| random+rewrite | 0.49 (18) | 0.51 (45) | 0.53 (109) | 0.59 (158) | 0.69 (113) | 0.63 (35) | +0.21 |
| success+accumulate | 0.43 (18) | 0.44 (45) | 0.50 (109) | 0.56 (158) | 0.62 (113) | 0.62 (35) | +0.21 |
| success+rewrite | 0.41 (18) | 0.46 (45) | 0.53 (109) | 0.61 (158) | 0.67 (113) | 0.70 (35) | +0.30 |
| hard+accumulate | 0.44 (18) | 0.51 (45) | 0.56 (109) | 0.59 (158) | 0.67 (113) | 0.67 (35) | +0.27 |
| hard+rewrite | 0.31 (18) | 0.50 (45) | 0.59 (109) | 0.67 (158) | 0.71 (113) | 0.76 (35) | +0.40 |

## 9. Sender entropy vs structure (within-seed correlation across all cells, seeds 0–9)

- corr(entropy, topsim) = -0.08; corr(entropy, test_acc) = +0.13; corr(entropy, n_unique) = +0.66

## 10. Receiver pretraining (reader=both): effect at step 250 of generations ≥ 1 (seeds 0–9)

| metric | both | sender | paired | | | | |
|---|---|---|---|---|---|---|---|
| train_acc @250 | 0.899 | 0.889 | 10 | 8/2 | +0.010 | [+0.004, +0.016] | 0.109 | TWO-SIDED: A>B (CI) | |
| intelligibility @250 | 0.261 | 0.246 | 10 | 9/0 | +0.016 | [+0.009, +0.024] | 0.004 | TWO-SIDED: A>B (CI) | |
| topsim @250 | 0.304 | 0.317 | 10 | 1/9 | -0.013 | [-0.022, -0.003] | 0.021 | TWO-SIDED: A<B (CI) | |

## 11. Which held-out splits are hard? (30 seeds; mean over the 8 cells present in both sets)

- spread of seed-mean test_acc: 0.46 – 0.68 (sd 0.049)
- corr(seed-mean test_acc, mean # training neighbours of held-out objects) = +0.69
- corr(seed-mean test_acc, seed-mean topsim) = +0.15

