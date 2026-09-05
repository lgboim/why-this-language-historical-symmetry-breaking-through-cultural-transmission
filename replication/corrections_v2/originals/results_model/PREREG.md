# Formal toy model (specified 2026-09-05, before simulation)
Objects = nodes of the Hamming graph (3 attributes × 4 values; edges between objects differing in one attribute). A language is a
partition P of the objects into message classes, plus surface forms: each class carries a form drawn by the learner (learner-specific
random code) unless an anchor supplies it. Learner objective (nothing about anchoring is built in):
  E(P) = c · #(within-class pairs)            [communicative cost: collisions]
       + λ · #(classes)                        [simplicity]
       + w · #(Hamming-1 edges cut by P)       [local smoothness]
Minimisers are many and symmetric (any relabelling / any choice of which neighbours merge). A learner runs greedy local search from a
seeded random initial partition; anchors are nodes whose class label is fixed to the record's label (records carry (object, form)
pairs; two anchors with the same form share a class). Reconstruction = the minimiser reached.
Derived predictions to test by simulation (and by hand on a 1-D chain where possible):
  T1 siblings (same anchors) converge to the same partition more than siblings with different anchors, more than with none.
  T2 an anchor stabilises an untaught neighbour's parent class iff the anchor's form is the neighbour's parent-class form
     (class-matched); an anchor carrying a different form does not — this must EMERGE from E, not be assumed.
  T3 anchors sampled from an early partition P_early coordinate siblings as well as anchors from P_final, but onto P_early.
  T4 iterated: with anchors resampled each generation from the parent's final partition (rewrite) vs from a frozen early partition
     (accumulate), similarity to the founder decays more slowly under rewrite.

Wording note (2026-09-05, after simulation): 'nothing about anchoring is built in' should read 'anchors are fixed nodes; the class-matched spillover effect is not built in'. Thresholds/predictions unchanged.
