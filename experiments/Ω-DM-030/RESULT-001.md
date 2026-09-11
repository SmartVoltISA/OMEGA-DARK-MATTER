# Ω-DM-030 — RESULT-001

**Status: FAIL-H1 / H0 RETAINED**

## Actual local execution
Three coordinate-free graph generators were tested, six seeds each. Analysis used only adjacency and shortest-path distance from a source node.

### Shell-growth exponents

| generator | mean p | sample SD |
|---|---:|---:|
| triadic preferential growth | -7.067 | 1.881 |
| 6-regular random graph | 1.500 | 0.165 |
| Barabási–Albert preferential attachment | -5.334 | 1.149 |

The triadic and preferential-attachment networks show non-polynomial/finite-shell behavior over the fitted range, so their negative fitted exponents are not interpreted as physical dimensions. The 6-regular random graph is much closer to a finite-dimensional polynomial regime but gives p≈1.50 rather than 2.

## Interpretation
The minimal coordinate-free relation-only growth rules tested here do **not** spontaneously produce a robust intrinsic 3D shell-growth signature.

Therefore H1 is rejected for this tested class. H0 is retained.

This is consistent with Ω-DM-026: local relational exchange and conservation do not by themselves determine 3D geometry. Ω-DM-029 showed that a known 3D relational lattice contains a recoverable r^2 shell signature; Ω-DM-030 shows that removing the prescribed 3D geometry does not automatically recreate it under generic graph growth.

## Important correction to the program
The current evidence does not justify saying that 3D space emerges from relations alone. A successful theory must identify an additional dynamical selection principle that produces a stable finite-dimensional metric with effective dimension near 3.

Promising next target: search for a coordinate-free local rule whose stable fixed point simultaneously controls degree, graph-distance growth, curvature/defect density, and large-scale effective dimension, with d_eff measured blindly from the resulting graph.

## Non-claim
No statement about physical spacetime, gravity, or dark matter follows from this experiment.

## Reproducibility
Protocol: `experiments/Ω-DM-030/PROTOCOL.md`
Runner: `experiments/Ω-DM-030/run_r30.py`
