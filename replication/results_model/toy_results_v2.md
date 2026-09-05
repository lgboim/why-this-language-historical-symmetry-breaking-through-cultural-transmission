# Toy model — corrected T4 and measured T2 move cost (20 seeds; design fixed in T4_correction_design.md before running)

founder vs its own early partition: ARI 0.701

## T4 (corrected): ARI to the founder by generation, mean over 20 seeds
| record | g1 | g2 | g3 | g4 | g5 |
|---|---|---|---|---|---|
| rewrite (anchors from the current parent's final partition) | 0.466 | 0.314 | 0.327 | 0.242 | 0.198 |
| accumulate (anchors from the founder's FROZEN early partition) | 0.382 | 0.324 | 0.376 | 0.399 | 0.306 |

g5 paired difference rewrite − accumulate: -0.109 [-0.175, -0.048] (5,000 paired bootstrap resamples); rewrite higher in 5/20, lower in 15/20, tied 0
per-generation mean differences rewrite − accumulate: g1 +0.085, g2 -0.010, g3 -0.049, g4 -0.158, g5 -0.109
Descriptive; no threshold was registered for T4. A higher endpoint is not by itself a slower decay rate.

Original (invalid for this claim) implementation drew a fresh unrelated shallow partition each generation: rewrite 0.466, 0.314, 0.327, 0.242, 0.198; accumulate 0.263, 0.196, 0.194, 0.158, 0.157 (results_model/toy_results.md).

## T2 move cost, measured at the converged child (untaught object o, anchored Hamming-1 neighbour a)
| anchor | n pairs | share of o already in a's class | mean ΔE of moving o into a's class (if not there) | share with ΔE ≤ 0 |
|---|---|---|---|---|
| same-class anchor | 614 | 0.44 | +1.11 | 0.35 |
| other-class anchor | 1798 | 0.13 | +1.85 | 0.13 |

ΔE = c·(m_dest − (m_src − 1)) + λ·Δ#classes + w·Δ#cut edges, with c = 1, λ = 6, w = 1. This replaces the published verbal claim that the marginal within-class cost is 'below w'.
