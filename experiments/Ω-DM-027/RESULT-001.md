# Ω-DM-027 — RESULT-001

**Status: PASS-H1 (structural minimality audit)**

## Actual execution
The audit runner was executed locally with deterministic numerical arrays. For conserved radial flux Q(r)=1 and isotropic shell measure S_d(r) proportional to r^(d-1), the measured response exponent is:

| dimension d | measured p | target d-1 |
|---:|---:|---:|
| 1 | 0.000000 | 0 |
| 2 | 1.000000 | 1 |
| 3 | 2.000000 | 2 |

The fitted values are exact to floating-point precision for this controlled identity.

## Conservation control
A leaky control with Q(r)=exp(-0.08 r) gives a fitted effective exponent of approximately 2.583 over r=1..20 rather than 2. The deviation is expected because the flux is no longer conserved; the response contains an additional exponential factor.

## Interpretation
This establishes the mathematical minimality statement tested here:

**constant conserved radial flux + isotropic d-dimensional shell measure S(r) proportional to r^(d-1) => radial flux density G(r) proportional to r^-(d-1).**

Therefore in 3D, p=2 follows from conservation plus isotropic shell geometry. The constitutive law is not what fixes the exponent in this identity.

The result also explains Ω-DM-026: antisymmetric local exchange can conserve total flux while irregular geometry and nonlinear constitutive response prevent the environmental field from behaving as an isotropic radial flux density with shell measure proportional to r².

## Relation to previous experiments
- Ω-DM-021/022: demonstrate p≈2 in specific conservative local models.
- Ω-DM-026: demonstrates that antisymmetry/conservation alone is insufficient on irregular nonlinear media.
- Ω-DM-027: isolates the geometric conservation mechanism that fixes the exponent once isotropic shell scaling is available.

## Non-claim
This is a model-level mathematical result, not a derivation of physical gravity or dark matter. A physical theory would still need to derive why the relevant physical relational flux is conserved, why an approximately isotropic 3D geometry applies, and how the relational observable maps quantitatively to measured gravitational phenomena.

## Reproducibility
Runner: `experiments/Ω-DM-027/run_r27.py`
Protocol: `experiments/Ω-DM-027/PROTOCOL.md`
