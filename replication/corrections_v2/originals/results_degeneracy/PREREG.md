# Boundary experiment D: does the symmetry-breaking effect scale with the number of viable reconstructions? (registered 2026-09-05, before running)
Manipulation: hard_frac ∈ {0.0, 0.5, 1.0} — the share of rounds whose 4 distractors are Hamming-1 neighbours of the target. At 1.0 every
round requires all attributes, so only near-injective languages succeed: the number of viable PARTITIONS collapses (few classes), while
viable FORM assignments remain many. At 0.0 (standard) many partitions of comparable value exist. GRU learner, small world, seeds 0–19;
parent = a fresh generation 0 trained under the same hard_frac; siblings design (same 19 / different 19 / none), one generation each.
Predictions from the toy model (fewer equivalent minimisers → smaller anchored gap):
- D1 (partition level): the sibling ARI gap (same − different) DECREASES monotonically with hard_frac (0.0 > 0.5 > 1.0), ≥80% of seeds
  for each adjacent pair, paired CI > 0.
- D2 (form level): the sibling exact-form-agreement gap (same − different) does NOT decrease correspondingly (equivalence band: the
  1.0 − 0.0 difference has |mean| < 0.10 with CI within ±0.15), because form-level underdetermination survives injectivity.
- D3 (descriptive, no verdict): distinct messages and owner share per hard_frac, to confirm the regime change.
If D1 holds and D2 holds, the effect scales with the degeneracy of the level at which it is measured — "cultural leverage is highest
under structured underdetermination" becomes a result. Script: probe49.py.
