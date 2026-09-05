# probe39 — stress-testing the distilled claim

## A. 'Not how many': final-generation structure by capacity, rewrite cells (select pooled), paired by seed where both exist

| capacity | seeds | topsim_distinct | CBM | n_owners | continuity proxy: parent form kept (untaught) |
|---|---|---|---|---|---|
| 8 | 30 | 0.206 | 0.513 | 12.0 | 0.267 |
| 19 | 30 | 0.306 | 0.543 | 22.0 | 0.393 |
| 40 | 30 | 0.329 | 0.519 | 36.5 | 0.421 |

cap 8 − cap 19, topsim_distinct: | 30 | 1/29 | -0.100 | [-0.119, -0.080] | 0.000 | TWO-SIDED: A<B (CI) |
cap 40 − cap 19, topsim_distinct: | 30 | 18/12 | +0.023 | [+0.005, +0.042] | 0.362 | TWO-SIDED: A>B (CI) |
cap 8 − cap 19, CBM: | 30 | 4/26 | -0.030 | [-0.040, -0.020] | 0.000 | TWO-SIDED: A<B (CI) |
cap 40 − cap 19, CBM: | 30 | 3/26 | -0.024 | [-0.034, -0.013] | 0.000 | TWO-SIDED: A<B (CI) |

## B. Literal reconstruction: for each untaught train object, predict the child's final form. Predictors: (i) copy parent's form; (ii) nearest same-class anchor's form if any, else nearest taught neighbour's form (Hamming distance, ties by parent's form); (iii) anchor-or-parent: same-class anchor's form if any, else parent's form. Accuracy = exact match with the child's form

| cell | n | copy parent | nearest anchor | anchor-or-parent | child form ∈ {any taught neighbour's form} |
|---|---|---|---|---|---|
| random+accumulate | 4350 | 0.249 | 0.214 | 0.249 | 0.275 |
| random+rewrite | 4350 | 0.319 | 0.234 | 0.319 | 0.372 |
| success+accumulate | 4350 | 0.218 | 0.189 | 0.218 | 0.220 |
| success+rewrite | 4350 | 0.266 | 0.269 | 0.266 | 0.399 |
| hard+accumulate | 4350 | 0.357 | 0.354 | 0.357 | 0.451 |
| hard+rewrite | 4350 | 0.380 | 0.365 | 0.380 | 0.466 |

## C. 'Same structure, different forms': adjusted Rand index between the parent's and the child's partition of train objects into form-classes, at generation ends; baseline = child partition vs a random permutation of the parent's partition; and share of forms shared

| cell | ARI parent→child | baseline ARI | share of train objects keeping parent's form | ARI among objects that CHANGED form |
|---|---|---|---|---|
| generations (no record) | 0.058 | 0.002 | 0.01 | 0.058 |
| random+accumulate | 0.299 | -0.002 | 0.34 | 0.235 |
| random+rewrite | 0.409 | 0.002 | 0.52 | 0.317 |
| success+accumulate | 0.256 | -0.002 | 0.31 | 0.225 |
| success+rewrite | 0.411 | -0.004 | 0.48 | 0.320 |
| hard+accumulate | 0.505 | 0.005 | 0.51 | 0.396 |
| hard+rewrite | 0.537 | -0.002 | 0.55 | 0.368 |

## D. 'Developmental state' literally (accumulate cells, gen 1 children of gen 0): maturity of a record entry = earliest step (250..2000) at which the parent's language held that form for that object continuously until... (first step it appeared). Child fidelity and pull by maturity

| first step the form appeared in parent | entries | form == parent's final | child holds it @2000 | untaught H1 nbrs adopt it | untaught H1 nbrs keep parent's form |
|---|---|---|---|---|---|
| ≤500 | 630 | 0.52 | 0.67 | 0.136 | 0.159 |
| 750-1250 | 190 | 0.95 | 0.77 | 0.140 | 0.210 |
| ≥1500 | 169 | 0.99 | 0.75 | 0.102 | 0.195 |
