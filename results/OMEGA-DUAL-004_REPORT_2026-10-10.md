# Ω-DUAL-004 — execution report
Date: 2026-10-10
Status: **Executed locally; synthetic benchmark.**

## Setup
300 independent trajectories, 300 steps each, first 50 burn-in, observation noise σ=0.5, seed 20261010. State dynamics xⱼ(t)=0.85xⱼ(t−1)+Normal(0,0.35²). Relevance weights alternate every 75 steps between (0.9,0.1) and (0.1,0.9). The adaptive system compares two candidate weightings on the most recent 15 steps and uses the better-performing weighting for subsequent steps. Bootstrap intervals resample trajectories 2,000 times.

## Main results
| Condition | Accuracy | 95% trajectory-bootstrap interval |
|---|---:|---:|
| Oracle specialists (diagnostic upper bound) | 79.78% | 79.46–80.10% |
| Fixed specialists | 65.29% | 64.81–65.80% |
| Adaptive specialists | 73.95% | 73.54–74.34% |
| Shared aggregate sensors | **83.39%** | 83.08–83.70% |
| No communication baseline | 66.48% | 66.08–66.86% |

Adaptive minus fixed accuracy was +8.65 percentage points, 95% CI [+8.15, +9.13] pp. Under this simulation, adaptation substantially improves on a fixed weighting rule.

## Regime-specific diagnostic
| Scored regime segment | Adaptive | Fixed |
|---|---:|---:|
| Segment 1 | 74.40% | 61.89% |
| Segment 2 | 74.81% | 79.92% |
| Segment 3 | 72.47% | 55.20% |

The adaptive policy's short history means it can lag when a regime changes. It does not win every segment; fixed weighting does better in segment 2. This is a useful limitation rather than something to hide.

## Communication cost
A predeclared accuracy-equivalent cost of 0.02 per message per scored step gives adaptive net score 71.95%, still above fixed accuracy 65.29%. This simple cost convention is a modeling assumption, not a measured real-world cost.

## Decision
**Narrow support for adaptation over fixed specialization in this particular changing-regime simulation.** The registered broad decision rule requiring net advantage in at least two regimes is not met: net score is a single aggregate metric, and the adaptive system does not beat fixed specialists in every regime. More importantly, shared aggregate sensing performs best overall. The result supports adaptation as a useful response to changing signal relevance, not the universal superiority of duality or specialization.

## Validity and reproducibility
This is a synthetic model, not a brain or physical model. Execution status is local Python/NumPy; GitHub Actions/CI was not run. The committed script should be rerun to independently verify the archived values. No claims are made about matter, consciousness, or a universal law.
