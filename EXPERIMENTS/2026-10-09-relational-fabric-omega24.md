# Ω-24 — Activity-matched continuous relational alignment

**Execution:** 40 paired seeds × 5 modes = 200 evaluations, actually computed in a Python analysis session. The preregistration was committed before the run. The script is committed for reproducibility; it was not run through GitHub Actions.

## Why this test
Ω-23's raw continuous margin was higher for frozen learned weights, but state activity was also higher. Ω-24 therefore rescales each post-evolution state **for scoring only** to the RMS of that seed's shared pre-perturbation state. The positive scaling preserves each state's sign pattern and equalizes amplitude across branches. The dynamics themselves are not altered by this scoring step.

Primary score: M_matched = mean(s_e × x_i × x_j) after RMS matching, over every edge. The no-coupling branch decays to numerical zero, so its matched score is undefined.

## Results

| Mode | Activity-matched margin | Raw margin | Raw activity | Raw RMS |
|---|---:|---:|---:|---:|
| Adaptive live | 0.054292 ± 0.020283 | 0.073738 | 0.081490 | 0.295121 |
| Frozen learned | 0.054859 ± 0.020592 | 0.059622 | 0.064510 | 0.263556 |
| Learned magnitudes permuted | 0.055220 ± 0.020783 | 0.047803 | 0.051063 | 0.235315 |
| Fixed original | 0.054864 ± 0.020758 | 0.050772 | 0.054679 | 0.243715 |
| No coupling | undefined | ~0 | ~0 | ~0 |

Values are mean ± sample SD for activity-matched margin; other columns are means across 40 seeds.

## Paired comparisons: frozen learned minus control

| Comparison | Activity-matched margin difference | 95% paired-bootstrap CI | Positive pairs |
|---|---:|---:|---:|
| vs permuted learned | −0.000361 | [−0.000487, −0.000247] | 6/40 |
| vs fixed original | −0.000005 | [−0.000086, +0.000071] | 19/40 |

10,000 paired bootstrap resamples. Raw margin still favours frozen learned weights because their activity is higher; after RMS matching, frozen learned weights are slightly worse than permuted weights and indistinguishable from the original fixed weights.

## Decision
**Ω-24 does not support a learned-magnitude advantage after matching state activity.** Against permuted weights, the activity-matched difference is small but consistently negative; against fixed original weights, the interval includes zero. This directly addresses the Ω-23 amplitude confound and weakens the claim that learned magnitude placement improves relational alignment in this toy model.

This is not a test of real dark matter, fundamental particles, or superluminal propagation. It only tests this specific network rule and these parameters.

## Reproduction
Run from the repository root:
`python experiments/relational_fabric_omega24_activity_matched.py > results/2026-10-09-relational-fabric-omega24.json`
The script emits all per-seed rows and bootstrap summaries.
