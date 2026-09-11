# Ω-DM-010 — Independent Source/Inertia Relation Test

Date: 2026-09-11
Status: PREREGISTERED

## Question
Can a single relational system produce a common scalar that predicts both source strength and inertial response when source and inertia are defined independently from the same graph but through different observables?

## Design
Use a weighted undirected graph W with positive edge weights. Generate two independent observables from distinct constructions:

1. SOURCE observable: response of a passive test field to a localized perturbation, measured by far-field amplitude.
2. INERTIA observable: response of a localized node cluster to an externally applied impulse, measured by inverse acceleration.

The source estimator does not use node degree or trace(L). The inertia estimator does not use the source response.

The graph is generated independently for each seed. The two observables are measured after graph generation and before any regression between them.

## Primary hypothesis
H1: SOURCE and INERTIA are positively and approximately linearly related across independently generated relational systems after normalization by the same fixed physical units of the simulation.

H0: There is no stable cross-system relation after controlling for graph size and direct graph statistics.

## Falsification
The hypothesis fails if the relationship disappears under held-out seeds, if it is fully explained by a direct graph statistic included as a covariate, or if label permutation produces a comparable relationship.

## Controls
- held-out seeds
- permutation of source/inertia pairing
- graph-size matched comparison
- degree/edge-count covariate control

## Important restriction
No mass symbol, Newtonian gravity law, inverse-square law, gravitational constant, or equation identifying source with mass is used in the generator or estimator.

## Physical status
This is a synthetic test of whether a relational model can generate two independently defined observables with a common scale. It is not a measurement of physical mass or gravity.

## Certification
Protocol frozen before certification execution. Any change to generator, estimator, seed list, metric, or acceptance criterion requires a new protocol version.
