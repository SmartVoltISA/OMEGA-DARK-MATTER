# Ω-18 — Spontaneous organization from random initial states

**Status:** 200 numerical evaluations executed in a Python session: 40 seeds × 5 modes. This report records the observed run. The committed script is a reproducible implementation; it was not executed by GitHub Actions.

## Question
Can adaptive relational weights generate a stable organized sign pattern from random initial states, without pre-seeded domains, and do they outperform fixed or shuffled controls?

## Protocol
- N=160 nodes; small-world-like ring graph, k=4, rewiring probability 0.03.
- Initial states are independent Gaussian noise N(0, 0.15); no domains are imposed.
- 40 paired seeds; same graph and initial state are reused across all modes.
- Hebbian-like training for 80 steps; evaluation for 160 steps.
- Modes: live adaptation, frozen learned weights, permuted learned weights, original fixed weights, and no coupling.
- Learned/live weights are mean-normalized to the original mean to avoid the previous mean-strength confound.
- Dynamics: synchronous update x' = tanh(0.45x + 1.65 weighted-neighbour-mean). This rule itself strongly favours sign alignment.

## Observed results

| Mode | Edge sign agreement | Sign components | State RMS |
|---|---:|---:|---:|
| Adaptive live | 0.92180 ± 0.01514 | 4.68 ± 1.54 | 0.96249 ± 0.00065 |
| Frozen learned | 0.92188 ± 0.01511 | 4.68 ± 1.54 | 0.96182 ± 0.00186 |
| Learned weights permuted | 0.92930 ± 0.01713 | 4.28 ± 1.43 | 0.92325 ± 0.01033 |
| Original fixed weights | **0.93688 ± 0.01581** | **3.75 ± 1.32** | 0.92239 ± 0.01140 |
| No coupling | 0.49469 ± 0.02607 | 37.50 ± 3.93 | approximately 0 |

Values are mean ± sample SD across 40 seeds. “Sign components” counts connected components of same-sign nodes in the graph; it is a graph diagnostic, not a universal measure of organization.

## Result
Coupling produces high local sign agreement compared with the no-coupling control. However, **the adaptive and learned weights do not outperform the original fixed weights** on the main structural diagnostics. Permuting learned weights also does not destroy the organized state. The result therefore fails to support the claim that learned relational memory is necessary for this organization.

## Important caveats
1. This is a toy network, not a physical model of matter.
2. The update rule explicitly favours neighbour agreement and saturation; organization is not emerging from “relations alone” without assumptions.
3. The run measures sign structure after a fixed number of steps. It does not establish robust metastability, universality, or predictive power about nature.
4. This test does not address superluminal propagation or information transfer.

## Decision
**Ω-18 is negative for the specific adaptive-weight advantage hypothesis.** Retain the result as a control, do not promote the model as validated. Next useful step: vary the update law and include anti-alignment/noise controls, with parameters preregistered before the next run.
