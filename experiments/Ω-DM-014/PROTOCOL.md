# Ω-DM-014 — Stiffness, density and motion

Status: PREREGISTERED
Date: 2026-09-11

## Question

Can an effective inertial response emerge from the combination of relational stiffness, relation density, and motion of a localized structural excitation, without inserting mass as a primitive parameter?

## Core idea

Do not try to make uniform translation massive. Instead construct a localized relational structure whose motion necessarily changes many internal relations.

The candidate chain is:

relation density -> collective stiffness -> internal deformation during motion -> kinetic response -> effective inertia

## Model

Use a one-dimensional chain of N nodes with scalar internal states q_i and nearest-neighbour relations.

Kinetic term:
T = 0.5 * sum_i (dq_i/dt)^2

Potential:
V = 0.5 * k * sum_i (q_(i+1)-q_i)^2 + sum_i lambda/4 * (q_i^2 - 1)^2

with k=1 and lambda=1.

No absolute translational mass parameter is introduced. The field kinetic term describes internal state dynamics; the effective mass of a moving localized structure is to be measured, not inserted.

A kink-like localized transition between q=-1 and q=+1 is prepared and relaxed to a static configuration. Its collective coordinate X is defined by the zero crossing / interpolated center.

## Density and stiffness sweeps

Primary systems:
N = 101, 201, 401.
Relation density is varied by using bond occupancy fractions d in {0.50, 0.75, 1.00}, with occupied bonds retaining k=1. Missing bonds are fixed for each run.

Stiffness sweep:
k in {0.5, 1.0, 2.0}.

The purpose is to test whether the effective response depends systematically on relational density and stiffness rather than on an inserted mass coefficient.

## Measurement A — energy-defined inertia

Construct a translated kink profile q_i(X) over an interior range of X. Compute
M_E(X) = sum_i (dq_i/dX)^2.

For a constant small collective velocity U, the predicted kinetic energy is
E_kin = 0.5 * M_E * U^2.

## Measurement B — dynamical response

Launch the relaxed kink with qdot_i = -U * dq_i/dX and integrate the full equations of motion.

Measure X(t) from the evolving field. In a homogeneous interior region, the kink should move approximately freely. M_D is inferred from the response to a weak, explicitly documented localized perturbation that produces a known potential gradient, using
M_D = -dU_p/dX / acceleration.

The perturbation is only a probe potential; it is not used to define inertia.

## Primary hypothesis H1

A stable nonzero effective inertial coefficient exists for the moving relational defect and is independently recovered by both measurements A and B.

Acceptance:
1. M_E > 0 on every full-density connected-chain run.
2. M_D > 0 and agrees with M_E within 10% on the validation subset.
3. M_E changes systematically with stiffness k and relation density d.
4. At fixed k and defect family, increasing relation density does not leave M_E invariant by construction.
5. No explicit mass term or absolute translational kinetic term is added.

H0:
No stable positive effective inertia is recovered, or independent energy and dynamical measurements disagree beyond the tolerance.

## Controls

1. Uniform state q_i=+1: verify no localized defect inertia is inferred.
2. Static kink: verify numerical drift is negligible.
3. Velocity scaling U={0.1,0.2,0.4}: M_E must be invariant.
4. Timestep halving on validation runs.
5. Broken-density control: compare disconnected / weakly connected cases separately and never mix them with the connected primary sample.

## Interpretation

A PASS would demonstrate an emergent inertial coefficient of a localized relational excitation in this concrete field model. It would not establish physical mass, gravity, or dark matter.

A FAIL would indicate that stiffness-density structure alone does not generate the required dynamical response in this construction.

The decisive distinction from Ω-DM-012/013 is that the moving object is a localized change of internal relational state, not a uniform translation of every coordinate. Therefore its motion can consume kinetic energy through internal rearrangement without requiring an absolute position-dependent term.

All equations use plain text for reproducibility and display safety.