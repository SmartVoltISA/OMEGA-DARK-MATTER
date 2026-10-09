# EXP-09 — Nonlinear domain formation versus linear control
Date: 2026-10-09
Status: partial toy-model result; physical hypothesis unconfirmed.

## Preregistered question
With the same band-limited small random initial field, does the nonlinear double-well model develop regions near its two preferred states more strongly than a single-well linear control? Does the qualitative result persist under spatial refinement?

## Model
Periodic 1-D field:
- Nonlinear: \(\rho u_{tt}=K u_{xx}-\lambda u(u^2-\eta^2)\)
- Null/control: \(\rho u_{tt}=K u_{xx}-\lambda u\)

Parameters: L=80, T=20, K=rho=lambda=eta=1, initial RMS 0.03, same 40-mode band-limited random field by seed, CFL factor 0.2. Resolutions N=256, 512, 1024. Seeds 20261009–20261011 for ensemble at N=512.

Operational metrics:
- near-vacuum fraction: fraction with ||u|-eta| < 0.2;
- sign-change count on periodic domain: crude domain-boundary proxy, not particle count;
- RMS field amplitude;
- relative energy drift.

## EXP-09A — Nonlinear grid refinement, seed 20261009

| N | dx | Relative energy drift | Sign changes at T=20 | Near-vacuum fraction | RMS at T=20 |
|---:|---:|---:|---:|---:|---:|
| 256 | 0.3125 | -0.002299 | 8 | 0.3516 | 0.7756 |
| 512 | 0.15625 | -0.001281 | 8 | 0.3359 | 0.7596 |
| 1024 | 0.078125 | -0.000642 | 8 | 0.3242 | 0.7571 |

**Result:** for this fixed band-limited initial field, the final sign-change proxy is 8 at all three resolutions; RMS and near-vacuum fraction shift modestly, while relative energy drift decreases with refinement. This supports numerical robustness of this particular toy-model outcome, not a physical claim.

## EXP-09B — Linear single-well control

| N | Relative energy drift | Sign changes at T=20 | Near-double-well-vacuum fraction | RMS at T=20 |
|---:|---:|---:|---:|---:|
| 256 | -0.010836 | 10 | 0 | 0.01062 |
| 512 | -0.006696 | 8 | 0 | 0.01093 |
| 1024 | -0.003344 | 6 | 0 | 0.01108 |

The linear control remains small-amplitude and does not approach ±eta. Sign changes still occur in this tiny oscillatory field, showing why sign-change count alone is not a sufficient structural metric. Its energy drift is larger than in the nonlinear run at these settings and should be improved before making fine quantitative comparisons.

## EXP-09C — Nonlinear seed ensemble, N=512

| Seed | Relative energy drift | Sign changes | Near-vacuum fraction | RMS |
|---:|---:|---:|---:|---:|
| 20261009 | -0.001281 | 8 | 0.3359 | 0.7596 |
| 20261010 | -0.003055 | 8 | 0.2891 | 0.7720 |
| 20261011 | +0.000243 | 10 | 0.2793 | 0.6879 |

Across these three seeds, the field evolves from small fluctuations to substantial amplitude and has a nonzero fraction of points near the two minima. Outcomes vary by seed, as expected.

## Interpretation
**Partial pass:** the nonlinear double-well field exhibits behavior consistent with domain formation; the linear single-well control remains near zero. A fixed-seed resolution sweep preserves the domain proxy and shows decreasing energy drift.

**Critical limitation:** the double-well potential explicitly assumes two preferred states, and the field equation is given in advance. This experiment does not derive the field, its potential, or matter from “relation alone.” It is not evidence that physical matter is a relational fabric.

## Not tested
- Long-time persistence or collisions of domain walls.
- Whether structures are stable under perturbations over much longer times.
- An operational test separating internal dynamics from controllable information transfer.
- Emergence of the physical speed of light.
- Any galaxy, lensing, or cosmological data relevant to dark matter.

## Decision
Record as **toy-model partial success**. Next improve the numerical integrator/energy conservation and perform longer-time perturbation tests, then assess whether any result survives controls that do not build the target structure into the potential.
Raw data: `results/2026-10-09-relational-fabric-control-sweep.json`
Code: `experiments/relational_fabric_control_sweep.py`
