#!/usr/bin/env python3
"""Reproducible Ω-I-EXP-001 synthetic test; Python 3 + NumPy only."""
import json, math
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent
SEEDS = list(range(1000, 1100))
RHO, PROCESS_SD, OBS_SD, T, BURN, TRAIN_N = 0.8, 1.0, 1.0, 400, 20, 70
BOOTSTRAPS, BOOT_SEED = 10_000, 20261010

def generate():
    rows = []
    for seed in SEEDS:
        rng = np.random.default_rng(seed)
        x = np.empty(T)
        x[0] = rng.normal(0, PROCESS_SD / math.sqrt(1 - RHO**2))
        for t in range(T - 1):
            x[t+1] = RHO*x[t] + rng.normal(0, PROCESS_SD)
        rows.append(x + rng.normal(0, OBS_SD, T))
    return np.asarray(rows)

def fit(X, y):
    return np.linalg.lstsq(np.column_stack([np.ones(len(X)), X]), y, rcond=None)[0]

def predict(X, beta):
    return np.column_stack([np.ones(len(X)), X]) @ beta

def main():
    data = generate()
    def xy(ids, lags):
        xs, ys = [], []
        for i in ids:
            y = data[i]
            for t in range(max(lags, BURN), T-1):
                xs.append([y[t-k] for k in range(lags)])
                ys.append(y[t+1])
        return np.asarray(xs), np.asarray(ys)
    X1tr, ytr = xy(range(TRAIN_N), 1)
    X5tr, y5tr = xy(range(TRAIN_N), 5)
    b1, b5 = fit(X1tr, ytr), fit(X5tr, y5tr)
    perm = np.random.default_rng(99123).permutation(len(X5tr))
    bsh = fit(X5tr[perm], y5tr)
    per = {}
    for i in range(TRAIN_N, len(SEEDS)):
        y = data[i]
        ts = range(max(5, BURN), T-1)
        X1 = np.asarray([[y[t]] for t in ts])
        X5 = np.asarray([[y[t-k] for k in range(5)] for t in ts])
        target = np.asarray([y[t+1] for t in ts])
        per[str(SEEDS[i])] = {
            "current_only_rmse": float(np.sqrt(np.mean((predict(X1,b1)-target)**2))),
            "causal_history_5_rmse": float(np.sqrt(np.mean((predict(X5,b5)-target)**2))),
            "shuffled_history_5_rmse": float(np.sqrt(np.mean((predict(X5,bsh)-target)**2)))}
    keys = ["current_only_rmse","causal_history_5_rmse","shuffled_history_5_rmse"]
    means = {k: float(np.mean([v[k] for v in per.values()])) for k in keys}
    sds = {k: float(np.std([v[k] for v in per.values()], ddof=1)) for k in keys}
    d = np.asarray([v["current_only_rmse"]-v["causal_history_5_rmse"] for v in per.values()])
    rng = np.random.default_rng(BOOT_SEED)
    boot = d[rng.integers(0,len(d),(BOOTSTRAPS,len(d)))].mean(axis=1)
    result = {
      "experiment_id":"OMEGA-I-EXP-001","status":"completed",
      "execution":"standalone Python script using NumPy; fixed seeds",
      "n_trajectories":100,"train_trajectories":70,"heldout_test_trajectories":30,
      "sequence_length":T,"burn_in_excluded":BURN,
      "parameters":{"rho":RHO,"process_noise_sd":PROCESS_SD,"observation_noise_sd":OBS_SD,"history_lags":5},
      "metrics":{"mean_heldout_rmse":means,"sd_across_test_trajectories":sds,
        "paired_rmse_improvement_current_minus_history":float(d.mean()),
        "paired_rmse_improvement_95pct_bootstrap_ci":[float(np.quantile(boot,.025)),float(np.quantile(boot,.975))],
        "shuffled_minus_causal_history_mean_rmse":float(means["shuffled_history_5_rmse"]-means["causal_history_5_rmse"])},
      "model_coefficients":{"current_only":b1.tolist(),"causal_history_5":b5.tolist(),"shuffled_history_5":bsh.tolist()},
      "per_test_trajectory":per,
      "interpretation":"Synthetic predictive benchmark only; not a test of consciousness, fundamental physics, or personal identity."}
    path = OUT / "OMEGA-I-EXP-001_RESULTS_2026-10-10.json"
    path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"experiment_id":result["experiment_id"],"metrics":result["metrics"]},indent=2))

if __name__ == "__main__":
    main()
