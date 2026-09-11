# Ω-DM-016 — INDEPENDENT DYNAMICAL INERTIA CHECK v1.0

Date: 2026-09-11
Status: PREREGISTRATION / EXECUTION REQUIRED

## Question

Does the positive energy-defined coefficient M_E found in Ω-DM-014 correspond to an independently measurable dynamical response M_D of the same localized relational defect?

## H1

A localized relational excitation has a nonzero dynamical inertial response. A weak external perturbation produces an acceleration whose independently measured value is consistent with the energy metric M_E from Ω-DM-014.

## H0

The apparent M_E does not produce a reproducible dynamical inertial response, or M_D disagrees with M_E beyond the preregistered tolerance.

## Anti-circularity

- No absolute mass parameter.
- No Newtonian force law.
- No 1/r^2 interaction.
- The external perturbation is a uniform, weak bias applied to the field configuration; it is not calibrated from M_E.
- M_D is obtained from measured acceleration under known perturbation strength.
- M_E is taken from the already locked Ω-DM-014 result and is not refit during this experiment.

## Model

Use the same 1D relational field family as Ω-DM-014:

T = 0.5 * sum_i(qdot_i^2)
V = 0.5 * k * sum_i(q_(i+1)-q_i)^2 + sum_i 0.25 * (q_i^2-1)^2

The localized excitation is the kink profile. Its center X is determined from the zero crossing of q using interpolation.

## Dynamical protocol

1. Relax a kink on N=201 and N=401 grids for k in {0.5, 1.0, 2.0}.
2. Give the relaxed profile a small translational velocity U in {0.05, 0.10} using qdot_i = -U * dq_i/dx.
3. Evolve the Hamiltonian equations with a symplectic velocity-Verlet integrator, with no damping.
4. Independently apply a small uniform generalized bias through an additive term -f * X(q) only for the response measurement. The sign and magnitude f are fixed before execution.
5. Measure X(t) over the initial linear-response window, before boundary effects or radiation return to the core.
6. Fit X(t) = X0 + V0*t + 0.5*a*t^2.
7. Define M_D = f / |a|.
8. Repeat for both signs of f and multiple seeds/phase offsets.

## Required controls

- f = 0 free-motion control: no systematic acceleration.
- +f and -f sign reversal: acceleration must reverse sign.
- factor-of-two perturbation control: M_D should remain stable in linear regime.
- N=201 vs N=401 boundary control.
- k = 0.5, 1.0, 2.0 stiffness series.
- stationary kink control.
- translated initial position control.

## Decision rule

For each k, compare M_D with locked Ω-DM-014 M_E.

Primary agreement criterion: relative difference |M_D-M_E|/M_E <= 10% after averaging the +f/-f response.

H1 dynamical validation requires:

- nonzero acceleration for both perturbation signs;
- sign reversal under f -> -f;
- M_D stable under factor-of-two f scaling;
- M_D convergent under N enlargement;
- M_D agrees with M_E within 10% for at least k=1.0 and does not systematically diverge for the other tested k values.

If acceleration is present but M_D and M_E disagree, classify as PARTIAL / OPEN rather than SUPPORT.

## Scope

A positive result would validate an independent dynamical-response interpretation of emergent inertia in this model. It would not establish physical inertia, gravity, dark matter, or an analogue Universe.

## Locked reference values from Ω-DM-014

k=0.5: M_E ~= 1.203
k=1.0: M_E ~= 0.913
k=2.0: M_E ~= 0.657
