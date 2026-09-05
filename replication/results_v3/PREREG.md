# Pre-registration — v3 factorial sweep

Written 2026-09-03 14:26 at commit `e885eb4` BEFORE any run in this directory.

Seeds: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]. Cells: 77. Overrides: none.

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
- `small__population`
- `small__generations`
- `small__sel-random_slots-fixed_fresh-accumulate_cap-8_noise-0.0_rd-sender`
- `small__sel-random_slots-fixed_fresh-accumulate_cap-8_noise-0.0_rd-both`
- `small__sel-random_slots-fixed_fresh-accumulate_cap-8_noise-0.2_rd-sender`
- `small__sel-random_slots-fixed_fresh-accumulate_cap-8_noise-0.2_rd-both`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-8_noise-0.0_rd-sender`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-8_noise-0.0_rd-both`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-8_noise-0.2_rd-sender`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-8_noise-0.2_rd-both`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-8_noise-0.0_rd-sender`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-8_noise-0.0_rd-both`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-8_noise-0.2_rd-sender`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-8_noise-0.2_rd-both`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-8_noise-0.0_rd-sender`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-8_noise-0.0_rd-both`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-8_noise-0.2_rd-sender`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-8_noise-0.2_rd-both`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-8_noise-0.0_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-8_noise-0.0_rd-both`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-8_noise-0.2_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-8_noise-0.2_rd-both`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-8_noise-0.0_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-8_noise-0.0_rd-both`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-8_noise-0.2_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-8_noise-0.2_rd-both`
- `small__sel-random_slots-fixed_fresh-accumulate_cap-19_noise-0.0_rd-sender`
- `small__sel-random_slots-fixed_fresh-accumulate_cap-19_noise-0.0_rd-both`
- `small__sel-random_slots-fixed_fresh-accumulate_cap-19_noise-0.2_rd-sender`
- `small__sel-random_slots-fixed_fresh-accumulate_cap-19_noise-0.2_rd-both`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-19_noise-0.0_rd-sender`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-19_noise-0.0_rd-both`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-19_noise-0.2_rd-sender`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-19_noise-0.2_rd-both`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-19_noise-0.0_rd-sender`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-19_noise-0.0_rd-both`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-19_noise-0.2_rd-sender`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-19_noise-0.2_rd-both`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-19_noise-0.0_rd-sender`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-19_noise-0.0_rd-both`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-19_noise-0.2_rd-sender`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-19_noise-0.2_rd-both`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-19_noise-0.0_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-19_noise-0.0_rd-both`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-19_noise-0.2_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-19_noise-0.2_rd-both`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-19_noise-0.0_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-19_noise-0.0_rd-both`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-19_noise-0.2_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-19_noise-0.2_rd-both`
- `small__sel-random_slots-fixed_fresh-accumulate_cap-40_noise-0.0_rd-sender`
- `small__sel-random_slots-fixed_fresh-accumulate_cap-40_noise-0.0_rd-both`
- `small__sel-random_slots-fixed_fresh-accumulate_cap-40_noise-0.2_rd-sender`
- `small__sel-random_slots-fixed_fresh-accumulate_cap-40_noise-0.2_rd-both`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-40_noise-0.0_rd-sender`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-40_noise-0.0_rd-both`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-40_noise-0.2_rd-sender`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-40_noise-0.2_rd-both`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-40_noise-0.0_rd-sender`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-40_noise-0.0_rd-both`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-40_noise-0.2_rd-sender`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-40_noise-0.2_rd-both`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-40_noise-0.0_rd-sender`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-40_noise-0.0_rd-both`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-40_noise-0.2_rd-sender`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-40_noise-0.2_rd-both`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-40_noise-0.0_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-40_noise-0.0_rd-both`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-40_noise-0.2_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-40_noise-0.2_rd-both`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-40_noise-0.0_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-40_noise-0.0_rd-both`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-40_noise-0.2_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-40_noise-0.2_rd-both`
- `small__sel-random_slots-redraw_fresh-accumulate_cap-19_noise-0.0_rd-sender`
- `small__sel-random_slots-redraw_fresh-rewrite_cap-19_noise-0.0_rd-sender`
