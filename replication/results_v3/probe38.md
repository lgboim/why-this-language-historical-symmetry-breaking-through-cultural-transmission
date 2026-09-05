# probe38 — inside the record-content experiment

## A. Coverage per content rule and inheritance of UNTAUGHT train objects' parent forms

| arm | taught nbrs per untaught obj | share with ≥1 anchor | untaught inheritance | inheritance given ≥1 anchor | given 0 anchors |
|---|---|---|---|---|---|
| random19 | 2.66 | 0.96 | 0.193 | 0.198 | 0.083 |
| owners19 | 2.70 | 0.96 | 0.182 | 0.185 | 0.091 |
| orphans19 | 2.66 | 0.96 | 0.221 | 0.224 | 0.143 |
| classes19 | 2.33 | 0.91 | 0.059 | 0.062 | 0.026 |
| stable19 | 2.38 | 0.95 | 0.148 | 0.157 | 0.000 |

corr(coverage, untaught inheritance) across arms×seeds: +0.37; mean within-seed corr across the 5 arms: +0.48; within random19 across seeds: -0.02

## B. Held-out objects at child end: share whose form is held by ≥1 train object; of those, share whose form-class contains a train OWNER (owner-present); held-out accuracy proxy = test_acc

| arm | held-out sharing a train form | of those, owner-present | held-out with unique form | test_acc |
|---|---|---|---|---|
| random19 | 0.84 | 0.99 | 0.15 | 0.585 |
| owners19 | 0.82 | 0.99 | 0.15 | 0.546 |
| orphans19 | 0.84 | 0.98 | 0.13 | 0.591 |
| classes19 | 0.94 | 0.99 | 0.05 | 0.605 |
| stable19 | 0.88 | 0.99 | 0.11 | 0.591 |

## C. Whole classes: collisions in the child's final train language, and sender entropy at 250 vs number of taught homonym pairs

| arm | taught homonym pairs (mean) | train objs in collisions @2000 | #train classes size≥2 | mean class size | entropy @250 |
|---|---|---|---|---|---|
| random19 | 3.7 | 0.65 | 12.3 | 2.55 | 0.164 |
| owners19 | 0.0 | 0.55 | 11.6 | 2.27 | 0.168 |
| orphans19 | 6.4 | 0.70 | 12.9 | 2.63 | 0.153 |
| classes19 | 11.6 | 0.82 | 12.8 | 3.09 | 0.121 |
| stable19 | 8.5 | 0.72 | 13.0 | 2.65 | 0.148 |

corr(taught homonym pairs, entropy @250) across arms×seeds: -0.60

## D. What predicts test accuracy (arms × seeds, n=150): standardised linear regression

| predictor | std. coefficient | zero-order corr |
|---|---|---|
| n_owners | -0.001 | +0.05 |
| held-out borrowing | -0.013 | -0.13 |
| coverage | -0.013 | -0.17 |
| untaught inheritance | -0.007 | -0.16 |
