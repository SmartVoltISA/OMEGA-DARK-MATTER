# Ω-DM-008 — Emergent Mass / Attraction Test

Date: 2026-09-11
Status: PREREGISTERED BEFORE NUMERICAL RUN

## Question

Can an attraction law with inverse-square scaling arise from a minimal local relation rule, without inserting `1/r^2` into the interaction law?

Can a source-strength parameter be recovered as an operational mass-like quantity from the same relational field?

## Minimal model

Use a scalar relational potential `phi` on a 3-D cubic lattice.

Local relation rule:

`sum_neighbours(phi_j - phi_i) = -q_i`

This is the discrete Poisson equation. No distance-dependent force law is supplied.

Boundary condition: phi = 0 on the outer boundary.

A source is a localized relational defect with source strength `q`.

Define the observable attraction field by the local gradient:

`F = -grad(phi)`.

The experiment tests whether the measured radial magnitude follows a power law `|F(r)| ~ r^(-p)` and whether `p` approaches 2 in the interior scaling regime.

## Mass operationalization

Do NOT identify `q` with physical mass by assumption.

Call `q` the relational source strength. Test whether it is:

1. additive for multiple separated sources;
2. linearly recoverable from the far-field amplitude;
3. dynamically equivalent to an inertial coefficient in a separate response test.

Only if these tests succeed may `q` be proposed as a mass-like relational quantity.

## Primary runs

Cubic lattice sizes: L = 41, 61, 81.

Single positive source at the center with q in `{1, 2, 4}`.

For each L and q:
- solve the discrete Poisson equation;
- compute central-difference gradient;
- bin |F| by radius;
- fit log(|F|) against log(r) only in the interior range `5 <= r <= L/5`;
- report exponent p, fit R^2, and amplitude A.

## Superposition / mass test

Run q = 1 and q = 2 independently and compare far-field amplitudes.

Run two separated sources q1=1, q2=2 and test whether the field is the sum of the independently measured fields within numerical tolerance.

## Null / falsification controls

1. 2-D version of the same local Poisson rule. It should produce a different radial law (logarithmic potential and approximately 1/r field), demonstrating that the exponent is not simply coded as `2`.
2. 1-D version, where the field is expected to have a different scaling.
3. Source sign reversal: force direction must reverse while magnitude scaling remains unchanged.

## Acceptance

PASS-CANDIDATE if:

- 3-D primary runs show p close to 2 with stable exponent across L;
- amplitude scales approximately linearly with q;
- superposition holds within numerical error;
- dimensional controls produce different scaling behaviour;
- no explicit inverse-square term occurs anywhere in the generator.

FAIL if the 3-D exponent is not approximately 2 or if the result is an artifact of a single lattice size.

## Critical interpretation

This experiment can establish only a mathematical emergence result: local relational balance on a 3-D lattice can generate an inverse-square field.

It does NOT establish Newtonian gravity or dark matter. In particular, it does not derive why physical gravity should obey this relational Poisson rule, nor does it derive physical units or the gravitational constant G.

The key question is whether the Ω relation language can supply the local balance principle from more primitive rules rather than taking Poisson's equation as a new axiom.
