# Data verification evidence — 2026-09-05

Verdict: the principal neural findings reproduce, but the manuscript is not accurate enough to approve unchanged. This audit changes no manuscript, training code, original result, or registration. All new outputs are confined to this directory.

## Scope and method

Reviewed current `PAPER_short.md`, `PAPER_short_numbers.md`, `PAPER.md`, `SUPPLEMENT.md`, registrations, evaluators, figure code, and the reconstruction model. Read 3,290 run JSONs across nine result directories and eight experiment JSONs. The inventory is not a claim that every exploratory assertion was independently recomputed. Main independent recomputations cover K10–K18 except a full independent recomputation of K13b, the C4 structural effect, C6 collision-free comparisons, second-architecture form effects, and selected figure statistics. K1–K9 and E/L/M results were checked by rerunning their existing evaluators and reviewing the implementations.

`recheck.py` imports no project measure or statistical function. It constructs train splits independently, implements a contingency-table ARI with standard identical-partition handling, uses SciPy's tie-corrected Spearman and assignment solver, and applies 5,000 paired seed-bootstrap resamples with random seed 0. The output field `supported` tests the POSITIVE directional rule only; for negative contrasts reverse the direction, and for K17a use `registered_noninferiority_pass`. K14 and K12 require their own stated mean/interval bands, not the generic directional field.

The existing 31 checks passed. Twelve evaluator executions completed successfully. Ten resulting Markdown files matched the originals byte-for-byte; two differed only in their headings. Reproducing a flawed evaluator is distinguished throughout from validating its statistical definition. Existing evaluators were executed with result writes redirected to `recomputed/`; their reads used original data and saved weights. No new full neural sweep was trained.

There were no generation-0 language mismatches within the audited matching training groups. `input_sha256.json` records hashes of inputs and relevant source/manuscript files. These establish which local files were audited, not an externally verified date of data collection.

## Principal numerical checks

| Claim | Independent recomputation | Assessment |
|---|---|---|
| K16, seeds 30–44: same record > different | 0.459767 vs 0.250978; Δ +0.208788, CI [+0.112508,+0.303702], 13/15 | Confirmed |
| K16: different > none | 0.250978 vs 0.105155; Δ +0.145824, CI [+0.064177,+0.232946], 12/15 | Confirmed under registered rule |
| K16 replication, seeds 100–119 | same−different +0.169776, 18/20; different−none +0.206282, 19/20; both CIs positive | Confirmed |
| K17c, seeds 30–44 | early-target ARI 0.427735 vs 0.209869; Δ +0.217867, CI [+0.160649,+0.277508], 15/15 | Confirmed |
| K17c replication | Δ +0.167946, CI [+0.123583,+0.210931], 19/20 | Confirmed |
| K17a, main learner | early−mature sibling ARI +0.087374, CI [−0.003222,+0.173747]; replication +0.082321, CI [+0.015114,+0.144173] | Passes registered noninferiority-like criterion, not proof of equality |
| K17b, seeds 30–74 | final-target ARI 0.354204 vs 0.275124; Δ +0.079080, CI [+0.039001,+0.119429], 33/45 | Correctly unconfirmed by 80% rule |
| K17b replication | Δ +0.074227, CI [+0.012267,+0.135271], 14/20 | Correctly unconfirmed |
| K13a confirmation | four family gaps +0.229129 / +0.643183 / +0.278483 / +0.426085; 20/20 each | Confirmed |
| K13a replication | +0.196078 / +0.610413 / +0.250935 / +0.394149; 20/20 each | Confirmed |
| K15 confirmation | same-form minus other-form anchor gaps +0.439383 / +0.303462 / +0.367345 / +0.414381; 20/20 each | Confirmed, including mean magnitude ≥0.15 |
| K15 replication | +0.424827 / +0.209574 / +0.361657 / +0.408537; 20/20 except cap40 19/20 | Confirmed under stated directional and mean rules |
| C4, success selection, seeds 10–29 | rewrite−accumulate topsim +0.070506, CI [+0.045455,+0.096474], 17/20 | Confirmed |
| Train-only collision-free geometry, gens 1–5 averaged, seeds 0–29 | accumulate−rewrite: random −0.094528, 28/30 negative; success −0.094884, 27/30 negative | Reproduces reported −0.095; scope differs from Fig. 4a |
| K18, founder at generation 5 | rewrite 0.166731 vs accumulate 0.074705; Δ +0.092026, CI [+0.052821,+0.130467], 16/20 | Confirmed |
| A3′, seeds 120–159 | same forms 0.438542 vs different 0.206250 vs none 0.002604; primary Δ +0.232292, CI [+0.185417,+0.279167], 37/40 | Confirmed |
| A4′ target | early-form alignment Δ +0.088542, CI [+0.069792,+0.107552], 38/40 | Confirmed |
| A4′ strength | early sibling agreement 0.374479 vs mature 0.438542; Δ −0.064062, CI [−0.111979,−0.015625] | Noninferiority criterion fails; short manuscript levels are correct |

