# Corrections v2 — working notes (2026-09-05)

## Metric correction (shared standard ARI, metrics.py)
Cross-checked against the audit's independent implementation: max |difference| 1e-16 on 500 random pairs; edge cases agree.
Re-scored from cached data (corrections_v2/recomputed/, originals preserved in corrections_v2/originals/):
- GRU tables: K13a cap40 +0.640 -> +0.643; K13b cap40 hard +0.055 [-0.019,+0.110] -> +0.065 [+0.011,+0.111] (still INCONCLUSIVE by seed rule 15/20);
  everything else identical (K16, K17a/b/c, K14, K18, M2, S, D, A3'/A4' unchanged).
- Discovery probes: probe39 now includes all 30 seeds in two rows (was 28/29; a degenerate ARI had excluded them): cap8-cap19 topsim_distinct
  -0.098 -> -0.100, CBM -0.029 -> -0.030; cap40 rows +0.023 -> +0.023, CBM -0.024 -> -0.024. probe43: untaught-object sibling ARI for
  'different' 0.198 -> 0.243; sibling ARI by anchoring status ('both'/'one'/'neither') 0.282/0.055/0.130 -> 0.532/0.584/0.152 (these are
  exploratory descriptives of tiny untaught subsets in which identical singleton partitions now correctly score 1).
- Architecture A (results_arch, seeds 100-119): A3 primary -0.010 [-0.116,+0.071] -> +0.290 [+0.058,+0.516] 12/4 (INCONCLUSIVE both times);
  A3 secondary +0.041 -> +0.141 [-0.005,+0.311]; A4/K17a +0.152 [+0.027,+0.286] SUPPORTED -> -0.198 [-0.477,+0.089] FAILED (band not met);
  A4/K17b +0.004 -> +0.029 (INCONCLUSIVE); A4/K17c unchanged +0.113 [+0.046,+0.187] 15/20.
- Not applicable: results_arch2/arch3 hold seeds 120-159 (form-level A3'/A4' via confirm8, unchanged); confirm4 on results_v3_confirm2 has no
  gen0/gen5 data (now fails clearly).

## Evaluator corrections (both cohorts)
- K12 registered subgroup (0 vs >=2): confirmation +0.038 [+0.009,+0.068] (inside band), replication +0.064 [+0.033,+0.094] (outside);
  3+ subgroup -0.007 / +0.023 (inside both); 0 anchors -0.124 / -0.101 (fail both).
- K11 adjacent steps (family-pooled per seed): confirmation cap40 13/20 per step, cap8 15/20 for 2v1 and 3+v2; replication mostly >= 16/20
  (cap40 1v0 15/20). Aggregate slope positive 20/20 per family (unchanged).
- K10 chance on untaught cases only: confirmation -0.058/+0.015/-0.074/+0.024; replication -0.065/+0.031/-0.082/+0.013 (all within +-0.10).
- K8 fidelity with the seed as unit: +0.052 [+0.040,+0.064] 20/20 (confirmation); +0.053 [+0.044,+0.061] 20/20 (replication).
- M1 evaluator label now: direction supported, magnitude below the registered 0.15 band.

## Model (model_v2.py, design fixed beforehand in results_model/T4_correction_design.md; model.py and toy_results.md untouched, verified byte-identical)
- T4 corrected (accumulate = anchors from the founder's FROZEN early partition, ARI founder-vs-early 0.701): ARI to founder g1..g5
  rewrite 0.466, 0.314, 0.327, 0.242, 0.198; accumulate 0.382, 0.324, 0.376, 0.399, 0.306. g5 rewrite - accumulate -0.109 [-0.175, -0.048],
  rewrite higher in 5/20. => The registered condition does NOT reproduce the neural K18 pattern: a frozen early record keeps the lineage
  closer to the founder than refreshed anchors do. Per the pre-commitment: the main-text T4 support clause is removed; the negative result
  goes to Table S4 / S3 with the explanation. (The neural 'accumulate' record is re-carved each generation and is not a frozen founder
  snapshot, so the model condition, as registered, was not the right analogue; this is stated, not used to rescue the claim.)
- T2 move cost measured at converged children: same-class anchored neighbour: o already in a's class 0.44 (n=614), mean dE of joining
  otherwise +1.11, dE <= 0 in 0.35; other-class anchored neighbour: 0.13 (n=1798), +1.85, 0.13. The published 'below w' claim is replaced
  by these measured quantities: joining is usually NOT free even for same-class anchors; the class-matched effect appears as a higher
  share already joined and a lower cost of joining, not as a guaranteed downhill move.

## Fig. 4d parent lookup (found by Codex after the first v2 build)
figures.py chose the generation-0 parent of discovery seeds by glob `*_seed{s}.json`; for seeds 4 and 24 this matched a long-generation file, so a step-12000 language of another experiment served as 'parent final'. With the explicit `small__generations` step-2000 language, per-seed Fig. 4d = 0.790 / 0.259 (n = 65), i.e. 79% / 26%, as the audit computed. Text and captions updated from 77/25 to 79/26; Fig. 1b and Fig. 3 regenerated.

## Readiness review fixes (verification_2026_09_05/PUBLICATION_READINESS.md)
1. K18 chronology synchronised in Supplement S1 (Pre-registration), S5 and main Methods: added while the replication was running, before inspection.
2. K12 rule stated fully (|mean| < 0.05 AND CI inside ±0.08); K14 point-estimate bands only.
3. Reproduction instructions: model.py = original T1–T3 (T4 superseded), model_v2.py = corrected T4 + move cost; figures -> figs_v2; replicate.py's tested
   workflow is seeds 100–119; arbitrary fresh seeds not verified end-to-end (Compute, S5, README).
4. Fig. 2b chance computed on the untaught-source cases only: 0.180 (was 0.186 pooled); untaught bar 0.189 unchanged.
5. Captions: n = 30 except capacity 40 / one anchor (n = 29, one seed without an eligible observation); chance-subset note added.
6. Changelog Fig. 4d: the mean shift has one cause (wrong parent endpoint for seeds 4 and 24); the seed unit changes only the s.e.m.
7. Fig. 4 panel b/c titles shortened to avoid overlap.

## Second readiness recheck
Architecture-A lineage tables re-scored (confirm3.py, K_OUT=results_arch, matches the audit's independent numbers): A1/K13a supported in all four families (+0.165/+0.685/+0.398/+0.442) where v1 said partial; K13b analogue large and positive at capacity 40 and for success selection (no verdict registered, kept so). Table S1 K13a +0.643; Supplement version block; METHODS.md synced.
