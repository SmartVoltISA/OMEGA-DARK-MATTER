# Ω-I-EXP-004 — Trajectory-first causal-history validation
Date: 2026-10-10
Status: preregistered before execution.

## Question
Does lagged history improve held-out next-observation prediction when trajectories are generated independently of the predictor and contain temporal structure, and does the effect disappear for IID trajectories?

## Data generation
- 200 independent trajectories per condition, length 600.
- Conditions: AR1 (phi=0.8); IID Gaussian; regime switch (phi=0.8 then -0.8 at midpoint); damped oscillator (x[t+1]=1.4*x[t]-0.6*x[t-1]+process noise, observation noise added).
- Each trajectory is generated entirely from the condition equation and seeded RNG before any model fitting. Labels do not exist in this prediction task.
- Fixed seeds: 20261010 + condition index*10000 + trajectory index.
- First 20 steps excluded. First 140 trajectories train; last 60 are held out.

## Models and metrics
- CURRENT_ONLY: OLS predicting y[t+1] from y[t].
- HISTORY_5: OLS predicting y[t+1] from y[t] through y[t-4].
- SHUFFLED_TARGET negative control: same history features with training targets permuted.
- Primary metric: pooled held-out RMSE. Secondary: per-trajectory paired RMSE improvement and 95% percentile bootstrap CI (10,000 resamples).
- IID control must show no robust history advantage. No test-set tuning.

## Validity checks
- Verify finite values, exact split sizes, deterministic rerun from same seeds.
- Generate trajectories independently of model labels/features.
- No classification target and no feature sampled conditionally on outcome.
- This is a predictive benchmark, not a test of metaphysical identity.

## Limits
Positive results can establish only that past observations help predict future observations under specified dynamics. They do not prove that history defines identity, consciousness, or a law of physics.
