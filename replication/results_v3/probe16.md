# probe16 — confidence as regularity, rule violation, held-out systematicity, matched object-level comparisons

Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## A. Is the sender's confidence an internal regularity index? within-run corr(p(greedy) of object, local fit of its form), final generation

| cell | n | mean within-run corr | runs with corr > 0 | corr with class size (frequency) | partial corr with fit given class size |
|---|---|---|---|---|---|
| generations | 30 | +0.29 | 0.90 | +0.30 | +0.26 |
| random+accumulate | 30 | +0.12 | 0.80 | +0.14 | +0.11 |
| random+rewrite | 30 | +0.21 | 0.97 | +0.13 | +0.23 |
| success+accumulate | 30 | +0.18 | 0.90 | +0.24 | +0.17 |
| success+rewrite | 30 | +0.19 | 0.83 | +0.17 | +0.21 |
| hard+accumulate | 30 | +0.14 | 0.83 | +0.17 | +0.16 |
| hard+rewrite | 30 | +0.13 | 0.77 | +0.20 | +0.17 |
| pair | 30 | +0.29 | 1.00 | +0.31 | +0.27 |

## B. Does the child change the inherited forms that violate the rule of the 19 taught pairs?

| cell | taught forms | share violating (≥ half of predictable positions) | P(child changes | violating) | P(changes | consistent) | paired | | | | |
|---|---|---|---|---|---|---|---|---|---|
| random+accumulate | 2850 | 0.44 | 0.31 | 0.31 | 30 | 16/14 | -0.007 | [-0.051, +0.037] | 0.856 | TWO-SIDED: no difference (CI) | |
| random+rewrite | 2850 | 0.30 | 0.16 | 0.17 | 30 | 13/17 | -0.013 | [-0.039, +0.013] | 0.585 | TWO-SIDED: no difference (CI) | |
| success+accumulate | 2850 | 0.36 | 0.39 | 0.35 | 30 | 18/12 | +0.037 | [-0.014, +0.089] | 0.362 | TWO-SIDED: no difference (CI) | |
| success+rewrite | 2850 | 0.21 | 0.25 | 0.18 | 30 | 20/10 | +0.068 | [+0.028, +0.108] | 0.099 | TWO-SIDED: A>B (CI) | |
| hard+accumulate | 2850 | 0.30 | 0.23 | 0.22 | 30 | 16/14 | +0.013 | [-0.018, +0.044] | 0.856 | TWO-SIDED: no difference (CI) | |
| hard+rewrite | 2850 | 0.28 | 0.23 | 0.19 | 30 | 21/9 | +0.042 | [+0.013, +0.071] | 0.043 | TWO-SIDED: A>B (CI) | |

## C. Child vs parent rule-consistency (rule from the 19 taught pairs) on HELD-OUT objects

| cell | n | child | parent | child − parent | | | | |
|---|---|---|---|---|---|---|---|---|
| random+accumulate | 30 | 0.338 | 0.314 | 30 | 29/1 | +0.024 | [+0.019, +0.029] | 0.000 | TWO-SIDED: A>B (CI) | |
| random+rewrite | 30 | 0.362 | 0.353 | 30 | 19/10 | +0.009 | [+0.001, +0.017] | 0.136 | TWO-SIDED: A>B (CI) | |
| success+accumulate | 30 | 0.344 | 0.318 | 30 | 27/2 | +0.026 | [+0.018, +0.034] | 0.000 | TWO-SIDED: A>B (CI) | |
| success+rewrite | 30 | 0.411 | 0.385 | 30 | 22/8 | +0.026 | [+0.014, +0.038] | 0.016 | TWO-SIDED: A>B (CI) | |
| hard+accumulate | 30 | 0.417 | 0.393 | 30 | 23/7 | +0.025 | [+0.015, +0.035] | 0.005 | TWO-SIDED: A>B (CI) | |
| hard+rewrite | 30 | 0.419 | 0.404 | 30 | 20/10 | +0.015 | [+0.005, +0.025] | 0.099 | TWO-SIDED: A>B (CI) | |

## D. Company effect (gen 0→1, identical parent): objects taught in BOTH hard+rewrite and random+rewrite with the same form

| n objects | fidelity: hard cell | random cell | fit: hard | random | owner: hard | random |
|---|---|---|---|---|---|---|
| 214 | 0.80 | 0.78 | 0.398 | 0.393 | 0.49 | 0.59 |

## E. Reader matched at the object level (random fixed slots, rewrite, seeds 0–9; same parent, same slots): reader=both vs reader=sender

| quantity | both | sender | paired | | | | |
|---|---|---|---|---|---|---|---|
| fidelity on taught | 0.878 | 0.816 | 10 | 7/3 | +0.062 | [+0.013, +0.116] | 0.344 | TWO-SIDED: A>B (CI) | |
| fit on taught | 0.421 | 0.428 | 10 | 4/6 | -0.007 | [-0.020, +0.005] | 0.754 | TWO-SIDED: no difference (CI) | |
| owner share on taught | 0.691 | 0.708 | 10 | 4/6 | -0.018 | [-0.068, +0.027] | 0.754 | TWO-SIDED: no difference (CI) | |
| fit on untaught train | 0.365 | 0.375 | 10 | 3/7 | -0.010 | [-0.022, +0.002] | 0.344 | TWO-SIDED: no difference (CI) | |
| decode correct on taught @250 | 0.739 | 0.620 | 10 | 9/1 | +0.119 | [+0.077, +0.160] | 0.021 | TWO-SIDED: A>B (CI) | |

## F. Noise spillover to UNTAUGHT objects (random fixed slots, rewrite, seeds 0–9; noise 0.2 vs 0, same parent, same slots)

| quantity | noise 0.2 | noise 0 | paired | | | | |
|---|---|---|---|---|---|---|---|
| fit of untaught train objects | 0.359 | 0.375 | 10 | 3/7 | -0.016 | [-0.031, +0.000] | 0.344 | TWO-SIDED: no difference (CI) | |
| fit of held-out objects | 0.277 | 0.291 | 10 | 3/7 | -0.014 | [-0.031, +0.005] | 0.344 | TWO-SIDED: no difference (CI) | |
| parent–child agreement on untaught | 0.192 | 0.290 | 10 | 1/8 | -0.098 | [-0.145, -0.048] | 0.039 | TWO-SIDED: A<B (CI) | |
| owners among untaught | 0.684 | 0.635 | 10 | 7/3 | +0.049 | [-0.001, +0.099] | 0.344 | TWO-SIDED: no difference (CI) | |

