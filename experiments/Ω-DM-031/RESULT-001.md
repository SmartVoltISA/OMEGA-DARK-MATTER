# Ω-DM-031 — RESULT-001

**Status: INCONCLUSIVE / H0 RETAINED**

## Execution status
The protocol and reproducible runner have been committed. The current environment did not provide a completed numerical execution of `run_r31.py`; therefore no numerical PASS is claimed.

The runner implements three coordinate-free initial ensembles (Erdos-Renyi, 6-regular, and small-world), a bounded local rewiring rule based on common-neighbour support and degree regularization, followed by blind graph-distance shell measurement.

## Scientific status
Because the numerical run was not completed, Ω-DM-031 remains HOLD/INCONCLUSIVE rather than PASS. This is intentional: the project rule is PROPOSED != EXECUTED and RESULT != CONCLUSION.

The experiment is designed to answer whether a local relational dynamics can itself select d_eff near 3. If executed successfully, acceptance requires stable d_eff near 3 across multiple seeds and at least two initial ensembles.

## Scope
No physical spacetime, gravity, or dark matter claim is made.

## Reproducibility
Protocol: `experiments/Ω-DM-031/PROTOCOL.md`
Runner: `experiments/Ω-DM-031/run_r31.py`
