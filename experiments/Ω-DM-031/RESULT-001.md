# Ω-DM-031 — RESULT-001

**Status: FAIL-H1 / H0 RETAINED (exact-runner execution; ER measurement invalid)**

## Question
Can coordinate-free local relational rewiring, without a prescribed spatial dimension, dynamically select a stable effective dimension near d_eff = 3?

## Execution
The committed runner `experiments/Ω-DM-031/run_r31.py` was executed locally without modification.

Configuration:
- N = 500 nodes
- 3 initial ensembles: Erdos-Renyi, 6-regular, Watts-Strogatz small-world
- 6 seeds per ensemble
- 60 local rewiring steps
- measurement from graph shortest-path shell counts only
- 8 random sources per realization
- no coordinate labels or target dimension supplied to the measurement

## Numerical results

### 6-regular ensemble — valid measurements
Final mean effective shell exponents by seed:

- seed 0: 0.8311
- seed 1: -0.7534
- seed 2: 0.3091
- seed 3: 0.7633
- seed 4: 0.4956
- seed 5: 0.5354

Ensemble mean = 0.3635; sample SD = 0.5975.

This is not near d_eff = 3 and is not stable across seeds.

### Small-world ensemble — valid measurements
Final mean effective shell exponents by seed:

- seed 0: 0.3553
- seed 1: 0.1749
- seed 2: 0.7744
- seed 3: 0.9958
- seed 4: 0.8844
- seed 5: 1.0167

Ensemble mean = 0.7002; sample SD = 0.3655.

This is not near d_eff = 3.

### Erdos-Renyi ensemble — measurement failure
The exact runner produced insufficient shell-radius points for the hard-coded fit window in 5/6 seeds, yielding NaN. One seed produced p = -2.6158. Therefore the ER ensemble is **INVALID for dimensional inference under the current measurement window**, not evidence for any physical dimension.

This is a runner/measurement limitation and is recorded explicitly rather than silently discarded.

## Decision
The preregistered acceptance criterion requires stable d_eff near 3 across multiple seeds and at least two initial ensembles.

That criterion is not met. The two ensembles with valid measurements (6-regular and small-world) remain far from 3 and show substantial seed dependence.

**H1 is rejected for the tested rewiring rule. H0 is retained.**

The result does **not** establish that relational dynamics can never generate d_eff ≈ 3. It establishes that this particular local rule — common-neighbour support plus degree regularization — does not robustly select d_eff ≈ 3 from the tested initial ensembles.

## Scientific interpretation
The failure is informative. A local closure/degree-regularization rule alone is insufficient to generate a stable three-dimensional metric signature in these coordinate-free graph ensembles.

This strengthens the Ω-DM research constraint: if a 3D relational geometry is to emerge, an additional selection principle is required. The next experiment should therefore identify and preregister such a principle rather than simply changing parameters until p ≈ 3.

Candidate classes to test separately:
- local curvature/defect regulation;
- triangulation-like local closure without a supplied dimension;
- causal/locality constraints;
- an invariant local distortion or energy functional that selects finite-dimensional geometry.

Any candidate must be defined without inserting d = 3 into the objective or acceptance rule beyond the preregistered test target.

## Scope
No claim about physical spacetime, gravity, or dark matter is made.

## Reproducibility
Protocol: `experiments/Ω-DM-031/PROTOCOL.md`
Runner: `experiments/Ω-DM-031/run_r31.py`

The exact runner remains committed unchanged. The ER NaNs expose a measurement-window weakness that should be corrected in a future version rather than retroactively changing this result.
