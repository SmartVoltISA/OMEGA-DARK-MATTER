#!/usr/bin/env python3
"""Reproduce Ω-I-EXP-004. Requires Python, numpy, scikit-learn."""
import json
import numpy as np
from sklearn.linear_model import LinearRegression

CONDITIONS = ["AR1", "IID", "REGIME_SWITCH", "DAMPED_OSCILLATOR"]
N, T = 200, 600

def generate(condition, seed):
    rng = np.random.default_rng(seed)
    x = np.zeros(T)
    x[0], x[1] = rng.normal(), rng.normal()
    for t in range(1, T-1):
        if condition == "IID":
            x[t+1] = rng.normal()
        elif condition == "AR1":
            x[t+1] = .8*x[t] + rng.normal()
        elif condition == "REGIME_SWITCH":
            phi = .8 if t < T//2 else -.8
            x[t+1] = phi*x[t] + rng.normal()
        else:
            x[t+1] = 1.4*x[t] - .6*x[t-1] + rng.normal(scale=.5)
    return x + rng.normal(size=T)

def design(y):
    X, target = [], []
    for t in range(4, T-1):
        X.append([y[t], y[t-1], y[t-2], y[t-3], y[t-4]])
        target.append(y[t+1])
    X, target = np.asarray(X), np.asarray(target)
    return X[:, [0]], X, target

def main():
    output = {}
    for ci, cond in enumerate(CONDITIONS):
        ds = [design(generate(cond, 20261010+ci*10000+i)) for i in range(N)]
        train, test = ds[:140], ds[140:]
        xc = np.concatenate([d[0] for d in train])
        xh = np.concatenate([d[1] for d in train])
        y = np.concatenate([d[2] for d in train])
        mc = LinearRegression().fit(xc, y)
        mh = LinearRegression().fit(xh, y)
        perm = np.random.default_rng(20261010+ci).permutation(len(y))
        ms = LinearRegression().fit(xh, y[perm])
        errors = {"current": [], "history": [], "shuffled_target": []}
        paired = []
        for a, b, target in test:
            predictions = {"current": mc.predict(a), "history": mh.predict(b),
                           "shuffled_target": ms.predict(b)}
            local = {}
            for key, pred in predictions.items():
                e = target-pred
                errors[key].extend(e**2)
                local[key] = float(np.sqrt(np.mean(e**2)))
            paired.append(local["current"]-local["history"])
        paired = np.asarray(paired)
        brng = np.random.default_rng(20261010+ci)
        boots = np.array([paired[brng.integers(0,len(paired),len(paired))].mean()
                          for _ in range(10000)])
        output[cond] = {
            "pooled_rmse": {k: float(np.sqrt(np.mean(v))) for k,v in errors.items()},
            "mean_paired_improvement": float(paired.mean()),
            "bootstrap_95_ci": [float(np.quantile(boots,.025)),float(np.quantile(boots,.975))],
            "n_trajectories":N,"n_train":140,"n_test":60,"length":T
        }
    print(json.dumps({"experiment":"Ω-I-EXP-004","results":output},indent=2))

if __name__ == "__main__":
    main()
