# Ω-DM-019 — Conservation-Constrained Relational Response

## Question

What minimal property of a relation system is sufficient to produce a long-range environmental response, without defining gravity or inverse-square interaction as an input?

## Hypothesis

H1: local, symmetric, positive, conservative relations with a connected 3D medium can generate a gapless environmental response. In three dimensions, the radial gradient may asymptotically approach an inverse-square law as an emergent consequence of dimensional propagation and conservation, not as an inserted force law.

## Model

Nodes are only computational sampling points. Relations are local conductances between neighbouring points. Each edge has a positive symmetric weight W_ij = W_ji > 0. The response minimizes relational disagreement subject to a localized intervention and zero outer boundary.

The operator is constructed from relation weights, not from a hard-coded inverse-square law. No gravitational potential, gravitational constant, mass law, or pairwise force is inserted.

## Intervention logic

Run two states:

1. control: no localized intervention;
2. intervention: one localized source condition.

The primary object is the environmental difference:

`ΔR(r) = R(r | intervention) - R(r | control)`

The primary observable is:

`G(r) = |dΔR/dr|`

The analysis asks which functional family best describes G(r): power law, exponential, screened power law, or finite-size alternatives.

## Relation classes

Run separate ensembles:

A. homogeneous local relations;
B. weakly random symmetric local relations;
C. strongly random symmetric local relations;
D. anisotropic but stationary local relations;
E. non-conservative directed relations as a negative structural control.

This isolates conservation/symmetry from mere locality.

## Blind inference

The exponent is not fixed during generation. Fit candidate families only after raw response data are frozen. Report fit quality, residuals, stability over radius windows, and realization-to-realization variation.

## Required controls

- intervention-location permutation
- source-amplitude scaling
- lattice-resolution scaling
- domain-size scaling
- relation-weight permutation preserving marginal distribution
- directed/non-conservative control

## H1 criterion

A result supports H1 only if the long-range response is present across independent realizations and resolution/domain checks, is absent or qualitatively altered in the non-conservative control, and the power-law exponent converges toward the 3D value expected for a gapless conserved response without that exponent being used in model generation.

A close numerical exponent alone is insufficient.

## Interpretation boundary

Even a successful result would establish only a mathematical/model-level mechanism for an environmental response. It would not establish physical gravity or dark matter.
