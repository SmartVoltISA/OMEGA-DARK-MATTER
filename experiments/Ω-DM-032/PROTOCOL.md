# Ω-DM-032 — Coordinate-free curvature-neutral rewiring

## Question
Can a local geometric regularity principle, defined only from relational graph structure and without a prescribed spatial dimension, select a stable finite-dimensional metric regime near d_eff = 3?

## Motivation
Ω-DM-031 showed that common-neighbour closure plus degree regularization does not robustly select three-dimensional shell growth. Ω-DM-032 tests a different class: local curvature/defect regulation.

## H1
A coordinate-free local rewiring dynamics that reduces relational curvature defects, without specifying d=3, produces a stable large-scale shell-growth dimension near 3 across independent seeds and initial ensembles.

## H0
Curvature-neutral local rewiring does not robustly select d_eff near 3, or the result depends strongly on initialization/parameters.

## Local observable
For an undirected simple graph, define edge triangle support t(u,v) as the number of common neighbours of u and v. Define a purely combinatorial edge-curvature proxy

K(u,v) = 4 - deg(u) - deg(v) + 3*t(u,v).

This is used only as a local relational defect observable. No coordinates, Euclidean distances, target dimension, or physical curvature are supplied.

Define the relational defect energy

E_K = mean(K(u,v)^2)

over all edges.

## Dynamics
Each update is a degree-preserving local 2-switch. Select a non-edge (u,v) at graph distance <=2. Select an existing edge (a,b) such that the proposed replacement removes (u,a) and (v,b) and adds (u,v) and (a,b), with all four nodes distinct and with no duplicate edge created. The switch is accepted only if it preserves connectivity and strictly decreases E_K.

Because the move is a 2-switch, every node degree is preserved exactly. No target degree is supplied.

The candidate scan is deterministic from the current graph ordering; no parameter is tuned to favour d=3.

## Initial ensembles
- Erdos-Renyi connected graph, p=0.045
- random 6-regular graph
- Watts-Strogatz small-world graph, k=6, rewiring=0.15

N=500, six seeds per ensemble.

## Blind measurement
After dynamics, randomly permute node labels. Measure shell population C(r) using shortest-path distance only, from eight random sources per realization. Fit log C(r) versus log r over an automatically selected interior range with at least four nonzero shells and excluding the final shell. Report d_eff, shell-fit residual, graph diameter, degree statistics, and E_K.

No coordinate embedding is used.

## Acceptance
H1 requires d_eff near 3 across multiple seeds, low seed-to-seed dispersion, stable shell scaling, and consistency across at least two initial ensembles. A single favourable seed or narrow finite-size crossover is insufficient.

## Scope
A positive result would establish only that this specified coordinate-free graph dynamics selects a 3D-like relational metric. It would not establish physical spacetime, gravity, or dark matter.
