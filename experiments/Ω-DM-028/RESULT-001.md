# Ω-DM-028 — RESULT-001

**Status: PASS-H1 (geometric condition isolated)**

## Actual local execution
Python deterministic runner executed on r=2..20 with conserved flux Q=1.

| s | expected p=2+s | measured p | error |
|---:|---:|---:|---:|
| -0.2 | 1.8 | 1.800000000000 | < 1e-15 |
| 0.0 | 2.0 | 2.000000000000 | < 1e-15 |
| +0.2 | 2.2 | 2.200000000000 | < 1e-15 |

## Result
The exponent is fixed by the asymptotic shell-measure scaling when radial flux is conserved:

Q = G(r) S(r), therefore if S(r) ~ r^(2+s), then G(r) ~ r^-(2+s).

Thus p=2 is not a consequence of conservation alone. It additionally requires an effective 3D shell measure with asymptotic radial scaling S(r)~r^2.

A fixed anisotropic deformation can alter the angular distribution and normalization without changing the radial exponent if it preserves S(r)~C*r^2. By contrast, scale-dependent radial density or geometry changes the exponent.

## Relation to Ω-DM-026/027
Ω-DM-026 showed that conservation can coexist with irregular nonlinear media where p is not 2.
Ω-DM-027 isolated conservation + r^2 shell scaling as sufficient for p=2.
Ω-DM-028 shows that the r^2 shell-scaling condition is also necessary within this tested radial-flux class: changing the shell exponent changes p one-for-one.

## Non-claim
This is a mathematical/model-level result. It does not derive physical spatial geometry, gravitational flux, or dark matter.

## Reproducibility
Runner: `experiments/Ω-DM-028/run_r28.py`
Protocol: `experiments/Ω-DM-028/PROTOCOL.md`
