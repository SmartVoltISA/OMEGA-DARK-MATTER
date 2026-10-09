# Ω-17 — Topology-specific connectivity memory under matched controls

**Date:** 2026-10-09  
**Status:** 40 paired seeds × 4 conditions = 160 condition runs.

## Question

Does the location of learned weights on specific edges matter, beyond the overall weight distribution and mean?

## Protocol

For each seed, construct one graph and train its edge weights for 80 steps using the adaptive rule. Reuse the same trained node state and graph across all four conditions. Evaluate recovery after flipping 8 nodes in one domain, for 80 steps.

Conditions:
1. `frozen_learned_norm`: learned edge weights frozen and rescaled to the original weight mean.
2. `permuted_learned_norm`: exact learned weight multiset randomly reassigned to edges.
3. `degreebin_permuted_norm`: weights shuffled within endpoint-degree-pair bins where possible.
4. `fixed_original`: original random weights, same mean by construction.

All conditions share the same initial trained node state per seed. The learned and permuted conditions preserve the exact weight distribution and mean; only edge assignment differs. The degree-bin shuffle additionally preserves weight assignments within coarse endpoint-degree classes as far as bin sizes allow.

## Main result

| Condition | Domain-label retention | Global agreement | Local patch recovery |
|---|---:|---:|---:|
| Frozen learned weights, normalized | 94.09% | 95.84% | 24.38% |
| Random permutation of learned weights | 89.92% | 94.14% | 17.81% |
| Permutation within degree bins | 90.30% | 94.36% | 17.50% |
| Original random fixed weights | 89.91% | 94.48% | 19.69% |

Paired comparisons for domain retention:
- Learned vs fully permuted: +4.172 percentage points; positive in 39/40 seeds; bootstrap 95% interval +3.375 to +5.016 points.
- Learned vs degree-bin permutation: +3.797 points; positive in 36/40 seeds; bootstrap interval +2.797 to +4.875 points.
- Learned vs original fixed weights: +4.188 points; positive in 37/40 seeds; bootstrap interval +3.266 to +5.078 points.

Local patch recovery is noisier. Learned minus permuted is +6.56 points, but the bootstrap interval crosses zero (-1.56 to +15.94 points), so this measure does not provide clear evidence of a local-recovery advantage.

## Interpretation

This is stronger evidence that **where** learned weights sit on this graph matters for retaining the pre-specified domain pattern, beyond the weight mean and multiset alone. The degree-bin control also weakens the explanation that the effect is only a coarse degree correlation.

Limits:
- The four domains were initialized by hand; they did not emerge spontaneously.
- The graph and update rule are toy choices.
- The score is domain-label retention, not a universal measure of organization.
- The bootstrap interval is descriptive, not a substitute for a preregistered confirmatory replication.
- No claim about physical matter or superluminal signalling is tested.

## Reproducibility

Script: `experiments/relational_fabric_connectivity_memory_controls.py`  
Raw results: `results/2026-10-09-relational-fabric-connectivity-memory-controls.json`

Numerical results were generated in the current Python session using equivalent functions. The saved script was fetched back from GitHub to verify content, but was not executed directly from the GitHub checkout in this run.
