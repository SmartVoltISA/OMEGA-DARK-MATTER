# Ω-15 — Recovery of multiple domains after a local perturbation

**Date:** 2026-10-09  
**Status:** 60 runs executed; 20 seeds per mode.

## Question
After a network develops four alternating domains, can it recover from a local inversion of eight node states? Does adaptive coupling improve recovery or preserve the original domain pattern compared with fixed or shuffled weights?

## Method
- N=160 nodes; ring lattice with k=4 and rewiring probability 0.03.
- Four alternating initial sign domains.
- 80 pre-perturbation steps, invert eight consecutive states, then evolve baseline and perturbed copies for 80 further steps.
- Modes: adaptive Hebbian-like weights, fixed weights, and weights reassigned randomly to edges each step.
- 20 seeds per mode: 20261030–20261049.

## Results

| Metric | Adaptive | Fixed | Shuffled |
|---|---:|---:|---:|
| Patch recovery | 8.75% | 18.13% | 20.63% |
| Global baseline agreement | 95.31% | 94.75% | 92.97% |
| Original domain-label retention | 93.69% | 89.50% | 89.88% |
| Baseline boundary count | 4.00 | 4.00 | 4.00 |
| Perturbed boundary count | 6.00 | 5.90 | 5.60 |

Adaptive weights developed greater heterogeneity (mean final weight standard deviation 0.409) than fixed weights (0.172).

Paired by seed, adaptive domain-label retention exceeded fixed-weight retention by an average of 4.19 percentage points; bootstrap 95% interval 3.13–5.22 percentage points. Adaptive retention was higher in 19 of 20 seed pairs. This is exploratory, not a preregistered confirmatory test.

## Interpretation
The result is mixed:
- Adaptive coupling preserved original domain labels better than fixed coupling in this setup.
- Recovery inside the directly inverted patch was worse under adaptive coupling (8.75%) than under fixed (18.13%) or shuffled weights (20.63%). Adaptive coupling did not restore the local perturbation; it more strongly preserved the broad pattern while leaving the damaged patch altered.
- Global agreement is high partly because most nodes were never perturbed; it is not a local recovery measure.
- The adaptive rule, initial four-domain pattern, graph topology, and update function are built into the model. This does not establish that matter emerges from relations.

## Verdict
**Mixed, model-specific result; no general confirmation of Ω.** Adaptive weights improved domain-label retention by about 4.2 percentage points versus fixed weights but did not improve local patch recovery.

## Reproducibility
Script: `experiments/relational_fabric_local_recovery.py`  
Summary data: `results/2026-10-09-relational-fabric-local-recovery.json`

The values were generated in the current Python session. The script was saved and fetched back for verification, but not executed directly from the GitHub checkout during this run.
