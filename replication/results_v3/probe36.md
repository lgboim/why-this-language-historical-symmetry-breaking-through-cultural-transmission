# probe36 — anatomy of an anchor

## A. The zero-anchor puzzle (caps 8/19/40; seeds 0–9 from results_v3 plus completed seeds 10–29 from results_v3_confirm2 for caps 8/40): untaught train objects with 0 taught H1 neighbours

| cap | n | mean #train H1 nbrs | share with ≤2 train nbrs | orphan in parent | parent per-obj acc | retention | retention, ≥3 train nbrs | retention, ≤2 train nbrs |
|---|---|---|---|---|---|---|---|---|
| 8 | 12926 | 6.48 | 0.00 | 0.59 | 0.91 | 0.142 | 0.142 | 0.120 |
| 19 | 3263 | 6.25 | 0.01 | 0.38 | 0.96 | 0.104 | 0.104 | 0.095 |
| 40 | 302 | 6.17 | 0.00 | 0.31 | 0.98 | 0.026 | 0.026 | nan |

## B. Anchor quality (6 focus cells, 30 seeds): untaught train o with exactly one taught H1 neighbour p (fresh: taught form == parent's final form). Retention of o's parent form by anchor type

| cell | same-class anchor (p's form == o's): n, retention | different-form anchor: n, retention | owner anchor | orphan anchor |
|---|---|---|---|---|
| random+accumulate | 296, 0.53 | 884, 0.18 | 0.24 | 0.29 |
| random+rewrite | 113, 0.57 | 487, 0.21 | 0.26 | 0.33 |
| success+accumulate | 302, 0.46 | 992, 0.19 | 0.24 | 0.26 |
| success+rewrite | 116, 0.53 | 712, 0.12 | 0.15 | 0.22 |
| hard+accumulate | 167, 0.56 | 661, 0.15 | 0.11 | 0.25 |
| hard+rewrite | 109, 0.67 | 564, 0.16 | 0.13 | 0.26 |

## C. Distance decay: untaught train o with 0 taught H1 neighbours, retention by number of taught H2 neighbours (6 focus cells pooled + cap 40 cells)

| cells | H2 anchors 0 | 1 | 2 | 3+ |
|---|---|---|---|---|
| focus (cap 19) | 0.022 (n=772) | 0.016 (n=430) | 0.081 (n=270) | 0.163 (n=1791) |
| cap 40 | 0.015 (n=67) | 0.000 (n=81) | 0.000 (n=72) | 0.085 (n=82) |
| cap 8 | 0.066 (n=1767) | 0.150 (n=1805) | 0.175 (n=2174) | 0.149 (n=7180) |

## D. Stale anchors (accumulate cells, where taught forms often differ from the parent's final form): untaught o with exactly one taught H1 neighbour. Retention of o's parent form, and adoption of the anchor's TAUGHT form, by anchor freshness

| cell | fresh anchors: n, o keeps parent form | stale anchors: n, o keeps parent form | stale: o adopts anchor's taught form | stale: o adopts anchor's parent-final form |
|---|---|---|---|---|
| random+accumulate | 347, 0.28 | 253, 0.13 | 0.24 | 0.08 |
| success+accumulate | 434, 0.28 | 391, 0.15 | 0.24 | 0.06 |
| hard+accumulate | 639, 0.22 | 42, 0.14 | 0.19 | 0.17 |
| hard+rewrite (control) | 673, 0.24 | 0, nan | nan | nan |

## E. Anchor pull: untaught train o whose parent form differs from its single fresh taught neighbour p. Child's final form for o: keeps parent form / adopts p's form / other. Compared with untaught o with no anchors whose parent form differs from a random H1 neighbour's (baseline adoption of that neighbour's form)

| cell | n | keeps | adopts anchor's form | other | baseline adoption (no anchor) |
|---|---|---|---|---|---|
| random+accumulate | 884 | 0.18 | 0.15 | 0.67 | 0.03 |
| random+rewrite | 487 | 0.21 | 0.16 | 0.63 | 0.04 |
| success+accumulate | 992 | 0.19 | 0.17 | 0.64 | 0.03 |
| success+rewrite | 712 | 0.12 | 0.21 | 0.66 | 0.03 |
| hard+accumulate | 661 | 0.15 | 0.18 | 0.67 | 0.08 |
| hard+rewrite | 564 | 0.16 | 0.17 | 0.67 | 0.06 |
