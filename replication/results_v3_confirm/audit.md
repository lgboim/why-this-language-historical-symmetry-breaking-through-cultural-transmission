# Replication audit — discovery seeds (0–9) vs confirmation seeds (10–29), 10 focus cells

Each row: a claim's per-seed statistic. sign = expected sign. For '+'/'−' claims the bar is ≥ 80% of seeds in the expected direction in BOTH sets; for 'high'/'low'/'0' claims the two sets must agree in level. mean (n; share in expected direction).

| claim | sign | discovery | confirm | verdict |
|---|---|---|---|---|
| 1 rewrite − accumulate (random slots), topsim | + | +0.050 (n=10; 0.70) | +0.065 (n=20; 0.90) | CONFIRM ONLY |
| 1 rewrite − accumulate (success slots), topsim | + | +0.085 (n=10; 1.00) | +0.071 (n=20; 0.85) | REPLICATES |
| 1 rewrite − accumulate (random slots), distinct | + | +0.078 (n=10; 0.80) | +0.076 (n=20; 0.90) | REPLICATES |
| 1 rewrite − accumulate (success slots), distinct | + | +0.092 (n=10; 0.90) | +0.062 (n=20; 0.70) | DISCOVERY ONLY |
| 1 rewrite − accumulate (random slots), CBM | + | +0.035 (n=10; 0.90) | +0.055 (n=20; 0.95) | REPLICATES |
| 1 rewrite − accumulate (success slots), CBM | + | +0.044 (n=10; 1.00) | +0.058 (n=20; 0.90) | REPLICATES |
| 1 rewrite − accumulate (random slots), owners_topsim | + | +0.087 (n=10; 0.70) | +0.085 (n=20; 0.75) | WEAK IN BOTH |
| 1 rewrite − accumulate (success slots), owners_topsim | + | +0.119 (n=10; 0.90) | +0.093 (n=20; 0.85) | REPLICATES |
| 1 rewrite − accumulate (random slots), intelligibility | + | +0.092 (n=10; 0.80) | +0.032 (n=20; 0.50) | DISCOVERY ONLY |
| 1 rewrite − accumulate (success slots), intelligibility | + | -0.075 (n=10; 0.40) | -0.047 (n=20; 0.35) | WEAK IN BOTH |
| 1 rewrite − accumulate (random slots), n_unique | ? | 6.800 (n=10; sd 7.997) | 2.300 (n=20; sd 9.482) | LEVEL DIFFERS |
| 1 rewrite − accumulate (success slots), n_unique | ? | -5.800 (n=10; sd 9.185) | -3.500 (n=20; sd 7.852) | LEVEL DIFFERS |
| 1.6 hard: rewrite − accumulate, topsim (expected ≈ 0) | 0 | 0.043 (n=10; sd 0.060) | 0.008 (n=20; sd 0.057) | REPLICATES (≈0) |
| 1.2 accumulate record: share of entries stale (≠ parent's final form) after gen 0 | high | 0.929 (n=10; sd 0.058) | 0.893 (n=20; sd 0.080) | REPLICATES (level) |
| 1.2 accumulate record: share carved at step ≤ 500 of gen 0 | high | 0.962 (n=10; sd 0.051) | 0.909 (n=20; sd 0.092) | REPLICATES (level) |
| 1.3 same object, same parent, gen 0→1: fit via rewrite − fit via accumulate (random slots) | + | +0.119 (n=10; 1.00) | +0.070 (n=20; 0.85) | REPLICATES |
| 1.4 changed inherited forms: fit(new) − fit(inherited) (all record cells) | + | +0.064 (n=10; 1.00) | +0.067 (n=20; 1.00) | REPLICATES |
| 1.4 parent confidence: kept − changed objects | + | +0.115 (n=10; 1.00) | +0.101 (n=20; 1.00) | REPLICATES |
| 1.4 mutation rate gen1 − gen5 (rewrite cells; lineage settles) | + | +0.107 (n=10; 1.00) | +0.157 (n=20; 1.00) | REPLICATES |
| 1.4 mutation rate gen1 − gen5 (accumulate cells; expected ≈ 0) | 0 | 0.237 (n=10; sd 0.061) | 0.246 (n=20; sd 0.063) | NON-ZERO IN CONFIRM |
| 1.7 record self-consistency gen4 − gen0 (rewrite) | + | +0.029 (n=10; 0.90) | +0.027 (n=20; 0.80) | REPLICATES |
| 1.7 symbol inventory gen0 − gen5 (success/hard rewrite; inventory shrinks) | + | +1.150 (n=10; 1.00) | +1.067 (n=20; 0.90) | REPLICATES |
| 1.7 steps to 90% train acc: generations − rewrite children | + | +415.000 (n=10; 0.90) | +412.500 (n=20; 0.95) | REPLICATES |
| 2.1 rewrite cells − generations, distinct (expected ≈ 0 or small) | ? | -0.010 (n=10; sd 0.041) | -0.017 (n=20; sd 0.068) | REPLICATES (level) |
| 2.1 accumulate cells − generations, distinct | - | -0.087 (n=10; 1.00) | -0.071 (n=20; 0.95) | REPLICATES |
| 2.1 rewrite cells − generations, CBM (expected ≈ 0 or small) | ? | 0.046 (n=10; sd 0.055) | 0.061 (n=20; sd 0.041) | REPLICATES (level) |
| 2.1 accumulate cells − generations, CBM | - | +0.011 (n=10; 0.40) | +0.018 (n=20; 0.30) | WEAK IN BOTH |
| 2.5 pair: topsim step 12000 − 1000 | - | -0.051 (n=10; 0.90) | -0.062 (n=20; 0.95) | REPLICATES |
| 2.5 pair: topsim_distinct step 12000 − 1000 (small) | ? | -0.010 (n=10; sd 0.051) | -0.028 (n=20; sd 0.045) | REPLICATES (level) |
| 2.5 pair: n_owners step 12000 − 1000 | + | +23.700 (n=10; 1.00) | +22.300 (n=20; 1.00) | REPLICATES |
| 2.1 generations − pair, topsim_distinct | + | +0.048 (n=10; 0.80) | +0.045 (n=20; 0.85) | REPLICATES |
| 2.6 drop-axis at step 500 = final (gens ≥ 1, record cells) | high | 0.787 (n=10; sd 0.109) | 0.847 (n=20; sd 0.076) | REPLICATES (level) |
| 3.2 corr(n_owners, n_unique) across cells within seed | + | +0.988 (n=10; 1.00) | +0.986 (n=20; 1.00) | REPLICATES |
| 3.3 owner is the most central member (share − chance), classes ≥ 3 | + | +0.107 (n=10; 0.90) | +0.114 (n=20; 0.90) | REPLICATES |
| 3.4 P(child owner | parent owner) − P(child owner | parent orphan) | + | +0.124 (n=10; 1.00) | +0.105 (n=20; 1.00) | REPLICATES |
| 3.4 orphan keeps the same patron across generations (share − chance) | + | +0.326 (n=10; 1.00) | +0.327 (n=20; 1.00) | REPLICATES |
| 3.5 mutation rate: parent owners − parent orphans | + | +0.139 (n=10; 1.00) | +0.141 (n=20; 1.00) | REPLICATES |
| 3.6 owner leaves its word: orphan keeps the old form (share) | high | 0.615 (n=10; sd 0.074) | 0.592 (n=20; sd 0.046) | REPLICATES (level) |
| 3.7 hard slots that are orphans − base orphan share | + | +0.408 (n=10; 1.00) | +0.398 (n=20; 1.00) | REPLICATES |
| 3.8 sender confidence: orphans − owners | + | +0.037 (n=10; 1.00) | +0.018 (n=20; 0.95) | REPLICATES |
| 3.8 corr(sender confidence, local fit) within run | + | +0.173 (n=10; 1.00) | +0.181 (n=20; 1.00) | REPLICATES |
| 3.9 early owners (step 250) have more training neighbours (diff) | + | +0.827 (n=10; 1.00) | +0.925 (n=20; 1.00) | REPLICATES |
| 3.10 convexity: connected classes (size ≥ 3) − random sets | + | +0.741 (n=10; 1.00) | +0.746 (n=20; 1.00) | REPLICATES |
| 4.1 absorbed held-out objects using a Hamming-1 neighbour's word (share − 0.14) | + | +0.635 (n=10; 1.00) | +0.671 (n=20; 1.00) | REPLICATES |
| 4.1 sender confidence: train − held-out objects | + | +0.140 (n=10; 1.00) | +0.129 (n=20; 1.00) | REPLICATES |
| 4.2 held-out acc: absorber absent − absorber present (weights; 60 trials each) | + | +0.736 (n=10; 1.00) | +0.726 (n=20; 1.00) | REPLICATES |
| 4.2 held-out objects never the receiver's argmax over 64 (share decoded correctly; expected ≈ 0) | low | 0.010 (n=10; sd 0.008) | 0.007 (n=20; sd 0.012) | REPLICATES (level) |
| 4.3 train errors with a same-word candidate present (share; weights, 2000 trials) | high | 0.979 (n=10; sd 0.020) | 0.986 (n=20; sd 0.009) | REPLICATES (level) |
| 4.4 rule fitted on train: consistency train − held-out | + | +0.157 (n=10; 1.00) | +0.156 (n=20; 1.00) | REPLICATES |
| 4.4 fresh receiver test_acc − co-adapted test_acc (expected ≈ 0) | 0 | -0.006 (n=10; sd 0.030) | 0.011 (n=20; sd 0.020) | REPLICATES (≈0) |
| 4.5 corr(held-out object acc, # training neighbours) | + | +0.237 (n=10; 1.00) | +0.248 (n=20; 1.00) | REPLICATES |
| 4.6 held-out word conserved: absorber taught − absorber untaught | + | +0.251 (n=10; 1.00) | +0.277 (n=20; 1.00) | REPLICATES |
| 4.6 child − parent rule-consistency on untaught objects (rule from 19 taught pairs) | + | +0.028 (n=10; 1.00) | +0.023 (n=20; 1.00) | REPLICATES |
| 5.1 founder intelligibility: rewrite cells (weights) | high | 0.589 (n=10; sd 0.063) | 0.604 (n=20; sd 0.049) | REPLICATES (level) |
| 5.1 founder intelligibility: rewrite − accumulate | + | +0.205 (n=10; 1.00) | +0.173 (n=20; 1.00) | REPLICATES |
| 5.1 founder intelligibility: generations (expected ≈ chance 0.2) | low | 0.196 (n=10; sd 0.058) | 0.239 (n=20; sd 0.070) | LEVEL DIFFERS |
| 5.3 role stability parent→child (record cells) − role stability of independent generations | + | +0.714 (n=10; 1.00) | +0.622 (n=20; 1.00) | REPLICATES |
| 5.3 role stability − word persistence (parent→child, record cells) | + | +0.259 (n=10; 1.00) | +0.287 (n=20; 1.00) | REPLICATES |
| 5.3 parent's receiver decodes child's MUTATED messages correctly (share) | high | 0.692 (n=10; sd 0.049) | 0.667 (n=20; sd 0.054) | REPLICATES (level) |
| 5.4 drop-axis inherited (share of transitions) − no-transmission baseline | + | +0.333 (n=10; 0.80) | +0.393 (n=20; 0.95) | REPLICATES |
| 5.5 parent–child agreement of receiver decode maps (record cells) − generations | + | +0.289 (n=10; 1.00) | +0.269 (n=20; 1.00) | REPLICATES |
| 5.5 corr(parent confidence, child confidence) per object (record cells) − independent generations | + | +0.176 (n=10; 1.00) | +0.213 (n=20; 1.00) | REPLICATES |
| 5.6 receiver decode correct at step 250: taught − untaught (child gens) | + | +0.222 (n=10; 1.00) | +0.189 (n=20; 1.00) | REPLICATES |
| 6.1 drift per 250 steps late in pair (steps > 6000) | high | 0.377 (n=10; sd 0.048) | 0.347 (n=20; sd 0.085) | REPLICATES (level) |
| 6.1 corr(entropy_t, drift_t→t+1) within pair | + | +0.618 (n=10; 1.00) | +0.692 (n=20; 1.00) | REPLICATES |
| 6.2 fossils (form kept gen0→5) − expected under independent mutation (random+rewrite) | + | +11.867 (n=10; 1.00) | +15.453 (n=20; 1.00) | REPLICATES |
| 6.2 class size of fossil words − non-fossil words | + | +0.986 (n=10; 0.90) | +0.585 (n=20; 0.80) | REPLICATES |
| 6.2 fit of fossils − fit of non-fossils | + | +0.067 (n=10; 1.00) | +0.067 (n=20; 0.95) | REPLICATES |
| 6.3 semantic drift: Jaccard(old, new extension) of forms present in both gen 0 and gen 5 (low) | low | 0.163 (n=10; sd 0.023) | 0.178 (n=20; sd 0.032) | REPLICATES (level) |
| 6.3 drift locality: disjoint new extension adjacent to old − random (consecutive gens) | + | +0.343 (n=10; 1.00) | +0.298 (n=20; 1.00) | REPLICATES |
| 6.4 sound-change concentration − shuffled baseline (expected ≈ 0) | 0 | 0.045 (n=10; sd 0.007) | 0.047 (n=20; sd 0.012) | NON-ZERO IN CONFIRM |
| 6.5 receiver tolerance of variants: gen 0 − gen 5 (record cells) | + | +0.201 (n=10; 1.00) | +0.197 (n=20; 0.95) | REPLICATES |
| 6.7 new forms owned − inherited forms owned (share) | + | +0.165 (n=10; 1.00) | +0.148 (n=20; 1.00) | REPLICATES |
| 6.6 rich-get-richer: P(grow | size ≥ 4) − P(grow | size 1) (expected ≤ 0) | - | -0.050 (n=10; 0.80) | -0.051 (n=20; 0.85) | REPLICATES |
| 6.6 symbol inventory: accumulate − rewrite at gen 5 (success/hard) | + | +0.817 (n=10; 0.80) | +0.767 (n=20; 0.90) | REPLICATES |

## Summary

- CONFIRM: 1
- REPLICATES: 64
- DISCOVERY: 2
- WEAK: 3
- LEVEL: 3
- NON-ZERO: 2
