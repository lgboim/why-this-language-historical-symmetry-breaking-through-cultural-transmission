# probe14 — decoupling mechanism, first names, word ages, co-mutation, shared receiver

Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## A. Receiver reliance per message position (share of decodes that change when the symbol at that position is randomised)

| cell | n | reliance sorted high→low: 1st | 2nd | 3rd | ratio 1st/3rd | sender info sorted: 1st | 3rd | ratio |
|---|---|---|---|---|---|---|---|---|
| generations | 30 | 0.92 | 0.86 | 0.82 | 1.13 | 1.91 | 1.43 | 1.36 |
| random+accumulate | 30 | 0.88 | 0.83 | 0.78 | 1.13 | 1.89 | 1.56 | 1.21 |
| random+rewrite | 30 | 0.87 | 0.82 | 0.76 | 1.15 | 1.80 | 1.47 | 1.24 |
| success+accumulate | 30 | 0.89 | 0.84 | 0.78 | 1.15 | 1.87 | 1.46 | 1.31 |
| success+rewrite | 30 | 0.89 | 0.81 | 0.74 | 1.22 | 1.74 | 1.31 | 1.38 |
| hard+accumulate | 30 | 0.87 | 0.79 | 0.72 | 1.24 | 1.77 | 1.37 | 1.32 |
| hard+rewrite | 30 | 0.88 | 0.80 | 0.73 | 1.22 | 1.82 | 1.35 | 1.40 |
| pair | 30 | 0.94 | 0.87 | 0.81 | 1.15 | 1.87 | 1.32 | 1.45 |

## B. Who gets a name first? Owners at step 250 of a fresh generation (`generations`, all gens) vs the rest

| property | early owners | others | paired diff | | | | |
|---|---|---|---|---|---|---|---|
| training neighbours (Hamming 1) | 7.537 | 6.644 | 30 | 30/0 | +0.893 | [+0.823, +0.961] | 0.000 | TWO-SIDED: A>B (CI) | |
| held-out neighbours | 1.463 | 2.356 | 30 | 0/30 | -0.893 | [-0.961, -0.823] | 0.000 | TWO-SIDED: A<B (CI) | |
| per-object accuracy at gen end | 0.972 | 0.971 | 30 | 17/13 | +0.001 | [-0.003, +0.004] | 0.585 | TWO-SIDED: no difference (CI) | |
| owner at gen end | 0.688 | 0.688 | 30 | 12/18 | -0.000 | [-0.031, +0.032] | 0.362 | TWO-SIDED: no difference (CI) | |

## C. What the child's receiver learns first: decode correctness at step 250 (child generations), taught vs untaught training objects

| cell | taught | untaught | paired | | | | | at step 2000: taught | untaught |
|---|---|---|---|---|---|---|---|---|---|
| random+accumulate | 0.43 | 0.25 | 30 | 29/1 | +0.179 | [+0.147, +0.209] | 0.000 | TWO-SIDED: A>B (CI) | 0.57 | 0.53 |
| random+rewrite | 0.55 | 0.31 | 30 | 30/0 | +0.243 | [+0.208, +0.280] | 0.000 | TWO-SIDED: A>B (CI) | 0.64 | 0.60 |
| success+accumulate | 0.37 | 0.19 | 30 | 28/2 | +0.179 | [+0.141, +0.217] | 0.000 | TWO-SIDED: A>B (CI) | 0.50 | 0.49 |
| success+rewrite | 0.44 | 0.24 | 30 | 30/0 | +0.199 | [+0.172, +0.226] | 0.000 | TWO-SIDED: A>B (CI) | 0.53 | 0.48 |
| hard+accumulate | 0.30 | 0.26 | 30 | 19/11 | +0.045 | [+0.012, +0.080] | 0.200 | TWO-SIDED: A>B (CI) | 0.38 | 0.45 |
| hard+rewrite | 0.31 | 0.26 | 30 | 22/8 | +0.050 | [+0.020, +0.079] | 0.016 | TWO-SIDED: A>B (CI) | 0.39 | 0.47 |

## D. Age of the words in generation 5: in which generation was each object's final form born? and fit by age

| cell | born gen 0 | 1 | 2 | 3 | 4 | 5 | fit: born ≤2 | born ≥4 | paired (old − new) | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| random+accumulate | 0.01 | 0.12 | 0.04 | 0.07 | 0.13 | 0.62 | 0.304 | 0.305 | 30 | 16/14 | -0.002 | [-0.025, +0.023] | 0.856 | TWO-SIDED: no difference (CI) | |
| random+rewrite | 0.15 | 0.04 | 0.06 | 0.08 | 0.15 | 0.52 | 0.419 | 0.339 | 30 | 29/1 | +0.080 | [+0.064, +0.096] | 0.000 | TWO-SIDED: A>B (CI) | |
| success+accumulate | 0.01 | 0.10 | 0.03 | 0.05 | 0.13 | 0.68 | 0.361 | 0.301 | 30 | 25/5 | +0.061 | [+0.034, +0.088] | 0.000 | TWO-SIDED: A>B (CI) | |
| success+rewrite | 0.04 | 0.03 | 0.07 | 0.11 | 0.23 | 0.53 | 0.480 | 0.370 | 30 | 27/3 | +0.110 | [+0.084, +0.133] | 0.000 | TWO-SIDED: A>B (CI) | |
| hard+accumulate | 0.08 | 0.05 | 0.08 | 0.11 | 0.18 | 0.51 | 0.422 | 0.364 | 30 | 24/6 | +0.057 | [+0.037, +0.078] | 0.001 | TWO-SIDED: A>B (CI) | |
| hard+rewrite | 0.08 | 0.06 | 0.08 | 0.13 | 0.22 | 0.44 | 0.437 | 0.387 | 30 | 25/5 | +0.050 | [+0.029, +0.071] | 0.000 | TWO-SIDED: A>B (CI) | |

born = earliest generation from which the form has been carried unchanged into generation 5.

## E. Co-mutation: when an owner changes its form between consecutive evals, does its orphan follow to the same new form?

| cell | owner-change events with an orphan | orphan adopts the owner's NEW form | orphan keeps the OLD form (becomes owner of it) | orphan goes elsewhere |
|---|---|---|---|---|
| generations | 5559 | 0.27 | 0.27 | 0.46 |
| random+accumulate | 1179 | 0.23 | 0.64 | 0.13 |
| random+rewrite | 1082 | 0.27 | 0.62 | 0.11 |
| success+accumulate | 1347 | 0.27 | 0.62 | 0.11 |
| success+rewrite | 1202 | 0.33 | 0.56 | 0.11 |
| hard+accumulate | 1214 | 0.38 | 0.53 | 0.09 |
| hard+rewrite | 1313 | 0.36 | 0.55 | 0.09 |
| pair | 1605 | 0.29 | 0.34 | 0.38 |

## F. A receiver shared by four senders (`population`, receiver 0 with sender 0) vs a private one (`pair`)

| cell | n | #owners | intelligibility | topsim | topsim_distinct | test_acc | train_acc |
|---|---|---|---|---|---|---|---|
| population | 10 | 39.2 | 0.61 | 0.322 | 0.307 | 0.578 | 0.982 |
| pair | 30 | 44.2 | 0.69 | 0.285 | 0.275 | 0.542 | 0.993 |
| generations | 30 | 36.5 | 0.57 | 0.340 | 0.321 | 0.616 | 0.978 |

