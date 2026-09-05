# Robustness battery (30 seeds, 10 focus cells)

Cells: mean [bootstrap 95% CI] share of seeds in the expected direction. LOCO = leave-one-cell-out minimum share.

| claim | sign | variant 1 | variant 2 | variant 3 | variant 4 |
|---|---|---|---|---|---|
| 1 rewrite − accumulate, distinct, random slots | + | +0.077 [+0.049,+0.103] 0.87 | +0.105 [+0.073,+0.137] 0.90 | +0.085 [+0.057,+0.114] 0.83 | +0.116 [+0.084,+0.147] 0.90 |
| 1 rewrite − accumulate, distinct, success slots | + | +0.072 [+0.040,+0.105] 0.77 | +0.085 [+0.048,+0.120] 0.70 | +0.083 [+0.044,+0.119] 0.80 | +0.093 [+0.051,+0.133] 0.80 |
| 1 rewrite − accumulate, distinct, hard slots | + | +0.035 [+0.004,+0.065] 0.77 | +0.045 [+0.010,+0.077] 0.80 | +0.033 [+0.004,+0.061] 0.63 | +0.043 [+0.011,+0.075] 0.73 |
| 1 rewrite − accumulate, CBM, random slots | + | +0.049 [+0.036,+0.062] 0.93 | +0.056 [+0.042,+0.069] 0.90 | +0.054 [+0.040,+0.069] 0.90 | +0.057 [+0.043,+0.070] 0.93 |
| 1 rewrite − accumulate, CBM, success slots | + | +0.053 [+0.039,+0.068] 0.93 | +0.063 [+0.047,+0.081] 0.87 | +0.048 [+0.035,+0.060] 0.90 | +0.058 [+0.042,+0.074] 0.87 |
| 1 rewrite − accumulate, CBM, hard slots | + | +0.019 [+0.005,+0.032] 0.63 | +0.014 [+0.001,+0.028] 0.57 | +0.018 [+0.006,+0.029] 0.67 | +0.011 [-0.002,+0.025] 0.57 |
| 1.4 changed inherited forms: fit(new) − fit(inherited) | + | +0.066 [+0.059,+0.073] 1.00 | +0.064 [+0.055,+0.072] 1.00 | +0.079 [+0.073,+0.086] 1.00 | +0.080 [+0.072,+0.088] 1.00 |
| 3.4 P(owner|parent owner) − P(owner|parent orphan) | + | +0.111 [+0.098,+0.125] 1.00 | +0.116 [+0.105,+0.127] 1.00 | +0.128 [+0.109,+0.146] 0.97 | +0.095 [+0.079,+0.111] 1.00 |
| 3.5 mutation: owners − orphans | + | +0.140 [+0.129,+0.150] 1.00 | +0.024 [+0.014,+0.033] 0.70 | +0.131 [+0.117,+0.145] 1.00 | +0.149 [+0.137,+0.161] 1.00 |
| 4.1 held-out borrows a Hamming-1 neighbour's word (share − 0.14) | + | +0.659 [+0.632,+0.685] 1.00 | +0.688 [+0.666,+0.710] 1.00 | +0.514 [+0.438,+0.590] 1.00 | +0.326 [+0.255,+0.398] 0.93 |
| 4.5 corr(held-out acc, training neighbours) | + | +0.242 [+0.197,+0.289] 0.97 | +0.260 [+0.156,+0.362] 0.77 | +0.352 [+0.259,+0.440] 0.93 | – |
| 5.3 role stability − word persistence (parent→child) | + | +0.278 [+0.249,+0.307] 1.00 | +0.232 [+0.201,+0.262] 1.00 | +0.257 [+0.228,+0.285] 1.00 | +0.019 [-0.071,+0.113] 0.47 |
| 6.2 fit of fossils − non-fossils | + | +0.067 [+0.053,+0.083] 0.97 | +0.067 [+0.053,+0.081] 1.00 | +0.075 [+0.055,+0.094] 0.90 | – |
| 3.10 convexity − random | + | +0.744 [+0.712,+0.775] 1.00 | +0.760 [+0.731,+0.790] 1.00 | +0.732 [+0.709,+0.754] 1.00 | +0.769 [+0.748,+0.791] 1.00 |
| 6.1 corr(entropy, drift) in pair | + | +0.667 [+0.622,+0.711] 1.00 | +0.820 [+0.768,+0.865] 1.00 | +0.296 [+0.224,+0.366] 0.93 | – |

Variant labels per row, in order: see the source (`robust.py`): freshness rows = (2000,all), (2000,train), (1000,all), (1000,train); regularisation = (spearman,2000), (spearman,1000), (pearson,2000), (pearson,1000); ownership inheritance = (2000), (child@1000), (rewrite), (accumulate); mutation asymmetry = (train), (all), (rewrite), (accumulate); borrowing = (2000), (1000), (generations), (pair); support = (record), (generations), (pair); grammar>words = (all), (train), (child@1000), (generations); fossils = (spearman,rewrite), (pearson,rewrite), (accumulate); convexity = (≥3), (≥4), (≥2), (1000); drift = (all), (first 4k), (last 6k).

## Leave-one-cell-out (minimum share of seeds in the expected direction when any one of the 6 record cells is dropped)

| claim | LOCO min share |
|---|---|
| 1.4 regularisation | min 1.00 |
| 3.4 ownership inheritance | min 1.00 |
| 3.5 owners mutate more | min 1.00 |
| 4.1 borrowing | min 1.00 |
| 5.3 grammar > words | min 1.00 |
| 3.10 convexity | min 1.00 |

