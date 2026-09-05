# probe33 — what must the channel carry?

## A. Child's final form for UNTAUGHT train objects, relative to the parent's final language (gens ≥ 1)

| cell | n | = parent's own form | = a parent-neighbour's form | 1 symbol from a neighbour's | other |
|---|---|---|---|---|---|
| random+accumulate | 4350 | 0.25 | 0.23 | 0.36 | 0.16 |
| random+rewrite | 4350 | 0.32 | 0.28 | 0.35 | 0.05 |
| success+accumulate | 4350 | 0.22 | 0.23 | 0.36 | 0.20 |
| success+rewrite | 4350 | 0.27 | 0.33 | 0.34 | 0.06 |
| hard+accumulate | 4350 | 0.36 | 0.29 | 0.30 | 0.05 |
| hard+rewrite | 4350 | 0.38 | 0.28 | 0.30 | 0.04 |

## B. Retention of the parent's exact form at the child's gen end, by derivability of that form in the parent, taught vs untaught (train objects)

| cell | taught, derivable | taught, non-derivable | untaught, derivable | untaught, non-derivable | share non-derivable in population |
|---|---|---|---|---|---|
| random+accumulate | 0.75 | 0.88 | 0.22 | 0.12 | 0.05 |
| random+rewrite | 0.83 | 0.79 | 0.33 | 0.10 | 0.03 |
| success+accumulate | 0.73 | 0.80 | 0.20 | 0.09 | 0.04 |
| success+rewrite | 0.80 | 0.79 | 0.27 | 0.05 | 0.02 |
| hard+accumulate | 0.79 | 0.85 | 0.36 | 0.06 | 0.02 |
| hard+rewrite | 0.80 | 0.77 | 0.39 | 0.07 | 0.02 |

## C. Record redundancy: share of record entries (matching the parent's final form) whose form is derivable from neighbours; and within-cell correlation across (seed, gen) of the NON-derivable share with the child's inheritance (share of train objects keeping the parent's form) and structure

| cell | entries | derivable share | corr(non-derivable share, inheritance) | corr(non-derivable share, child topsim_distinct) | corr(non-derivable share, child n_owners) |
|---|---|---|---|---|---|
| random+accumulate | 1598 | 0.92 | +0.25 | -0.05 | -0.03 |
| random+rewrite | 2850 | 0.97 | -0.25 | +0.03 | +0.23 |
| success+accumulate | 1507 | 0.95 | +0.17 | -0.04 | +0.28 |
| success+rewrite | 2850 | 0.98 | -0.18 | +0.01 | +0.32 |
| hard+accumulate | 2662 | 0.98 | -0.23 | +0.12 | +0.42 |
| hard+rewrite | 2850 | 0.98 | -0.28 | +0.05 | +0.42 |

## D. Across 74 record cells (seeds 0–9, cell means): non-derivable share of the record vs continuity +0.38, vs final topsim_distinct +nan, vs fidelity of taught forms at child end +0.37

