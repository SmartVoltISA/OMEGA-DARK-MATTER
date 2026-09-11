# Ω-DM-013..016 — RELATIONAL SPACE / FAR-FIELD PROTOCOL v1.0

Date: 2026-09-11
Status: PREREGISTRATION DRAFT / BEFORE EXECUTION

## Scientific question

Can a minimal relational dynamical medium generate, without an imposed gravitational law, a localized persistent structure with measurable effective inertia and a reproducible long-range interaction whose falloff can be compared with known physical laws?

## Central hypothesis

H1: A sufficiently structured relational medium can generate localized dynamical states whose effective inertial response and mutual interaction arise from the medium dynamics. The far-field law is not specified in the generator.

H0: No stable relational-only localized state with an independently measurable inertial response and reproducible long-range interaction survives the controls, or the apparent interaction is explained by finite-size, boundary, discretization, noise, or explicitly encoded coupling.

## Hard anti-circularity rules

The generator MUST NOT contain:

- Newtonian mass as the target source parameter;
- a force proportional to 1/r^2;
- a Poisson equation selected specifically to create 1/r^2;
- a prescribed gravitational potential;
- a fitted exponent fed back into the generator;
- source amplitude defined from the final far-field observable.

## Layer 1 — relational medium

Use a 3D degree-normalized local relational medium. Each site carries an internal state q_i. Coupling strength must be normalized against local degree so the Ω-DM-006 finite-size failure is not repeated.

Candidate energy:

T = 0.5 * sum_i(qdot_i^2)
V = 0.5 * sum_(i,j) W_ij * (q_i-q_j)^2 + sum_i lambda/4 * (q_i^2-1)^2

The local state potential is an internal relational-state mechanism, not a mass term for the emergent object.

## Layer 2 — localized structure

Search for self-confined localized states without external walls or traps. Require:

- bounded RMS radius over the measurement window;
- convergence under grid refinement;
- convergence under box enlargement;
- persistence under independent seeds;
- no dependence on boundary reflections.

A state that fails stability is not promoted.

## Layer 3 — effective inertia

Define an emergent collective coordinate X from the measured center/shape of the localized state. Apply small controlled translations/velocities and measure independently:

1. kinetic-energy increment versus Xdot^2;
2. momentum/response versus Xdot;
3. acceleration under a weak external test perturbation.

Estimate M_eff independently from at least two observables. Agreement is required before using M_eff in Layer 4.

## Layer 4 — two-object interaction

Generate two localized structures independently, separated by r. Do not insert an object-object force. Measure:

- total energy E(r);
- acceleration of each structure;
- momentum transfer;
- response of the surrounding medium.

Estimate interaction from multiple independent observables.

## Blind far-field fit

Before revealing the generating parameters, fit the measured force/acceleration over a preregistered far-field interval to:

A) F(r) = A / r^p
B) F(r) = A * exp(-r/L)
C) F(r) = A / (r^2 + r0^2)^(p/2)
D) constant/finite-range null

The primary exponent p is estimated only after the generator and simulation seeds are locked.

No fit is declared evidence merely because p is near 2.

## 3D requirement

The far-field must be measured outside the localized source core and before the outer numerical boundary can influence the signal. Repeat at increasing box sizes and source separations.

## Controls

1. Linear/non-self-confined control.
2. Randomized relation topology with matched low-level statistics.
3. Shuffled source labels.
4. Boundary-size control.
5. Grid-resolution control.
6. Degree-normalization control.
7. Single-object no-partner control.
8. Sign-reversal/perturbation control where mathematically appropriate.
9. Independent seed replication.
10. Coordinate/partition transformation test.

## Success criteria

A strong SUPPORT result requires all of:

- stable localized structures;
- independently measured M_eff;
- interaction survives nulls;
- far-field interval survives box/grid changes;
- blind model comparison selects a reproducible law;
- exponent confidence interval excludes clearly incompatible alternatives;
- source strength and M_eff vary independently;
- no generator term encodes the selected law.

If any essential criterion fails, status is FAIL or INCONCLUSIVE, not SUPPORT.

## Interpretation boundary

Even a successful synthetic result would establish only that the proposed relational mechanism can generate the observed behavior in the model. It would NOT by itself establish dark matter, emergent physical spacetime, or an analogue Universe.

The next scientific step after a successful synthetic result is connection to independent physical observables and comparison against established gravitational models.
