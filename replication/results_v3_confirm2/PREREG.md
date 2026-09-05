# Pre-registration — v3 factorial sweep

Written 2026-09-03 23:49 at commit `e885eb4` BEFORE any run in this directory.

Seeds: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]. Cells: 24. Overrides: none.

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

- `small__sel-random_slots-fixed_fresh-accumulate_cap-8_noise-0.0_rd-sender`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-8_noise-0.0_rd-sender`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-8_noise-0.0_rd-sender`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-8_noise-0.0_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-8_noise-0.0_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-8_noise-0.0_rd-sender`
- `small__sel-random_slots-fixed_fresh-accumulate_cap-19_noise-0.0_rd-both`
- `small__sel-random_slots-fixed_fresh-accumulate_cap-19_noise-0.2_rd-sender`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-19_noise-0.0_rd-both`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-19_noise-0.2_rd-sender`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-19_noise-0.0_rd-both`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-19_noise-0.2_rd-sender`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-19_noise-0.0_rd-both`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-19_noise-0.2_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-19_noise-0.0_rd-both`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-19_noise-0.2_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-19_noise-0.0_rd-both`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-19_noise-0.2_rd-sender`
- `small__sel-random_slots-fixed_fresh-accumulate_cap-40_noise-0.0_rd-sender`
- `small__sel-random_slots-fixed_fresh-rewrite_cap-40_noise-0.0_rd-sender`
- `small__sel-success_slots-dynamic_fresh-accumulate_cap-40_noise-0.0_rd-sender`
- `small__sel-success_slots-dynamic_fresh-rewrite_cap-40_noise-0.0_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-accumulate_cap-40_noise-0.0_rd-sender`
- `small__sel-hard_slots-dynamic_fresh-rewrite_cap-40_noise-0.0_rd-sender`

## Second confirmation (seeds 10–29): the claims of REPORT_v3.md that rested on seeds 0–9 only
Same decision rule; comparisons at the object/cell level as in probe22 §A and REPORT §5.2 / §7.4.
- **K1** (topsim_distinct): capacity 8 < capacity 19 (record too small destroys geometry).
- **K2** (topsim_distinct): capacity 19 vs 40: no difference (two-sided).
- **K3** (CBM and owners-only topsim): capacity 19 > 40.
- **K4** (founder intelligibility): capacity 40 > 19 > 8, each step ≥ +0.15.
- **K5** (founder intelligibility): correlation with topsim_distinct across these cells > 0, with convexity < 0.
- **K6** (topsim_distinct, CBM): noise 0.2 < noise 0 (noise does not repair; it damages).
- **K7** (n_owners): noise 0.2 > noise 0 (corrupted forms become new words).
- **K8** (topsim_distinct, CBM, test_acc): reader=both vs sender: no difference; fidelity of taught forms higher with reader=both.
- **K9** (convexity): accumulate > rewrite; capacity 8 > 19 > 40.

## Added 2026-09-04 (before inspecting results_v3_confirm2 for these quantities): coordination-by-anchoring
Discovered post hoc on seeds 0-29 of cap-19/noise-0/reader-sender cells (FINDINGS_v3 appendices לה–לו). To be tested on
results_v3_confirm2 cells (cap 8/40, noise 0.2, reader both; seeds 10-29), which were not used in the discovery.
- K10 (anchored choice): for untaught train objects whose parent form was borrowed from neighbour p (other neighbours holding
  different forms), the child repeats the parent's choice more often when p was taught than when p was untaught; predicted
  gap ≥ 0.15 in every cell; untaught-p rate within 0.10 of chance (1/#distinct neighbour forms).
- K11 (anchoring gradient): retention of an untaught train object's parent form increases monotonically with its number of
  taught neighbours (0 < 1 < 2 < 3+) in every cell; pooled correlation > 0.
- K12 (capacity acts through coverage): with cap 8 and cap 40 on seeds 10-29, retention conditional on #taught neighbours
  (0 vs ≥2) differs between capacities by < 0.05, while unconditional retention and mean #taught neighbours rise with capacity.
Decision rule as in PREREG.md above (≥80% of seeds in predicted direction and bootstrap CI excluding 0 where a paired
statistic applies; K12 is an equivalence claim: |difference| < 0.05 with CI inside ±0.08).

## Added 2026-09-04, after K10–K12 were evaluated and BEFORE any partition / class-matched / content-rule quantity was
## computed on results_v3_confirm2 (proposal by Codex, adopted). Thresholds fixed now.
Disclosure: results_v3_confirm2 was already inspected for anchoring counts and retention (K10–K12) and the sweep-level
`confirm2.py` metrics (K1–K9). The quantities below (partition similarity, class-matched anchoring, content-rule
effects on new seeds) have not been computed on it.
- K13 (partition inheritance). Adjusted Rand index between parent and child form-partitions of TRAIN objects at
  generation ends (gens 1–5 averaged per run). (a) rewrite cells of results_v3_confirm2 vs the no-record `generations`
  cell (results_v3_confirm, seeds 10–29; its pooled ARI 0.06 was seen in probe39, per-seed values not): predicted
  rewrite > no-record in ≥80% of seeds, paired bootstrap CI > 0, in each of the four cell families (cap 8, cap 40,
  noise 0.2, reader both). (b) fully unseen: rewrite > accumulate ARI within results_v3_confirm2, same rule, predicted
  for random/success selection (hard is exempt, per the weak freshness effect there).
- K14 (item identity is secondary). probe32's five content rules re-run on NEW seeds 30–44 (parents trained fresh).
  Effect-size thresholds fixed now: a rule is "not materially different from random" if |mean paired Δ topsim_distinct|
  < 0.03 AND |mean paired Δ CBM| < 0.02. Prediction: ≥4 of the 4 non-random rules... i.e. at least 3 of the 4
  (owners, orphans, classes, stable) satisfy both; and every rule's |Δ topsim_distinct| < 0.05, i.e. less than half the
  freshness effect (accumulate − rewrite ≈ −0.08 to −0.10) and the coverage effect (cap 8 − cap 19 ≈ −0.10).
- K15 (class-matched anchoring). Untaught TRAIN objects with ≥1 taught H1 neighbour: retention of the parent's form
  when ≥1 taught neighbour shares the object's parent form vs when all taught neighbours carry other forms. Predicted
  same-form > other-form in ≥80% of seeds with paired CI > 0, in each of the four families of results_v3_confirm2;
  predicted gap ≥ 0.15.

## Added 2026-09-04, before running on seeds 30–44 (parents = the K14 parents, `k14_raw.json`; sibling test never run on them)
- K16 (sibling symmetry breaking). Two independently initialized children trained from the same parent (end of gen 0)
  will exhibit greater partition similarity (ARI over train objects, final languages) when given the SAME 19-item fresh
  record than when given DIFFERENT random 19-item records, and both will exceed the no-record condition. Primary
  contrast: same > different; secondary: different > none. Decision rule: predicted direction in ≥80% of seeds and
  paired bootstrap CI > 0. Discovery values on seeds 0–29 (probe41): 0.415 / 0.243 / 0.077.

## Added 2026-09-04, before running on seeds 30–44 (parents retrained deterministically to capture the step-500 snapshot; final language verified against k14_raw.json)
- K17a (coordination survives immaturity). Sibling partition similarity (ARI, train objects) when both siblings are taught
  the parent's STEP-500 snapshot of the same 19 objects is no more than δ below the mature (final-language) condition.
  δ = 0.05 on the paired mean (stale − fresh ≥ −0.05), and the 95% paired bootstrap CI lower bound ≥ −0.10 (resolution
  of 15 seeds ≈ ±0.10; discovery value +0.08). Equivalence claim: no seed-proportion rule.
- K17b (immaturity misaligns). Child–parent(final) ARI is lower for stale-snapshot siblings than for mature-snapshot
  siblings: fresh − stale > 0 in ≥80% of seeds, CI > 0 (discovery +0.094, 26/30).
- K17c (immaturity redirects). Child–step-500 ARI is higher for stale-snapshot siblings: stale − fresh > 0 in ≥80% of
  seeds, CI > 0 (discovery +0.185).

## CORE FREEZE — 2026-09-04
The central theory is frozen as of this line: "Learners can independently construct structured languages, but transmission
determines which region of that structured solution space successive learners converge on. Shared anchors break symmetry;
their developmental state determines the basin." From here on, new experiments are robustness or boundary-condition tests
only; no new mechanism search. Thresholds and decision rules for K1–K17 are as written above and will not be changed.
- Power extension (registered now, before running): K14 and K17b re-evaluated on seeds 45–74 (fresh parents), pooled with
  seeds 30–44 (n = 45). Same thresholds. K14: ≥3 of 4 rules with |Δtopsim_distinct| < 0.03 and |ΔCBM| < 0.02.
  K17b: fresh − stale child–parent ARI > 0 in ≥80% of seeds, CI > 0.

## Added 2026-09-04 (overnight replication `results_replicate`, seeds 100–119, still running; nothing from it inspected)
- K18 (historical persistence without permanence). Lineage-level partition persistence ARI(gen 0, gen 5) over train
  objects: (a) rewrite > accumulate at capacity 19 (cap-19 partner cells, select ∈ {random, success}) in ≥80% of seeds with
  paired CI > 0; (b) rewrite lineages retain ARI(0,5) > 0.10 on average (persistence), while accumulate lineages fall below
  0.10 (no permanence). Discovery values (seeds 0–29): rewrite 0.17–0.24, accumulate 0.06–0.09. Evaluated by `confirm4.py`
  on results_replicate only.
