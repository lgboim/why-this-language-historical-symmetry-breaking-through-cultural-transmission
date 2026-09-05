# probe20 — held-out inheritance, form pool, hubs, grammar drift in a dyad, standardisation, rich-get-richer

## A. Why are held-out words inherited? Conservation of a held-out object's word parent→child, by whether its absorber (a training object with the same word) was TAUGHT

| cell | held-out transitions | conserved overall | absorber taught: conserved | absorber untaught: conserved | no absorber (unique word): conserved |
|---|---|---|---|---|---|
| random+accumulate | 2400 | 0.20 | 0.28 | 0.11 | 0.05 |
| random+rewrite | 2400 | 0.24 | 0.37 | 0.14 | 0.09 |
| success+accumulate | 2400 | 0.20 | 0.28 | 0.12 | 0.04 |
| success+rewrite | 2400 | 0.24 | 0.38 | 0.09 | 0.07 |
| hard+accumulate | 2400 | 0.31 | 0.48 | 0.10 | 0.04 |
| hard+rewrite | 2400 | 0.33 | 0.50 | 0.11 | 0.07 |

## B. Form pool vs assignment: what fraction of the child's distinct forms existed in the parent's lexicon (for ANY object), vs (object, form) pairs conserved

| cell | child forms present in parent's pool | (object, form) pairs conserved | forms in the pool but re-assigned (share of child forms) |
|---|---|---|---|
| random+accumulate | 0.57 | 0.30 | 0.16 |
| random+rewrite | 0.72 | 0.45 | 0.13 |
| success+accumulate | 0.55 | 0.28 | 0.16 |
| success+rewrite | 0.74 | 0.42 | 0.15 |
| hard+accumulate | 0.72 | 0.46 | 0.12 |
| hard+rewrite | 0.73 | 0.49 | 0.12 |

## C. What makes a hub? Owners with ≥ 3 orphans vs owners with 0 (final generation)

| cell | hubs | training neighbours: hubs | lone owners | held-out neighbours: hubs | lone | hub was already an owner in the parent generation | lone owners were |
|---|---|---|---|---|---|---|---|
| random+accumulate | 170 | 6.68 | 6.82 | 2.32 | 2.18 | 0.50 | 0.64 |
| random+rewrite | 130 | 6.65 | 6.78 | 2.35 | 2.22 | 0.61 | 0.74 |
| success+accumulate | 187 | 6.81 | 6.97 | 2.19 | 2.03 | 0.46 | 0.62 |
| success+rewrite | 219 | 6.85 | 6.65 | 2.15 | 2.35 | 0.47 | 0.66 |
| hard+accumulate | 233 | 6.95 | 6.83 | 2.05 | 2.17 | 0.41 | 0.63 |
| hard+rewrite | 241 | 6.84 | 6.86 | 2.16 | 2.14 | 0.46 | 0.63 |

## D. Grammar drift inside one dyad (`pair`, from step 6000): role-matrix correlation and word persistence over Δ steps

| Δ steps | 250 | 1000 | 2000 | 4000 | 6000 |
|---|---|---|---|---|---|
| role stability | +0.92 | +0.88 | +0.80 | +0.86 | +0.77 |
| word persistence | 0.69 | 0.62 | 0.56 | 0.54 | 0.46 |

(across generations with a fresh record, role stability parent→child was 0.5–0.8 with word persistence 0.3–0.5)

## E. Receiver tolerance of the sender's variants, by generation (share of non-greedy sampled messages decoded correctly over all 64)

| cell | gen 0 | gen 1 | gen 2 | gen 3 | gen 4 | gen 5 | variant rate gen 0 → gen 5 |
|---|---|---|---|---|---|---|---|
| generations | 0.37 | 0.30 | 0.35 | 0.32 | 0.37 | 0.37 | 0.36 → 0.34 |
| random+accumulate | 0.37 | 0.17 | 0.18 | 0.19 | 0.15 | 0.15 | 0.36 → 0.10 |
| random+rewrite | 0.37 | 0.19 | 0.19 | 0.18 | 0.21 | 0.19 | 0.36 → 0.10 |
| success+accumulate | 0.37 | 0.16 | 0.16 | 0.13 | 0.15 | 0.17 | 0.36 → 0.10 |
| success+rewrite | 0.37 | 0.21 | 0.17 | 0.17 | 0.09 | 0.15 | 0.36 → 0.07 |
| hard+accumulate | 0.37 | 0.20 | 0.16 | 0.12 | 0.10 | 0.09 | 0.36 → 0.07 |
| hard+rewrite | 0.37 | 0.20 | 0.15 | 0.15 | 0.08 | 0.13 | 0.36 → 0.05 |

## F. Rich get richer? Probability that a word's extension grows / shrinks / dies (form disappears) between consecutive generations, by its current size

| cell | size 1: grow | shrink/die | size 2–3: grow | shrink/die | size ≥ 4: grow | shrink/die |
|---|---|---|---|---|---|---|
| random+accumulate | 0.19 | 0.66 | 0.20 | 0.63 | 0.14 | 0.72 |
| random+rewrite | 0.26 | 0.46 | 0.20 | 0.54 | 0.12 | 0.72 |
| success+accumulate | 0.17 | 0.71 | 0.21 | 0.64 | 0.16 | 0.72 |
| success+rewrite | 0.26 | 0.54 | 0.27 | 0.53 | 0.17 | 0.64 |
| hard+accumulate | 0.19 | 0.68 | 0.27 | 0.53 | 0.24 | 0.53 |
| hard+rewrite | 0.19 | 0.68 | 0.26 | 0.51 | 0.21 | 0.51 |

