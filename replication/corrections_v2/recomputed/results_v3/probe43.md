# probe43 — anatomy of the basin

## A. Restricted to objects UNTAUGHT in both siblings' records (45 seeds): ARI sibling–sibling vs child–parent; exact-form agreement

| arm | untaught objs | ARI sib–sib | ARI child–parent | form agreement sib–sib | child–parent | sib−parent ARI: seeds > 0 |
|---|---|---|---|---|---|---|
| same | 29 | 0.342 | 0.235 | 0.34 | 0.19 | 34/45 |
| different | 18 | 0.131 | 0.243 | 0.15 | 0.20 | 11/45 |
| none | 48 | 0.086 | 0.048 | 0.01 | 0.01 | 24/45 |

## B. What siblings jointly invent (same-record arm): untaught objects where both siblings hold the SAME form ≠ parent's form. That form is: a taught anchor's form (H1 taught neighbour) / 1 symbol from an anchor's form / parent's form of some other H1 neighbour (untaught) / other

| count | anchor's form | 1 symbol from anchor | untaught neighbour's parent form | other | (share of untaught objects that are joint inventions) |
|---|---|---|---|---|---|
| 316 | 0.49 | 0.37 | 0.02 | 0.12 | 0.24 |

## C. Different-records arm: sibling exact-form agreement and ARI by anchoring stratum of untaught objects (same-class anchor present in both records / in one / in neither)

| stratum | objs | form agreement sib–sib | ARI sib–sib | (same-record arm, untaught with ≥1 same-class anchor) |
|---|---|---|---|---|
| both | 2.7 | 0.33 | 0.532 | 0.45 |
| one | 3.6 | 0.15 | 0.584 | 0.45 |
| neither | 12.6 | 0.13 | 0.152 | 0.45 |

## D. Decay of partition similarity along a lineage (sweep, 30 seeds): mean ARI between generations at gap 1..5, train objects; and ARI(gen 0, gen 5) vs product of consecutive ARIs (Markov expectation)

| cell | gap 1 | gap 2 | gap 3 | gap 4 | gap 5 | ARI(0,5) / Π consecutive |
|---|---|---|---|---|---|---|
| generations | 0.058 | 0.063 | 0.075 | 0.072 | 0.054 | nan |
| random+accumulate | 0.299 | 0.288 | 0.264 | 0.208 | 0.088 | 36.5 |
| random+rewrite | 0.409 | 0.368 | 0.324 | 0.286 | 0.240 | 14.4 |
| success+accumulate | 0.256 | 0.254 | 0.230 | 0.184 | 0.059 | 25.2 |
| success+rewrite | 0.411 | 0.293 | 0.231 | 0.184 | 0.167 | 10.3 |
| hard+accumulate | 0.505 | 0.394 | 0.312 | 0.245 | 0.183 | 5.2 |
| hard+rewrite | 0.537 | 0.399 | 0.329 | 0.259 | 0.210 | 4.5 |
