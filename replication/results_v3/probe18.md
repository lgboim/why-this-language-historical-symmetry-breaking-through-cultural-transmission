# probe18 — borrowing graph, semantic drift, morphemes, convexity, receiver sink, phonotactics, ambiguity lineage

Paired columns: n | wins/losses | mean diff | 95% CI | p | verdict.

## A. The borrowing graph: owners as hubs (final generation; edge = orphan → the owner it decodes to)

| cell | n | owners with ≥1 orphan (hubs) | largest hub (orphans) | share of orphans attached to the top-3 hubs | hub is Hamming-1 to all its orphans | hub status inherited: P(hub in child | hub in parent) | P(hub | non-hub) |
|---|---|---|---|---|---|---|---|
| generations | 30 | 19.2 | 3.3 | 0.29 | 0.64 | 0.41 | 0.40 |
| random+accumulate | 30 | 17.7 | 5.7 | 0.36 | 0.56 | 0.39 | 0.35 |
| random+rewrite | 30 | 18.5 | 5.2 | 0.35 | 0.61 | 0.43 | 0.35 |
| success+accumulate | 30 | 16.0 | 7.1 | 0.41 | 0.51 | 0.37 | 0.32 |
| success+rewrite | 30 | 16.5 | 6.9 | 0.38 | 0.54 | 0.42 | 0.34 |
| hard+accumulate | 30 | 14.2 | 8.5 | 0.43 | 0.47 | 0.40 | 0.29 |
| hard+rewrite | 30 | 15.5 | 8.0 | 0.40 | 0.52 | 0.41 | 0.31 |
| pair | 30 | 14.8 | 2.7 | 0.34 | 0.45 | nan | nan |

## B. Semantic drift: words whose form exists in both gen 0 and gen 5 — does their extension survive?

| cell | n words present in both | Jaccard of their object sets | same owner in both | extension grew | shrank | words present in both but with DISJOINT extensions (pure reuse) |
|---|---|---|---|---|---|---|
| random+accumulate | 7.6 | 0.11 | 0.12 | 0.52 | 0.23 | 0.67 |
| random+rewrite | 17.8 | 0.33 | 0.35 | 0.44 | 0.21 | 0.39 |
| success+accumulate | 6.3 | 0.08 | 0.08 | 0.58 | 0.18 | 0.72 |
| success+rewrite | 10.2 | 0.14 | 0.14 | 0.65 | 0.14 | 0.59 |
| hard+accumulate | 9.9 | 0.20 | 0.19 | 0.73 | 0.09 | 0.45 |
| hard+rewrite | 10.0 | 0.18 | 0.12 | 0.70 | 0.12 | 0.53 |

## C. Morpheme continuity: (position, symbol) → (attribute, value) associations conserved parent → child, vs conservation of whole words

association = the best one-to-one matching (Hungarian) between the 24 (position, symbol) units and the 12 (attribute, value) concepts, keeping only matches supported by ≥ 4 objects.

| cell | n transitions | associations per language | conserved parent → child (share) | whole words conserved (share of 64) | chance for associations (random relabel) |
|---|---|---|---|---|---|
| random+accumulate | 150 | 11.3 | 0.30 | 0.30 | 0.05 |
| random+rewrite | 150 | 11.4 | 0.45 | 0.45 | 0.07 |
| success+accumulate | 150 | 11.2 | 0.30 | 0.28 | 0.06 |
| success+rewrite | 150 | 11.2 | 0.47 | 0.42 | 0.07 |
| hard+accumulate | 150 | 10.8 | 0.43 | 0.46 | 0.07 |
| hard+rewrite | 150 | 10.8 | 0.45 | 0.49 | 0.07 |

## D. Convexity of word extensions: is each homonym class (size ≥ 3) a connected region under Hamming-1 adjacency?

| cell | classes | connected | random sets of the same sizes | classes that are a straight line (vary in ONE attribute only) |
|---|---|---|---|---|
| generations | 97 | 0.66 | 0.04 | 0.35 |
| random+accumulate | 278 | 0.76 | 0.03 | 0.19 |
| random+rewrite | 233 | 0.73 | 0.04 | 0.23 |
| success+accumulate | 274 | 0.80 | 0.03 | 0.18 |
| success+rewrite | 311 | 0.78 | 0.03 | 0.23 |
| hard+accumulate | 287 | 0.86 | 0.03 | 0.23 |
| hard+rewrite | 317 | 0.85 | 0.03 | 0.28 |
| pair | 66 | 0.56 | 0.04 | 0.27 |

## E. The receiver's sink: decoding all 512 possible messages (final receiver)

| cell | n | distinct objects reached by the 512 messages | share of UNUSED messages decoded to the single most popular object | most popular object is an owner | it is the object with the largest class |
|---|---|---|---|---|---|
| generations | 30 | 48.2 | 0.11 | 0.83 | 0.03 |
| random+accumulate | 30 | 52.7 | 0.10 | 0.77 | 0.03 |
| random+rewrite | 30 | 51.1 | 0.10 | 0.87 | 0.00 |
| success+accumulate | 30 | 49.7 | 0.11 | 0.87 | 0.00 |
| success+rewrite | 30 | 48.6 | 0.12 | 0.67 | 0.07 |
| hard+accumulate | 30 | 47.1 | 0.12 | 0.67 | 0.03 |
| hard+rewrite | 30 | 47.6 | 0.12 | 0.60 | 0.07 |
| pair | 30 | 47.8 | 0.13 | 1.00 | 0.00 |

## F. Phonotactics: mutual information between message positions, and how much of it the attributes explain

| cell | n | MI(pos0,pos1)+MI(pos1,pos2)+MI(pos0,pos2) (bits) | same for a language with the same per-position symbol→attribute mapping but independent positions (shuffle within attribute value) |
|---|---|---|---|
| generations | 30 | 1.74 | 1.31 |
| random+accumulate | 30 | 3.07 | 1.59 |
| random+rewrite | 30 | 2.24 | 1.12 |
| success+accumulate | 30 | 3.04 | 1.31 |
| success+rewrite | 30 | 2.10 | 0.96 |
| hard+accumulate | 30 | 2.51 | 1.45 |
| hard+rewrite | 30 | 2.27 | 1.16 |
| pair | 30 | 1.64 | 1.48 |

## G. Ambiguity lineage: forms in the bottom confidence quartile of the parent — what happens to them in the child?

| cell | n | kept the form AND still bottom-quartile | kept, moved up | changed the form | of changed: child's new form in top half of confidence |
|---|---|---|---|---|---|
| random+accumulate | 2400 | 0.06 | 0.09 | 0.85 | 0.30 |
| random+rewrite | 2400 | 0.08 | 0.18 | 0.73 | 0.23 |
| success+accumulate | 2400 | 0.07 | 0.09 | 0.84 | 0.30 |
| success+rewrite | 2400 | 0.07 | 0.21 | 0.72 | 0.26 |
| hard+accumulate | 2400 | 0.07 | 0.20 | 0.73 | 0.29 |
| hard+rewrite | 2400 | 0.08 | 0.22 | 0.70 | 0.26 |

