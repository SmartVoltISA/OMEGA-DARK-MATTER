# Ω-23 — Continuous signed-relation margin

**Execution:** 40 paired seeds × 5 modes = 200 evaluations, actually computed in a Python analysis session. The preregistration was committed before the run. The experiment script is committed for reproduction; it was not run through GitHub Actions.

## Why this test
Ω-22's sign score used an amplitude threshold and left many edges unscored. Ω-23 instead uses every edge and scores continuous signed products. For edge sign s and endpoint states x_i, x_j:

- **Primary margin:** M = mean(s × x_i × x_j) over all edges.
- **Activity:** A = mean(|x_i × x_j|), to distinguish stronger state amplitude from better alignment.
- **Normalized alignment:** Q = M / A (with a tiny numerical stabilizer); secondary, always interpreted with A.

Edge signs were fixed across conditions; only edge-magnitude placement/adaptation differed. All branches started from the same trained state and received the same perturbation.

## Results

| Mode | Continuous margin M | Activity A | Normalized alignment Q | State recovery |
|---|---:|---:|---:|---:|
| Adaptive live | 0.07989 ± 0.02540 | 0.08895 ± 0.02845 | 0.89891 ± 0.01728 | 0.68299 ± 0.20178 |
| Frozen learned | 0.06375 ± 0.02095 | 0.06930 ± 0.02269 | 0.91956 ± 0.01487 | 0.73519 ± 0.21823 |
| Learned magnitudes permuted | 0.05254 ± 0.01718 | 0.05637 ± 0.01816 | 0.93069 ± 0.01355 | 0.71103 ± 0.19376 |
| Fixed original | 0.05459 ± 0.01723 | 0.05893 ± 0.01834 | 0.92497 ± 0.01565 | 0.71400 ± 0.20358 |
| No coupling | effectively 0 | effectively 0 | not interpretable near zero | 0.50000* |

Values are mean ± sample SD across 40 paired seeds. *No-coupling state decays to numerical zero; its alignment is not evidence of organized structure.

## Paired comparisons: frozen learned minus control

| Metric | Versus permuted learned | Versus fixed original |
|---|---:|---:|
| Primary margin M | +0.01120 [0.00940, 0.01299] | +0.00916 [0.00726, 0.01096] |
| Activity A | +0.01292 [0.01080, 0.01512] | +0.01036 [0.00818, 0.01239] |
| Normalized alignment Q | −0.01113 [−0.01376, −0.00841] | −0.00541 [−0.00701, −0.00374] |
| State recovery | +0.02416 [0.00770, 0.04078] | +0.02119 [0.00595, 0.03805] |

95% paired-bootstrap percentile intervals, 10,000 resamples. The raw margin is higher for frozen learned weights in 40/40 pairs against the permuted control and 38/40 against fixed original. However, activity also rises, and the normalized alignment Q is **lower** against both controls.

## Decision
The raw-margin criterion is positive, but the preregistered safeguard says the benefit must not be explained by state activity alone. Since A increases while Q decreases, Ω-23 does **not** establish that learned connectivity improves relational alignment independently of amplitude. The result is mixed; no general structural advantage is established.

This is a toy-network experiment. It provides no evidence about real dark matter, fundamental particles, or superluminal propagation.

## Reproduction
Run the committed script locally with NumPy:
`python experiments/relational_fabric_omega23_continuous_margin.py > results/2026-10-09-relational-fabric-omega23.json`
The script writes all per-seed rows along with summary and bootstrap comparisons. The committed summary artifact records aggregate statistics and paired comparisons; rerun the script to regenerate the full per-seed JSON.
