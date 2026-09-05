# probe25 — forced ownership break at the start of a generation (30 seeds, parent = end of gen 0, child taught the full language)

| arm | group (parent status) | n objs | change / 250 steps | owner-rate @250 | owner-rate @2000 | paired vs owners in same arm | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|
| control | owners | 33.7 | 0.075 | 0.80 | 0.88 | – |
| control | orphans | 30.3 | 0.153 | 0.17 | 0.25 | 30 | 26/4 | +0.078 | [+0.056, +0.100] | 0.000 | TWO-SIDED: A>B (CI) |
| control | orphans, TRAIN objects | 14.5 | 0.087 | 0.37 | 0.55 | 29 | 17/12 | +0.013 | [-0.005, +0.030] | 0.458 | TWO-SIDED: no difference (CI) |
| control | orphans, HELD-OUT objects | 15.8 | 0.214 | 0.03 | 0.03 | 30 | 26/4 | +0.139 | [+0.104, +0.173] | 0.000 | TWO-SIDED: A>B (CI) |
| emancipate | owners (untouched) | 33.7 | 0.040 | 0.89 | 0.97 | – |
| emancipate | ex-orphans, TRAIN | 14.5 | 0.046 | 0.88 | 0.97 | 29 | 14/15 | +0.006 | [-0.007, +0.020] | 1.000 | TWO-SIDED: no difference (CI) |
| emancipate | ex-orphans, HELD-OUT | 15.8 | 0.231 | 0.01 | 0.01 | 30 | 30/0 | +0.191 | [+0.166, +0.216] | 0.000 | TWO-SIDED: A>B (CI) |
| emancipate | ex-orphans (unique word) | 30.3 | 0.152 | 0.40 | 0.44 | 30 | 30/0 | +0.112 | [+0.092, +0.133] | 0.000 | TWO-SIDED: A>B (CI) |
| collide | owners (untouched) | 17.1 | 0.050 | 0.59 | 0.76 | – |
| collide | ex-owners (forced homonym) | 16.6 | 0.059 | 0.45 | 0.73 | 30 | 15/12 | +0.009 | [-0.003, +0.023] | 0.701 | TWO-SIDED: no difference (CI) |
| collide | orphans (untouched) | 30.3 | 0.155 | 0.19 | 0.22 | 30 | 30/0 | +0.105 | [+0.087, +0.123] | 0.000 | TWO-SIDED: A>B (CI) |

Same objects across arms (paired by seed):
- parent's orphans: emancipate − control | 30 | 13/17 | -0.001 | [-0.027, +0.026] | 0.585 | INCONCLUSIVE |
- parent's TRAIN orphans only: emancipate − control | 29 | 6/23 | -0.042 | [-0.059, -0.024] | 0.002 | INCONCLUSIVE |
- parent's owners chosen for collision: collide − control | 30 | 11/16 | -0.018 | [-0.038, +0.001] | 0.442 | INCONCLUSIVE |

By status at step 250 of the child (receiver's decode), pooled over arms:

| arm | owners @250 | orphans @250 |
|---|---|---|
| control | 0.076 | 0.150 |
| emancipate | 0.040 | 0.191 |
| collide | 0.044 | 0.130 |
