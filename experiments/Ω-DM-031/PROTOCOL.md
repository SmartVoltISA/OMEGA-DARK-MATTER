# Ω-DM-031 — Dynamic selection of effective dimension

## Question
Can a coordinate-free relational dynamics select a stable finite-dimensional metric with effective dimension near 3, without embedding the graph in a prescribed Euclidean lattice?

## H1
A local rewiring rule based only on graph-local state can produce a stable large-scale metric regime with d_eff near 3 across independent seeds.

## H0
The tested coordinate-free dynamics does not robustly select d_eff near 3, or the result is strongly dependent on initialization/parameters.

## Construction
Start from coordinate-free random connected graphs with fixed node count. Nodes have no spatial coordinates. Each update evaluates only graph-local quantities: degree, common-neighbour count, and shortest-path distances within a bounded hop radius.

Candidate edge additions favour pairs with high common-neighbour support; edge deletions favour edges whose endpoints have weak local support. Degree regularization prevents runaway hubs. Updates are accepted synchronously by a deterministic score rule, with no target dimension supplied.

Three initial graph ensembles are tested independently: Erdos-Renyi connected graphs, random regular graphs, and small-world graphs. Six seeds per ensemble.

## Blind measurement
After relaxation, node labels are randomly permuted. The analysis then uses only adjacency and graph shortest-path distance.

For several source nodes, measure shell population C(r), local volume growth, and effective dimension from the slope of log C(r) versus log r in an interior scaling window. Also report graph diameter, degree coefficient of variation, and seed-to-seed spread.

No coordinate embedding is used in the measurement and no dimension target is used in the dynamics.

## Acceptance
H1 requires d_eff approximately 3 with stable scaling over multiple shells, low seed-to-seed dispersion, and consistency across at least two initial ensembles. A single favourable seed or narrow finite-size crossover is insufficient.

## Scope
A positive result would establish only that this specified relational dynamics selects a 3D-like graph metric. It would not establish physical space, gravity, or dark matter. A negative result identifies that further structural selection principles are required.
