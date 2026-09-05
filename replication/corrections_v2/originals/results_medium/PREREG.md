# Boundary experiment M: medium world with hard distractors (registered 2026-09-05, before running)
World: 4 attributes × 4 values = 256 objects (64 held out), vocab 8, message length 4, 4,000 steps per generation, capacity 77 (≈ 40%
of 192 training objects, the analogue of 19/48). Half of all rounds (hard_frac = 0.5) draw their 4 distractors from the target's
Hamming-1 neighbours, so one attribute cannot identify the target; the other half are standard. Cells: the six record cells at
capacity 77 (select × fresh) + `generations`; seeds 0–9. Purpose (Codex): does anchoring / symmetry breaking survive when the
learner cannot rely on memorisation and easy discrimination? Same decision rule (≥80% seeds, paired CI).
- M1 (= K15, class-matched anchoring): retention with ≥1 same-form Hamming-1 taught neighbour − with other-form taught neighbours
  only ≥ 0.15, pooled over the six record cells, ≥80% of seeds.
- M2 (= K16, sibling symmetry breaking): two independently initialised children of the gen-0 parent, taught the same 77 random
  training pairs / two different random 77-sets / nothing (one 4,000-step generation): ARI same > different (primary) and
  different > none (secondary), ≥80%, CI > 0. Seeds 0–9 (10 seeds: verdicts allowed at n ≥ 8).
- M3 (= K13a, partition inheritance): parent–child ARI, rewrite cells − generations cell > 0, ≥80%, CI > 0.
- M4 (= H3/C4, snapshot effect): rewrite − accumulate topsim_distinct > 0 for random/success selection, ≥80%, CI > 0.
- Descriptive (no verdict): share of rounds solvable by one attribute; held-out accuracy; structure levels.
Evaluated by `confirm7.py`; siblings by `probe48.py`.
