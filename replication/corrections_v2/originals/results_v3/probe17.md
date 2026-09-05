# probe17 — shared instability, permanent orphans, the record ratchet, robust intelligibility

Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## A. Is instability a property of the object? Per-object sender confidence: parent vs child (same lineage), and across different lineages of the same seed

| comparison | n pairs | mean corr of per-object confidence | share positive |
|---|---|---|---|
| parent → child, same lineage (6 record cells) | 900 | +0.26 | 0.92 |
| different lineages, same seed (3 rewrite channels, final senders) | 30 | +0.20 | 0.90 |
| independent generations, same seed (`generations`, no transmission) | 150 | +0.07 | 0.64 |

In `generations`, corr(confidence of a training object, its number of HELD-OUT neighbours) = +0.06 (negative in 0.35 of generations): objects next to the unseen region are the unstable ones.

## B. Permanent orphans: training objects that never own a word in any generation of a lineage

| cell | n | permanent orphans (of 48) | permanent owners | their training neighbours: perm. orphans | perm. owners | held-out neighbours: perm. orphans | perm. owners |
|---|---|---|---|---|---|---|---|
| generations | 30 | 0.1 | 5.3 | 7.00 | 6.83 | 2.00 | 2.17 |
| random+accumulate | 30 | 1.1 | 3.5 | 6.47 | 6.88 | 2.53 | 2.12 |
| random+rewrite | 30 | 1.2 | 6.4 | 6.43 | 6.79 | 2.57 | 2.21 |
| success+accumulate | 30 | 1.3 | 2.6 | 6.33 | 6.94 | 2.67 | 2.06 |
| success+rewrite | 30 | 1.8 | 2.6 | 6.47 | 7.13 | 2.53 | 1.87 |
| hard+accumulate | 30 | 3.3 | 1.4 | 6.35 | 6.95 | 2.65 | 2.05 |
| hard+rewrite | 30 | 2.4 | 1.7 | 6.25 | 6.80 | 2.75 | 2.20 |

## C. Does the parent's per-object ACCURACY predict the child's change, like confidence does?

| cell | acc of objects the child kept | changed | paired | | | | |
|---|---|---|---|---|---|---|---|
| random+accumulate | 0.897 | 0.849 | 30 | 28/2 | +0.047 | [+0.036, +0.058] | 0.000 | TWO-SIDED: A>B (CI) | |
| random+rewrite | 0.923 | 0.826 | 30 | 30/0 | +0.097 | [+0.086, +0.108] | 0.000 | TWO-SIDED: A>B (CI) | |
| success+accumulate | 0.873 | 0.842 | 30 | 25/5 | +0.031 | [+0.015, +0.044] | 0.000 | TWO-SIDED: A>B (CI) | |
| success+rewrite | 0.910 | 0.828 | 30 | 30/0 | +0.082 | [+0.074, +0.090] | 0.000 | TWO-SIDED: A>B (CI) | |
| hard+accumulate | 0.874 | 0.844 | 30 | 24/6 | +0.029 | [+0.017, +0.042] | 0.001 | TWO-SIDED: A>B (CI) | |
| hard+rewrite | 0.882 | 0.845 | 30 | 24/6 | +0.037 | [+0.024, +0.049] | 0.001 | TWO-SIDED: A>B (CI) | |

## D. Systematicity of the transmitted record itself: rule-consistency of the 19 pairs among themselves, by generation; and does it predict the child's structure?

| cell | rec after gen 0 | gen 1 | gen 2 | gen 3 | gen 4 | corr(record systematicity, child topsim_distinct) | corr with child owners |
|---|---|---|---|---|---|---|---|
| random+accumulate | 0.526 | 0.526 | 0.526 | 0.526 | 0.526 | +0.20 | -0.24 |
| random+rewrite | 0.595 | 0.605 | 0.614 | 0.619 | 0.623 | +0.29 | -0.14 |
| success+accumulate | 0.565 | 0.565 | 0.565 | 0.565 | 0.565 | +0.13 | -0.28 |
| success+rewrite | 0.641 | 0.661 | 0.674 | 0.661 | 0.673 | +0.19 | -0.18 |
| hard+accumulate | 0.601 | 0.601 | 0.604 | 0.612 | 0.607 | +0.26 | -0.00 |
| hard+rewrite | 0.601 | 0.604 | 0.609 | 0.627 | 0.623 | +0.39 | -0.02 |

(rule-consistency of 19 random (object, message) pairs with random messages ≈ 0.435)

## E. Robust intelligibility: the receiver decodes (over all 64) the sender's SAMPLED messages (50 per object) vs its greedy messages

| cell | n | greedy intelligibility | sampled | sampled messages that differ from greedy | of those, decoded correctly |
|---|---|---|---|---|---|
| generations | 30 | 0.57 | 0.51 | 0.36 | 0.36 |
| random+accumulate | 30 | 0.40 | 0.39 | 0.09 | 0.14 |
| random+rewrite | 30 | 0.45 | 0.44 | 0.09 | 0.18 |
| success+accumulate | 30 | 0.36 | 0.35 | 0.10 | 0.17 |
| success+rewrite | 30 | 0.31 | 0.30 | 0.05 | 0.12 |
| hard+accumulate | 30 | 0.26 | 0.25 | 0.06 | 0.11 |
| hard+rewrite | 30 | 0.27 | 0.27 | 0.05 | 0.12 |
| pair | 30 | 0.69 | 0.68 | 0.35 | 0.67 |

## F. Are fossils (form unchanged gen 0 → 5) owners?

| cell | fossils that are owners in gen 5 | owner share among non-fossils |
|---|---|---|
| random+accumulate | 0.44 | 0.40 |
| random+rewrite | 0.51 | 0.44 |
| success+accumulate | 0.33 | 0.36 |
| success+rewrite | 0.36 | 0.30 |
| hard+accumulate | 0.30 | 0.26 |
| hard+rewrite | 0.27 | 0.27 |

