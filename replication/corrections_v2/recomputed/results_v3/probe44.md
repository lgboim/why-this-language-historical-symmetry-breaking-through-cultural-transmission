# probe44 — where the basin comes from

## A. Stale vs fresh anchors (same 19 objects; 30 seeds; two independent siblings per arm): sibling–sibling ARI, child–parent(final) ARI, child–snapshot(500) ARI; staleness of the taught forms

| arm | taught forms ≠ parent final | ARI sib–sib | ARI child–parent final | ARI child–step-500 | sib−parent: seeds > 0 |
|---|---|---|---|---|---|
| fresh | 0.00 | 0.421 | 0.341 | 0.214 | 19/30 |
| stale | 0.72 | 0.502 | 0.246 | 0.399 | 30/30 |

sibling ARI, stale − fresh: | 30 | 17/13 | +0.080 | [-0.012, +0.175] | 0.585 | TWO-SIDED: no difference (CI) |
child–parent ARI, stale − fresh: | 30 | 4/26 | -0.094 | [-0.139, -0.048] | 0.000 | SUPPORTED |

## B. Founder-specific or world-generic? ARI between FINAL languages (train objects)

| comparison | n | ARI |
|---|---|---|
| different channels, same founder (same seed) | 450 | 0.148 |
| same channel, different founders (different seeds; common train objects) | 600 | 0.095 |
| gen 0 → gen 5, same lineage | 180 | 0.158 |
| gen 0 of seed A → gen 5 of seed B | 600 | 0.057 |

## C. Basin depth: sibling exact-form agreement on untaught objects (same-record arm, 45 seeds) by number of same-class anchors, and by distance to the nearest taught object

| same-class anchors 0 | 1 | 2+ | nearest taught at d=1 | d=2 | d=3 |
|---|---|---|---|---|---|
0.31 (n=1011) | 0.44 (n=246) | 0.48 (n=48) | 0.35 (n=1275) | 0.20 (n=30) | nan (n=0) |
