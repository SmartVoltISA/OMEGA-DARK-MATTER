# Ω-19 — Coupling-strength sweep

**Preregistration:** [protocol](2026-10-09-relational-fabric-coupling-sweep-preregistration.md) committed before the run.
**Execution:** 40 paired seeds × 4 coupling strengths × 4 conditions = 640 condition evaluations, executed in a Python session. The committed script is reproducible; it was not run by GitHub Actions.

## Primary result: edge sign agreement

| Coupling J | Frozen learned | Permuted learned | Fixed original |
|---:|---:|---:|---:|
| 0.25 | 0.97055 ± 0.01920 | 0.97148 ± 0.01732 | 0.97078 ± 0.01816 |
| 0.60 | 0.97789 ± 0.01558 | 0.97805 ± 0.01530 | 0.97750 ± 0.01603 |
| 1.00 | 0.94680 ± 0.01868 | 0.95281 ± 0.01909 | 0.95164 ± 0.01830 |
| 1.65 | 0.92875 ± 0.02466 | 0.93422 ± 0.02454 | 0.93867 ± 0.01842 |

Values are mean ± sample SD over 40 paired seeds.

## Paired bootstrap (10,000 resamples)

Differences are frozen-learned minus control; positive would favour learned weights.

| J | Versus fixed: mean (95% CI) | Versus permuted: mean (95% CI) |
|---:|---:|---:|
| 0.25 | −0.00023 [−0.00195, 0.00156] | −0.00094 [−0.00383, 0.00180] |
| 0.60 | +0.00039 [−0.00148, 0.00250] | −0.00016 [−0.00203, 0.00133] |
| 1.00 | −0.00484 [−0.00820, −0.00188] | −0.00602 [−0.01031, −0.00211] |
| 1.65 | −0.00992 [−0.01414, −0.00594] | −0.00547 [−0.01023, −0.00094] |

## Decision
**Preregistered H1 is not supported.** Frozen learned weights did not outperform both controls at any tested coupling strength. At J=1.0 and 1.65, learned weights performed significantly worse on the primary metric than both controls.

At J=0.25, state RMS collapsed to approximately zero; sign agreement is then a fragile diagnostic because signs can persist numerically after the continuous state has decayed. At J=0.60, sign agreement was strong but learned edge assignment had no measurable advantage.

This strengthens the null result for this specific update rule: neighbour coupling itself is sufficient to produce sign alignment, while learned weights do not improve it. This toy-network experiment provides no evidence for a physical fabric, dark matter, or faster-than-light causal propagation.
