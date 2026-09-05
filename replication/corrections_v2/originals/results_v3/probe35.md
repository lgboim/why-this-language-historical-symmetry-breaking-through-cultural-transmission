# probe35 — robustness of coordination-by-anchoring

## A. Share of train forms that are 'derivable' under alternative definitions (final languages, gens ≥ 1, 6 focus cells pooled, 30 seeds); chance = same statistic after permuting forms across train objects within the language

| definition | observed | permutation chance |
|---|---|---|
| H1 neighbour, exact form | 0.719 | 0.222 |
| H1 neighbour, ≤1 symbol (used) | 0.976 | 0.682 |
| H≤2 neighbour, exact | 0.760 | 0.587 |
| H≤2 neighbour, ≤1 symbol | 0.994 | 0.971 |

## B. Anchoring gradient (retention by #taught neighbours) under variants

| variant | 0 | 1 | 2 | 3+ | monotone |
|---|---|---|---|---|---|
| baseline: exact form, gen end, all | 0.104 | 0.243 | 0.293 | 0.392 | yes |
| outcome ≤1 symbol | 0.346 | 0.536 | 0.603 | 0.686 | yes |
| child step 250 | 0.106 | 0.256 | 0.305 | 0.418 | yes |
| gen 1 only | 0.028 | 0.111 | 0.168 | 0.249 | yes |
| gens 2-5 | 0.172 | 0.267 | 0.314 | 0.423 | yes |
| seeds 0-9 | 0.094 | 0.239 | 0.272 | 0.357 | yes |
| seeds 10-29 | 0.108 | 0.246 | 0.303 | 0.411 | yes |
| LOCO without random+accumulate | 0.113 | 0.237 | 0.292 | 0.395 | yes |
| LOCO without random+rewrite | 0.098 | 0.239 | 0.291 | 0.407 | yes |
| LOCO without success+accumulate | 0.103 | 0.241 | 0.295 | 0.397 | yes |
| LOCO without success+rewrite | 0.105 | 0.254 | 0.306 | 0.405 | yes |
| LOCO without hard+accumulate | 0.102 | 0.245 | 0.288 | 0.377 | yes |
| LOCO without hard+rewrite | 0.104 | 0.243 | 0.284 | 0.372 | yes |

## C. Anchored choice (repeat parent's choice: source taught vs untaught vs chance) under variants

| variant | taught source | untaught source | chance | n taught / untaught |
|---|---|---|---|---|
| baseline | 0.58 | 0.19 | 0.19 | 8436 / 7667 |
| child step 250 | 0.70 | 0.17 | 0.19 | 8436 / 7667 |
| gen 1 only | 0.54 | 0.07 | 0.18 | 782 / 1244 |
| gens 2-5 | 0.59 | 0.21 | 0.19 | 7654 / 6423 |
| seeds 0-9 | 0.56 | 0.18 | 0.19 | 2607 / 2403 |
| seeds 10-29 | 0.59 | 0.19 | 0.19 | 5829 / 5264 |
| LOCO without random+accumulate | 0.60 | 0.19 | 0.19 | 7207 / 6139 |
| LOCO without random+rewrite | 0.60 | 0.18 | 0.19 | 7039 / 6661 |
| LOCO without success+accumulate | 0.60 | 0.19 | 0.19 | 7412 / 5919 |
| LOCO without success+rewrite | 0.59 | 0.20 | 0.19 | 7201 / 6204 |
| LOCO without hard+accumulate | 0.56 | 0.19 | 0.19 | 6723 / 6603 |
| LOCO without hard+rewrite | 0.56 | 0.18 | 0.19 | 6598 / 6809 |

## D. Capacity acts through coverage

Linear regression of retention (seeds 0-9, caps 8/19/40, n=23100): on anchors + log capacity → anchors +0.070 per anchor, log-capacity -0.038; log-capacity alone +0.068.

### Pre-registered K10–K12 on results_v3_confirm2 (seeds 10–29; only seeds with the run present)

| cell family | seeds | K10: taught / untaught / chance | K11: 0 / 1 / 2 / 3+ | monotone |
|---|---|---|---|---|
| cap 8 | 17 | 0.56 / 0.16 / 0.23 | 0.15 / 0.28 / 0.33 / 0.40 | yes |
| cap 40 | 16 | 0.57 / 0.19 / 0.17 | 0.03 / 0.15 / 0.28 / 0.39 | yes |
| noise 0.2 | 17 | 0.47 / 0.10 / 0.18 | 0.07 / 0.14 / 0.21 / 0.28 | yes |
| reader both | 17 | 0.61 / 0.20 / 0.18 | 0.13 / 0.26 / 0.34 / 0.41 | yes |

K12: retention | 0 anchors: cap 8 0.151 vs cap 40 0.034 (diff -0.117); | ≥2 anchors: cap 8 0.347 vs cap 40 0.380 (diff +0.033); unconditional: cap 8 0.243 vs cap 40 0.355
