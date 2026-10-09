# Ω relational-fabric experiment — continuous-field candidate (2026-10-09)

Status: exploratory numerical model; not evidence that real matter is a relational fabric.

## Question
Can a continuous field model (without preassigned particle nodes) produce a stable localized structure, and can its characteristic propagation speed be calculated from its dynamical coefficients rather than set as a separate speed cap?

## Preregistered scope and caveat
This experiment tests a *candidate continuum-field analogue*. A scalar field is still an assumed mathematical degree of freedom; this does not establish “relation without nodes” as the ontology of nature. The physical speed of light is not identified with the model speed.

## Model
One-dimensional nonlinear Klein–Gordon / phi^4 equation:

\[
\rho u_{tt}=K u_{xx}-\lambda u(u^2-\eta^2).
\]

Linearizing around a vacuum gives the characteristic high-frequency propagation scale

\[
v_{\mathrm{char}}=\sqrt{K/\rho}.
\]

This speed follows from coefficients in the equation, not from an independent cap. However, the form of the equation and its local continuum structure are assumptions; the model does not derive them from a more primitive relation.

A static kink initial condition is

\[
u(x,0)=\eta\tanh\left(x\sqrt{\frac{\lambda\eta^2}{2K}}\right),
\]

with zero initial velocity. A second test perturbs the +eta vacuum with a Gaussian pulse and records threshold arrival times at x=3,5,7. Threshold arrival speed is explicitly **not** treated as the exact causal-front speed.

## EXP-07A — Kink stability / grid refinement
Parameters: K=rho=lambda=eta=1; domain length L=40; final time T=8; CFL-like time-step factor 0.35. The kink centre and relative energy drift were measured.

| N | dx | Steps | Relative energy drift | Kink centre |
|---:|---:|---:|---:|---:|
| 201 | 0.2000 | 114 | -2.4771e-08 | ~0 |
| 401 | 0.1000 | 229 | -9.4183e-10 | ~0 |
| 801 | 0.0500 | 457 | -3.2032e-11 | ~0 |
| 1601 | 0.0250 | 914 | -1.0399e-12 | ~0 |

**Result:** the initialized localized kink remains centred and numerical energy drift decreases with refinement. This is consistent with a stable solution of the chosen equation. Because the initial condition is already the analytic static kink, this is a numerical preservation test—not spontaneous emergence from generic initial conditions.

## EXP-07B — Coefficient-to-speed and pulse-arrival sweep
Parameters: N=1601, L=40, T=10, lambda=eta=1, amplitude=0.05, sigma=0.3; threshold = 3% of initial amplitude.

| K | rho | Predicted characteristic speed sqrt(K/rho) | Threshold arrivals at x=3,5,7 | Fitted threshold-feature speed |
|---:|---:|---:|---|---:|
| 0.25 | 1 | 0.5 | 5.22, 9.70, not reached by T=10 | 0.446 (2 points only; weak estimate) |
| 1 | 1 | 1.0 | 2.51, 4.53, 6.55 | 0.990 |
| 4 | 1 | 2.0 | 1.25, 2.25, 3.25 | 2.000 |
| 1 | 4 | 0.5 | 5.02, 9.06, not reached by T=10 | 0.495 (2 points only; weak estimate) |

**Result:** for the measured threshold feature, fitted speeds track sqrt(K/rho) in the cases with three arrival points; the slower cases have only two points and a shorter observation window, so their speed estimates are weak. These are threshold-based pulse observations in a massive/dispersive nonlinear field, not a measurement of an exact causal front. The exact characteristic scale is derived from the chosen PDE coefficients.

## What passed
- The script defines and evolves a continuous field without explicit particle nodes.
- A localized kink solution is numerically preserved under grid refinement.
- The model's characteristic speed depends on K/rho as sqrt(K/rho).
- The pulse-threshold measurements are broadly consistent with that scale where enough arrival points are available.

## What did not pass / remains untested
- **Spontaneous emergence:** not tested. The kink is supplied as the initial condition.
- **Node-free ontology:** not established; a scalar field is assumed from the start.
- **Emergent physical c:** not established. The characteristic speed is model-dependent and not calibrated to the speed of light.
- **Faster hidden dynamics without superluminal signalling:** not tested by this model.
- **Dark matter:** no galactic, lensing, or cosmological data are used; this experiment says nothing for or against dark matter.

## Falsification / next tests
1. Start from random small-amplitude fields and generic finite-energy initial conditions; test whether stable localized structures arise without seeding a kink.
2. Compare with a linear-field null control and randomized initial conditions.
3. Test structure persistence after perturbations and collisions; define stability metrics before running.
4. Repeat pulse tests with domain, grid, time-step, threshold, and observation-window sweeps.
5. Define an operational controllable-information test. If any intervention can be detected at a receiver outside the causal cone implied by the model, the claimed separation between internal dynamics and information fails.
6. Only after the toy model passes should it be compared with empirical physics. Do not identify v_char with c by naming alone.

## Reproducibility
Executable source: `experiments/relational_fabric_phi4.py` (NumPy required). It prints a JSON record of the grid and coefficient sweeps. Reported values above were calculated using the same equations and parameters in a Python numerical run. Future reruns should preserve the raw JSON output alongside the code version.

## Decision
**Partial toy-model success, physical hypothesis unconfirmed.** A continuous nonlinear field can support a stable localized solution and has a characteristic speed set by its coefficients. The experiment does not show that matter is made of relations, that structures emerge spontaneously, or that the speed of light is derived from the fabric.