Family order above is capacity 8, capacity 40, noise 0.2, reader both. Seed counts follow the preregistered rule, not a replacement requirement that sign-test p must also be below .05. For example 8/10 can satisfy that rule with a positive bootstrap interval even if the two-sided sign-test p is .109.

## Findings requiring correction

### 1. High: nonstandard ARI edge case changes the second-architecture verdict

[confirm3.py:21](../replication/confirm3.py), [probe46.py:20](../replication/probe46.py), and multiple other scripts return zero when both partitions contain only singletons or both have a single class. The standard convention gives 1 for identical partitions up to relabelling. See the [official metric documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html). [tests.py:469](../replication/tests.py) explicitly enforces the singleton-zero convention; it is not an independent safeguard.

On architecture-A seeds 100–119, changing ONLY this edge case changes same-record sibling ARI from 0.054871 to 0.454871, different-record from 0.065329 to 0.165329, and early-record from 0.207238 to 0.257238. Thus the A4 coordination contrast changes from +0.152368, CI [+0.027120,+0.285908], to −0.197632, CI [−0.477479,+0.088956]. The reported pass in [Supplement Table S4](../paper/supplement.md) no longer passes its registered criterion. This corrected interval does not establish a directional decrease under the main rule either.

The A3 primary gap becomes +0.289542, CI [+0.058164,+0.515867], but only 12/20 seeds are positive, so it remains unconfirmed. The broader measurement problem of singleton partitions remains: identical injective partitions say little about actual form identity. Form-level A3′/A4′ findings remain supported. Correct the shared metric and rerun ALL affected partition tables; this audit quantifies the original sibling/snapshot arm effects, not every architecture-A lineage contrast.

### 2. High: K12 changes the registered subgroup; the original subgroup fails replication

[Registration](../replication/results_v3_confirm2/PREREG.md) specifies zero versus **at least two** taught neighbours. [confirm2b.py:40](../replication/confirm2b.py) tests zero versus **three or more** instead. These are different estimands.

Using at least two mature anchors, with exactly the same seed-level pooling as the existing evaluator, gives confirmation Δ +0.038354, CI [+0.008725,+0.068017] (inside the registered equivalence bounds), but replication Δ +0.063654, CI [+0.033197,+0.094407] (outside both |mean|<.05 and CI within ±.08). The 3+ subgroup reproduces the published −0.007324 and +0.022598 and passes its bands. The zero-anchor subgroup fails in both sets, as already disclosed.

Revise [Supplement Table S1 and interpretation](../paper/supplement.md) and the main text's "except no anchors" generalization: the original ≥2 subgroup also fails equivalence in replication. Present 3+ as a separately labelled analysis, preserving the original registration unchanged. This limits the coverage-only explanation without overturning K15's class-matched gap.

### 3. High: T4 implements unrelated fresh partitions rather than a frozen early record

[model.py:77](../replication/model.py) creates `reconstruct({}, RandomState(2000 + 10*s + g), sweeps=1)` anew at every generation of its "accumulate" arm. It neither freezes a founder's early partition nor takes an early state from the current parent's reconstruction trajectory. The current parent `P` is ignored by this source expression.

