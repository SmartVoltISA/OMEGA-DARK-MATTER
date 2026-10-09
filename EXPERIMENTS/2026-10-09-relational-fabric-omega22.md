# Ω-22 — Amplitude-gated signed-relation stability

**Execution:** 40 paired seeds × 5 modes = 200 evaluations, actually computed in a Python analysis session. Protocol was committed before execution. The script is saved for reproducibility; it was not run from GitHub Actions.

## Why this test
Earlier sign-based scores could become misleading when node amplitudes approached zero. Ω-22 scores an edge only when both endpoint magnitudes satisfy |x| ≥ 0.20. It also reports the fraction of edges that meet this threshold (coverage).

## Results

| Mode | Gated relation score | Scoreable-edge coverage | State recovery |
|---|---:|---:|---:|
| Adaptive live | 0.9587 ± 0.0186 | 36.34% ± 12.73% | 0.7078 ± 0.1633 |
| Frozen learned | 0.9694 ± 0.0161 | 31.82% ± 11.55% | 0.7539 ± 0.1743 |
| Learned weights permuted | 0.9790 ± 0.0147 | 27.78% ± 9.76% | 0.7494 ± 0.1492 |
| Fixed original | 0.9769 ± 0.0141 | 29.27% ± 9.66% | 0.7496 ± 0.1571 |
| No coupling | not scoreable | 0% | 0.5000* |

Values are mean ± sample SD over 40 seeds. *No-coupling state decays to nearly zero; its recovery score and sign-based measures are not interpretable as organized structure.

## Paired comparisons: frozen learned minus control

| Metric | Versus permuted learned | Versus fixed original |
|---|---:|---:|
| Gated relation score | −0.00969 [−0.01350, −0.00595] | −0.00758 [−0.01264, −0.00281] |
| Relation retention | +0.00003 [0.00000, 0.00010] | +0.00002 [0.00000, 0.00005] |
| State recovery | +0.00455 [−0.00689, +0.01579] | +0.00429 [−0.00665, +0.01414] |

95% paired bootstrap CIs, 10,000 resamples.

## Decision
The preregistered decision rule required at least 50% scoreable-edge coverage. **That requirement failed**: mean coverage was below 37% in all coupled modes, and only 2.5–12.5% of runs reached 50% coverage. The overall result is therefore **inconclusive by the preregistered rule**.

Within the available scoreable edges, frozen learned weights did not outperform either control; both paired differences were negative with intervals excluding zero. State recovery did not significantly differ from controls. This is not positive evidence for the proposed mechanism.

## Next step
Do not tune the amplitude threshold after seeing these results. A new preregistration should use a more informative state/dynamics measure (for example continuous signed edge margin and its change from pre-perturbation), with an explicit minimum coverage criterion and null controls. Treat this run as a methodological warning, not as a physical result.
