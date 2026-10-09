# Ω-10 follow-up — collision convergence and speed scan

**Date:** 2026-10-09  
**Status:** Numerical tests executed; previous collision anomaly investigated.

## Question

The earlier run appeared to lose both zero crossings near t≈35 and showed an apparent energy spike. Was that physical, a detector failure, or a time-integration artifact?

## Model and improved numerical method

Dimensionless \(\phi^4\) field equation:

\[
u_{tt}=u_{xx}-u(u^2-1).
\]

Periodic grid, centered second-difference Laplacian, and velocity-Verlet time stepping. The discrete energy diagnostic uses the same forward-difference gradient as the discrete Laplacian. The double-well potential \(V(u)=(u^2-1)^2/4\) explicitly encodes two preferred field values \(\pm1\). This is a toy model, not a first-principles theory of matter.

## A. Resolution and time-step convergence

Six runs: N=512 and N=1024, each with CFL factors 0.2, 0.1, and 0.05; initial wall centers approximately ±8 and inward speed 0.2.

| N | CFL | dt | Relative energy drift at T=50 | Walls at t=30 |
|---:|---:|---:|---:|---|
| 512 | 0.20 | 0.03125 | −2.5291×10⁻⁶ | ±1.9935 |
| 512 | 0.10 | 0.015625 | −6.3422×10⁻⁷ | ±1.9935 |
| 512 | 0.05 | 0.0078125 | −1.5868×10⁻⁷ | ±1.9935 |
| 1024 | 0.20 | 0.015625 | −6.1221×10⁻⁷ | ±1.9864 |
| 1024 | 0.10 | 0.0078125 | −1.5325×10⁻⁷ | ±1.9864 |
| 1024 | 0.05 | 0.00390625 | −3.8326×10⁻⁸ | ±1.9864 |

Energy drift decreases by about a factor of four when dt is halved, consistent with second-order time-discretization error. Wall positions at t=30 are stable across time steps and close across spatial resolutions.

## B. What happens around the apparent disappearance?

High-resolution run: N=1024, dt=0.00390625, samples every 0.5 time units.

| t | Zero crossings | Center u(0) | Field minimum | Field maximum | Relative energy drift |
|---:|---:|---:|---:|---:|---:|
| 30.0 | 2 | −0.7776 | −0.7776 | 1.0013 | ~0 |
| 32.0 | 2 | −0.4054 | −0.4054 | 1.0010 | +0.0000002 |
| 33.0 | 0 | +0.1441 | +0.1441 | 1.0009 | +0.0000006 |
| 34.0 | 0 | +1.3465 | +0.9989 | 1.3465 | −0.0000079 |
| 34.5 | 0 | +1.6797 | +0.9991 | 1.6797 | +0.0000065 |
| 35.0 | 0 | +1.2737 | +0.9991 | 1.3012 | −0.0000072 |
| 36.0 | 0 | +0.2137 | +0.2137 | 1.0205 | +0.0000003 |
| 36.5 | 2 | −0.0668 | −0.0668 | 1.0046 | +0.0000004 |
| 37.0 | 2 | −0.2541 | −0.2541 | 1.0010 | +0.0000002 |
| 40.0 | 2 | −0.8766 | −0.8766 | 1.0011 | ~0 |

**Finding:** zero crossings disappear temporarily and return around t≈36.5. The central field makes a positive excursion, then the two boundaries re-emerge. This is a nonlinear encounter and re-emergence in this simulated trajectory, not confirmed annihilation.

With the improved energy definition and velocity-Verlet integrator, energy stays close to conserved through this interval. The earlier apparent ~1.1% energy spike was caused by an inconsistent energy diagnostic/integration pairing and should not be interpreted as physical energy creation.

## C. Incoming-speed scan

N=512, CFL=0.1, initial wall centers ±8. Each run continued beyond the first encounter.

| Initial speed | Duration | Relative energy drift at end | Wall count at end | Interpretation |
|---:|---:|---:|---:|---|
| 0.1 | 168.0 | −5.65×10⁻⁷ | 0 | No walls detected at final sample after long evolution |
| 0.2 | 88.0 | −1.95×10⁻⁶ | 0 | No walls detected at final sample after longer evolution |
| 0.3 | 61.33 | −1.23×10⁻⁶ | 2 | Two walls detected at final sample |

Endpoint counts alone do not classify scattering: zero crossings can disappear temporarily and reappear. A future classifier must track field profiles, wall trajectories, and energy distribution throughout the run.

## Conclusions

1. The collision-region behavior is robust across tested time steps and two spatial resolutions.
2. The apparent disappearance is temporary in the detailed speed-0.2 trajectory: the central field becomes positive and the two zero crossings return.
3. The old energy spike was not trustworthy. The improved discrete-energy diagnostic and velocity-Verlet update show relative energy drift below about 0.00026% across the six convergence runs.
4. The longer-term outcome depends on initial speed and later dynamics; this is an exploratory scan, not a complete scattering phase diagram.
5. No claim about real matter or superluminal propagation follows. The equation, nonlinear potential, and characteristic speed were stipulated in advance.

## Reproducibility

- Script: `experiments/relational_fabric_collision_convergence.py`
- Data: `results/2026-10-09-relational-fabric-collision-convergence.json`

The numerical runs were executed in the current Python session. The committed script is a reproducible implementation; it was not executed directly from the GitHub checkout during this run.