This conflicts with the [registered frozen-early T4 condition](../replication/results_model/PREREG.md) and [Table S4](../paper/supplement.md). The existing result compares transmission from the current parent against new unrelated constraints. It cannot establish the stated provenance/persistence mechanism. Reimplement the intended lineage relationship and rerun, or remove this correspondence claim. This does not invalidate neural K18.

The model's derivation also needs correction: MODEL.md:23 (`MODEL.md`:23, working repository) says the marginal within-class cost of joining an anchor's class is below w. With c=w=1 and a nonempty destination class of size m, adding an object creates m collision pairs, so that component alone costs m≥1, not less than w. A valid move calculation must include removed pairs from the source class, all changed edges, and any change in the class-count penalty. Greedy endpoints with different ARI do not prove equal-energy global minima. T1–T3 stored summary numbers were inspected, but the model simulation was not independently rerun; do not treat them as independently numerically verified by this audit.

### 4. Medium: wrong A4′ magnitude and misleading K17b interval summary

[Supplement Table S4:280](../paper/supplement.md) reports A4′ strength −0.117 [−0.181,−0.053] and levels 0.35/0.46, inconsistent with its stated 40-seed dataset. Both independent calculation and `confirm8.py` give −0.064062 [−0.111979,−0.015625], levels 0.374479/0.438542. The failure label is unchanged.

[Table S1:214](../paper/supplement.md) says K17b's CI was positive "three times" although the displayed original 15-seed CI includes zero. Two of the three displayed analyses have positive intervals. Also avoid "seed rule never met" without limiting it to confirmation: the registration itself discloses discovery at 26/30.

### 5. Medium: dependent observations used as independent units in K8 and figures

[confirm2.py:95](../replication/confirm2.py) feeds 20 seeds × 6 cells into its fidelity test as n=120. The protocol requires first averaging matched-cell differences within seed. With that correction, confirmation is n=20, Δ +0.051842, CI [+0.039561,+0.064386], 20/20; replication Δ +0.052895, CI [+0.044386,+0.061318], 20/20. Both pass; the correction strengthens the confirmation verdict despite retaining the same mean.

[Figure 2 error bars](../replication/figures.py) use pooled object observations. In the same-form, 3+ anchor stratum there are 5,045 observations but 30 seeds: pooled-object SEM .006874 versus SEM of 30 seed means .014511. These measure different uncertainty and the former does not represent variation across independent runs. [Figure 4 panels b–d](../replication/figures.py) similarly pool generations/cells/siblings within seeds. Recompute bars with a stated seed-clustered estimator and preserve pairing for contrasts. K15's actual confirmatory CI already uses seeds, so its support survives this figure correction.

### 6. Medium: figure references mix populations and estimands

The −0.095 structural contrast is real, but is **train objects only, inherited generations averaged, separate random/success families**. Figure 4a instead uses **all 64 objects, final generation, averaged families**; its recomputed contrast is −0.074434 with 24/30 negative, CI [−0.099273,−0.051015]. Both support the direction, but the quoted number/28-of-30 count should not be identified as the figure's statistic.

The [current Figure 4d code](../replication/figures.py) pools 65 seeds (30 discovery +15 confirmation +20 replication): mature final-form retention .789879 and immature .259109, approximately 79%/26%, whereas the text says 77%/25%. Either use the actual pooled values or identify the separate cohort behind the older pair. Final within-generation record fidelity .661579/.816140 does reproduce the text's .66/.82.

### 7. Medium: positive slopes are not the registered every-step monotonicity claim

The original K11 wording requires increasing retention across 0,1,2,3+ anchors in every cell. [confirm2b.py:35](../replication/confirm2b.py) tests a pooled per-seed linear slope. Those slopes reproduce and are positive in 20/20 seeds per family. However, even after pooling cells, confirmation cap40's three adjacent contrasts have only 13/20 positive seeds each; cap8's 1→2 and 2→3+ have 15/20. Thus the broader every-step/per-cell claim is not established. Report the positive aggregate trend and disclose that it is weaker than the original registration.

K10's uniform-neighbour-form chance rate is also a stipulated reference, not an empirically fitted counterfactual. The existing evaluator pools its chance reference over taught and untaught cases while comparing an untaught rate. Recomputing chance only for untaught cases still gives differences within ±.10 in all four families (confirmation −.0585 to +.0243; replication −.0825 to +.0310), so this particular correction does not overturn its registered band result.

