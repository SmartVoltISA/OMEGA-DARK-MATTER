# Ω-10 — Perturbed kink persistence and kink–antikink approach

**Date:** 2026-10-09  
**Status:** Numerical toy-model tests executed; interpretation limited.

## Question

Does a localized topological transition in a 1D nonlinear scalar field remain approximately localized under a small perturbation, and what happens when a kink and antikink move toward each other?

## Model and numerical method

Dimensionless equation:

\[
u_{tt}=u_{xx}-u(u^2-1)
\]

This is the \(\phi^4\) scalar-field equation with a double-well potential \(V(u)=(u^2-1)^2/4\). The potential explicitly builds in two preferred field values, \(u=\pm1\); the experiment does **not** derive them from relations alone. Time stepping uses a centered finite-difference spatial Laplacian and leapfrog-style update. Results are dimensionless and are not calibrated to physical particles or SI units.

## Test A — perturbed single kink

- Grid: N=1024, L=80; dt=0.015625; T=30; 1920 steps.
- Fixed boundaries u(-L/2)=-1 and u(L/2)=+1.
- Initial state: \(\tanh(x/\sqrt2)\), plus small seeded localized random perturbations (seed 20261012).
- Initial energy: 1.0009963319.
- Final energy: 1.0013704116.
- Relative energy drift: +0.0003737 (+0.0374%).
- Measured kink center: 0 initially, -0.05908 at T=30.
- RMS difference from the unperturbed kink rose from 0.00171 at t=3 to 0.00659 at t=30.

**Result:** the kink remained identifiable and its center moved only slightly over this run. The perturbation measure grew gradually; this is not proof of asymptotic stability, only finite-time persistence under this specific perturbation and discretization.

## Test B — inward-moving kink–antikink pair

- Periodic grid: N=1024, L=80; dt=0.015625; T=50; 3200 steps.
- Initial wall centers approximately -8 and +8; prescribed inward speed 0.2.
- Initial energy: 1.9225640746.
- Final energy: 1.9230243770.
- Relative energy drift at T=50: +0.0002394 (+0.0239%).

| t | Detected zero crossings (wall positions) | Center field u(0) | Energy |
|---:|---|---:|---:|
| 0 | -8.000, +8.000 | -0.99995 | 1.922564 |
| 10 | -6.039, +6.039 | -1.00073 | 1.922552 |
| 20 | -4.079, +4.079 | -0.99089 | 1.922544 |
| 30 | -1.986, +1.986 | -0.77759 | 1.922658 |
| 35 | none detected | +1.27359 | 1.944160 |
| 40 | -2.069, +2.069 | -0.87659 | 1.921833 |
| 45 | -2.392, +2.392 | -0.85815 | 1.922426 |
| 50 | -2.076, +2.076 | -0.66623 | 1.923024 |

**Important diagnostic warning:** at t=35 the simple zero-crossing detector reports no walls while the center field overshoots above +1 and the computed energy spikes by about 1.12%; the energy then returns near its earlier value. Do not interpret this snapshot as confirmed annihilation. It is a transient diagnostic/numerical anomaly requiring a smaller time step, alternative integrator, and direct field-profile inspection.

## Conclusions

1. **Finite-time persistence: provisionally observed** for one perturbed kink over T=30, with small center displacement and ~0.0374% energy drift.
2. **Approach: observed** for the kink–antikink pair; their zero crossings move inward from ±8 to around ±2 by t=30.
3. **Collision outcome: unresolved.** The t=35 anomaly makes a claim of annihilation or clean passage invalid.
4. This model assumes a nonlinear field and a double-well potential. It does not demonstrate that matter is literally a relational fabric, does not derive particles from first principles, and says nothing about superluminal information transfer.

## Reproducibility

Script: `experiments/relational_fabric_stability_collision.py`  
Raw numerical record: `results/2026-10-09-relational-fabric-stability-collision.json`

The run values above came from equivalent Python functions executed in the current session. The committed script is the reproducible implementation; it was not executed directly from the GitHub checkout during this run.
