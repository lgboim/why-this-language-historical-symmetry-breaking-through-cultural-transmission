# probe34 — the record as coordination

## A. Choice inheritance without teaching: untaught train object o whose parent form = form of neighbour p, with ≥1 other neighbour holding a different form. Child's final form: same as parent's choice / another neighbour's form / neither. Chance = 1/#distinct neighbour forms

| cell | cases | child repeats parent's choice | picks another neighbour's form | neither | chance | repeats when p was taught | when p untaught |
|---|---|---|---|---|---|---|---|
| random+accumulate | 2757 | 0.32 | 0.21 | 0.47 | 0.19 | 0.51 | 0.17 |
| random+rewrite | 2403 | 0.41 | 0.23 | 0.36 | 0.18 | 0.52 | 0.25 |
| success+accumulate | 2772 | 0.27 | 0.21 | 0.52 | 0.19 | 0.44 | 0.17 |
| success+rewrite | 2698 | 0.35 | 0.28 | 0.38 | 0.19 | 0.57 | 0.16 |
| hard+accumulate | 2777 | 0.49 | 0.23 | 0.28 | 0.19 | 0.67 | 0.19 |
| hard+rewrite | 2696 | 0.54 | 0.20 | 0.26 | 0.19 | 0.68 | 0.24 |

## B. Anchoring: untaught train objects, retention of the parent's exact form at child gen end, by number of Hamming-1 train neighbours that were taught (with their parent form)

| cell | 0 taught nbrs: n, retained | 1 | 2 | 3+ | corr |
|---|---|---|---|---|---|
| random+accumulate | 1119, 0.09 | 1180, 0.27 | 1088, 0.30 | 963, 0.36 | +0.21 |
| random+rewrite | 150, 0.22 | 600, 0.28 | 1225, 0.30 | 2375, 0.34 | +0.08 |
| success+accumulate | 1418, 0.10 | 1294, 0.25 | 1016, 0.28 | 622, 0.32 | +0.17 |
| success+rewrite | 235, 0.09 | 828, 0.18 | 1294, 0.23 | 1993, 0.34 | +0.19 |
| hard+accumulate | 202, 0.13 | 828, 0.23 | 1272, 0.32 | 2048, 0.46 | +0.23 |
| hard+rewrite | 139, 0.10 | 673, 0.24 | 1238, 0.33 | 2300, 0.46 | +0.22 |

## C. Anchor value of a record entry: for each taught object (form kept by child), share of its untaught train neighbours retaining the parent's form, by number of untaught neighbours; and entries with 0 untaught neighbours (pure content, no anchoring)

| cell | entries | untaught nbrs mean | nbr retention | entries with 0 untaught nbrs |
|---|---|---|---|---|
| random+accumulate | 1219 | 4.11 | 0.34 | 0.00 |
| random+rewrite | 2362 | 4.10 | 0.35 | 0.00 |
| success+accumulate | 1106 | 3.56 | 0.30 | 0.02 |
| success+rewrite | 2290 | 3.67 | 0.33 | 0.01 |
| hard+accumulate | 2101 | 4.03 | 0.46 | 0.00 |
| hard+rewrite | 2278 | 4.05 | 0.47 | 0.00 |

## D. Are the alternatives equivalent? untaught train objects with a derivable parent form: per-object accuracy at child gen end, kept parent's form vs switched to another neighbour's form (paired over seeds)

| cell | kept | switched | paired (kept − switched) | | | | | |
|---|---|---|---|---|---|---|---|---|
| random+accumulate | 0.935 | 0.933 | 30 | 19/11 | +0.002 | [-0.007, +0.011] | 0.200 | TWO-SIDED: no difference (CI) | |
| random+rewrite | 0.954 | 0.942 | 30 | 22/8 | +0.012 | [+0.002, +0.022] | 0.016 | TWO-SIDED: A>B (CI) | |
| success+accumulate | 0.921 | 0.921 | 30 | 16/14 | +0.001 | [-0.013, +0.015] | 0.856 | TWO-SIDED: no difference (CI) | |
| success+rewrite | 0.933 | 0.921 | 30 | 19/11 | +0.012 | [+0.003, +0.020] | 0.200 | TWO-SIDED: A>B (CI) | |
| hard+accumulate | 0.935 | 0.907 | 30 | 21/9 | +0.027 | [+0.012, +0.044] | 0.043 | TWO-SIDED: A>B (CI) | |
| hard+rewrite | 0.941 | 0.922 | 30 | 23/7 | +0.019 | [+0.010, +0.029] | 0.005 | TWO-SIDED: A>B (CI) | |

## E. Capacity (seeds 0–9, select × fresh pooled): retention of untaught train forms, mean taught neighbours per untaught object, and retention with 0 vs ≥2 taught neighbours

| capacity | untaught objs | retention | taught nbrs mean | retention, 0 taught nbrs | ≥2 |
|---|---|---|---|---|---|
| 8 | 12000 | 0.21 | 0.91 | 0.12 | 0.30 |
| 19 | 8700 | 0.28 | 2.21 | 0.09 | 0.32 |
| 40 | 2400 | 0.32 | 4.58 | 0.02 | 0.34 |
