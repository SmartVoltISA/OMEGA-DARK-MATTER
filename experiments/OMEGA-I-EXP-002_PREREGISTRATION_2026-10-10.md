# Ω-I-EXP-002 — Multi-dynamics and identity-continuity controls
Date: 2026-10-10
Status: preregistered before execution; synthetic computational experiment only.

## Question
Does a history-aware predictor outperform a current-observation-only predictor specifically when the data-generating process contains temporal dependence, and does this advantage disappear under an IID negative control?

## Conditions
1. AR1_CONTINUITY: latent x[t+1]=0.8*x[t]+epsilon, epsilon~N(0,1), observation y[t]=x[t]+eta, eta~N(0,1).
2. IID_NEGATIVE_CONTROL: latent x[t] is independent N(0,1) each step; same observation noise.
3. REGIME_SWITCH: latent AR coefficient is +0.8 for first half and -0.8 for second half; history model gets five observed lags but no explicit regime label.
4. REPLACEMENT_WITH_PERSISTENT_RULE: a scalar state follows AR(1) but each time step its carrier identity is replaced; the transition rule and scalar state are preserved. This deliberately tests functional/causal continuity versus carrier continuity, not personal identity.

## Design
- 120 independent trajectories per condition, seeds 20261010 + condition_index*10000 + trajectory_index.
- Each trajectory length 500; first 20 steps excluded from scoring.
- 70 trajectories train, 50 held-out test, fixed split by trajectory index.
- Models: CURRENT_ONLY OLS using y[t]; HISTORY_5 OLS using y[t-4:t]; SHUFFLED_HISTORY_5 negative control, where training feature rows are permuted relative to targets.
- Primary metric: pooled held-out RMSE, also report per-trajectory paired RMSE differences.
- 95% percentile bootstrap CI over held-out trajectories, 10,000 resamples, fixed RNG seed 20261010.
- No parameter tuning on held-out test data. No condition-specific thresholds.
- All conditions run with the same sample size and noise scale.

## Decision rules
- Evidence for history benefit in a condition: HISTORY_5 RMSE < CURRENT_ONLY and paired 95% CI for (CURRENT_ONLY RMSE - HISTORY_5 RMSE) excludes zero.
- Negative-control sanity check: IID condition should not show a reliable positive history benefit; shuffled history should not outperform correctly aligned history in AR1.
- REGIME_SWITCH is exploratory because the regime changes at a fixed midpoint and no regime indicator is supplied.
- REPLACEMENT_WITH_PERSISTENT_RULE can only establish predictive continuity under carrier replacement; it cannot establish personal identity or a universal law.

## Limitations
Synthetic data only. This does not test consciousness, subjective identity, fundamental physics, dark matter, or whether time emerges from memory. Results apply only to these data-generating processes and model choices.