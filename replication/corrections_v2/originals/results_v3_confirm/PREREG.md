# Pre-registration — v3 factorial sweep

Written 2026-09-03 19:47 at commit `e885eb4` BEFORE any run in this directory.

Seeds: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]. Cells: 10. Overrides: none.

## Decision rule (fixed in advance)
A directional hypothesis is SUPPORTED if the paired-by-seed difference is in the predicted direction in at least 80% of seeds AND the bootstrap 95% CI of the mean difference excludes 0. It is REFUTED if the opposite direction meets the same bar. Otherwise INCONCLUSIVE. No verdict below 8 seeds. Pairing: each record cell is matched to the cell that differs only in the factor under test; per-seed differences are averaged over matched pairs before testing.

## Hypotheses
- **H1** (topsim): Selection: random slots beat success-selected slots (the v2 surprise is about WHAT gets recorded)
- **H2** (topsim): Capacity: a smaller record yields a more compositional language (bottleneck = structure)
- **H3** (topsim): Freshness: rewriting from the final language beats accumulating carved forms
- **H4** (topsim): Erosion repairs an accumulating record: noise raises topsim when forms accumulate
- **H5** (test_acc): A record both agents read changes held-out accuracy (direction unknown)
- **H6** (n_unique_msgs): Every bottlenecked record compresses the lexicon vs no transmission
- **H7** (topsim): v2 replication: oral_fixed beats bone_edition
- **H8** (test_acc): Recording the HARD objects helps held-out accuracy more than random objects
- **H9** (intelligibility): Rewritten records are more mutually intelligible than accumulated ones

## Cells

- `small__pair`
- `small__generations`
- `small__sel-random_slots-fixed_fresh-accumulate_cap-19_noise-0.0_rd-sender`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-19_noise-0.0_rd-sender`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-19_noise-0.0_rd-sender`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-19_noise-0.0_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-19_noise-0.0_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-19_noise-0.0_rd-sender`
- `small__sel-random_slots-redraw_fresh-accumulate_cap-19_noise-0.0_rd-sender`
- `small__sel-random_slots-redraw_fresh-rewrite_cap-19_noise-0.0_rd-sender`

## Confirmation hypotheses (post-hoc findings from results_v3 seeds 0–9, now pre-registered on NEW seeds 10–29)
Same decision rule; n = 20 seeds; all comparisons at capacity 19, noise 0, reader = sender.
- **C1** (topsim): `hard + rewrite` > `random(fixed) + rewrite`.
- **C2** (test_acc): `hard + rewrite` > `random(fixed) + rewrite`  — the surprising part: in seeds 0–9 this cell topped BOTH metrics while `hard` on average hurt test_acc.
- **C3** (test_acc): `hard + rewrite` > `success + rewrite` (= bone_edition).
- **C4** (topsim): `success + rewrite` > `success + accumulate` (bone_edition > bone) — replication of the strongest v3 result, 0/10 in seeds 0–9.
- **C5** (topsim): `random(fixed) + rewrite` (= oral_fixed) vs `success + rewrite` (= bone_edition): two-sided, v2 said 9/10 for oral_fixed, v3 said 5/5.
- **C6** (topsim): every record cell vs `generations` (no transmission): two-sided — does transmission ADD structure over a fresh generation, or only preserve it?
