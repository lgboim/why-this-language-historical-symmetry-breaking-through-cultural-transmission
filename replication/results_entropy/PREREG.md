# Boundary experiment E: entropy-bonus scan (registered 2026-09-05, before running)
Purpose (Codex): can the dynamics be an artefact of one exploration hyper-parameter? Cells: the six cap-19 record cells + `generations`
(no record), seeds 0–9, entropy_coef ∈ {0.005, 0.08} (default 0.02 = results_v3). Everything else unchanged.
- E1 (snapshot effect survives): rewrite > accumulate in topsim_distinct (random/success pooled) at BOTH coefficients, ≥80% of seeds, CI > 0.
- E2 (standardisation is imitation, not exploration): child sender entropy at step 250 of an inheriting generation < 0.5 × gen-0 entropy at
  step 250, at both coefficients, ≥80% of seeds.
- E3 (drift rate follows the bonus): within-generation form change per 250 steps in inheriting generations is monotone in the coefficient
  (0.005 < 0.02 < 0.08), pooled over record cells, ≥80% of seeds for each adjacent pair.
- E4 (anchoring is not an exploration artefact): K15's same-form − other-form anchor gap ≥ 0.15 at both coefficients, ≥80% of seeds.
Decision rule as in results_v3_confirm2/PREREG.md. Evaluated by `confirm5.py`.

## Power extension (registered 2026-09-05, before running): E1 at entropy 0.005 on seeds 10–29
E1 was inconclusive at 0.005 with n = 10 (+0.024, 6/10). Re-test on 20 new seeds, pooled with seeds 0–9 (n = 30), same rule
(rewrite > accumulate topsim_distinct, ≥80% of seeds, CI > 0). Prediction, given the staleness mechanism: NOT supported (the
effect is absent or small when the parent's language barely changes after capture). Either outcome is informative: support
would remove the boundary; failure confirms it. Cells: cap-19 random/success × accumulate/rewrite only.
