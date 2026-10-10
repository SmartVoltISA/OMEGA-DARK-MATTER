# Ω-DUAL-002B — execution report
Date: 2026-10-10
Status: **Executed locally; corrected matched-score attempt.**

## Design
300 independent trajectories per observation-noise setting; 200 steps per trajectory, first 50 burn-in and 150 scored; seed 20261010; 2,000 trajectory bootstrap resamples. State coordinates followed x(t)=0.75x(t−1)+Normal(0,0.25²). The binary target was sign(x1+x2). All conditions were scored with the same binary accuracy metric.

## Results
| Observation noise σ | Coupled specialists | Uncoupled specialists | Shuffled partner | Shared-target sensor | Paired accuracy gain, coupled − uncoupled (95% CI) |
|---:|---:|---:|---:|---:|---:|
| 0.1 | 91.81% | 73.96% | 66.98% | 91.90% | +17.84 pp [17.39, 18.30] |
| 0.5 | 70.66% | 64.08% | 60.31% | 70.71% | +6.58 pp [6.12, 7.07] |
| 1.0 | 61.40% | 58.04% | 55.90% | 61.55% | +3.36 pp [2.88, 3.85] |

At σ=0.5, message reliability q produced accuracies 60.87% (q=.25), 64.13% (q=.5), 67.17% (q=.75), and 70.53% (q=1). Better communication reliability was associated with better performance in this run.

## Decision under the registered local criterion
The paired 95% bootstrap interval for coupled-minus-uncoupled accuracy was above zero at all three noise levels. Thus the narrow benchmark criterion is met: in this constructed task, joint access to complementary observations improved prediction over the specified uncoupled local-majority baseline.

## Important counter-result
The shared-target-sensor control performed slightly better than the coupled-specialist condition at all three noise levels. Therefore the experiment does **not** show that specialization is superior to direct access to the target-related signal. It shows only that exchanging complementary observations helps relative to this particular no-message baseline.

## Validity and scope
- This run uses the corrected protocol Ω-DUAL-002B; the earlier Ω-DUAL-002 pilot remains archived as invalid and is not used for inference.
- This is a synthetic linear stochastic process and a binary sign-prediction task, not a model of brain hemispheres or a test of universal duality.
- The reliability sweep uses an independent batch of trajectories at σ=0.5.
- Execution was local Python/NumPy. GitHub Actions/CI was not run. The committed runner and archived results should be rerun together for independent reproduction.
- Result does not establish a law of nature, a claim about matter, or that all wholes require two parts.

## Decision
**NARROW SUPPORT for information exchange between complementary sensors in this benchmark; no support for universal duality.** The shared-target control is at least as good, so the next test should vary communication cost, sensor asymmetry, and time-varying relevance under equal information budgets.
