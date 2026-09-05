# probe23 — who causes standardisation?

## A. Tolerance of the sender's variants: the ORIGINAL child receiver vs a FRESH receiver trained (greedy language only) on the same inheriting sender; and the same for a non-inheriting sender (gen 0)

| sender | n | original receiver tolerance | fresh receiver tolerance | paired (fresh − original) | | | | | sender variant rate |
|---|---|---|---|---|---|---|---|---|---|
| inheriting sender (gen 5, rewrite cells) | 20 | 0.16 | 0.09 | 20 | 0/20 | -0.067 | [-0.087, -0.051] | 0.000 | TWO-SIDED: A<B (CI) | 0.07 |
| non-inheriting sender (gen 0) | 20 | 0.36 | 0.16 | 20 | 0/20 | -0.203 | [-0.223, -0.182] | 0.000 | TWO-SIDED: A<B (CI) | 0.34 |

If the fresh receiver is as intolerant as the original on the inheriting sender, intolerance is a property of the sender's language (variants are simply not decodable); if it is more tolerant, the child receiver learned to be strict.

## B. Sender message entropy (nats) at step 250 and 2000: gen 0 (no inheritance) vs child generations

| cell | gen 0 @250 | gens ≥ 1 @250 | gen 0 @2000 | gens ≥ 1 @2000 |
|---|---|---|---|---|
| generations | 1.33 | 1.31 | 0.37 | 0.38 |
| random+accumulate | 1.33 | 0.16 | 0.37 | 0.11 |
| random+rewrite | 1.33 | 0.16 | 0.37 | 0.10 |
| success+accumulate | 1.33 | 0.16 | 0.37 | 0.10 |
| success+rewrite | 1.33 | 0.13 | 0.37 | 0.08 |
| hard+accumulate | 1.33 | 0.11 | 0.37 | 0.07 |
| hard+rewrite | 1.33 | 0.11 | 0.37 | 0.07 |

