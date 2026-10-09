# Preregistration — Ω-I-EXP-001
**Date:** 2026-10-10  
**Hypothesis:** Historical observations improve prediction of a system's next state beyond its current noisy observation when the underlying process has temporal continuity. This is a narrow operational test of the Ω-I idea, not a test of personal identity or a universal law.

## Question
Does retaining a short causal history help predict the next state of a changing system, compared with using only its current observation?

## Data-generating model
Generate independent scalar latent trajectories with AR(1) dynamics: x[t+1] = rho*x[t] + epsilon, where rho=0.8 and epsilon is standard normal. Observations are y[t] = x[t] + eta, where eta is independent Gaussian noise with standard deviation 1.0. Initial state is drawn from the stationary distribution. This is an intentionally simple synthetic benchmark with known temporal continuity and observation noise.

## Conditions
1. **CURRENT_ONLY:** linear regression predicting y[t+1] from y[t].
2. **CAUSAL_HISTORY_5:** same linear regression class predicting y[t+1] from y[t], y[t-1], ..., y[t-4].
3. **SHUFFLED_HISTORY_5:** history feature rows are shuffled across training examples, disrupting causal alignment; evaluate on correctly aligned held-out sequences. This is a negative control for the benefit of correctly aligned history.

All models use ordinary least squares with an intercept. Train and test sequences are disjoint. No test sequence is used for fitting. The same seeds and generated trajectories are used for paired comparison.

## Fixed parameters
- Random seeds: 1000–1099 (100 independent sequences).
- Sequence length: 400 observations; first 20 time points excluded from scoring to reduce initialization effects.
- Train/test split: 70/30 by independent trajectory seeds; 70 training sequences and 30 held-out test sequences.
- rho = 0.8; observation noise SD = 1.0; process noise SD = 1.0.
- Primary metric: held-out RMSE for predicting the next observed state.
- Secondary metric: paired per-test-trajectory RMSE difference (CURRENT_ONLY minus CAUSAL_HISTORY_5).
- Uncertainty: bootstrap 95% percentile interval over held-out test trajectories, fixed bootstrap seed 20261010, 10,000 resamples.
- Significance threshold: descriptive 95% interval for the paired difference excludes zero. This is a single preregistered primary comparison; no multiple-test correction is needed for it.

## Validity and interpretation
- The positive-control process is deliberately temporally correlated. Better performance of history here only shows that aligned history can help in this specified noisy autoregressive system.
- The shuffled-history condition is a negative control; it should not systematically outperform correctly aligned history.
- This does **not** establish that time emerges from change, that the universe is a spiral, that DNA is a universal template, or that a computational model has consciousness.
- It does **not** directly settle metaphysical identity. It tests one operational claim: historical continuity can carry predictive information not present in a single noisy observation.
- If history does not outperform current-only, or the negative control performs similarly, report that result without changing the preregistered model or thresholds.
- Preserve raw per-trajectory results and script. Do not overwrite earlier Ω experiments.
