# Ω-19 — Coupling-strength sweep (preregistration)

**Status:** preregistered before execution. No outcomes should be inspected until the full sweep is run.

## Question
Does the learned edge-to-weight assignment outperform fixed and permuted controls when coupling strength is varied, or is apparent organization primarily caused by the state-update rule?

## Hypothesis
H1: At one or more non-saturating coupling strengths, frozen learned weights produce greater edge sign agreement than fixed original weights and permuted learned weights.
H0: Frozen learned weights do not consistently outperform both controls across paired seeds and coupling strengths.

## Fixed protocol
- 40 paired seeds: 20261900–20261939.
- N=160; ring-derived graph with k=4 and rewiring probability 0.03.
- Initial state independently sampled from Normal(0, 0.15); no preset domains.
- Initial edge weights sampled Uniform(0.7, 1.3).
- Train adaptive weights for 80 steps using the preregistered Ω-18 Hebbian-like rule; normalize the learned weight mean to the original weight mean.
- Evaluation: 160 synchronous steps.
- Coupling strengths J ∈ {0.25, 0.60, 1.00, 1.65}; update x' = tanh(0.45x + J × weighted-neighbour-mean).
- Conditions at each J: frozen learned weights, a permutation of the learned weight multiset, and original fixed weights. Also report no-coupling baseline.
- The same seed, graph, initial state, and initial weights are paired across conditions.
- Primary metric: edge sign agreement. Secondary metrics: number of same-sign connected components, state RMS, plus-state fraction.
- Report means and sample SD over 40 seeds. Compute paired seed-level differences and 95% bootstrap intervals with 10,000 resamples; fixed bootstrap RNG seed 20261999.
- Do not choose a preferred J after looking at results without correcting for the four tested strengths. No post-hoc parameter changes.

## Decision rule
Support for H1 requires frozen learned weights to outperform **both** fixed and permuted controls in paired mean edge sign agreement, with both 95% bootstrap intervals excluding zero at a given J. Results at other strengths remain reported. Otherwise, record the hypothesis as unsupported by this sweep.

## Limits
This is a toy network and tests a specific algorithmic claim only. It cannot validate a physical substrate, dark matter, or superluminal propagation.
