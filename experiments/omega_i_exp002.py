#!/usr/bin/env python3
"""Reproduce Ω-I-EXP-002 summary with NumPy. Python 3 + numpy required."""
import json
import numpy as np

CONDS = ["AR1_CONTINUITY", "IID_NEGATIVE_CONTROL", "REGIME_SWITCH", "REPLACEMENT_WITH_PERSISTENT_RULE"]
N, T = 120, 500

def trajectory(cond, seed):
    rng = np.random.default_rng(seed)
    if cond == "IID_NEGATIVE_CONTROL":
        x = rng.normal(size=T)
    else:
        x = np.zeros(T)
        x[0] = rng.normal()
        for t in range(T-1):
            phi = (0.8 if t < T//2 else -0.8) if cond == "REGIME_SWITCH" else 0.8
            x[t+1] = phi*x[t] + rng.normal()
    return x + rng.normal(size=T)

def design(y):
    xc, xh, target = [], [], []
    for t in range(4, T-1):
        xc.append([1.0, y[t]])
        xh.append([1.0, y[t], y[t-1], y[t-2], y[t-3], y[t-4]])
        target.append(y[t+1])
    return np.asarray(xc), np.asarray(xh), np.asarray(target)

def rmse(y, p):
    return float(np.sqrt(np.mean((y-p)**2)))

def run():
    out = {}
    boot_rng = np.random.default_rng(20261010)
    for ci, cond in enumerate(CONDS):
        ds = [design(trajectory(cond, 20261010 + ci*10000 + i)) for i in range(N)]
        tr, te = ds[:70], ds[70:]
        xc = np.concatenate([d[0] for d in tr]); xh = np.concatenate([d[1] for d in tr])
        y = np.concatenate([d[2] for d in tr])
        bc = np.linalg.lstsq(xc, y, rcond=None)[0]
        bh = np.linalg.lstsq(xh, y, rcond=None)[0]
        perm = np.random.default_rng(20261010 + ci).permutation(len(y))
        bs = np.linalg.lstsq(xh[perm], y, rcond=None)[0]
        sq = {"current": [], "history": [], "shuffled": []}
        paired = []
        for a,b,target in te:
            pc, ph, ps = a@bc, b@bh, b@bs
            vals = {"current":rmse(target,pc),"history":rmse(target,ph),"shuffled":rmse(target,ps)}
            for k,p in [("current",pc),("history",ph),("shuffled",ps)]:
                sq[k].extend((target-p)**2)
            paired.append(vals["current"]-vals["history"])
        paired = np.asarray(paired)
        boots = np.array([np.mean(paired[boot_rng.integers(0,len(paired),len(paired))]) for _ in range(10000)])
        out[cond] = {
            "rmse_pooled": {k:float(np.sqrt(np.mean(v))) for k,v in sq.items()},
            "improvement_current_minus_history":float(np.mean(paired)),
            "bootstrap_95_ci":[float(np.quantile(boots,.025)),float(np.quantile(boots,.975))],
            "n_train":70,"n_test":50,"trajectory_length":T
        }
    print(json.dumps({"experiment":"Ω-I-EXP-002","results":out}, indent=2))

if __name__ == "__main__":
    run()
