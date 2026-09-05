# Boundary experiment L: long generations (registered 2026-09-05, before running)
Purpose (Codex): is the Snapshot Effect a transient training artefact? Generations of 6,000 steps instead of 2,000 (record and
teaching unchanged). Cells: the six cap-19 record cells + `generations`, seeds 0–9, `--steps 6000` (≈ 3× cost: ~270 runs-equivalent).
- L1 (snapshot effect survives longer training): rewrite > accumulate in topsim_distinct at generation end, ≥80% of seeds, CI > 0.
  Mechanistic expectation (not a test): accumulated entries are still fixed early (share fixed by step 1,500 ≥ 0.8), so staleness grows
  with generation length rather than shrinking.
- L2 (fidelity erosion continues): fidelity to the record at step 6,000 < at step 2,000 within the same generation, both cells, ≥80%.
- L3 (anchoring survives): K15 gap ≥ 0.15 at generation end, ≥80% of seeds.
- L4 (it can kill the claim): if L1 fails, the Snapshot Effect is a short-generation artefact and the paper's claim is restricted to
  regimes where transmission happens before convergence.
Launch after the entropy scan: `python lab.py run --out results_long --workers 10 --seeds 0..9 --cells cap-19_noise-0.0_rd-sender generations --steps 6000 --no_weights`

## Power extension (registered 2026-09-05, before running): L1 on seeds 10–29
L1 was inconclusive at n = 10 (+0.042 [+0.005, +0.076], 7/10). Re-run the four cap-19 random/success × accumulate/rewrite cells
with 6,000-step generations on 20 new seeds, pool to n = 30, same rule. Prediction: supported (the effect is present in direction
and CI at n = 10 and staleness is higher with longer generations).
