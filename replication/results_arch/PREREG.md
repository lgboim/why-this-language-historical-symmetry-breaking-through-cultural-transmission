# Second architecture A (registered 2026-09-05, before implementation is finished or any run)
Agents: MLP sender and MLP receiver with straight-through Gumbel-softmax message sampling, trained end-to-end by cross-entropy on the
receiver's choice; no REINFORCE, no entropy bonus. Everything else (world, record, channel, teaching by supervised imitation,
measures, seeds) unchanged; `--arch gumbel`. Predictions: same DIRECTION as the GRU results under the frozen seed rule (≥80% of seeds,
paired CI); effect sizes are NOT required to match.
- A1 (= K13a): parent–child ARI, rewritten record − no record > 0 (cap-19 families available; seeds 100–119 via replicate.py).
- A2 (= K15): retention with a same-form Hamming-1 taught neighbour − with other-form taught neighbours only > 0, gap ≥ 0.15.
- A3 (= K16): sibling ARI same record > different records (primary), different > none (secondary).
- A4 (= K17a/K17c): sibling ARI with step-500 anchors not more than 0.05 below mature anchors (CI lower ≥ −0.10); ARI to the
  step-500 snapshot higher with immature anchors.
Also reported, no verdict: H3/C4 analogue (rewrite − accumulate structure) — the snapshot effect depends on post-capture divergence,
which a different learning rule may change.

## Interpretation committed BEFORE the Gumbel results are read (2026-09-05, Codex)
Two levels: (1) general principle — sparse transmission breaks symmetry among reconstructable structured solutions (A1, A3, A4);
(2) specific mechanism in compressed languages — class-matched anchors propagate the historical bias through shared conventions
(A2). The Gumbel learner produces nearly injective languages (≈61/64 distinct messages in the smoke test), i.e. few message classes.
If A1/A3/A4 replicate and A2 weakens or vanishes, that is read as: the principle is broader than one mechanism, and class-matched
anchoring is the local implementation of symmetry breaking when the language is compressed — not as a failure of the theory. The
second architecture is not required to reproduce the GRU's full phenomenology; it may sit in a different region of phase space.
Descriptive quantities to report for context: number of distinct messages, owner share, share of untaught objects with any
same-form neighbour.

## Decision tree committed before reading (Codex, 2026-09-05)
- A1/A3/A4 replicate with few collisions → the principle is general: sparse constraints break symmetry.
- A2 vanishes but coordination (A3) remains → class-matched anchoring is one realization of the principle, specific to compressed lexicons.
- A3 itself weakens → compression is probably needed to create the degeneracy that culture acts on; the principle is regime-bound.

## Addendum registered after reading A1–A4 on seeds 100–119 and BEFORE running seeds 120–139 (2026-09-05)
Finding on seeds 100–119: the Gumbel learner is near-injective (59.3/64 distinct messages; 4% of training objects have a same-form
neighbour vs 75% for the GRU). The registered partition measure (ARI) is degenerate in this regime (singleton partitions give ARI ≈ 0
by construction), so A3 by ARI is inconclusive for a measurement reason. Exploratory form-level agreement between siblings on
seeds 100–119: same record 0.45, different 0.23, none 0.00 (GRU: 0.47 / 0.25 / 0.01).
- A3′ (form-level symmetry breaking; new seeds 120–139): exact-form agreement between two independent siblings on training objects,
  same record > different records (primary) and different > none (secondary), ≥80% of seeds, paired CI > 0.
- A4′ (form-level target): agreement of siblings with the parent's step-500 forms is higher with stale anchors than with fresh
  anchors, ≥80%, CI > 0; and sibling–sibling form agreement with stale anchors is not more than 0.05 below fresh (CI lower ≥ −0.10).

## A3′/A4′ power extension (registered before running): seeds 140–159, pooled with 120–139 (n = 40), same rules.
