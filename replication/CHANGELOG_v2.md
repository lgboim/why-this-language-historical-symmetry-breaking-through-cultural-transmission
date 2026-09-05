# Changelog: Version 1.0 (2026-09-04, Zenodo 10.5281/zenodo.22305643) → Version 2.0 (2026-09-05, Zenodo 10.5281/zenodo.22338453)

Trigger: the independent data verification of 2026-09-05 (`verification_2026_09_05/REPORT.md`, `EVIDENCE.md`). Plan:
`CORRECTIONS_PLAN_2026_09_05.md`. Working notes and every re-scored table: `corrections_v2/` (originals preserved in
`corrections_v2/originals/` and `corrections_v2/manuscript_v1/`). No neural network was retrained; every number below was recomputed from
saved data with the corrected code, or from the corrected reconstruction model. Version 2.0 was published on 2026-09-05 as new versions of both Zenodo records: preprint 10.5281/zenodo.22338453, code 10.5281/zenodo.22338797; the v1 archive is unchanged.

## Verdict changes

| Claim | Version 1.0 | Version 2.0 | Reason |
|---|---|---|---|
| A4 / K17a analogue, second architecture (Table S4) | +0.152 [+0.027, +0.286], band met, SUPPORTED | −0.198 [−0.477, +0.089], band not met; no directional decrease established either | ARI edge case: identical singleton partitions scored 0 instead of 1 in every local copy of the metric |
| A3 / K16 analogue, second architecture (Table S4) | −0.010 [−0.116, +0.071]; +0.041 [−0.045, +0.151]; inconclusive | +0.290 [+0.058, +0.516] 12/20; +0.141 [−0.005, +0.311] 15/20; still inconclusive | same |
| A4 / K17b analogue | +0.004 | +0.029, inconclusive | same |
| A1 / K13a analogue, second architecture (Table S4) | +0.152 (20/20) / +0.035 (12/20) / +0.028 (15/20) / +0.126 (18/20), "partial: 2 of 4 families" | +0.165 (19/20) / +0.685 (20/20) / +0.398 (20/20) / +0.442 (20/20): supported in all four families | same; identical singleton partitions of parent and child now score 1 |
| H3/C4 analogue (K13b by ARI), second architecture (Table S4) | "inconclusive in all families" (e.g. capacity 40 random +0.091 [+0.010, +0.207]) | capacity 40 random +0.461 [+0.311, +0.597] 19/20, success +0.420 18/20; noise success +0.441 20/20; reader-both success +0.342 17/20; capacity 8 near 0. No verdict, as registered; a partition-inheritance measure, not a structural claim | same |
| K12 (Table S1, Note 3, §2.3, Limitations, Fig. 2c caption) | "≥ 3 anchors" reported as the registered test: equivalent ×2 | registered subgroup ≥ 2: +0.038 [+0.009, +0.068] equivalent in confirmation, +0.064 [+0.033, +0.094] not equivalent in replication; 3+ subgroup relabelled additional (equivalent ×2); 0 anchors failed ×2 | evaluator tested "3+" where the registration says "0 vs ≥2" |
| T4, reconstruction model (Table S4, S3, MODEL.md, §2.4) | "reproduced (neural K18: 0.167 vs 0.075)" | withdrawn: implemented as registered (anchors from the founder's frozen early partition), accumulate stays closer to the founder: g5 0.306 vs rewrite 0.198, −0.109 [−0.175, −0.048], rewrite higher in 5/20 | the v1 "accumulate" arm drew a fresh unrelated shallow partition every generation |
| K8 fidelity (Table S1) | "mixed: CI > 0 both times, seed rule met once" (79% of 115 pooled pairs) | supported ×2: +0.052 [+0.040, +0.064] 20/20; +0.053 [+0.044, +0.061] 20/20 | seed made the independent unit (matched-cell differences averaged within seed) |
| K8 structure (Table S1) | "supported (structure unchanged)" | descriptive: no difference detected; CBM slightly lower in confirmation; no equivalence band registered, equivalence not established | no registered band; one CI below zero |
| M1 evaluator label | "SUPPORTED" at +0.072 | "direction supported, magnitude below the registered 0.15 band" (text already said so) | evaluator ignored the registered magnitude |
| K11 (Table S1) | supported ×2 (slopes) | supported as an aggregate slope; every-step monotonicity per cell not established (adjacent steps 13–15/20 in confirmation for capacity 40 / 8) | registration wording was monotonicity in every cell |

## Number corrections

| Location | Version 1.0 | Version 2.0 |
|---|---|---|
| Table S4, A4′ strength | −0.117 [−0.181, −0.053] (0.35 vs 0.46) | −0.064 [−0.112, −0.016] (0.374 vs 0.439); PAPER.md 0.35→0.37 / 0.46→0.44 |
| Table S1, K17b summary | "CI > 0 three times, seed rule never met" | CI > 0 in the pooled 45-seed and replication analyses, not in the 15-seed confirmation; seed rule not met in any confirmation cohort (discovery 26/30) |
| Table S1, K18 provenance | "registered before the replication run" | "added to the registration while the replication was running, before inspection" |
| Table S1, K13a capacity 40 | +0.640 | +0.643 (metric correction; CI [+0.573, +0.701]) |
| Table S1, K13b capacity 40 hard | +0.055 [−0.019, +0.110] | +0.065 [+0.011, +0.111], still inconclusive (15/20) |
| Table S1, K10 chance reference | pooled over taught and untaught cases | computed on untaught cases only: −0.058 / +0.015 / −0.074 / +0.024 (confirmation), −0.065 / +0.031 / −0.082 / +0.013 (replication); all within ±0.10 |
| Fig. 4a caption | no statistic | this panel's population (all 64 objects, final generation): rewrite − accumulate +0.074, 24/30; the train-object, inherited-generations statistic (−0.095, 28/30) is a different scope |
| Fig. 4d and the text (§2.2, captions) | 77% / 25% | 79% / 26% (n = 65 seeds). The mean changed for one reason: the figure code selected the generation-0 parent by a filename glob which, for seeds 4 and 24, matched a long-generation run instead of the `small__generations` run, so a wrong parent time point was used for those two seeds; corrected to the explicit step-2000 language of the right file. Separately, the independent unit is now the seed (each arm has exactly two siblings per seed, so this changes only the s.e.m., 0.012 / 0.015, not the mean). The same parent lookup fed Fig. 1b (sibling–parent) and Fig. 3 for discovery seeds; their values moved marginally and were regenerated |
| Fig. 2a, 2b, 2c, 4b, 4c, 4d error bars | s.e.m. over pooled objects / generations / siblings | s.e.m. over per-seed means (e.g. Fig. 2a same-form 3+ stratum: 0.0069 → 0.0145; central estimates recomputed as means of per-seed means; capacity 40 with one anchor in Fig. 2c has n = 29). Fig. 2b chance reference now computed on the untaught-source cases only (0.180 instead of 0.186 pooled) |
| Discovery probes 39, 43 (results_v3) | excluded seeds with degenerate ARI; untaught-object sibling values | all 30 seeds; values updated (exploratory descriptives, not cited in the main text) |

## Wording corrections (no number changes)

- Abstract, Introduction, README: "comparably structured solutions/languages" → "multiple structured solutions" / "structured languages".
- §2.1: no-record learners reach "structure of the same order" (collision-free geometry within a few hundredths; concept matching lower by
  0.05–0.07, all CIs positive) instead of "comparable structure"; "so nothing in the task ranks them" replaced by "whether the task ranks
  complete alternative languages was not tested directly"; *viable* defined by the observed structure and accuracy range.
- §2.2, Abstract, Plain Language Summary, Fig. 3 caption, Discussion: K17a is a one-sided no-material-weakening criterion (mean ≥ −0.05,
  CI lower ≥ −0.10), not "equivalence", not "just as well", not "at least as well".
- §2.3: "five rules" → four non-random rules vs one random baseline; the whole-classes rule fell outside the band (−0.031) in replication;
  the same-form vs other-form split is a conditional comparison. "Capacity acts largely through coverage" → "is partly associated with coverage".
- §2.4: T4 support clause removed; metric-correction sentence added for the second learner; "derivations" → "measured move-cost analysis".
- Limitations: registered K12 subgroup did not replicate; model persistence comparison did not reproduce the neural result.
- Methods and Supplementary S1: seed as the independent unit; K17a criterion named precisely; repository history cannot independently date
  thresholds; experiment D manipulates distractor geometry and does not control the number of viable partitions (the injectivity premise
  is false: (a1 + a2 + a3) mod 4 separates every Hamming-1 pair).
- Supplement title block: Version 2.0, September 5, 2026. `METHODS.md` (standalone source) synchronised with the corrected Supplementary Methods.
- Supplementary Methods, second architecture: the reason partition measures are uninformative is that identical injective languages have
  identical singleton partitions (ARI 1), not that "singleton partitions give ARI ≈ 0".
- MODEL.md / S3: the "below w" derivation replaced by the measured move cost (same-class anchored neighbour: already joined 0.44, joining
  cost +1.11, ΔE ≤ 0 in 0.35; other-class: 0.13, +1.85, 0.13); greedy endpoints not claimed to be global minimisers; T1–T3 not
  independently rerun.
- FINDINGS_v3.md: dated correction note appended; historical entries left as written.

## Code changes

- `metrics.py` (new): standard adjusted Rand index; all 14 local copies replaced by imports; `tests.py` asserts identical singleton and
  single-class partitions score 1 (v1 asserted 0). Cross-checked against the verification's independent implementation (max difference 1e-16).
- `confirm2b.py`: registered K12 ≥2 contrast added (3+ kept, labelled additional); K11 adjacent-step contrasts; K10 chance on untaught cases.
- `confirm2.py`: K8 fidelity with the seed as the unit (pooled line kept for the record). `confirm7.py`: M1 magnitude label.
- `confirm4.py`: clear failure when the named cohort has no gen0/gen5 data. `manifest_k.json`: K18 entry with provenance (metadata only).
- `figures.py`: seed-level aggregation for Fig. 2a–c and 4b–d; generation-0 parent read from the `small__generations` file explicitly (the v1 glob matched a wrong file for seeds 4 and 24); writes to `figs_v2/` with `figure_stats.json`; `figs/` (v1) untouched.
- `model_core.py` (definitions only) and `model_v2.py` (corrected T4, measured T2 cost); `model.py` and `results_model/toy_results.md` untouched
  (verified byte-identical); design fixed beforehand in `results_model/T4_correction_design.md`.
- Re-scored reports: `corrections_v2/recomputed/`; originals: `corrections_v2/originals/`; input hashes: `corrections_v2/input_sha256.json`.

## Unchanged (independently reproduced)

K16, K17c, K13a, K15, C4, K18, K17a (GRU), K14 verdicts, A3′, A4′-target, M2, M3, S1–S3, D1–D2 verdicts, and the collision-free C6 direction.

## Not done in this version

No neural retraining; no rerun of model T1–T3; no literature or originality check; the reproducibility limits of `replicate.py`
(dependence on original K14/K17 files, hardcoded seed ranges) are stated, not fixed. Publication of Version 2.0 is a separate decision.
