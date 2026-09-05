# probe15 — matched corruption, hesitation → innovation, rule vs copy, entropy → drift

Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## A. One corrupted symbol, matched at the object level (random fixed slots, rewrite, seeds 0–9: noise 0.2 vs noise 0; same parent, same 19 slots)

| entry | n | child keeps the recorded form | child's final local fit | child owner |
|---|---|---|---|---|
| corrupted (noise cell) | 180 | 0.74 | 0.323 | 0.69 |
| same object, no-noise cell [matched to corrupted] | 180 | 0.83 | 0.404 | 0.68 |
| intact (noise cell) | 770 | 0.79 | 0.387 | 0.75 |
| same object, no-noise cell [matched to intact] | 770 | 0.81 | 0.434 | 0.71 |

Does the child keep a corruption more when it hits an UNINFORMATIVE position? (rank 0 = least informative position of the parent's language)

| position rank | n | kept |
|---|---|---|
| 0 | 55 | 0.67 |
| 1 | 65 | 0.78 |
| 2 | 60 | 0.75 |

## B. Does the parent's hesitation predict the child's innovation? (parent sender's p(greedy) per object vs whether the child changed that object's form)

| cell | n transitions | p(greedy) of objects the child KEPT | CHANGED | paired (kept − changed) | | | | | within-run corr(confidence, changed) |
|---|---|---|---|---|---|---|---|---|---|
| random+accumulate | 150 | 0.944 | 0.811 | 30 | 30/0 | +0.133 | [+0.121, +0.145] | 0.000 | TWO-SIDED: A>B (CI) | -0.21 |
| random+rewrite | 150 | 0.908 | 0.807 | 30 | 30/0 | +0.100 | [+0.092, +0.108] | 0.000 | TWO-SIDED: A>B (CI) | -0.24 |
| success+accumulate | 150 | 0.943 | 0.822 | 30 | 30/0 | +0.121 | [+0.111, +0.130] | 0.000 | TWO-SIDED: A>B (CI) | -0.17 |
| success+rewrite | 150 | 0.913 | 0.833 | 30 | 30/0 | +0.079 | [+0.069, +0.090] | 0.000 | TWO-SIDED: A>B (CI) | -0.18 |
| hard+accumulate | 150 | 0.926 | 0.832 | 30 | 30/0 | +0.094 | [+0.086, +0.103] | 0.000 | TWO-SIDED: A>B (CI) | -0.23 |
| hard+rewrite | 150 | 0.927 | 0.820 | 30 | 30/0 | +0.106 | [+0.099, +0.114] | 0.000 | TWO-SIDED: A>B (CI) | -0.25 |

## C. Does the child generalise the 19 taught pairs by RULE or by COPY? (untaught training objects)

rule = best position↔attribute-value matching fitted on the 19 taught pairs only; rule-consistency = share of predictable positions where the child's symbol matches; copy = share of untaught objects where the child's message equals the parent's. Also the parent's own rule-consistency on those objects (what a perfect copy would score).

| cell | n | rule-consistency: child | parent | child − parent | | | | | copy rate |
|---|---|---|---|---|---|---|---|---|---|
| random+accumulate | 30 | 0.381 | 0.356 | 30 | 29/0 | +0.026 | [+0.021, +0.031] | 0.000 | TWO-SIDED: A>B (CI) | 0.25 |
| random+rewrite | 30 | 0.431 | 0.418 | 30 | 24/5 | +0.013 | [+0.008, +0.018] | 0.001 | TWO-SIDED: A>B (CI) | 0.32 |
| success+accumulate | 30 | 0.354 | 0.328 | 30 | 28/1 | +0.026 | [+0.019, +0.033] | 0.000 | TWO-SIDED: A>B (CI) | 0.22 |
| success+rewrite | 30 | 0.452 | 0.422 | 30 | 27/3 | +0.029 | [+0.019, +0.040] | 0.000 | TWO-SIDED: A>B (CI) | 0.27 |
| hard+accumulate | 30 | 0.449 | 0.423 | 30 | 21/8 | +0.026 | [+0.013, +0.038] | 0.024 | TWO-SIDED: A>B (CI) | 0.36 |
| hard+rewrite | 30 | 0.460 | 0.434 | 30 | 28/2 | +0.026 | [+0.019, +0.035] | 0.000 | TWO-SIDED: A>B (CI) | 0.38 |

## D. Within `pair`: does the sender's entropy at eval t predict how many messages change by t+1?

- within-run corr(entropy_t, drift_t→t+1) = +0.67 (positive in 30/30 runs)
- entropy: first 2000 steps 0.64 nats → last 2000 steps 0.33; drift per 250 steps: 0.44 → 0.38

## E. When does a generation settle on which attribute to merge? Agreement of the drop axis at step t with the final drop axis (gens ≥ 1)

| cell | 250 | 500 | 1000 | 1500 |
|---|---|---|---|---|
| generations | 0.64 | 0.82 | 0.87 | 0.90 |
| random+accumulate | 0.77 | 0.78 | 0.84 | 0.89 |
| random+rewrite | 0.81 | 0.89 | 0.89 | 0.94 |
| success+accumulate | 0.72 | 0.77 | 0.87 | 0.89 |
| success+rewrite | 0.75 | 0.78 | 0.86 | 0.93 |
| hard+accumulate | 0.85 | 0.90 | 0.92 | 0.95 |
| hard+rewrite | 0.83 | 0.85 | 0.93 | 0.92 |

chance ≈ 0.33 (three attributes)

