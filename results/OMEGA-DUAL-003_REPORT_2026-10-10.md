# Ω-DUAL-003 — execution report
Date: 2026-10-10
Status: **Executed locally; valid for the registered synthetic benchmark as implemented.**

## Design
300 independent trajectories per noise level; 240 time steps each, first 40 burn-in and 200 scored; seed 20261010; 2,000 trajectory-bootstrap resamples. Hidden state followed xⱼ(t)=0.82xⱼ(t−1)+Normal(0,0.3²). The target was sign(w₁x₁+w₂x₂), with weights changing from (0.8,0.2) to (0.2,0.8) at t=120. All conditions used the same binary accuracy metric.

## Results
| Observation noise σ | Specialized sensors | Shared aggregate sensors | Misallocated specialists | Single shared sensor + noise | Paired difference: specialized − shared (95% CI) |
|---:|---:|---:|---:|---:|---:|
| 0.2 | 88.36% | **89.93%** | 65.02% | 62.57% | −1.57 pp [−1.88, −1.28] |
| 0.6 | 72.71% | **75.45%** | 59.58% | 61.34% | −2.74 pp [−3.19, −2.31] |
| 1.0 | 65.41% | **67.60%** | 57.48% | 59.49% | −2.19 pp [−2.71, −1.68] |

Shared aggregate sensing outperformed specialized sensing at every tested noise level; the paired bootstrap intervals for specialized minus shared were entirely below zero. The registered criterion for specialization superiority was not met.

## Secondary findings
Misallocated specialists performed substantially worse than correctly weighted specialists, consistent with the target weights being task-relevant. Shuffling the partner stream also reduced performance. These comparisons are diagnostic and should not be overinterpreted because the shuffled stream breaks temporal and cross-component alignment.

## Decision
**Negative result for the tested claim that specialization is superior to shared-aggregate sensing under equal sensor-channel count.** A direct noisy measurement of the aggregate target is easier for this task than reconstructing it from two noisy component measurements. This is an informative control result, not a failure of the experiment.

## Scope and reproducibility
This is a synthetic model, not a brain model and not evidence for a universal principle of duality. Execution was local Python/NumPy; GitHub Actions/CI was not run. The committed runner was aligned to the executed RNG sequence before archiving the results. Independent reproduction still requires rerunning the committed script and comparing the output.
