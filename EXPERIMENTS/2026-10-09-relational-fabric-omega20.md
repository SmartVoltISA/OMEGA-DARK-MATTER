# Ω-20 — Competing links and perturbation recovery

**Execution:** 40 paired seeds × 6 modes = 240 mode evaluations, executed in a Python session. The preregistration was committed before running. Summary values below are the observed run; the script and summary are recorded separately.

## Observed results

| Mode | Pre-run relation score | Post-perturbation relation retention | Continuous-state recovery |
|---|---:|---:|---:|
| Adaptive signed links | 0.8091 ± 0.0156 | 0.9221 ± 0.0402 | 0.7039 ± 0.2001 |
| Frozen learned signed links | 0.8120 ± 0.0158 | **0.9645 ± 0.0303** | **0.7853 ± 0.2239** |
| Permuted learned signed weights | 0.8113 ± 0.0139 | 0.9622 ± 0.0299 | 0.7702 ± 0.2263 |
| Fixed unsigned links | 0.9692 ± 0.0140 | 0.9722 ± 0.0177 | 0.7560 ± 0.1322 |
| Adaptive unsigned links | 0.9688 ± 0.0141 | 0.9796 ± 0.0096 | 0.7644 ± 0.1003 |
| No coupling | 0.5009 ± 0.0234 | 0.5041 ± 0.0234 | 0.0000 ± 0.0000 |

Mean ± sample SD over 40 seeds.

## Paired comparisons: adaptive signed minus control

| Control | Retention difference (95% bootstrap CI) | Recovery difference (95% bootstrap CI) |
|---|---:|---:|
| Frozen learned signed | −0.04242 [−0.05172, −0.03281] | −0.08143 [−0.09938, −0.06481] |
| Permuted learned signed | −0.04008 [−0.05078, −0.02930] | −0.06630 [−0.08611, −0.04677] |
| Fixed unsigned | −0.05008 [−0.06141, −0.03883] | −0.05209 [−0.12310, +0.01429] |
| Adaptive unsigned | −0.05750 [−0.06977, −0.04523] | −0.06054 [−0.12617, +0.00164] |

10,000 paired bootstrap resamples, seed 20262099.

## Decision
**The preregistered hypothesis is not supported.** Adaptive signed links were worse than frozen learned and permuted signed controls on both relation retention and continuous-state recovery. Unsigned controls showed higher relation retention. No-coupling dynamics collapsed toward zero, so its apparent post-perturbation relation score is not meaningful as organization; retention correctly stayed near chance.

## Interpretation and limitation
This run does not support the claim that ongoing adaptation or competing signed links create a more robust structure than simpler controls. The frozen learned condition performed better than live adaptation in this implementation. The model remains a toy network; it cannot establish a physical substrate, explain dark matter, or imply superluminal information transfer.

**Protocol caveat:** the evaluation conditions do not all start from an identical trained continuous state: the live-adaptive mode has its own 100-step trajectory, while frozen/permuted modes continue from the learned trajectory. Paired seeds control the random graph and initialization, but this state-history difference limits a strict causal interpretation of the live-versus-frozen comparison. A follow-up should freeze a common pre-perturbation state per seed, then branch all weight conditions from that exact state.
