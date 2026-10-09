# Ω-16 — Corrected connectivity memory vs online adaptation

**Date:** 2026-10-09  
**Status:** Corrected protocol executed; 80 runs total (20 seeds × 4 modes).

## Question
Does the learned edge-weight pattern itself store useful memory, or does recovery require continued adaptation?

## Protocol
N=160, ring-like graph with sparse rewiring, 80 preconditioning steps, then an eight-node local sign inversion and 80 recovery steps. Same seed set (20261040–20261059) across modes. Crucially, both **adaptive_live** and **frozen_learned** train weights during preconditioning; frozen_learned then holds weights constant during recovery. **Fixed_original** never trains. **Shuffled_learned** trains weights, then randomly reassigns learned weight values to edges each recovery step.

Parameters: initial weights U(0.7,1.3); rewiring probability 0.03; state update tanh(0.45*self + 1.65*weighted-neighbor mean); eta=0.03; decay=0.01.

## Results

| Mode | Patch recovery | Global agreement with unperturbed copy | Original-domain retention | Learned/final weight SD |
|---|---:|---:|---:|---:|
| Adaptive live | 8.75% | 95.38% | 93.56% | 0.4167 |
| Frozen learned | 20.00% | 95.66% | 93.84% | 0.4167 |
| Fixed original | 16.88% | 93.69% | 88.97% | 0.1736 |
| Shuffled learned | 21.88% | 90.66% | 90.41% | 0.4167 |

## Paired comparisons

- **Frozen learned vs fixed original:** domain retention +4.875 percentage points; all 20 paired seeds favored frozen learned. Bootstrap 95% interval [+3.66, +6.16] points.
- **Frozen learned vs shuffled learned:** +3.44 points; 17/20 seeds favored frozen learned, 1 opposed, 2 tied. Bootstrap interval [+2.34, +4.59] points.
- **Adaptive live vs frozen learned:** −0.281 points on domain retention; 4 seeds favored live adaptation, 8 favored frozen, 8 tied. Bootstrap interval [−0.94, +0.31] points: no clear difference in global domain retention.
- **Adaptive live vs frozen learned:** local patch recovery was lower by 11.25 points; bootstrap interval [−21.88, −3.13] points.

## Interpretation

**Evidence in this toy model favors a role for the learned placement of weights:** freezing trained weights preserved the imposed domain labels better than never-trained weights and better than shuffling the trained values across edges. This is consistent with learned edge-specific structure carrying information relevant to the pattern.

Continuing adaptation did not improve global domain retention over frozen learned weights, and it repaired the locally inverted patch less often. In this model, online adaptation can destabilize the damaged patch rather than repair it.

This is still not proof that connections are the fundamental substance of matter. The initial four-domain pattern is imposed, the graph is preselected, and the learning rule is hand-designed. The result is limited to a toy network and needs independent models and stronger controls.

## Reproducibility
Script: `experiments/relational_fabric_connectivity_memory.py`  
Summary data and paired comparisons: `results/2026-10-09-relational-fabric-connectivity-memory.json`

The corrected equations were executed in the current Python session; the GitHub script was fetched back to verify the stored version, but was not executed directly from the GitHub checkout.
