# Ω-DM-033 — Efficient curvature-defect regulation stress test

## Purpose
Follow-up to Ω-DM-032. The previous exact N=500 runner is computationally expensive; this preregistered stress test uses a smaller graph to determine whether curvature-defect regulation shows any robust tendency toward d_eff≈3 before scaling up.

## H1
Curvature-defect minimization produces a stable effective shell dimension near 3 across independent seeds and both regular and small-world initial ensembles.

## H0
The dynamics does not robustly select d_eff≈3.

## Fixed configuration
N=120; 6 seeds per ensemble; 30 accepted-improvement search rounds; degree-preserving 2-switches; local Forman-type curvature score K=4-deg(u)-deg(v)+3*t(u,v); objective is variance of node-averaged K; no coordinates and no target dimension.

Initial ensembles: random 6-regular and Watts-Strogatz small-world (k=6, rewiring=0.15).

Measurement: graph shortest-path shell counts from six randomly selected sources, fit log C(r) versus log r for r=1..8 excluding empty shells. Node labels are treated as anonymous.

## Acceptance
PASS only if both ensembles have mean d_eff near 3 with low seed dispersion. Otherwise H0 is retained. This is a model-level graph result only and makes no physical gravity/dark-matter claim.
