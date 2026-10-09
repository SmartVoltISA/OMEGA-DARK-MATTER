# EXP-08 — Spontaneous domains from random initial field
Date: 2026-10-09
Status: exploratory numerical result; not a physical confirmation.

## Preregistered question
Starting without a pre-seeded kink or particle node, does a continuous nonlinear field evolve from small random fluctuations into regions near distinct stable field values, with localized domain boundaries?

## Model and setup
Periodic 1-D domain, N=1024, L=80, T=20; K=rho=lambda=eta=1; initial field u(x,0)=0.03*Normal(0,1), zero initial velocity; fixed seeds 20261009, 20261010, 20261011. Evolution:
\[
\rho u_{tt}=K u_{xx}-\lambda u(u^2-\eta^2).
\]
The double-well potential has minima at u=+/-eta and u=0 is unstable. Therefore the mechanism for domain formation is explicitly built into the assumed equation; it is not derived from relation alone.

## Results

| Seed | Relative energy drift | Periodic sign changes (domain-wall proxy) | Fraction near |u|=eta within 0.2 |
|---:|---:|---:|---:|
| 20261009 | +0.000753 | 6 | 0.2871 |
| 20261010 | -0.001097 | 10 | 0.3496 |
| 20261011 | -0.002049 | 10 | 0.4150 |

The sign-change count is a crude indicator of domains/domain walls. It is not a certified count of stable solitons, and the energy drift is small but nonzero.

## Interpretation
**Partial pass:** in this selected continuous nonlinear field model, random initial fluctuations evolve into regions of both signs with multiple sign changes, without inserting a kink in the initial condition. This is a meaningful improvement over the seeded-kink preservation test.

**Not established:** this does not show that physical matter emerges from fundamental relations. The scalar field, its double-well potential, local differential equation, and characteristic speed are assumptions. Domain-wall persistence, collision behavior, ensemble statistics, and grid/time-step convergence for random starts still need tests.

## Controls still required
1. Linear-field/null-potential control (remove the double-well instability).
2. Amplitude sweep and multiple-seed ensemble.
3. Grid/time-step convergence using a consistent band-limited initial field across resolutions.
4. Longer-time persistence and perturbation/collision tests.
5. Operational causal-information test; do not equate characteristic speed with physical c without independent evidence.

Raw data: `results/2026-10-09-spontaneous-domains.json`
Code: `experiments/relational_fabric_spontaneous_domains.py`
