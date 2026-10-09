# Ω-13 — Adaptive vs fixed vs shuffled vs absent couplings

**Date:** 2026-10-09  
**Status:** 80 runs executed (20 seeds × 4 modes).

## Preregistered comparison

Same graph-generation rule, state initialization procedure, noise amplitude, node update rule, and seed set per mode. The graph is a ring-lattice with random rewiring. Node state evolves as a noisy tanh of self-persistence plus the average weighted state of neighbors. Adaptive mode updates edge weights by a Hebbian-like correlation term and decay. Controls use fixed weights, shuffled weight-to-edge assignment each step, or no coupling.

Parameters: N=120; nominal degree k=8; rewiring probability 0.15; 500 steps; noise=0.08; adaptation eta=0.015; decay=0.005; seeds 20261020–20261039 per mode.

## Results (means over 20 runs)

| Mode | Edge sign agreement | Absolute sign polarization | Largest same-sign component / N | Sign persistence |
|---|---:|---:|---:|---:|
| Adaptive weights | 0.9452 | 0.6508 | 0.8254 | 1.0000 |
| Fixed weights | 0.9953 | 0.9567 | 0.9784 | 0.99995 |
| Shuffled weights | 0.9947 | 0.9593 | 0.9797 | 0.99977 |
| No coupling | 0.5004 | 0.0725 | 0.5324 | 0.7235 |

Adaptive edge weights became more heterogeneous (mean standard deviation 0.3373) than fixed weights (0.1437), but that heterogeneity did **not** produce stronger consensus or larger same-sign components. Fixed and shuffled coupling controls were more polarized than adaptive coupling. The no-coupling control remained close to 50% sign agreement.

## Interpretation / falsification

This result does not support the stronger claim that adaptive connections outperform simpler fixed couplings at creating persistent same-sign organization under this update rule. It does show that coupling itself changes node-state organization relative to the no-coupling control.

A caveat: the tanh dynamics saturate, and sign persistence approaches 1 in the coupled modes. That makes long-run consensus partly a consequence of the chosen update equation. These metrics measure sign alignment, not general structural emergence. The hypothesis must be narrowed or the dynamics redesigned before claiming relational self-organization.

## Reproducibility

Script: `experiments/relational_fabric_network_controls.py`  
Raw summary and all 80 runs: `results/2026-10-09-relational-fabric-network-controls.json`

The numerical results were generated in the current Python session. The script was committed and fetched back for content verification, but not executed directly from the GitHub checkout in this run.
