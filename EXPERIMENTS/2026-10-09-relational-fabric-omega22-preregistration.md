# Ω-22 — Amplitude-gated signed-relation stability

**Status:** preregistered before execution.

## Question
Does learned signed edge structure improve perturbation recovery when the primary relation metric excludes near-zero states?

## Primary metric
For each edge, the preferred relation is positive when a positive edge joins equal-sign states or a negative edge joins opposite-sign states. An edge is scoreable only when both endpoint amplitudes exceed ε=0.20. Primary score = fraction of scoreable edges satisfying the preferred relation. Also report scoreable-edge coverage; a high score with low coverage is not treated as success.

## Protocol
- 40 paired seeds, 20262200–20262239; N=160; ring-derived graph with k=4, rewiring probability 0.03.
- Random Gaussian initial state N(0,0.15); edge magnitudes Uniform(0.7,1.3); edge signs assigned independently with probability 0.5.
- Train one common network for 100 steps. All conditions branch from the same trained state and receive the same 10% node sign-flip perturbation.
- Conditions: frozen learned signed weights; same learned magnitudes permuted across edges (edge signs remain fixed); original fixed signed weights; live adaptation from the same trained weights; no coupling.
- Dynamics: x' = tanh(0.35x + 0.85 × signed weighted-neighbour field), normalized by total incident absolute weight.
- Live adaptation uses the same preregistered update rule as Ω-21, then magnitude mean-normalization.
- Evaluate 100 post-perturbation steps.
- Primary outcome: amplitude-gated signed-relation score at ε=0.20. Report coverage. Secondary outcomes: state recovery, RMS amplitude, and relation retention only on edges scoreable both before and after perturbation.
- 40 paired seeds; mean ± sample SD; paired bootstrap 95% CIs with 10,000 resamples, bootstrap seed 20262299.
- No parameter tuning after observing outcomes.

## Decision rule
Support for learned-edge advantage requires frozen learned weights to outperform both permuted learned and fixed original weights on the primary metric, with paired 95% CIs excluding zero, while scoreable-edge coverage is at least 50% in both compared modes. Report live adaptation separately; do not conflate it with frozen memory.

## Limits
This tests a toy network only and cannot validate a physical substrate, dark matter, or superluminal propagation.