### 8. Medium: equivalence and functional neutrality are overstated

K14's 4/4 mean-band verdict and 3/4 replication reproduce, but the rule uses **point estimates**, not CIs contained inside the small-effect bands. For example whole-class selection at n=45 has Δ geometry about −.028 with an interval reaching roughly −.047. Preserve the preregistered effect-size rule, but do not describe it as a full statistical equivalence test; Table S1 already partly acknowledges this distinction.

[Main §2.1](../paper/paper.md) says collision-free geometry and concept matching are comparable. In confirmation seeds 10–29, rewrite−no-record CBM is +.048177 (random, 18/20), +.069531 (success, 19/20), and +.066146 (hard, 19/20), all positive CIs. Geometry gaps are small and inconclusive. This supports **structure can arise without a record**, but not equivalent structure on every measure. C6's preregistered metric was plain topsim, so its collision-free follow-up should not silently inherit the same confirmatory status.

[Main §2.1:114](../paper/paper.md) further infers that nothing in the task ranks viable alternatives from descriptive object-level accuracies of .92–.95. Similar averages do not establish functional equivalence of complete alternative languages or uniform learner preference. Retain the empirically supported underdetermination and historical bias; label exact functional neutrality as an interpretation needing a direct test. Likewise, class-matched versus other-form anchor comparisons are conditional associations; the underlying record manipulation is causal, but that conditional gap alone does not fully identify mediation or rule out all object difficulty effects.

### 9. Additional reporting and reproducibility limits

`confirm7.py` labels M1 "SUPPORTED" at +.072 despite the registered .15 magnitude threshold. Main text and Table S3 correctly qualify direction versus magnitude; the evaluator's verdict should agree with them. Several evaluators similarly ignore `min_effect` metadata. `replicate.py` reads and prints the manifest, but its thresholds are implemented separately in evaluators; it does not enforce them from that file. K18 is omitted from the manifest and `confirm4.py` ignores the advertised K_SEEDS filter. The driver/evaluators also retain dependencies on original K14/K17 files and hardcoded world seed ranges. These are reproducibility limitations, not evidence that the completed local results were fabricated.

The degeneracy registration's claim that fully Hamming-1 distractors force near-injective languages is mathematically false. The four-label code `(attribute1 + attribute2 + attribute3) mod 4` distinguishes every Hamming-1 neighbour across all 64 objects (zero equal-label H1 pairs, verified exhaustively). It solves these hard-only discrimination rounds without near-injectivity. This is a counterexample about task constraints, not a claim that the present neural learner can learn this code. Report D as a manipulation of distractor geometry, not as demonstrated control of the number of viable partitions. Its registered D1 already remains inconclusive.

Registration files contain detailed disclosure, but the available history has only three commits, with most work in one snapshot. Their text is not independent proof that each threshold preceded observation. This audit does not adjudicate registration chronology, authorship/originality, external citations, or the published PDF/archive package.

## Reproduction and audit outputs

Run from the repository root:

```sh
python3 verification_2026_09_05/recheck.py
python3 verification_2026_09_05/additional_checks.py
python3 verification_2026_09_05/rerun_evaluator.py confirm3.py
K_OUT=results_replicate K_SEEDS=100..119 python3 verification_2026_09_05/rerun_evaluator.py confirm3.py
```

The complete evaluator execution set was: confirm2, confirm2b, confirm3, confirm4, confirm5, confirm6, confirm7, confirm8 with defaults; confirm2, confirm2b, confirm3 and probe46 with K_OUT=results_replicate and K_SEEDS=100..119. Only cached-data branches of probe46 were used. Do not pass arbitrary training scripts to the output-redirection wrapper.

[Independent seed-level results](../verification/independent_results.json), [additional figure/fidelity results](../verification/additional_results.json), and [input hashes](../verification/input_sha256.json) accompany the rerun logs and reproduced Markdown tables. Recommended manuscript conclusion: shared evidence biases independently learned reconstructions and its developmental provenance shifts their target in these tested settings; capacity mediation, precise functional equivalence, and the formal model's persistence mechanism require the corrections above.
