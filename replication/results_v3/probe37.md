# probe37 — stale anchors and the snapshot effect

## A. Zero-anchor untaught train objects by selection rule: n and retention, cap 8 vs cap 40 (seeds 0–9 + completed 10–29)

| select | cap 8: n, retention | cap 40: n, retention | cap 40: share of untaught objects that are zero-anchor |
|---|---|---|---|
| random | 4492, 0.153 | 132, 0.023 | 0.06 |
| success | 5064, 0.156 | 169, 0.030 | 0.08 |
| hard | 3682, 0.109 | 1, 0.000 | 0.00 |

## B. Stale forms in the child's final language (train objects): taught-stale (record form ≠ parent-final, child keeps it) and adopted-stale (untaught object takes a stale anchor's form). Structure gap accumulate − rewrite on all train objects vs excluding stale-holding objects (paired by seed, gens ≥ 1 averaged)

| select | taught-stale share | adopted-stale share | gap (acc − rew), all train | | | | | | gap excluding stale objects | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| random | 0.10 | 0.08 | 30 | 2/28 | -0.095 | [-0.115, -0.075] | 0.000 | TWO-SIDED: A<B (CI) | | 30 | 3/27 | -0.081 | [-0.103, -0.059] | 0.000 | TWO-SIDED: A<B (CI) |
| success | 0.10 | 0.08 | 30 | 3/27 | -0.095 | [-0.119, -0.072] | 0.000 | TWO-SIDED: A<B (CI) | | 30 | 5/25 | -0.076 | [-0.102, -0.052] | 0.000 | TWO-SIDED: A<B (CI) |
| hard | 0.02 | 0.02 | 30 | 9/21 | -0.024 | [-0.038, -0.009] | 0.043 | TWO-SIDED: A<B (CI) | | 30 | 8/22 | -0.024 | [-0.039, -0.008] | 0.016 | TWO-SIDED: A<B (CI) |

## C. Do stale adoptions create collisions? class size (train) of the adopting object at child end vs its class size in the parent; and vs untaught objects that kept the parent form

| select | adopters: parent class size → child class size | keepers: parent → child |
|---|---|---|
| random | 1.98 → 3.22 (n=611) | 2.96 → 3.03 (n=1085) |
| success | 2.24 → 3.95 (n=573) | 3.36 → 3.40 (n=949) |
| hard | 2.86 → 4.17 (n=126) | 3.35 → 3.72 (n=1553) |

## D. Age of a record entry (generations since the object first appeared in the record with this form) vs: its own fidelity in the child (child holds it at gen end), and its pull (untaught H1 neighbours adopting it), accumulate cells pooled

| age | entries | fresh (== parent final) | child holds it | untaught nbrs adopt it |
|---|---|---|---|---|
| 0 | 2770 | 0.63 | 0.72 | 0.119 |
| 1 | 1733 | 0.71 | 0.70 | 0.095 |
| 2 | 1490 | 0.71 | 0.69 | 0.088 |
| 3 | 1327 | 0.69 | 0.68 | 0.087 |
| 4 | 1230 | 0.68 | 0.70 | 0.102 |

## E. Across 74 record cells (seeds 0–9): corr(stale share of record, final topsim_distinct) = -0.47; corr(stale-holding share of child language, final topsim_distinct) = -0.48

