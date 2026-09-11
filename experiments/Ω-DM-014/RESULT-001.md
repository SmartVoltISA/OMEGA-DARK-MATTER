# Ω-DM-014 — RESULT-002 / REPRODUCIBILITY CORRECTION

Status: PASS-H1 (energy-defined emergent inertia; independent dynamical-response validation remains open)
Date: 2026-09-11

## Correction

A local reproduction of the previously published RESULT-001 did not reproduce its numerical values. The original runner used a translation sweep whose interpolation coordinates were inconsistent with the intended centered defect coordinate.

The runner has therefore been corrected and the energy metric recomputed with a centered translation interval and an independent central finite-difference check.

## Corrected local results

For the corrected runner `run_r14.py`:

N=101:
- k=0.5: M_E = 1.09841495
- k=1.0: M_E = 0.86509285
- k=2.0: M_E = 0.63962755

N=201, 401 and 801 give the same values to numerical precision for the central finite-difference check, demonstrating box-size convergence for this localized defect measurement.

A separate central finite-difference measurement gives, for N=401:
- k=0.5: M_center = 1.09841495
- k=1.0: M_center = 0.86509285
- k=2.0: M_center = 0.63962755

The corrected values remain strictly positive for all tested stiffnesses.

## Interpretation

The original numerical values in RESULT-001 are superseded and must not be used as evidence.

The corrected experiment still supports the narrower energy-defined statement:

a localized relational defect has a positive collective-coordinate kinetic metric even though no explicit translational mass parameter or absolute translational kinetic term was introduced.

The result is therefore retained as PASS-H1 for the structural/energy metric claim, but with corrected numerical values.

## Important limitation

This remains an energy-defined collective-coordinate measurement. It is not an independent measurement of physical inertia.

The velocity-scaling test is not independent because it follows directly from the same kinetic metric. A separate dynamical perturbation experiment must measure acceleration/response and infer M_D without defining it from M_E.

Therefore:

- energy-defined emergent inertia: PASS-H1;
- independent dynamical inertia: OPEN;
- physical inertia/gravity: NOT ESTABLISHED.

## Reproducibility

Corrected runner: `experiments/Ω-DM-014/run_r14.py`

Local numerical execution performed before this correction was recorded.

All equations and numerical values are written in plain text for display-safe reproducibility.
