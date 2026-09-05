# probe26 — follow-ups to the ownership-break intervention

## A. Repair mechanics in the collide arm: each forced homonym pair (intruder = ex-owner given the incumbent's message). At each snapshot: who holds the taught message, who owns it under the child receiver

| step | pair still homonyms | intruder moved away | incumbent moved away | both moved | owner of the taught message = incumbent | = intruder | neither |
|---|---|---|---|---|---|---|---|
| 250 | 0.22 | 0.24 | 0.30 | 0.23 | 0.23 | 0.23 | 0.42 |
| 500 | 0.18 | 0.28 | 0.30 | 0.24 | 0.26 | 0.26 | 0.36 |
| 1000 | 0.14 | 0.30 | 0.30 | 0.27 | 0.29 | 0.27 | 0.33 |
| 2000 | 0.11 | 0.30 | 0.30 | 0.29 | 0.26 | 0.30 | 0.33 |

## B. Resolving collisions at the start → the language at the end (step 2000), emancipate − control, paired by seed

| metric | control | emancipate | paired | | | | | |
|---|---|---|---|---|---|---|---|---|
| topsim_distinct | 0.290 | 0.165 | 30 | 0/30 | -0.125 | [-0.142, -0.107] | 0.000 | TWO-SIDED: A<B (CI) | |
| CBM | 0.486 | 0.392 | 30 | 2/28 | -0.094 | [-0.111, -0.077] | 0.000 | TWO-SIDED: A<B (CI) | |
| n_owners (train) | 37.300 | 46.800 | 30 | 30/0 | +9.500 | [+7.467, +11.700] | 0.000 | TWO-SIDED: A>B (CI) | |
| distinct messages | 42.700 | 58.167 | 30 | 29/0 | +15.467 | [+12.167, +18.700] | 0.000 | TWO-SIDED: A>B (CI) | |
| distinct messages, train objs | 37.533 | 46.800 | 30 | 29/0 | +9.267 | [+7.233, +11.434] | 0.000 | TWO-SIDED: A>B (CI) | |
| held-out objs sharing a train form | 0.660 | 0.271 | 30 | 1/28 | -0.390 | [-0.475, -0.302] | 0.000 | TWO-SIDED: A<B (CI) | |

## C. Is ownership a property of the objects or of the receiver? Parent's collision classes (gen 0, ≥2 train members): does the independent child receiver (control arm, fresh init, same taught language) pick the same owner?

Among 226 parent collision classes still intact at the child's step 250 (mean size 2.5), the child's receiver chose the parent's owner in 0.60 (chance ≈ 0.45).

## D. Naming attempts in the sweep (gens ≥ 1, TRAIN orphans that break away from their owner's form within a window): does the object become an owner at the next snapshot?

| cell | attempts / gen | new form unique in language | → owner next snapshot (unique) | → owner (new form collides elsewhere) | still owner at gen end |
|---|---|---|---|---|---|
| random+accumulate | 17.5 | 0.28 | 0.87 | 0.32 | 0.64 |
| random+rewrite | 15.5 | 0.33 | 0.89 | 0.35 | 0.69 |
| success+accumulate | 19.0 | 0.25 | 0.86 | 0.30 | 0.60 |
| success+rewrite | 17.0 | 0.22 | 0.84 | 0.31 | 0.56 |
| hard+accumulate | 16.9 | 0.18 | 0.85 | 0.28 | 0.51 |
| hard+rewrite | 16.7 | 0.20 | 0.86 | 0.30 | 0.52 |

## E. Held-out objects when they move (sweep, gens ≥ 1): new form = form of a Hamming-1 TRAIN neighbour? vs chance (share of such moves if the new form were a random train form)

| cell | moves | new form = H1 train neighbour's | = some train form | = no train form (invention) | chance for H1 |
|---|---|---|---|---|---|
| generations | 9735 | 0.37 | 0.54 | 0.46 | 0.22 |
| random+accumulate | 4770 | 0.59 | 0.83 | 0.17 | 0.25 |
| random+rewrite | 5080 | 0.50 | 0.80 | 0.20 | 0.22 |
| success+accumulate | 4393 | 0.61 | 0.86 | 0.14 | 0.28 |
| success+rewrite | 4196 | 0.58 | 0.85 | 0.15 | 0.26 |
| hard+accumulate | 3829 | 0.65 | 0.87 | 0.13 | 0.29 |
| hard+rewrite | 3636 | 0.64 | 0.86 | 0.14 | 0.28 |

## F. Does the record transmit collisions? share of record entries whose form is shared with another entry; and of those pairs, share the child still produces as homonyms at step 250 / 2000

| cell | entries in a collision | pairs | child homonym @250 | @2000 | child's owner among the pair = parent's owner |
|---|---|---|---|---|---|
| random+accumulate | 0.34 | 1150 | 0.66 | 0.28 | 0.13 |
| random+rewrite | 0.24 | 455 | 0.96 | 0.81 | 0.40 |
| success+accumulate | 0.48 | 3020 | 0.60 | 0.34 | 0.21 |
| success+rewrite | 0.48 | 1090 | 0.94 | 0.78 | 0.43 |
| hard+accumulate | 0.62 | 1863 | 0.92 | 0.72 | 0.41 |
| hard+rewrite | 0.58 | 1619 | 0.95 | 0.74 | 0.42 |

## G. Sender-side variant rate at generation end (weights), by status under the receiver, TRAIN objects only; held-out for reference

| cell | train owners | train orphans | paired (orphan − owner) | | | | | | held-out |
|---|---|---|---|---|---|---|---|---|---|
| random+accumulate | 0.067 | 0.034 | 30 | 0/30 | -0.033 | [-0.039, -0.027] | 0.000 | TWO-SIDED: A<B (CI) | 0.242 |
| random+rewrite | 0.064 | 0.035 | 30 | 0/30 | -0.029 | [-0.034, -0.024] | 0.000 | TWO-SIDED: A<B (CI) | 0.232 |
| success+accumulate | 0.074 | 0.034 | 30 | 0/30 | -0.039 | [-0.047, -0.032] | 0.000 | TWO-SIDED: A<B (CI) | 0.222 |
| success+rewrite | 0.050 | 0.033 | 30 | 2/28 | -0.017 | [-0.022, -0.012] | 0.000 | TWO-SIDED: A<B (CI) | 0.186 |
| hard+accumulate | 0.053 | 0.029 | 30 | 1/29 | -0.023 | [-0.029, -0.018] | 0.000 | TWO-SIDED: A<B (CI) | 0.154 |
| hard+rewrite | 0.053 | 0.031 | 30 | 1/29 | -0.022 | [-0.028, -0.017] | 0.000 | TWO-SIDED: A<B (CI) | 0.157 |
