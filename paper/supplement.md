# Supplementary Material: Why This Language? Historical Symmetry Breaking through Cultural Transmission

**Ariel Elboim**  
Independent Researcher, Israel  
Corresponding author: lgboim@gmail.com  
Working Paper, Version 2.0, September 5, 2026  
Previous version (1.0): [archived preprint](https://doi.org/10.5281/zenodo.22305643)  
Original code and results: [Version 1 archive](https://doi.org/10.5281/zenodo.22305564)

*Companion to the main article. See also the accompanying Version 2 Revision Notes. Contents: S1 Supplementary Methods; S2 Supplementary Tables S1–S4 (every
pre-registered outcome, including failures); S3 the minimal reconstruction model and its move-cost analysis; S4 Supplementary Figure
Legends; S5 registration timeline and reproduction; S6 references. Test codes (K16, A3′, …) are the identifiers used in the
registration files `results_*/PREREG.md` and in `manifest_k.json`. Effects are paired differences by seed with 95% bootstrap CIs
(5,000 resamples); "k/n" is the number of seeds in the predicted direction. The decision rule, fixed in advance, is ≥ 80% of seeds
in the predicted direction AND a CI excluding 0 (directional), or a pre-stated band (equivalence). Verdicts follow that rule
mechanically; where a result missed it but had a CI excluding 0, it is labelled "CI > 0, seed rule not met".*

## S1. Supplementary Methods


### Environment and task
Objects are the full product of 3 attributes × 4 values (64 objects), encoded one-hot (12 dimensions). For each seed, 25%
of the objects (16) are held out: they are never targets during training or teaching, but they do appear as distractors
(distractors are drawn from all other 63 objects), so the receiver sees held-out objects as candidates without ever being
rewarded for picking them. A round is a Lewis referential game: the sender
sees a target and emits a message of 3 symbols from a vocabulary of 8 (512 possible messages); the receiver sees the message
and 5 candidates (the target plus 4 distractors drawn without replacement, uniformly from the other 63 objects) and picks one.
Reward is 1 for a correct pick. Distractor sampling is a bijection (no duplicate distractors; the earlier duplicate bug affected
0.27% of rows and was fixed before all v3 runs).

### Agents
Sender: linear encoder (12 → 64, tanh), a GRU cell (hidden 64) that emits the 3 symbols autoregressively from a start token,
with a linear output head; symbols are sampled during training and taken greedily for all reported languages. Receiver: the
message is embedded and read by a GRU (hidden 64); each candidate is scored independently by a dot product between the message
representation and a linear projection of the candidate's one-hot encoding; the candidate with the highest score is chosen.
Because scoring is independent and deterministic, two objects that share a message always resolve to the same candidate
(the "owner"); this mechanical fact defines ownership and orphans (Supplementary Note 1).

### Training
Each generation is a fresh sender–receiver pair (new initialisation), trained for 2,000 steps on batches of 64 rounds over the
training objects. The receiver is trained by cross-entropy; the sender by REINFORCE with a moving-average baseline (0.95) and
an entropy bonus of 0.02 (the boundary experiment E varies this to 0.005 and 0.08). Adam, learning rate 1e-3. Six generations
per lineage. Random streams: the world split, the training batches, and the record each have their own seeded generators, so
generation 0 is bit-identical across all transmission conditions of a seed, and every cross-condition comparison is paired by seed.

### Transmission channel ("record")
Between generations, the child sender is taught up to *capacity* (8 / 19 / 40) (object, message) pairs by 200 supervised steps
(learning rate 3e-3) before its own training starts; optionally the child receiver is also taught to pick the recorded object
among distractors ("reader = both"). Six factors define the channel: **selection** of which objects occupy record slots (random;
by communicative success; "hard" = lowest per-object accuracy), **slot dynamics** (fixed for the lineage; redrawn each
generation; dynamic = re-selected each generation), **freshness**, which takes two values. *Accumulate*: during the parent's training, every *successful* round (object o, message m) is offered to the
record. If o is not recorded and a slot is free, (o, m) is stored with a success count of 1. If o is recorded with the same
m, its count is incremented. If o is recorded with a different m, the incumbent is replaced only if its count is below 2 (a
single success); otherwise the new form is discarded. If o is not recorded and the record is full, the entry with the lowest
count is evicted only if that count is below 2; ties among counts are broken by dictionary order (first minimum), never by
recency. Counts grow into the thousands, so an entry that succeeded twice is in practice permanent. At the end of a generation
empty slots are filled with the parent's final greedy forms. *rewrite*: every slot is overwritten with the parent's final greedy
form at the end of the generation (count reset to 1). The remaining factors are **capacity**, **noise** (each recorded symbol independently corrupted with
probability 0 / 0.2), and **reader** (sender / both). The named v2 conditions (pair, population, generations, oral, oral_fixed,
bone, bone_edition) are cells of this grid. A "generations" cell has no record (fresh pair every generation); "pair" trains a
single pair for 12,000 steps.

### Logging
Every 250 steps: the sender's full greedy language (64 messages), the receiver's decode map (which of the 64 objects each of the
64 messages resolves to), message entropy, train / held-out accuracy. At every generation end: per-object accuracy, record
contents, slot set, transmitted objects, and both agents' weights.

### Measures
- **topsim**: Spearman correlation (tie-corrected) between attribute Hamming distances and message Hamming distances over all
  pairs of the 64 objects (held-out included; the sender produces a greedy message for every object); reported for comparability but inflated by semantically local message collisions (Supplementary Note 2).
- **topsim_distinct**: the same over pairs with distinct messages only (collision-free geometry).
- **CBM** (concept–best matching): over all 64 objects, a 24 × 12 co-occurrence matrix between (position, symbol) and
  (attribute, value) is built from the greedy language; a one-to-one Hungarian assignment maximises total co-occurrence, and
  CBM is that total divided by 64 × 3 (the number of symbol slots), so CBM = 1 iff every symbol slot is explained by one
  (attribute, value) under a consistent assignment. Sibling and content-rule comparisons additionally report topsim_distinct
  and CBM restricted to the 48 training objects where stated.
- **convexity**: share of message classes (≥ 3 objects) that are connected in the Hamming-1 graph of objects.
- **decode map / ownership**: for each of the sender's 64 greedy messages, the receiver scores all 64 objects as candidates
  and the arg-max is the decoded object (floating-point arg-max, deterministic). Object o *owns* its message if the decode
  of its own message is o; otherwise o is an *orphan* and the decoded object is its owner.
- **ARI**: adjusted Rand index (Hubert & Arabie) between two languages' partitions of the 48 training objects into
  same-message classes; used for parent–child, sibling–sibling, and generation-gap comparisons. Held-out objects are excluded
  because their forms are never reinforced.
- **continuity**: the last generation's receiver plays 512 rounds with the generation-0 sender's greedy messages: targets are
  training objects, candidates are the target plus 4 distractors drawn from all other 63 objects (held-out included), with a
  fixed evaluation seed; continuity is the accuracy. Chance is 0.20.
- **anchor**: a taught training object that is a Hamming-1 (one attribute differs) training neighbour of an untaught training
  object. **Class-matched (same-form) anchor**: an anchor whose recorded form equals the untaught object's own parent form,
  i.e. both belong to the same message class in the parent. **Provenance** of an anchor is the parent training step at which
  its recorded form was sampled: *mature* = the parent's final (step-2,000) form; *immature* = the step-500 form (snapshot
  design) or, in accumulate cells, the carved form, which typically differs from the parent's final form. Anchor counts in
  K10–K12 and K15 use mature anchors only (recorded form == parent's final form); the snapshot design (K17) varies
  provenance while holding the anchor set fixed.

### Experiments
- Factorial sweep: 77 cells × 10 seeds (`results_v3`); confirmation 1: 10 cells × 20 new seeds (`results_v3_confirm`);
  confirmation 2: 24 cells × 20 seeds (`results_v3_confirm2`); content-rule, sibling and snapshot experiments on seeds 30–74
  (parents trained fresh); independent replication on seeds 100–119 by one command (`replicate.py`; K16 and K17a/c were added to the driver after that run and evaluated from its raw files, the K16 sibling arms
  being trained afterwards from the same saved parents).
- **Sibling design**: two children with different initialisations and training streams are taught from the same parent (end of
  generation 0): the same 19 random training objects with the parent's final forms; two different random 19-sets; or nothing.
- **Snapshot design**: the same 19 objects taught with the parent's forms at step 500 (immature; 72% differ from the final forms)
  vs at step 2,000 (mature).
- **Content rules**: 19 taught objects chosen at random / owners only / orphans only / whole homonym classes / the 19 most stable.

### Medium world (boundary experiment M)
4 attributes × 4 values = 256 objects (64 held out), vocabulary 8, message length 4, 4,000 steps per generation, capacity 77 (≈ 40% of
the 192 training objects, the analogue of 19/48). Half of all rounds (hard_frac = 0.5) draw their 4 distractors from the target's
Hamming-1 neighbours, so a single attribute cannot identify the target; the remaining rounds are standard. Cells: the six record
cells at capacity 77 and the no-record generation; seeds 0–9; hypotheses M1–M4 registered before running (`results_medium/PREREG.md`).
Siblings for M2 are trained as in the main design with 77 taught pairs.

### Second architecture (experiment A)
Sender: a two-layer MLP (12 → 64 → 64, tanh) with a linear head producing 3 × 8 logits, one softmax per message position (no
recurrence); messages are sampled with straight-through Gumbel-softmax (temperature 1) during training and taken greedily for all
reported languages. Receiver: the one-hot message (24 dimensions) is mapped by a two-layer MLP (24 → 64 → 64, tanh) to a message
representation, and each candidate is scored by a dot product with a linear projection of its one-hot encoding, as in the GRU
receiver. Both agents are trained end-to-end by the receiver's cross-entropy alone (Adam, 1e-3, batch 64, 2,000 steps); there is no
REINFORCE term and no entropy bonus. Teaching (200 supervised steps on the record) and all channel factors are unchanged. The learner
produces nearly injective languages (59 of 64 messages distinct on average; 4% of training objects have a same-form neighbour vs 75%
for the GRU); because partition measures are uninformative in this regime (two fully injective languages have identical singleton partitions and
hence ARI = 1 regardless of their forms; the calculations in Version 1.0 assigned 0 to this edge case, corrected on 2026-09-05), the pre-registered ARI tests (A1–A4) were supplemented, after
this was observed and before new seeds were run, by form-level tests (A3′, A4′: exact-form agreement between siblings and with the
parent's step-500 forms) on seeds 120–159. Registration and decision tree: `results_arch/PREREG.md`.

### Degeneracy scan (boundary experiment D)
Same GRU learner and 64-object world, seeds 0–19, with hard_frac = 0 / 0.5 / 1.0 (the share of rounds whose 4 distractors are
Hamming-1 neighbours of the target); a fresh generation-0 parent is trained under each hard_frac, and the sibling design (same 19 /
different 19 / none) is run once per parent. Measures: the partition-level sibling gap (ARI, same − different) and the form-level gap
(exact-form agreement, same − different). D1 (partition gap decreases monotonically with hard_frac, ≥80% of seeds per adjacent pair) and
D2 (form gap within a pre-set equivalence band) were registered before running (`results_degeneracy/PREREG.md`). Correction (2026-09-05): D manipulates
distractor geometry; it does not control the number of viable partitions. The registration's premise that Hamming-1 distractors force near-injective
languages is false: the code (attribute1 + attribute2 + attribute3) mod 4 separates every Hamming-1 pair with four labels (a statement about the task,
not about what this learner can learn). D1 remains inconclusive under the corrected metric.

### Pre-registration and decision rule
Two kinds of pre-registration are distinguished in the registration files. *Registered before the runs*: H1–H9 (factorial
sweep), C1–C6 (confirmation 1), K1–K9 (confirmation 2), K14, K16 and K17 (new seeds), and E1–E4. K18 was added to the registration file
while the replication (seeds 100–119) was already running and before anything from it had been inspected (addendum of 2026-09-04). *Registered before
computation on held-back data*: K10–K13 and K15, quantities discovered post hoc on seeds 0–29 of the cap-19 cells and then
fixed in writing before being computed on the confirmation-2 cells (capacity 8/40, noise, reader), which had not been used for
those quantities; the registration notes what had already been inspected on that sweep (its K1–K9 metrics). All registrations
are in `results_*/PREREG.md` and the thresholds are frozen in `manifest_k.json`.
A directional hypothesis is supported if ≥ 80% of seeds fall in the predicted direction and the paired bootstrap 95% CI (5,000
resamples) excludes 0; equivalence hypotheses state their band in advance. Results that miss the seed rule but have a CI
excluding 0 are reported in full and labelled as such. The K17a criterion (mean ≥ −0.05 and CI lower bound ≥ −0.10) is one-sided, a no-material-weakening
criterion rather than a symmetric equivalence test, although the registration file calls it "equivalence". K14 uses point-estimate bands with no interval condition; K12 requires both
|mean| < 0.05 and a CI inside ±0.08. All
uncertainty statements use the seed as the independent unit (corrected on 2026-09-05 for K8 and the figure error bars). The repository history available at the
verification of 2026-09-05 has three commits and cannot independently date each threshold; the registration files document the stated chronology. The theory was frozen on 2026-09-04; later experiments are robustness
and boundary tests only.

### Compute
CPU only (10-core laptop); a 6-generation run takes ~2 minutes; 10 parallel workers. All code, registrations and results are in
the repository; `replicate.py --seeds A..B` runs the sweep, the child, sibling and snapshot experiments and the evaluators K1–K18. The
tested workflow is seeds 100–119 as actually run (K16 and K17a/c were added to the driver after that run and evaluated there from the
same saved parents). The driver still depends on the original K14/K17 raw files and on hardcoded seed and world ranges, so replication on an
arbitrary fresh seed range has not been verified end-to-end (verification of 2026-09-05).


**Supplementary Note 1 (ownership).** Because the receiver scores candidates independently and deterministically, every message
resolves to exactly one object over the full 64-object candidate set. An object *owns* its message if its own message decodes to
itself; otherwise it is an *orphan* of the decoded object, its *owner*. Ownership is therefore a mechanical consequence of the
receiver architecture; the consequences reported in the main text (borrowing of a neighbour's form, elimination of orphans,
class-level inheritance) are not.

**Supplementary Note 2 (topsim inflation).** Plain topographic similarity counts pairs of objects that share a message as
maximally similar in message space. In a compressed language such collisions are semantically local, so topsim rises with
compression even when the collision-free geometry does not. All structure claims in the main text therefore use topsim_distinct
(pairs with distinct messages only) and CBM; plain topsim is reported only where a registered hypothesis named it (H1–H9, C1–C6).

**Supplementary Note 3 (anticipated objections and where the evidence stands).**
1. *Early target without loss of final alignment (K17c vs K17b).* Immature anchors redirect siblings toward the parent's step-500
   partition decisively (ARI 0.43 vs 0.21, 15/15 and 19/20), but the predicted reduction in alignment with the parent's final partition
   reached only 70–73% of seeds with a CI above zero (Table S1). The reconstruction model illustrates one reason this need not occur: where the early and final partitions of a parent overlap (ARI 0.70 in the model), moving toward the early state need not move away from the final one; whether the neural partitions overlap to the same degree was not measured. The main text reports K17b as consistent but unconfirmed.
2. *Capacity as coverage (K12).* The additional pooled subgroup with three or more mature anchors met the equivalence bands in both cohorts.
   The registered subgroup (two or more) met them in confirmation but not in replication (+0.064 [+0.033, +0.094]); objects with no anchor retain the
   parent's form less at capacity 40 than at capacity 8 (−0.10 to −0.12, twice). The bins overlap, so no cutoff at exactly three anchors is inferred. One hypothesis, not tested here, is that at high capacity an unanchored object sits among many taught neighbours of other
   classes and is pulled by them, whereas at low capacity it is free to drift. The failure is reported in the main text and in
   Table S1; the coverage claim is scoped to well-anchored objects and stated as an association.
3. *One-shot decay vs recurring persistence (S1–S3 vs K18).* A single immature snapshot at generation 1 redirects strongly (ARI to
   the snapshot 0.40 vs 0.23) but the redirection is inconclusive by generation 3 under refreshed records, whereas an accumulating
   record re-supplies immature provenance every generation and its founder signature is measurably weaker at generation 5 (K18).
   The persistence claim in the main text is therefore scoped to recurring immature provenance; redirection weakens after refreshed transmission, and the longer-term persistence of a one-shot event remains inconclusive.
4. *The near-injective learner (A1–A4).* The MLP learner's languages have almost no message classes, so partition measures are
   uninformative by construction and class-matched anchoring has nothing to act on. Form-level tests registered on fresh seeds show
   that symmetry breaking (A3′) and the provenance-target shift (A4′) survive; what does not survive is the class-matched mechanism
   and the "coordination without loss" finding. This is presented as a regime boundary, not as a failure of the claim, because the
   boundary was predicted in the decision tree committed before the results were read (`results_arch/PREREG.md`).

## S2. Supplementary Tables

### Table S1. Core pre-registered tests on the main (GRU) learner: confirmation cohort and independent replication

Confirmation cohorts: K1–K13 and K15 on seeds 10–29 (`results_v3_confirm2`, 20 seeds, four channel families: capacity 8,
capacity 40, noise 0.2, reader = both, each compared with its capacity-19 baseline where applicable); K14, K16, K17 on seeds
30–44 with parents trained fresh (15 seeds), K14 and K17b extended to seeds 30–74 (n = 45). Replication: seeds 100–119 by one
command (`replicate.py`), 20 seeds. Family order in multi-family cells: capacity 8 / capacity 40 / noise 0.2 / reader both.

| id | prediction (metric) | confirmation cohort | replication (seeds 100–119) | verdict |
|---|---|---|---|---|
| K1 | capacity 8 < capacity 19 (topsim_distinct) | −0.072 [−0.089, −0.055], 20/20 | −0.075 [−0.092, −0.057], 19/20 | supported ×2 |
| K2 | capacity 19 = capacity 40, two-sided (topsim_distinct) | −0.017 [−0.033, −0.003]: 40 higher | −0.027 [−0.044, −0.010]: 40 higher | not supported (40 slightly higher, CI excludes 0, both cohorts) |
| K3 | capacity 19 > 40 (CBM) | +0.024 [+0.015, +0.034], 17/20 | +0.015 [+0.003, +0.027], 13/20 | supported once; weakened in replication (CI > 0, seed rule not met) |
| K3 | capacity 19 > 40 (owners-only topsim) | +0.028 [+0.005, +0.049], 14/20 | +0.019 [−0.002, +0.038], 14/20 | inconclusive ×2 |
| K4 | founder intelligibility 40 > 19 > 8, each step ≥ +0.15 (continuity) | +0.195 and +0.205, 20/20 each | +0.228 and +0.194, 20/20 each | supported ×2 |
| K5 | corr(continuity, topsim_distinct) > 0; corr(continuity, convexity) < 0, across 30 cells | +0.86 / −0.68 | +0.88 / −0.67 | supported ×2 (descriptive correlations, no CI) |
| K6 | noise 0.2 < noise 0 (topsim_distinct) | −0.010 [−0.025, +0.006], 15/20 | −0.013 [−0.022, −0.004], 12/20 | not supported (seed rule not met ×2) |
| K6 | noise 0.2 < noise 0 (CBM) | −0.023 [−0.030, −0.015], 17/20 | −0.020 [−0.026, −0.013], 17/20 | supported ×2 |
| K7 | noise 0.2 > noise 0 (number of owners) | +4.8 [+3.6, +5.9], 19/20 | +4.4 [+3.4, +5.5], 19/20 | supported ×2 |
| K8 | reader = both vs sender: no difference (topsim_distinct, CBM, held-out accuracy) | no difference ×2; CBM −0.008 [−0.014, −0.001] | no difference ×3 | descriptive: no difference detected for geometry and held-out accuracy; CBM slightly lower in confirmation, inconclusive in replication; no equivalence band was registered, so structural equivalence is not established |
| K8 | reader = both > sender: fidelity of taught forms | +0.052 [+0.040, +0.064], 20/20 seeds | +0.053 [+0.044, +0.061], 20/20 | supported ×2 (seed as the unit, matched-cell differences averaged within seed; Version 1.0 pooled 120 dependent seed × cell pairs) |
| K9 | accumulate > rewrite (convexity) | +0.010 [−0.052, +0.076], 9/20 | −0.011 [−0.059, +0.038], 9/20 | failed ×2 |
| K9 | capacity 8 > 40 (convexity) | +0.216 [+0.165, +0.266], 20/20 | +0.152 [+0.095, +0.209], 17/20 | supported ×2 |
| K10 | child repeats the parent's borrowed choice: taught source − untaught source ≥ 0.15; untaught within 0.10 of chance | +0.40 / +0.38 / +0.36 / +0.40, 20/20 ×4; untaught − chance −0.06 to +0.02 (chance computed on the untaught cases only) | +0.38 / +0.30 / +0.36 / +0.41, 20/20 ×4; −0.08 to +0.03 | supported ×2 (family-pooled; the registered "in every cell" wording was not tested cell by cell; chance is a stipulated uniform-neighbour reference) |
| K11 | per-seed slope of retention on number of taught neighbours > 0 (registered as monotone in every cell) | slope +0.08 / +0.12 / +0.07 / +0.09 per anchor, 20/20 ×4; adjacent steps (family-pooled per seed) weaker: capacity 40 13/20 per step, capacity 8 15/20 for 1→2 and 2→3+ | slope +0.07 / +0.12 / +0.07 / +0.10, 20/20 ×4; adjacent steps 15–20/20 | supported as an aggregate slope; every-step monotonicity per cell not established |
| K12 | retention at equal anchor count, capacity 40 = capacity 8 (equivalence: \|mean\| < 0.05, CI within ±0.08); registered subgroups 0 vs ≥ 2 | ≥ 2 anchors (registered): +0.038 [+0.009, +0.068] supported; ≥ 3 anchors (additional, non-registered): −0.007 [−0.052, +0.036] supported; 0 anchors: −0.124 [−0.149, −0.097] failed | ≥ 2: +0.064 [+0.033, +0.094] failed; ≥ 3: +0.023 [−0.012, +0.055] supported; 0: −0.101 [−0.116, −0.085] failed | registered subgroup equivalent once out of twice; additional 3+ subgroup equivalent twice; zero-anchor stratum failed twice (Version 1.0 reported only the 3+ subgroup as the registered test) |
| K13a | parent–child ARI, rewritten record − no record > 0 | +0.229 / +0.643 / +0.278 / +0.426, 20/20 ×4 | +0.196 / +0.610 / +0.251 / +0.394, 20/20 ×4 | supported ×2 |
| K13b | parent–child ARI, rewrite − accumulate > 0 (random / success selection) | capacity 40: +0.394 (20/20), +0.371 (19/20); noise: +0.046 (13/20), +0.103 (19/20); reader both: +0.133 (15/20), +0.108 (16/20); capacity 8: −0.024 (9/20), −0.103 (4/20) | capacity 40: +0.375 (19/20), +0.389 (20/20); noise: +0.088, +0.065 (16/20 each); reader both: +0.112 (15/20), +0.064 (13/20); capacity 8: −0.013 (9/20), −0.061 (6/20) | supported at capacity 40; reversed at capacity 8 ×2 (the coverage boundary, main text §2.4); mixed elsewhere |
| K14 | content rule vs random 19: \|Δtopsim_distinct\| < 0.03 and \|ΔCBM\| < 0.02 for ≥ 3 of 4 rules (point-estimate bands; CIs not required inside the band) | seeds 30–44: 2/4 (failed); seeds 30–74 pooled: 4/4 (supported) | 3/4 (whole classes: Δtopsim_distinct −0.031, outside the band) | supported at n ≥ 20 after failing at n = 15; small effects of item choice, not an equivalence test |
| K15 | retention with ≥ 1 same-form anchor − with other-form anchors only ≥ 0.15 | +0.439 / +0.303 / +0.367 / +0.414, 20/20 ×4 (same / other: 0.56/0.12, 0.57/0.26, 0.46/0.09, 0.60/0.19) | +0.425 / +0.210 / +0.362 / +0.409; 20, 19, 20, 20 of 20 | supported ×2 |
| K16 | sibling ARI: same record − different records > 0 (primary); different − none > 0 (secondary) | seeds 30–44: +0.209 [+0.113, +0.304], 13/15; +0.146 [+0.064, +0.233], 12/15 (levels 0.460 / 0.251 / 0.105) | +0.170 [+0.106, +0.236], 18/20; +0.206 [+0.151, +0.263], 19/20 (levels 0.428 / 0.259 / 0.052; sibling arms trained from the saved replication parents) | supported ×2 |
| K17a | sibling ARI, immature − mature anchors: one-sided no-material-weakening criterion (mean ≥ −0.05, CI lower ≥ −0.10; called "equivalence" in the registration) | +0.087 [−0.003, +0.174] (0.547 vs 0.460) | +0.082 [+0.015, +0.144] | criterion met ×2 (no material weakening detected; not evidence of equality) |
| K17b | child–parent(final) ARI, mature − immature > 0 | seeds 30–44: +0.039 [−0.042, +0.126], 9/15; pooled n = 45: +0.079 [+0.039, +0.119], 33/45 (73%) | +0.074 [+0.012, +0.135], 14/20 (70%) | not confirmed: CI > 0 in the pooled 45-seed and replication analyses, not in the 15-seed confirmation alone; seed rule not met in any confirmation cohort (discovery reached 26/30) |
| K17c | child–parent(step 500) ARI, immature − mature > 0 | +0.218 [+0.161, +0.278], 15/15 (0.428 vs 0.210) | +0.168 [+0.124, +0.211], 19/20 | supported ×2 |
| K18 | ARI(gen 0, gen 5): rewrite − accumulate > 0 (a); rewrite > 0.10 and accumulate < 0.10 (b) | added to the registration while the replication was running, before inspection (registration addendum of 2026-09-04); no earlier cohort | (a) +0.092 [+0.053, +0.130], 16/20; (b) 0.167 vs 0.075 | supported (one cohort, exactly at the 80% rule) |

### Table S2. Earlier registrations: factorial sweep (H1–H9, seeds 0–9) and first confirmation (C1–C6, seeds 10–29)

These hypotheses were written before the v3 sweep and were the source of the K-series. Metrics are those named in the
registration (plain topsim where stated; see Supplementary Note 2 for why later tests use topsim_distinct).

| id | prediction (metric) | seeds 0–9 (n = 10) | seeds 10–29 (n = 20) | verdict |
|---|---|---|---|---|
| H1 | random record slots beat success-selected slots (topsim) | −0.007 [−0.013, −0.002], 3/10 | not run | inconclusive |
| H2 | a smaller record yields a more compositional language (topsim) | −0.016 [−0.024, −0.008], 8/10 in predicted direction | not run | met the rule, then **retracted**: the gain is collision inflation of plain topsim; topsim_distinct reverses it (K1) |
| H3 | rewriting from the final language beats accumulating carved forms (topsim) | +0.039 [+0.033, +0.045], 10/10 | C4: +0.071 [+0.045, +0.096], 17/20 | supported ×2 (the Snapshot Effect, structural cost) |
| H4 | noise repairs an accumulating record (topsim) | −0.039 [−0.051, −0.025], 1/10 | not run | refuted |
| H5 | a record both agents read changes held-out accuracy (two-sided) | −0.004 [−0.022, +0.014] | K8: no difference | no difference ×2 |
| H6 | every record compresses the lexicon vs no transmission (unique messages) | −16.2 [−18.2, −14.2], 10/10 | not run | supported |
| H7 | fixed random slots beat success-rewritten slots (v2 replication; topsim) | −0.014 [−0.045, +0.016], 5/10 | C5: −0.020 [−0.047, +0.005], 9/11 | not replicated (no difference) |
| H8 | recording the hardest objects helps held-out accuracy (test_acc) | −0.044 [−0.065, −0.019], 1/10 | not run | refuted |
| H9 | rewritten records are more mutually intelligible (intelligibility) | +0.032 [+0.018, +0.045], 9/10 | not run | supported on 10 seeds; superseded by K4/K5 (continuity), not used in the main text |
| C1 | hard + rewrite > random + rewrite (topsim) | +0.039 [−0.002, +0.084], 5/10 | +0.027 [−0.004, +0.054], 14/20 | inconclusive ×2 |
| C2 | hard + rewrite > random + rewrite (test_acc) | +0.088 [+0.049, +0.130], 9/10 | +0.019 [−0.035, +0.068], 12/20 | not replicated |
| C3 | hard + rewrite > success + rewrite (test_acc) | +0.104 [+0.045, +0.169], 9/10 | +0.010 [−0.048, +0.071], 9/20 | not replicated |
| C4 | success + rewrite > success + accumulate (topsim) | +0.085 [+0.046, +0.132], 10/10 | +0.071 [+0.045, +0.096], 17/20 | supported ×2 |
| C5 | random-fixed + rewrite vs success + rewrite, two-sided (topsim) | −0.014, no difference | −0.020, no difference | no difference ×2 |
| C6 | each record cell vs the no-record generation, two-sided (topsim) | accumulate cells below (−0.043, −0.064); rewrite cells no difference; hard + rewrite above (+0.046) | random + accumulate −0.049 [−0.068, −0.031] (2/18); success + accumulate −0.035; random + rewrite +0.016 (no difference); success + rewrite +0.036; hard + accumulate +0.035; hard + rewrite +0.043 | a no-record generation reaches structure comparable to record lineages: rewrite cells within a few hundredths, accumulating cells below (main text §2.1) |

### Table S3. Boundary experiments E, L, S, M, D (all registered before running)

| id | manipulation and prediction | result | verdict |
|---|---|---|---|
| E1 | entropy bonus 0.005 / 0.02 / 0.08: rewrite > accumulate in topsim_distinct at each | 0.005: +0.047 [+0.026, +0.068], 21/30 (extended to n = 30 as registered); 0.02: +0.085 [+0.042, +0.131], 9/10; 0.08: +0.041 [+0.027, +0.058], 10/10 | supported at 0.02 and 0.08; at 0.005 CI > 0 but 70% of seeds: weakened where the parent barely changes after capture (26% stale entries vs 35% and 41%) |
| E2 | standardisation is imitation: child entropy at step 250 < 0.5 × generation-0 entropy | 100% of seeds at all three coefficients | supported |
| E3 | within-generation form change per 250 steps is monotone in the bonus | 0.102 / 0.129 / 0.289; 0.02 − 0.005: +0.027, 9/10; 0.08 − 0.02: +0.160, 10/10 | supported |
| E4 | class-matched anchor gap ≥ 0.15 at each coefficient | +0.389 (30/30), +0.385 (10/10), +0.218 (10/10) | supported |
| L1 | 6,000-step generations: rewrite > accumulate in topsim_distinct at generation end | n = 10: +0.042 [+0.005, +0.076], 7/10 (inconclusive); extended to n = 30 as registered: +0.053 [+0.031, +0.073], 24/30 | supported; stale entries at generation end 53% (vs 35% at 2,000 steps) |
| L2 | fidelity to the record keeps eroding: step 6,000 < step 2,000 | +0.158 [+0.150, +0.167], 30/30 | supported |
| L3 | class-matched anchor gap ≥ 0.15 at generation end | +0.251 [+0.221, +0.280], 30/30 | supported |
| S1 | one-shot immature snapshot at generation 1, refreshed records after: redirection toward the snapshot persists at generation 3 | ARI to step-500 partition, immature − mature lineage: g1 0.397 vs 0.225; g3 +0.060 [+0.005, +0.122], 19/30 | inconclusive (fades within two generations) |
| S2 | the immature lineage is less aligned with the parent's final language at generation 5 | −0.037 [−0.083, +0.004], 11/30 (0.175 vs 0.139, reversed) | not supported |
| S3 | generation-to-generation ARI unaffected (equivalence \|mean\| < 0.05, CI within ±0.08) | +0.056 [+0.013, +0.096] | band missed in the favourable direction (immature lineage more coordinated) |
| M1 | medium world (256 objects, hard distractors in 50% of rounds): class-matched anchor gap ≥ 0.15 | +0.072 [+0.018, +0.117], 9/10 | direction supported, magnitude below the band set on the small world |
| M2 | sibling ARI same > different (primary), different > none (secondary) | +0.103 [+0.042, +0.164], 8/10; +0.161 [+0.106, +0.220], 10/10 | supported |
| M3 | parent–child ARI, rewrite − no record > 0 | +0.288 [+0.234, +0.339], 10/10 | supported |
| M4 | rewrite > accumulate in topsim_distinct | +0.021 [−0.003, +0.045], 7/10 (stale entries 56% vs 35%) | inconclusive at n = 10 |
| D1 | hard-distractor share 0 / 0.5 / 1.0: partition-level sibling gap (same − different) decreases monotonically | gaps 0.255 → 0.142 → 0.087; 0 − 0.5: +0.113 [−0.012, +0.234], 14/20; 0.5 − 1.0: +0.055 [−0.049, +0.157], 12/20 | inconclusive (trend in the predicted direction) |
| D2 | form-level sibling gap does not decrease (equivalence \|mean\| < 0.10, CI within ±0.15) | 0.286 → 0.222 → 0.220; 1.0 − 0: −0.067 [−0.141, +0.003] | supported |
| D3 | descriptive: regime change | distinct messages 38.2 / 47.3 / 44.7 of 64; owner share 0.49 / 0.64 / 0.58 | the GRU does not reach injectivity even at 100% hard rounds |

### Table S4. Second architecture (A) and minimal reconstruction model (T)

Second architecture: MLP sender and receiver with straight-through Gumbel-softmax, no REINFORCE, no entropy bonus (Supplementary Methods, "Second architecture"). Seeds 100–119 for A1–A4 and the K10–K12 analogues; seeds 120–159 (n = 40) for the form-level tests A3′/A4′,
registered after the near-injectivity of this learner was seen on seeds 100–119 and before the new seeds were run. Descriptive
regime: 59.3 of 64 messages distinct; 4% of training objects have a same-form neighbour (GRU: 75%).

| id | prediction | result | verdict |
|---|---|---|---|
| A1 (= K13a) | parent–child ARI, rewrite − no record > 0, four families | corrected metric: +0.165 [+0.116, +0.211] (19/20) / +0.685 [+0.646, +0.723] (20/20) / +0.398 [+0.315, +0.480] (20/20) / +0.442 [+0.364, +0.524] (20/20) (Version 1.0, singleton-zero convention: +0.152 (20/20) / +0.035 (12/20) / +0.028 (15/20) / +0.126 (18/20), "partial") | supported in all four families under the corrected metric; partition inheritance holds in the near-injective learner |
| A2 (= K15) | class-matched anchor gap ≥ 0.15 | +0.203 (18/20) / −0.076 (7/19) / +0.015 (11/20) / +0.057 (11/20) | vanishes except at capacity 8: a regime boundary of the mechanism |
| K10 analogue | anchored choice, taught − untaught source | +0.238 (20/20) / +0.256 (13/16) / +0.221 (19/20) / +0.202 (19/20) | 3 of 4 families |
| K11 analogue | retention slope on taught neighbours > 0 | +0.10 / +0.15 / +0.11 / +0.10, 20/20 ×4 | supported |
| K12 analogue | retention at equal anchor count, capacity 40 = 8 | 0 anchors: +0.030 [−0.002, +0.062] (equivalent); ≥ 3 anchors: +0.203 [+0.150, +0.261] (differs) | pattern reversed relative to the GRU; reported for completeness |
| A3 (= K16, ARI) | sibling ARI same > different; different > none | corrected metric: +0.290 [+0.058, +0.516], 12/20; +0.141 [−0.005, +0.311], 15/20 (Version 1.0, singleton-zero convention: −0.010; +0.041) | inconclusive both ways; near-singleton partitions limit what partition agreement can reveal about form coordination (see A3′) |
| A4 (= K17a/c, ARI) | immature anchors: coordination within band; alignment to step-500 partition higher | corrected metric: K17a −0.198 [−0.477, +0.089] (band NOT met; Version 1.0 reported +0.152 [+0.027, +0.286] under the singleton-zero convention); K17c +0.113 [+0.046, +0.187], 15/20; K17b +0.029 | K17a band not met and no directional decrease established either; K17c CI > 0, seed rule not met; superseded by A4′ |
| A3′ | form-level sibling agreement: same − different > 0 (primary); different − none > 0 (secondary) | +0.232 [+0.185, +0.279], 37/40; +0.204 [+0.173, +0.239], 40/40 (levels 0.44 / 0.21 / 0.00; GRU 0.47 / 0.25 / 0.01) | supported |
| A4′ target | sibling agreement with the parent's step-500 forms, immature − mature > 0 | +0.089 [+0.070, +0.108], 38/40 | supported |
| A4′ strength | sibling–sibling form agreement, immature − mature: not more than 0.05 below (CI lower ≥ −0.10) | −0.064 [−0.112, −0.016] (0.374 vs 0.439) (Version 1.0 printed −0.117 [−0.181, −0.053], not the 40-seed values) | failed: immature anchors coordinate less well in this learner (main text §2.4) |
| H3/C4 analogue | rewrite − accumulate partition inheritance (no verdict registered) | corrected metric, K13b by ARI: capacity 40 random +0.461 [+0.311, +0.597] 19/20, success +0.420 [+0.314, +0.526] 18/20 (2 ties); noise success +0.441 [+0.351, +0.530] 20/20, random +0.264 [+0.123, +0.417] 15/20; reader both success +0.342 [+0.219, +0.465] 17/20, random +0.206 [+0.062, +0.345] 14/20; capacity 8 +0.061 / −0.025 (Version 1.0 under the singleton-zero convention: e.g. capacity 40 random +0.091 [+0.010, +0.207], "inconclusive in all families") | reported without verdict, as registered; ARI measures partition inheritance, not language structure, so this is not a structural claim |
| T1 | model siblings: same anchors > different > none (ARI) | 0.414 > 0.273 > 0.236 (sibling–parent 0.454 / 0.437 / 0.213) | reproduced (neural: 0.46 > 0.25 > 0.10) |
| T2 | class-matched anchoring emerges from the objective | untaught object keeps its parent classmates: same-class anchor 0.47 (n = 480); other-class anchors only 0.32 (391); no anchor 0.31 (29); measured move cost at the converged child (2026-09-05): with a same-class anchored neighbour the object is already in the anchor's class in 0.44 of pairs and joining otherwise costs ΔE +1.11 on average (ΔE ≤ 0 in 0.35); with an other-class anchor 0.13, +1.85, 0.13 | reproduced without being built in (neural: 0.46–0.60 / 0.09–0.26 / 0.10); the earlier verbal derivation ("below w") was incorrect and is replaced by the measured cost |
| T3 | early-partition anchors coordinate siblings comparably but onto the early partition | sibling ARI 0.368 vs 0.414; alignment to early partition 0.397 vs 0.376, to final 0.374 vs 0.454 (early vs final partitions of the same parent: ARI 0.70) | reproduced in direction; small shift because the model's early and final partitions are close |
| T4 | founder similarity decays more slowly under refreshed than under frozen early anchors | Version 1.0 implementation drew a fresh unrelated shallow partition every generation (not the registered frozen-record condition): rewrite 0.466, 0.314, 0.327, 0.242, 0.198; "accumulate" 0.263, 0.196, 0.194, 0.158, 0.157. Corrected implementation (design fixed before running, `results_model/T4_correction_design.md`; anchors from the founder's frozen early partition, ARI founder–early 0.70): rewrite unchanged; accumulate 0.382, 0.324, 0.376, 0.399, 0.306; g5 rewrite − accumulate −0.109 [−0.175, −0.048], rewrite higher in 5/20 | NOT reproduced: implemented as registered, a frozen early record keeps the lineage closer to the founder than refreshed anchors do; the correspondence with neural K18 is withdrawn (the neural accumulating record is re-carved each generation and is not a frozen founder snapshot, so the registered model condition was not its analogue) |

## S3. The minimal reconstruction model


### Model specification
Objects are the nodes of the Hamming graph of a 3 × 4 world (64 nodes; edges join objects differing in one attribute). A language is
a partition P of the nodes into message classes plus surface forms (one random code per class, learner-specific unless supplied by
an anchor). A learner minimises
  E(P) = c · #(within-class pairs) + λ · #(classes) + w · #(cut Hamming-1 edges),   c = 1, λ = 6, w = 1,
by greedy local search from a seeded random partition. The class-matched spillover effect is not built in. Anchors are nodes whose class label is
fixed by the record (two anchors with the same recorded form share a class). Minimisers are non-unique: two unanchored learners of
the same world agree at ARI 0.23 (chance 0), relabellings are free, and many alternative local merges of neighbours are equal or near-equal in cost.

### Simulation results (20 seeds)
| prediction | result | matches the neural system? |
|---|---|---|
| T1 siblings: same anchors > different > none | ARI 0.414 > 0.273 > 0.236 | yes (0.46 > 0.25 > 0.10; the model's "none" floor is higher because E favours a world-generic optimum) |
| T2 class-matched anchoring emerges | untaught object keeps its parent classmates: same-class anchor 0.47; other-class anchors only 0.32; no anchor 0.31 | yes (0.46–0.60 vs 0.09–0.26 vs 0.10); not assumed, derived from E |
| T3 strength vs target | anchors from the early partition: sibling ARI 0.368 vs 0.414; alignment to the early partition 0.397 vs 0.376, to the final 0.374 vs 0.454 | yes in direction; the model's early/final partitions are close (ARI 0.70), so the shift is small |
| T4 persistence | corrected run (frozen founder early partition): ARI to founder at g5 rewrite 0.198, accumulate 0.306; −0.109 [−0.175, −0.048], rewrite higher in 5/20 | no: the registered model condition does not reproduce neural K18 (Version 1.0's "reproduced" rested on an implementation that used unrelated fresh partitions) |

### Why T2 emerges in this regime (measured, not derived; 2026-09-05)
The move cost for an untaught node o entering a class of size m_dest from a class of size m_src is
ΔE = c·(m_dest − (m_src − 1)) + λ·Δ#classes + w·Δ#cut edges. Version 1.0 claimed the marginal collision cost of joining an anchored
neighbour's class is "below w"; with c = w = 1 that is false in general (joining a class of size m adds m collision pairs). Measured at
the converged children of the T2 simulation: with a same-class anchored neighbour, the untaught object is already in the anchor's class
in 0.44 of pairs and, when it is not, joining costs +1.11 on average (ΔE ≤ 0 in 0.35 of pairs); with an other-class anchored neighbour,
0.13, +1.85 and 0.13. The class-matched effect therefore appears as a higher share of objects that ended in the anchor's class and a
lower cost of joining, not as a guaranteed downhill move. Greedy local-search endpoints are not shown to be global minimisers. A one-dimensional chain makes the mechanism transparent:
with c small and w > λ/2, a class boundary placed between two anchors of different labels is free to sit anywhere, whereas an anchor
sharing a segment's label pins the segment.

### Why the model separates strength and target
The objective does not privilege anchor provenance: any consistent set of fixed labels constrains the search in the same way, so
provenance changes the target directly (the reconstructed partition is biased toward the partition the labels are consistent
with), while coordination strength changes only modestly in this regime (0.368 vs 0.414 in the simulation), through the optimisation
trajectory rather than the objective.

### What the model does not capture
Surface-form turnover (forms are free per class here; in the neural system forms are re-derived with partial reuse), the
structural cost of immature anchors (E has no notion of "less systematic"; the neural cost arises from learning dynamics), the
exact magnitudes, and persistence: the registered T4 condition, once implemented, does not reproduce neural K18 (above). It is a model
of the reconstruction step, not of learning. T1–T3 numbers are from the original run (`model.py`); the verification of 2026-09-05
reviewed the implementation but did not independently rerun them; the corrected T4 and the move-cost measurement are in `model_v2.py`.


## S4. Supplementary Figure Legends


**Figure 1. Historical symmetry breaking among independently trained siblings.** Two children of the same parent, trained separately, become substantially more similar when they were shown the same limited set of examples: same record → siblings look alike; different records → less alike; no record → almost unrelated. (a)
Partition similarity (adjusted Rand index over the 48 training objects) between two independently initialised siblings taught the
same 19 (object, message) pairs, two different random 19-sets, or nothing; n = 45 seeds (30 discovery + 15 pre-registered, K16).
(b) Siblings taught the same record resemble each other more than either resembles the parent. (c) The same pattern in a second
learner: an MLP sender and receiver trained with straight-through Gumbel-softmax (no REINFORCE, no exploration bonus) produce nearly
injective languages, so agreement is measured as the share of objects on which the two siblings use identical forms; GRU (seeds
0–29) vs Gumbel MLP (seeds 120–159; A3′, pre-registered). Error bars: s.e.m. over seeds.

**Figure 2. Class-matched anchors propagate transmitted conventions.** A transmitted example steadies the meanings around it, especially the ones that use its convention. (a)
Share of untaught objects that keep the parent's form, by number of taught neighbours, split by whether at least one neighbour
shares the object's own form (K11, K15). (b) When the parent had borrowed a neighbour's form for an untaught object, the child
repeats that choice if the neighbour was taught, and at chance if not (K10). (c) Part of the benefit of a bigger record is more
anchors per object: at equal anchor counts, retention is similar across capacities for well-anchored objects (three or more taught
neighbours, an additional subgroup); the registered subgroup of two or more did not replicate equivalence, and unanchored objects retain
less at capacity 40 (K1, K12). Error bars in all panels: s.e.m. over seeds (n = 30 in every stratum except capacity 40 with one anchor in panel c, n = 29: one seed had no eligible observation). Chance in panel b is computed on the same untaught-source cases as the bar it is compared with.

**Figure 3. Developmental provenance shifts the reconstruction target.** In the GRU learner, examples taken from an immature stage of the parent's language coordinate
children without a detectable weakening under the pre-specified criterion, but toward the immature version (in the second learner
they coordinate somewhat less well; main text §2.4). Bars: sibling–sibling similarity (coordination), similarity to the parent's final language, and
similarity to the parent's step-500 snapshot, for children taught mature vs immature forms of the same 19 objects (K17a, K17c;
n = 45: 30 discovery + 15 pre-registered).

**Figure 4. The Snapshot Effect and its structural consequences.** (a) Lineages whose record accumulates early forms build less structured languages than lineages
whose record is rewritten from the parent's final language, paired by seed (H3, C4; collision-free geometry). (b) Within a
generation, communication erodes what imitation installed, twice as fast when the record is immature. (c) With a very small record
(capacity 8) the advantage of mature records disappears or reverses; with a large one it is strong (K13b). (d) Same objects, same
parent: a child taught the mature form ends with the parent's final form 79% of the time; taught the step-500 form, 26% (per-seed
means, n = 65 seeds: 30 discovery, 15 pre-registered, 20 replication). Error bars in all panels: s.e.m. over seeds.


## S5. Registration timeline and reproduction

File paths and commands in this section identify materials within the research code repository. They are provided for
reproducibility, rather than as links to a reader's local computer. The archive linked on the title page is the original
Version 1 release; the corrected analysis requires the revised code described below. The accompanying *Version 2 Revision
Notes* summarize the analytical changes.

Two kinds of registration are distinguished throughout. *Registered before the runs*: H1–H9 (`results_v3/PREREG.md`), C1–C6
(`results_v3_confirm/PREREG.md`), K1–K9 (`results_v3_confirm2/PREREG.md`), K14, K16, K17 (new seeds, same file; K18 was added to that file
while the replication was running, before inspection), E1–E4
(`results_entropy/PREREG.md`), L1–L3 (`results_long/PREREG.md`), S1–S3 (`results_oneshot/PREREG.md`), M1–M4
(`results_medium/PREREG.md`), D1–D2 (`results_degeneracy/PREREG.md`), A1–A4 with the A3′/A4′ addendum and its power extension
(`results_arch/PREREG.md`), and T1–T4 (`results_model/PREREG.md`). *Registered before computation on held-back data*: K10–K13
and K15, quantities discovered post hoc on seeds 0–29 of the capacity-19 cells and fixed in writing before being computed on the
confirmation-2 families (capacity 8 / 40, noise, reader), which had not been used for those quantities. The theory was frozen on
2026-09-04; every experiment after that date is a robustness or boundary test and none was added to the core claims.
Thresholds for K1–K17 are frozen in `manifest_k.json`; a K18 entry was added on 2026-09-05 as missing metadata, with its provenance.

Reproduction. `python3 tests.py` (31 checks) before any run. `python3 replicate.py --seeds 100..119 --out DIR` is the tested workflow
(see Compute for its limits); `--arch gumbel` does the same for the second architecture. `python3 model.py` reproduces the original
T1–T3 and the superseded T4 implementation (kept for the record); `python3 model_v2.py` reproduces the corrected T4 and the T2 move-cost
measurement. `python3 figures.py` regenerates Figures 1–4 into `figs_v2/`. Cached-data re-scoring with the corrected metric:
`corrections_v2/rerun_all.sh`. CPU only; a 6-generation run takes about two minutes on a 10-core laptop. `PROBES_INDEX.md` maps every
script to its output file.

## S6. References (all works cited in the main text or this Supplement)

Acerbi, A. (2021). Culture without copying or selection. Evolutionary Human Sciences, 3, e50.

Alemohammad, S., et al. (2024). Self-consuming generative models go MAD. ICLR.

Baronchelli, A., Felici, M., Loreto, V., Caglioti, E., & Steels, L. (2006). Sharp transition towards shared vocabularies in multi-agent systems. J. Stat. Mech., P06014.

Ben Zion, R., Carmeli, B., Paradise, O., & Belinkov, Y. (2024). Semantics and spatiality of emergent communication. NeurIPS (arXiv:2411.10173).

Carlsson, E., Dubhashi, D., & Regier, T. (2024). Cultural evolution via iterated learning and communication explains efficient color naming systems. J. Language Evolution, 9, 49–66.

Carmeli, B., Belinkov, Y., & Meir, R. (2024). Concept-best-matching: evaluating compositionality in emergent communication. Findings of ACL (arXiv:2403.14705).

Carr, J. W., Smith, K., Cornish, H., & Kirby, S. (2017). The cultural evolution of structured languages in an open-ended, continuous world. Cognitive Science, 41, 892–923.

Carr, J. W., Smith, K., Culbertson, J., & Kirby, S. (2020). Simplicity and informativeness in semantic category systems. Cognition, 202, 104289.

Chaabouni, R., Kharitonov, E., Dupoux, E., & Baroni, M. (2019). Anti-efficient encoding in emergent communication. NeurIPS.

Chaabouni, R., et al. (2021). Communicating artificial neural networks develop efficient color-naming systems. PNAS, 118.

Cho, J. H., & Hariharan, B. (2019). On the efficacy of knowledge distillation. ICCV.

Claidière, N., Scott-Phillips, T. C., & Sperber, D. (2014). How Darwinian is cultural evolution? Phil. Trans. R. Soc. B, 369, 20130368.

Fehér, O., Wang, H., Saar, S., Mitra, P. P., & Tchernichovski, O. (2009). De novo establishment of wild-type song culture in the zebra finch. Nature, 459, 564–568.

Griffiths, T. L., & Kalish, M. L. (2007). Language evolution by iterated learning with Bayesian agents. Cognitive Science, 31, 441–480.

Guo, S., Ren, Y., Mathewson, K., Kirby, S., Albrecht, S. V., & Smith, K. (2022). Expressivity of emergent languages is a trade-off between contextual complexity and unpredictability. ICLR.

Havrylov, S., & Titov, I. (2017). Emergence of language with multi-agent games: learning to communicate with sequences of symbols. NeurIPS.

Hubert, L., & Arabie, P. (1985). Comparing partitions. J. Classification, 2, 193–218.

Hudson Kam, C. L., & Newport, E. L. (2005). Regularizing unpredictable variation. Language Learning and Development, 1, 151–195.

Hudson Kam, C. L., & Newport, E. L. (2009). Getting it right by getting it wrong. Cognitive Psychology, 59, 30–65.

Kalish, M. L., Griffiths, T. L., & Lewandowsky, S. (2007). Iterated learning: intergenerational knowledge transmission reveals inductive biases. Psychonomic Bulletin & Review, 14, 288–294.

Kharitonov, E., Chaabouni, R., Bouchacourt, D., & Baroni, M. (2020). Entropy minimization in emergent languages. ICML.

Kirby, S., Cornish, H., & Smith, K. (2008). Cumulative cultural evolution in the laboratory. PNAS, 105, 10681–10686.

Li, F., & Bowling, M. (2019). Ease-of-teaching and language structure from emergent communication. NeurIPS.

Lu, Y., Singhal, S., Strub, F., Courville, A., & Pietquin, O. (2020). Countering language drift with seeded iterated learning. ICML.

Panigrahi, A., Liu, B., Malladi, S., Risteski, A., & Goel, S. (2025). Progressive distillation induces an implicit curriculum. ICLR.

Perfors, A., & Navarro, D. J. (2014). Language evolution can be shaped by the structure of the world. Cognitive Science, 38, 775–793.

Puglisi, A., Baronchelli, A., & Loreto, V. (2008). Cultural route to the emergence of linguistic categories. PNAS, 105, 7936–7940.

Ren, Y., Guo, S., Labeau, M., Cohen, S. B., & Kirby, S. (2020). Compositional languages emerge in a neural iterated learning model. ICLR.

Scott-Phillips, T. C. (2017). A (simple) experimental demonstration that cultural evolution is not replicative, but reconstructive. J. Cognition and Culture, 17, 1–11.

Senghas, A., & Coppola, M. (2001). Children creating language. Psychological Science, 12, 323–328.

Senghas, A., Kita, S., & Özyürek, A. (2004). Children creating core properties of language. Science, 305, 1779–1782.

Sevestre, A., & Dupoux, E. (2025). Frequency and compositionality in emergent communication. EMNLP.

Shumailov, I., et al. (2024). AI models collapse when trained on recursively generated data. Nature, 631, 755–759.

Silvey, C., Kirby, S., & Smith, K. (2019). Communication increases category structure and alignment only when combined with cultural transmission. J. Memory and Language, 109, 104051.

Singleton, J. L., & Newport, E. L. (2004). When learners surpass their models. Language, 80, 370–407.

Skyrms, B. (2010). Signals: Evolution, Learning, and Information. Oxford University Press.

Strachan, J. W. A., et al. (2021). Evaluating the relative contributions of copying and reconstruction processes in cultural transmission episodes. PLoS ONE.

Talebirad, Y., Redman, E., Parsaee, A., & Zaïane, O. R. (2026). From signals to structure: how memory architecture drives language emergence in LLM agents. arXiv:2607.00233.

Wang, C., Yang, Q., Huang, R., Song, S., & Huang, G. (2022). Efficient knowledge distillation from model checkpoints. NeurIPS.

Xu, J., Dowman, M., & Griffiths, T. L. (2013). Cultural transmission results in convergence towards colour term universals. Proc. R. Soc. B, 280, 20123073.
