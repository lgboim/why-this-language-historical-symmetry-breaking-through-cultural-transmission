# T4 correction: design fixed before running (2026-09-05)

## Why
The verification of 2026-09-05 found that `model.py:75` implements the "accumulate" arm of T4 as a *fresh, unrelated* shallow
partition every generation (`reconstruct({}, RandomState(2000 + 10*s + g), sweeps=1)`), ignoring the founder and the current parent.
The registration (`results_model/PREREG.md`, T4) specifies anchors resampled from a **frozen early partition**. The published T4 row
therefore did not test the registered condition. The original outputs (`results_model/toy_results.md`) are preserved unchanged as
invalid-for-this-claim historical results.

## Operational definition (the only interpretive choice, taken here before any new result is seen)
"Frozen early partition" = the founder's own early developmental state, E_s = `reconstruct({}, RandomState(1000 + s), sweeps=1)`:
the same object already used as "the parent's early partition" in T3 (it is the shallow search from the founder's own initialisation,
so it stands to the founder as the step-500 snapshot stands to the final language in the neural experiments). It is fixed once per
seed and reused at every generation of the accumulate arm. The rewrite arm is unchanged: anchors are resampled each generation
from the current parent's final partition.

A variant in which each generation's record is the *current parent's* early state would be a different experiment (it is not the
registered frozen-record condition) and is not part of this correction.

## Procedure (identical to model.py except for the one line)
- Seeds 0–19; founder = `parents[s]`; same random streams as the original (`RandomState(500 + s)` for anchor sampling,
  `RandomState(300 + 10*s + g)` for each generation's reconstruction); 19 anchors per generation; 5 generations.
- accumulate: `src = E_s` (frozen); rewrite: `src = P` (current parent).
- Outcome per seed and generation: ARI(child_g, founder). Report the full paired trajectories (means and per-seed values), the
  per-seed g5 difference rewrite − accumulate with a 5,000-resample paired bootstrap CI and sign counts, and the founder-vs-early ARI.
- No numerical threshold was registered for T4; any inferential rule stated here is a correction-stage analysis, labelled as such:
  we report the g5 paired contrast and its CI descriptively. A higher endpoint alone is not proof of a slower decay *rate*; we also
  report the per-generation differences.
- The outcome is reported whatever its sign, in `results_model/toy_results_v2.md`, Table S4, MODEL.md and the changelog. If the
  registered condition does not reproduce the neural K18 pattern, the main-text support clause is removed and the negative result
  is kept in the Supplement.

## T2 derivation check (same run)
The published sketch claimed the marginal within-class cost of joining an anchored neighbour's class is "below w". With c = w = 1 that
is false in general (joining a class of size m adds m collision pairs). The corrected sketch must use the full move cost
ΔE = c·(m_dest − (m_src − 1)) + λ·(Δ#classes) + w·(Δ#cut edges). In the same run we therefore measure directly, for every untaught
object o with an anchored Hamming-1 neighbour, the greedy ΔE of moving o into that neighbour's class at the converged child, split
by whether the anchor carries o's parent-class label (same-class) or another label. This replaces the verbal argument with a
measured quantity; it is descriptive.
