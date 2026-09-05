# Boundary experiment S: persistence after a ONE-SHOT immature snapshot (registered 2026-09-05, before running)
Purpose: K18 compared lineages whose records are immature every generation (accumulate) with refreshed ones. Does a single immature
snapshot also leave a shorter historical signature? Design: parent = gen 0 (seeds 0–29). Generation 1 is taught 19 objects with either
the parent's step-500 forms (immature) or final forms (mature); generations 2–5 then use an ordinary rewritten record (success
selection, capacity 19). Measure ARI(parent final, gen g) and ARI(parent step-500, gen g) for g = 1..5.
- S1 (redirection persists): ARI to the step-500 snapshot is higher in the immature lineage than in the mature lineage at g = 1 (known,
  K17c) AND still at g = 3, ≥80% of seeds, CI > 0.
- S2 (shorter signature): ARI(parent final, gen 5) is lower in the immature lineage, ≥80% of seeds, CI > 0.
- S3 (coordination unaffected): sibling-free proxy — parent–child ARI at gap 1 (gen g → g+1) does not differ between lineages
  (equivalence |mean| < 0.05, CI within ±0.08).
Script: `probe47.py` (to write). Cost: 30 seeds × 2 lineages × 5 generations ≈ 300 generation-runs ≈ 30 min.
