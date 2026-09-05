# Why This Language? Historical Symmetry Breaking through Cultural Transmission

**Ariel Elboim**  
Independent Researcher, Israel  
Corresponding author: lgboim@gmail.com  
Working Paper, Version 2.0, September 5, 2026  
Previous version (1.0): [archived preprint](https://doi.org/10.5281/zenodo.22305643)  
Original code and results: [Version 1 archive](https://doi.org/10.5281/zenodo.22305564)

## Abstract

In iterated learning of emergent languages, cultural transmission can align semantic category systems and steer learners
toward structured, efficient regions of language space. We show that limited transmitted evidence can also break symmetry among
multiple structured solutions, biasing independent learners toward a shared, historically contingent reconstruction despite
substantial item-level turnover. The target and strength of coordination are empirically distinguishable: developmental provenance
can shift what learners reconstruct without necessarily changing how strongly they coordinate. In a controlled referential-game
model, anchors captured from an immature snapshot of a parent's language steer descendants toward the immature organization; in
the main GRU learner, this occurs without a detectable weakening of coordination under a pre-specified criterion, but at a cost to systematicity. We call this the
**Snapshot Effect**. A second architecture and a minimal reconstruction model recover the same symmetry-breaking and
provenance-target pattern. The local propagation mechanism is regime-dependent: in the compressed languages of the GRU learner,
class-matched anchors preferentially stabilize untaught neighbouring meanings that use the same convention, whereas this mechanism
does not carry over to a near-injective learner. Here, symmetry breaking refers to historical evidence resolving underdetermination
among multiple viable structured reconstructions, not to competition among labels.

**Culture need not create structure. It makes one structured possibility historical.**

**Keywords:** cultural transmission; iterated learning; emergent communication; symmetry breaking; developmental provenance; language evolution.

## Plain Language Summary

Two learners exposed to the same parent could each build a good language, but not necessarily the same one. In a small
controlled model, we show that a limited set of inherited examples can make independent learners converge on the same organization
of meaning even when many individual forms change. The examples also carry information about when they were recorded. If they come
from an immature stage of the parent's language, learners are biased toward reconstructing that earlier organization rather than
the parent's final one. In the main learner, this shift occurs without reducing coordination between descendants. The results
suggest that cultural transmission can preserve historical continuity not by copying a language, but by biasing which viable
language is reconstructed.

## AI Use Disclosure

Generative AI tools (Anthropic Claude via Claude Code and OpenAI Codex) were used to assist with code development, experimental
execution, adversarial review, literature discovery, and language editing. The author formulated the research questions, established
the pre-registration framework and interpretive constraints, reviewed and verified all analyses and outputs, and takes full
responsibility for the manuscript.

## Supplementary Material and Code

The accompanying Supplementary Material contains the complete Methods, evidence tables, registered outcomes including
failed predictions, and the reconstruction model and move-cost analysis. The accompanying *Version 2 Revision Notes* describe
the corrections to the first version. The [original preprint](https://doi.org/10.5281/zenodo.22305643) and
[original code, registrations and results](https://doi.org/10.5281/zenodo.22305564) remain archived as Version 1; these links
identify the earlier release. Instructions for the corrected analyses and their reproducibility limits appear in Supplementary
Section S5. Headline numbers are pre-registered unless marked [exploratory]; the tests behind each section are listed at its
end and tabulated in the Supplementary Material. All structure claims in the main text use collision-free measures
(Supplementary Note 2).

## 1. Introduction

Two children learn to talk from the same parent. Each of them could have built a language of their own, a different one and just as good. Why do they end up speaking the same one? And if the parent's speech was recorded while the parent was still learning, what
exactly do the children inherit: the language, or the moment it was recorded?

Prior work has answered neighbouring questions. Iterated learning through a transmission bottleneck makes emergent languages more
structured and more learnable (Kirby, Cornish & Smith 2008; Ren et al. 2020; Li & Bowling 2019); transmission aligns speakers'
category systems beyond what shared biases produce (Silvey, Kirby & Smith 2019) and steers them toward efficient regions of the space
of category systems (Xu, Dowman & Griffiths 2013; Carr et al. 2020; Carlsson, Dubhashi & Regier 2024). What these accounts leave open
is the case where many structured languages are already available: how does a lineage end up speaking one of them rather
than another, and what is the thing that is passed on?

We answer with a miniature version of the situation. It is a minimal controlled model built to isolate the causal effects of
transmission, not a model of human language. Neural agents play a referential game over 64 objects, every combination of three attributes with four values each, so the "meaning space" is a small grid of things to talk about, and a language is a way of assigning each of them a three-symbol message. Each generation is a fresh pair
that first learns 19 of its parent's (object, message) pairs from a record and then trains on the game. Because generation 0 is
bit-identical across conditions, the parent, the children and the record can each be held fixed while the others vary: two
independently initialised children can be given the same or different records, and the record can be sampled from the parent at
different stages of its development.

Three claims follow. **(1) Structured underdetermination.** Learners build structured languages without any record, but do not reliably
reconstruct the same one. **(2) Anchored symmetry breaking.** A limited set of transmitted examples biases independent learners toward the same reconstruction: among the alternative structured reconstructions available to them, limited evidence biases them toward one. We use the term
differently from the naming-game literature, where symmetry breaking is a population resolving competition among labels
(Baronchelli et al. 2006; Puglisi et al. 2008). **(3) Developmental provenance.** The stage at which the evidence was captured biases
what is reconstructed; how strongly learners coordinate, and through which local mechanism, depends on the learner and
representational regime. A second learner with a different learning rule, and a minimal reconstruction model with no learning at
all, recover the same symmetry-breaking and provenance-target pattern, so the pattern is not an artefact of one architecture,
though the model demonstrates sufficiency in one setting, not universality. The core confirmatory hypotheses were registered before their confirmatory analyses on data not used for
their discovery; failures and later robustness tests are reported in full in the Supplementary Material.

## 2. Results

### 2.1 Structured underdetermination and symmetry breaking

*Learners can build structure on their own; what they do not reliably do alone is reconstruct the same one. A shared record makes them converge much more strongly.*

A fresh sender–receiver pair trained with no record reaches structure of the same order as lineages with one (collision-free geometry within a few hundredths, concept matching 0.05–0.07 lower;
concept-matching within a few hundredths of rewritten-record lineages; C6). What it does not reach is a particular solution. We measure how similarly two languages group meanings into messages with the
adjusted Rand index (ARI): the chance-corrected agreement between two partitions of the training objects into same-message classes,
1 for identical grouping and 0 at chance. Because it compares groupings rather than the messages themselves, it separates inheritance
of organisation from copying of forms. Two no-record children of the same parent agree at ARI 0.08–0.10, and a no-record child agrees
with its parent at 0.06. At the item level the alternatives carry similar communicative value
(per-object accuracy 0.92–0.95 whether an object keeps the parent's form or a neighbour's) [exploratory]. The solution space is
structured but underdetermined.

Yet a limited transmitted record is enough to break the symmetry. Two independently initialised children taught the same 19 pairs agree at ARI 0.46;
taught two different random 19-sets, 0.25; taught nothing, 0.10 (same − different +0.21 [+0.11, +0.30], 13/15 seeds; different −
none +0.15 [+0.06, +0.23], 12/15; replication on 20 untouched seeds: +0.17 [+0.11, +0.24], 18/20 and +0.21 [+0.15, +0.26], 19/20; Fig. 1a; K16). Siblings with the same record resemble each other (0.46) more than either resembles the
parent (0.31; Fig. 1b), and this holds on objects neither sibling was taught (0.34 vs 0.24, 34/45) [exploratory]: the record
constrains reconstruction beyond the items it contains. Lineages inherit the same way: with a rewritten record, parent–child ARI
exceeds the no-record baseline by +0.23 to +0.64 across four channel families, 20/20 seeds in each (K13a), and again on twenty
untouched replication seeds. All of this coexists with substantial turnover: only 31–55% of training objects keep the parent's exact
form across a generation [exploratory]. In the compressed GRU regime, the organisation into classes is inherited more reliably than the forms that realise it.

The symmetry can be stated without metaphor. Call a language *viable* if it reaches the structure and communicative value that
learners reach in this task; the opening of this section shows that many partitions of meaning space are viable at once. The symmetry is a property of the
learner given the task alone: it does not distinguish among viable partitions, so independently initialised learners land on
different ones (sibling ARI near chance) while matching each other in structure and accuracy. Breaking that symmetry means
supplying evidence that does distinguish among them: a record consistent with one partition and not the others. The claim is not
that a record makes learners converge in some general sense, which shared biases already do, but that it selects which viable
partition they converge on, and that the selection is historical, fixed by what happened to be transmitted rather than by task
value. Two observations separate this from mere seed variance: each viable partition is stable enough to be inherited when it is
transmitted (the lineage result above), and the alternatives carry similar communicative value at the item level. Whether the task ranks complete alternative
languages was not tested directly.

**Takeaway:** what is transmitted is a bias on reconstruction, not a copy: siblings with the same record resemble each other more
than they resemble the parent, even on items neither was taught.

### 2.2 Developmental provenance biases the reconstruction target

*Give both siblings a record taken early, before the parent had settled: they still agree with each other, but on the parent's early
language.*

We taught the same 19 objects with the parent's forms sampled either at the end of training (mature) or at step 500 of 2,000
(immature; 72% of these forms differ from the final ones). Crucially, immature anchors steer reconstruction toward the immature organisation:
siblings taught the immature snapshot align with the parent's step-500 partition at ARI 0.43 vs 0.21 for mature anchors (+0.22
[+0.16, +0.28], 15/15; replication +0.17, 19/20; Fig. 3; K17c). In the GRU learner they do so without detectably weakening coordination:
sibling ARI 0.55 vs 0.46 (K17a, within the pre-set equivalence band; replication +0.08). Alignment with the parent's *final* language is
lower with immature anchors (0.28 vs 0.35 on 45 seeds), but only in 73% of seeds, below our rule, reported as a consistent but
unconfirmed effect (K17b). The reconstruction model illustrates one reason this need not occur: where the early and final partitions of a parent overlap (ARI 0.70 in the model), alignment with the early state need not reduce alignment with the final one. At the item level, a child taught an object's mature form ends with the parent's final form 79% of the
time; taught the step-500 form, 26% (Fig. 4d; per-seed means over 65 seeds): learners reconstruct toward the organisation they were given rather than automatically recovering
the mature one. This is the Snapshot Effect: transmitted evidence biases reconstruction toward the developmental state in which it was captured.

A record that accumulates forms carved during the parent's training tends to preserve an early developmental state (91–96% of its entries are
fixed within the first 500 steps [exploratory]), and lineages transmitting it build less systematic languages than lineages whose
record is rewritten from the parent's final language (H3, 10/10; C4 on new seeds +0.07 [+0.05, +0.10], 17/20; in collision-free
geometry −0.095, 28/30; Fig. 4a). The child must replace more of what it was taught (fidelity to the record falls to 0.66 within a
generation vs 0.82 for mature anchors; Fig. 4b), and excluding every object that carries a stale form closes only ~15–20% of the gap
[exploratory], suggesting that much of the cost is systemic. Under "hard" selection, where record slots turn over every generation, the advantage appears in only
57–80% of seeds, consistent with forms having less time to become stale.

**Takeaway:** what learners coordinate on and how strongly they coordinate are distinguishable quantities; the developmental
provenance of transmitted evidence biases the first, and its effect on the second depends on the learner (§2.4).

### 2.3 How the bias propagates in compressed languages

*A child sees only a limited set of inherited examples, yet an inherited example can stabilise nearby meanings the child never saw, especially when they use the same convention. We call such an example a class-matched anchor.*

In the compressed languages of the GRU learner (24 of 64 messages distinct; 75% of training objects have a neighbour with the same
form), the taught items are learned by supervised imitation, and their influence spills over to neighbours that were never taught. An
untaught object keeps the parent's form in 0.46–0.60 of cases when a taught Hamming-1 neighbour shares that form, and in 0.09–0.26 when
its taught neighbours carry other forms, close to the 0.10 seen with no taught neighbour at all (gap +0.30 to +0.44 across four
channel families, 20/20 seeds each; replication +0.21 to +0.43; Fig. 2a; K15). Retention rises with the number of taught neighbours (K11,
20/20 ×4), and the anchor transmits a *choice*: when the parent had borrowed a neighbour's form for an untaught object, the child
repeats that choice in 0.56–0.61 of cases if the neighbour was taught and at chance (0.16–0.20) if not (K10, 20/20 ×4; Fig. 2b).
Consistent with a mechanism that works through anchors rather than item identity, four non-random rules for choosing which 19 items to transmit differed from a random choice by less than the pre-set point-estimate bands (pooled 45-seed cohort; three of four in replication, where the whole-classes rule fell outside the band at −0.031; two of four in the original 15-seed test) (K14, 4/4 rules on 45 seeds; 3/4 on replication seeds). The record is partial rather than exhaustive: 19 of 48 training meanings (30% of the full 64-object world), enough to leave most
untaught objects with at least one anchor. Capacity acts
in part through coverage: a record of 8 items leaves most objects unanchored and yields the least structured languages (−0.07, 20/20; K1),
founder intelligibility rises by +0.20 per capacity step (K4, 20/20), and at equal anchor counts retention is similar across
capacities for anchored objects, though not for objects with no anchor at all (K12, failed in that stratum; Fig. 2c).

**Takeaway:** in compressed languages, a transmitted example affects nearby meanings that were never taught; which examples are
transmitted matters much less than whether they anchor their neighbourhoods.

### 2.4 Boundaries and generality

*Three ways to break the story, two ways to test whether it is about our learner, and one model with no learning at all.*

*Persistence.* With mature anchors the founder's partition is still detectable five generations later (ARI 0.17); with immature
anchors, repeatedly transmitted, it is substantially weaker (0.08; K18: +0.09 [+0.05, +0.13], 16/20, replication seeds). History
persists across the generations observed, but weakens. After a *single* immature snapshot, redirection weakened over the next two refreshed generations, but persistence was
inconclusive (S), so the persistence claim is scoped to recurring immature provenance.

*Regime.* Under very low exploration, where the parent's language changes little after the
snapshot (26% of accumulated entries stale vs 35%), the Snapshot Effect weakened and missed the seed rule, although its mean stayed
positive (+0.05, 21/30; E1); with generations three times longer, where the parent moves further, it held (+0.05, 24/30; staleness
53%; L1). Developmental divergence after capture, rather than snapshot age as such, appears to moderate the effect.

Making the task more decisive (Hamming-1 distractors in 0 / 50 / 100% of rounds) lowers the partition-level sibling
gap in the predicted direction (0.26 → 0.14 → 0.09) but not decisively (D1 inconclusive), while the form-level gap remains within the pre-set equivalence band (D2):
that cultural leverage is highest under structured underdetermination remains a prediction with trend-level support.

*Scale and coverage.* With very low coverage (capacity 8) the maturity advantage in partition inheritance disappears or
reverses (−0.10 at capacity 8 vs +0.37 to +0.39 at capacity 40; K13b). In a world four times larger with hard distractors (256
objects, half of all rounds requiring more than one attribute), symmetry breaking and partition inheritance hold (+0.10, 8/10 and
+0.16, 10/10; M3: +0.29, 10/10; M2), class-matched anchoring keeps its direction but not its magnitude (+0.07, 9/10; band set at 0.15; M1),
and the structural cost of immature records is inconclusive at n = 10 (M4) despite staler records (56%); anchor leverage, not staleness alone, appears to limit how much redirection propagates.

*Learner and model.* An MLP sender and receiver trained end-to-end with straight-through Gumbel-softmax (no REINFORCE, no exploration bonus) produce nearly injective languages (59 of 64 messages distinct; 4% of objects have a same-form neighbour), an
empirical property of this learner. Partition measures are uninformative there (two fully injective languages have identical singleton partitions), so we registered form-level tests on fresh seeds. Partition-level tests in this learner were re-scored after a metric correction (identical singleton partitions now score 1): partition inheritance with a rewritten record (A1) is supported in all four channel families under the corrected metric (Version 1.0 reported it as partial), while the sibling-coordination contrast (A4) no longer meets its band; the form-level conclusions are unchanged (Supplementary Table S4).
Symmetry breaking holds: sibling form agreement 0.44 with the same record, 0.21 with different records, 0.00 with none (+0.23
[+0.19, +0.28], 37/40; +0.20, 40/40; Fig. 1c; A3′). Immature anchors redirect the target here too (+0.09, 38/40; A4′) but coordinate
siblings somewhat *less* well (0.37 vs 0.44), so the "without detectable weakening" finding belongs to the GRU regime. Class-matched
anchoring vanishes except at the smallest capacity. This is a regime boundary of the class-matched mechanism, not a failure of
the claim: the broader symmetry-breaking effect persists. We interpret this
as a consequence of there being almost no message classes to anchor, so the mechanism belongs to categorical, compressed languages
(a hypothesis, not a demonstrated geometric account). Anchoring gradients and anchored choice remain.

The cleanest demonstration that the pattern does not require neural learning comes from a model with no learning at all.
A search that minimises collisions + number of classes + cut Hamming-1 edges greedily, with
anchors as nodes whose labels are fixed, reproduces the pattern: same anchors > different > none (ARI 0.41 > 0.27 > 0.24); the
class-matched spillover emerges without being built in (0.47 vs 0.32 vs 0.31); early-partition anchors bias reconstruction toward the
early partition; the persistence comparison (T4), once implemented as registered, does not reproduce the neural pattern (Supplementary S3). The other patterns can arise without neural
learning, from underdetermined structured reconstruction under sparse historical constraints (derivations in Supplementary Methods).
This is a sufficiency result in one setting, not a demonstration of universality.

**Takeaway:** mechanism regime-specific, principle robust across the settings tested. What carries across is not a particular form of inheritance but the computational
role of historical evidence: limited
constraints break symmetry among reconstructable solutions and their developmental provenance biases the target; how strongly they
coordinate, and through which local mechanism, depends on the learner and representational regime.

## 3. Discussion

*In one sentence: learners can build a structured language alone, but a limited set of inherited examples biases which one they build, and the examples carry the developmental state in which they were captured.*

The role of cultural transmission depends on the regime of the learning problem. When structure is not reconstructable without
transmission, the bottleneck creates it (Kirby et al. 2008; Ren et al. 2020); when structure is already reconstructable but
underdetermined, the regime studied here, transmission acts primarily as historical symmetry breaking. Prior work treated languages
as partitions of meaning space and compared them with the adjusted Rand index (Perfors & Navarro 2014; Xu et al. 2013); our use of the
measure is to separate inherited organisation from item-level copying and to compare independently reconstructed descendants. This
suggests a mechanistic interpretation of the alignment reported by Silvey et al. (2019): transmission coordinates semantic systems not by copying
them but by resolving underdetermination during reconstruction. It also sits between cultural attraction theory, which holds that
transmission is reconstructive (Claidière et al. 2014; Scott-Phillips 2017; Acerbi 2021), and iterated-learning theory, which holds
that transmitted data are asymptotically irrelevant (Griffiths & Kalish 2007): shared biases explain why languages occupy a structured
region of solution space, and limited historical evidence biases where within that region independent learners converge, a finite-time historical contingency compatible with asymptotic attraction. Carlsson et al. (2024) showed that many colour-naming systems are
comparably efficient; we show that a small inherited record biases fresh learners toward particular alternatives.

That the developmental stage of a teacher matters is not new: intermediate checkpoints can be better distillation teachers than
converged ones (Cho & Hariharan 2019; Wang et al. 2022; Panigrahi et al. 2025), and seeded iterated learning varies how long a teacher
interacts before it is imitated (Lu et al. 2020). Those results ask which stage teaches better; ours asks whether stage changes what
is reconstructed. We are not aware of prior work that isolates the dissociation between coordination target and coordination
strength under a stage manipulation with items held fixed. Nor is this a claim that learners cannot regularise imperfect input: children do (Singleton & Newport 2004; Hudson Kam & Newport 2005, 2009), Nicaraguan Sign Language cohorts added structure (Senghas et
al. 2004), and zebra-finch song returns to wild type over generations (Fehér et al. 2009). It is a claim about identifiability under
historical constraints: when a limited anchor set provides sufficient coverage in this reconstruction regime, learners coordinate around the
organisation encoded in the captured evidence rather than inferring the source's later organisation.

The three forces this separates are often conflated: inductive and communicative biases shape the space of viable structured
solutions; cultural transmission breaks symmetry among those solutions, making one historically contingent organisation recurrent;
and the developmental provenance of transmitted evidence biases reconstruction toward one organisation (in the GRU learner without detectably weakening coordination, in a second learner with some loss), while repeated transmission of that provenance shapes how long
its historical influence persists.

**Limitations.** A small world, small learners, and predictions that did not hold: the capacity–coverage equivalence fails for objects
with no anchor; under very low coverage persistence can beat freshness; convexity is not a product of accumulation; the reduced
alignment of immature-anchored children with the parent's final language reached 70–73% of seeds; the class-matched gap shrinks in a
larger world and vanishes in a near-injective learner; and the degeneracy scan gave a trend, not a verdict. Ownership of shared
messages is a mechanical consequence of the receiver's independent, deterministic candidate scoring; its consequences are not. All
pre-registered outcomes, including these, are tabulated in Supplementary Tables S1–S4.

The question in our title therefore has a historical answer once functional constraints leave multiple viable solutions: this language, because these were the examples that happened to be transmitted, captured at this stage of the parent's development. Culture does not have to preserve particular solutions. It can transmit limited historical evidence that biases independent learners
toward the same historically contingent region of solution space, and that evidence encodes the developmental state in which it was
captured.

**Culture need not create structure. It makes one structured possibility historical.**

## 4. Methods

Essentials only; the full specification is in Supplementary Methods. Objects are the 64 combinations of 3 attributes × 4 values; 16 are held out (never targets, but present as distractors). A round:
the sender emits 3 symbols from a vocabulary of 8; the receiver picks the target among 5 candidates. GRU sender and receiver (hidden
64); REINFORCE with an entropy bonus of 0.02 for the sender, cross-entropy for the receiver; 2,000 steps of 64 rounds per generation;
six generations; every generation a fresh pair. Before training, the child sender is taught up to *capacity* (8/19/40) recorded pairs
by 200 supervised steps. The record's freshness is either *accumulate* (forms carved during the parent's training under an
incumbent rule, so most entries are fixed early) or *rewrite* (the parent's final forms). Measures: topsim and its collision-free
variant, concept-best matching, ownership (the receiver's decode of each message among all 64 objects), and ARI between languages'
partitions of the 48 training objects. Anchors are taught Hamming-1 neighbours of an untaught object; class-matched anchors share its
parent form; provenance is the parent step at which the recorded form was sampled. Sibling design: two children with different
initialisations taught the same 19 pairs, different 19-sets, or nothing. Snapshot design: the same 19 objects with step-500 vs final
forms. Second architecture: MLP agents with straight-through Gumbel-softmax, no REINFORCE, no entropy bonus. Medium world: 4 × 4 = 256
objects, message length 4, capacity 77, Hamming-1 distractors in half of all rounds. Decision rule for every registered prediction:
≥ 80% of seeds in the predicted direction and a paired bootstrap 95% CI excluding 0; equivalence claims state their band in advance.
Registered-before-run and registered-before-computation hypotheses are distinguished in the registration files; the replication
pipeline was run by one command on seeds 100–119; two tests added afterwards were evaluated from the same raw files.

## Figures

**Figure 1. Historical symmetry breaking among independently trained siblings.** Two children of the same parent, trained separately, become substantially more similar when they were shown the same limited set of examples: same record → siblings look alike; different records → less alike; no record → almost unrelated. (a)
Partition similarity (adjusted Rand index over the 48 training objects) between two independently initialised siblings taught the
same 19 (object, message) pairs, two different random 19-sets, or nothing; n = 45 seeds (30 discovery + 15 pre-registered, K16).
(b) Siblings taught the same record resemble each other more than either resembles the parent. (c) The same pattern in a second
learner: an MLP sender and receiver trained with straight-through Gumbel-softmax (no REINFORCE, no exploration bonus) produce nearly
injective languages, so agreement is measured as the share of objects on which the two siblings use identical forms; GRU (seeds
0–29) vs Gumbel MLP (seeds 120–159; A3′, pre-registered). Error bars: s.e.m.

**Figure 2. Class-matched anchors propagate transmitted conventions.** A transmitted example steadies the meanings around it, especially the ones that use its convention. (a)
Share of untaught objects that keep the parent's form, by number of taught neighbours, split by whether at least one neighbour
shares the object's own form (K11, K15). (b) When the parent had borrowed a neighbour's form for an untaught object, the child
repeats that choice if the neighbour was taught, and at chance if not (K10). (c) The benefit of a bigger record is mostly more
anchors per object: at equal anchor counts, retention is similar across capacities for well-anchored objects (three or more taught neighbours, an additional subgroup); the registered subgroup of two or more did not replicate equivalence, and unanchored objects retain less at capacity 40 (K1, K12). Error bars: s.e.m. over seeds.

**Figure 3. Developmental provenance shifts the reconstruction target.** In the GRU learner, examples taken from an immature stage of the parent's language coordinate
children without a detectable weakening under the pre-specified criterion, but toward the immature version (in the second learner they coordinate somewhat less well; §2.4). Bars: sibling–sibling similarity (coordination), similarity to the parent's final language, and
similarity to the parent's step-500 snapshot, for children taught mature vs immature forms of the same 19 objects (K17a, K17c;
n = 45: 30 discovery + 15 pre-registered).

**Figure 4. The Snapshot Effect and its structural consequences.** (a) Lineages whose record accumulates early forms build less structured languages than lineages
whose record is rewritten from the parent's final language, paired by seed (H3, C4; collision-free geometry). (b) Within a
generation, communication erodes what imitation installed, twice as fast when the record is immature. (c) With a very small record
(capacity 8) the advantage of mature records disappears or reverses; with a large one it is strong (K13b). (d) Same objects, same
parent: a child taught the mature form ends with the parent's final form 79% of the time; taught the step-500 form, 26% (per-seed means, n = 65 seeds). Error bars: s.e.m. over seeds.

## References

Acerbi, A. (2021). Culture without copying or selection. Evolutionary Human Sciences, 3, e50.

Baronchelli, A., Felici, M., Loreto, V., Caglioti, E., & Steels, L. (2006). Sharp transition towards shared vocabularies in multi-agent systems. J. Stat. Mech., P06014.

Carlsson, E., Dubhashi, D., & Regier, T. (2024). Cultural evolution via iterated learning and communication explains efficient color naming systems. J. Language Evolution, 9, 49–66.

Carr, J. W., Smith, K., Culbertson, J., & Kirby, S. (2020). Simplicity and informativeness in semantic category systems. Cognition, 202, 104289.

Cho, J. H., & Hariharan, B. (2019). On the efficacy of knowledge distillation. ICCV.

Claidière, N., Scott-Phillips, T. C., & Sperber, D. (2014). How Darwinian is cultural evolution? Phil. Trans. R. Soc. B, 369, 20130368.

Fehér, O., Wang, H., Saar, S., Mitra, P. P., & Tchernichovski, O. (2009). De novo establishment of wild-type song culture in the zebra finch. Nature, 459, 564–568.

Griffiths, T. L., & Kalish, M. L. (2007). Language evolution by iterated learning with Bayesian agents. Cognitive Science, 31, 441–480.

Hudson Kam, C. L., & Newport, E. L. (2005). Regularizing unpredictable variation. Language Learning and Development, 1, 151–195.

Hudson Kam, C. L., & Newport, E. L. (2009). Getting it right by getting it wrong. Cognitive Psychology, 59, 30–65.

Kirby, S., Cornish, H., & Smith, K. (2008). Cumulative cultural evolution in the laboratory. PNAS, 105, 10681–10686.

Li, F., & Bowling, M. (2019). Ease-of-teaching and language structure from emergent communication. NeurIPS.

Lu, Y., Singhal, S., Strub, F., Courville, A., & Pietquin, O. (2020). Countering language drift with seeded iterated learning. ICML.

Panigrahi, A., Liu, B., Malladi, S., Risteski, A., & Goel, S. (2025). Progressive distillation induces an implicit curriculum. ICLR.

Perfors, A., & Navarro, D. J. (2014). Language evolution can be shaped by the structure of the world. Cognitive Science, 38, 775–793.

Puglisi, A., Baronchelli, A., & Loreto, V. (2008). Cultural route to the emergence of linguistic categories. PNAS, 105, 7936–7940.

Ren, Y., Guo, S., Labeau, M., Cohen, S. B., & Kirby, S. (2020). Compositional languages emerge in a neural iterated learning model. ICLR.

Scott-Phillips, T. C. (2017). A (simple) experimental demonstration that cultural evolution is not replicative, but reconstructive. J. Cognition and Culture, 17, 1–11.

Senghas, A., Kita, S., & Özyürek, A. (2004). Children creating core properties of language. Science, 305, 1779–1782.

Silvey, C., Kirby, S., & Smith, K. (2019). Communication increases category structure and alignment only when combined with cultural transmission. J. Memory and Language, 109, 104051.

Singleton, J. L., & Newport, E. L. (2004). When learners surpass their models. Language, 80, 370–407.

Wang, C., Yang, Q., Huang, R., Song, S., & Huang, G. (2022). Efficient knowledge distillation from model checkpoints. NeurIPS.

Xu, J., Dowman, M., & Griffiths, T. L. (2013). Cultural transmission results in convergence towards colour term universals. Proc. R. Soc. B, 280, 20123073.
