#!/usr/bin/env python3
"""Ω-DUAL-004 adaptive specialization toy simulation. Requires NumPy."""
import json
from pathlib import Path
import numpy as np

SEED=20261010
N=300
T=300
BURN=50
SIGMA=0.5
BOOT=2000
WINDOW=15
MESSAGE_COST=0.02

def sign_pm(z):
    return np.where(z >= 0, 1, -1)

def bootstrap_ci(values, rng):
    values=np.asarray(values, dtype=float)
    n=len(values)
    samples=np.empty(BOOT)
    for i in range(BOOT):
        samples[i]=values[rng.integers(0,n,n)].mean()
    return [float(np.quantile(samples,0.025)), float(np.quantile(samples,0.975))]

def main():
    rng=np.random.default_rng(SEED)
    trajectories=[]
    for _ in range(N):
        x=np.zeros((T,2))
        eps=rng.normal(0,0.35,(T,2))
        for t in range(1,T):
            x[t]=0.85*x[t-1]+eps[t]
        weights=np.array([[0.9,0.1] if (t//75)%2==0 else [0.1,0.9] for t in range(T)])
        obs=x+rng.normal(0,SIGMA,(T,2))
        target=sign_pm(np.sum(x*weights,axis=1))
        oracle=sign_pm(np.sum(obs*weights,axis=1))
        fixed=sign_pm(0.9*obs[:,0]+0.1*obs[:,1])
        adaptive=np.zeros(T)
        dominant=0
        for t in range(T):
            if t>=BURN and (t-BURN)%WINDOW==0 and t>=BURN+WINDOW:
                start=t-WINDOW
                p0=sign_pm(0.9*obs[start:t,0]+0.1*obs[start:t,1])
                p1=sign_pm(0.1*obs[start:t,0]+0.9*obs[start:t,1])
                dominant=0 if np.mean(p0==target[start:t])>=np.mean(p1==target[start:t]) else 1
            adaptive[t]=sign_pm(0.9*obs[t,0]+0.1*obs[t,1] if dominant==0 else 0.1*obs[t,0]+0.9*obs[t,1])
        aggregate=np.sum(x*weights,axis=1)
        shared1=aggregate+rng.normal(0,SIGMA,T)
        shared2=aggregate+rng.normal(0,SIGMA,T)
        shared=sign_pm(shared1+shared2)
        local1=sign_pm(obs[:,0]); local2=sign_pm(obs[:,1])
        ties=rng.choice(np.array([-1,1]),T)
        no_comm=np.where(local1+local2==0,ties,sign_pm(local1+local2))
        sl=slice(BURN,T)
        row={
          "oracle":float(np.mean(oracle[sl]==target[sl])),
          "fixed":float(np.mean(fixed[sl]==target[sl])),
          "adaptive":float(np.mean(adaptive[sl]==target[sl])),
          "shared":float(np.mean(shared[sl]==target[sl])),
          "no_communication":float(np.mean(no_comm[sl]==target[sl]))
        }
        for i,(start,end) in enumerate([(BURN,150),(150,225),(225,T)]):
            row[f"adaptive_regime{i}"]=float(np.mean(adaptive[start:end]==target[start:end]))
            row[f"fixed_regime{i}"]=float(np.mean(fixed[start:end]==target[start:end]))
        trajectories.append(row)
    summary={}
    for key in ["oracle","fixed","adaptive","shared","no_communication"]:
        vals=[r[key] for r in trajectories]
        summary[key]={"accuracy":float(np.mean(vals)),"trajectory_bootstrap95":bootstrap_ci(vals,rng)}
    diffs=[r["adaptive"]-r["fixed"] for r in trajectories]
    summary["adaptive_minus_fixed"]={"mean_accuracy_difference":float(np.mean(diffs)),"trajectory_bootstrap95":bootstrap_ci(diffs,rng)}
    for i in range(3):
        summary[f"regime{i}"]={k:float(np.mean([r[f"{k}_regime{i}"] for r in trajectories])) for k in ["adaptive","fixed"]}
    summary["adaptive_net_after_message_cost"]={
      "raw_accuracy":summary["adaptive"]["accuracy"],
      "message_cost_per_scored_step":MESSAGE_COST,
      "net_score":summary["adaptive"]["accuracy"]-MESSAGE_COST
    }
    result={"experiment":"OMEGA-DUAL-004","status":"EXECUTED_LOCALLY","date":"2026-10-10","seed":SEED,
      "n_trajectories":N,"steps_per_trajectory":T,"burn_in":BURN,"observation_noise_sigma":SIGMA,
      "bootstrap_resamples":BOOT,"adaptation_window":WINDOW,"message_cost":MESSAGE_COST,
      "summary":summary,"scope":"Synthetic task-dependent adaptive sensor allocation only."}
    out=Path(__file__).resolve().parents[1]/"results"/"OMEGA-DUAL-004_RESULTS_2026-10-10.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
