# Toy model — simulation results (20 seeds)

parents: 20.2 classes on average; energy minimisers are non-unique (ARI between two no-anchor learners of the same world = 0.23)

## T1 siblings
| anchors | ARI sib–sib | ARI sib–parent |
|---|---|---|
| same | 0.414 | 0.454 |
| different | 0.273 | 0.437 |
| none | 0.236 | 0.213 |

## T2 class-matched anchoring (emergent): untaught object keeps its parent classmates
| anchor situation | n | kept |
|---|---|---|
| same-class anchor | 480 | 0.47 |
| other-class anchors only | 391 | 0.32 |
| no anchor | 29 | 0.31 |

## T3 strength vs target
| anchors from | ARI sib–sib | ARI to parent final | ARI to parent early |
|---|---|---|---|
| final | 0.414 | 0.454 | 0.376 |
| early | 0.368 | 0.374 | 0.397 |
(early vs final partitions of the same parent: ARI 0.70)

## T4 persistence (ARI to founder by generation)
| record | g1 | g2 | g3 | g4 | g5 |
|---|---|---|---|---|---|
| rewrite | 0.466 | 0.314 | 0.327 | 0.242 | 0.198 |
| accumulate | 0.263 | 0.196 | 0.194 | 0.158 | 0.157 |
