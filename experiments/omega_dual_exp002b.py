#!/usr/bin/env python3
"""Ω-DUAL-002B matched binary-accuracy simulation. Requires NumPy."""
import json
from pathlib import Path
import numpy as np

SEED=20261010
SIGMAS=[0.1,0.5,1.0]
N=300
T=200
BURN=50
BOOT=2000

def boot_mean_ci(values, rng):
    values=np.asarray(values); n=len(values)
    samples=np.empty(BOOT)
    for i in range(BOOT):
        samples[i]=values[rng.integers(0,n,n)].mean()
    return [float(np.quantile(samples,.025)),float(np.quantile(samples,.975))]

def sign_pm(v,ties=None):
    out=np.where(v>=0,1,-1).astype(np.int8)
    if ties is not None: out=np.where(v==0,ties,out)
    return out

def per_trajectory_accuracy(pred,target):
    return np.mean(pred==target,axis=1)

def main():
    rng=np.random.default_rng(SEED)
    rows=[]
    for sigma in SIGMAS:
        x=np.zeros((N,T,2))
        eps=rng.normal(0,.25,(N,T,2))
        for t in range(1,T):
            x[:,t,:]=.75*x[:,t-1,:]+eps[:,t,:]
        obs=x+rng.normal(0,sigma,x.shape)
        sl=slice(BURN,T)
        o1,o2=obs[:,sl,0],obs[:,sl,1]
        y=sign_pm(x[:,sl,0]+x[:,sl,1])
        ties=rng.choice(np.array([-1,1],dtype=np.int8),size=y.shape)
        preds={
            "coupled_specialists":sign_pm(o1+o2),
            "uncoupled_specialists":sign_pm(sign_pm(o1).astype(float)+sign_pm(o2).astype(float),ties=ties)
        }
        shuffled=np.empty_like(o2)
        for i in range(N): shuffled[i]=rng.permutation(o2[i])
        preds["shuffled_partner"]=sign_pm(o1+shuffled)
        shared=(x[:,sl,0]+x[:,sl,1])/2
        s1=shared+rng.normal(0,sigma,shared.shape)
        s2=shared+rng.normal(0,sigma,shared.shape)
        preds["shared_target_sensor"]=sign_pm(s1+s2)
        traj={k:per_trajectory_accuracy(v,y) for k,v in preds.items()}
        cond={}
        for k,v in traj.items():
            cond[k]={"accuracy":float(v.mean()),"trajectory_bootstrap95":boot_mean_ci(v,rng)}
        diff=traj["coupled_specialists"]-traj["uncoupled_specialists"]
        cond["paired_coupled_minus_uncoupled"]={"mean_accuracy_difference":float(diff.mean()),"trajectory_bootstrap95":boot_mean_ci(diff,rng)}
        rows.append({"sigma":sigma,"n_trajectories":N,"scored_steps":T-BURN,"conditions":cond})
    # Independent reliability-sweep batch at sigma=.5.
    sigma=.5
    x=np.zeros((N,T,2)); eps=rng.normal(0,.25,(N,T,2))
    for t in range(1,T): x[:,t,:]=.75*x[:,t-1,:]+eps[:,t,:]
    obs=x+rng.normal(0,sigma,x.shape); sl=slice(BURN,T)
    o1,o2=obs[:,sl,0],obs[:,sl,1]
    y=sign_pm(x[:,sl,0]+x[:,sl,1])
    qrows=[]
    for q in [.25,.5,.75,1.0]:
        received=o2.copy()
        bad=rng.random(received.shape)>q
        received[bad]=rng.normal(0,1,int(bad.sum()))
        acc=per_trajectory_accuracy(sign_pm(o1+received),y)
        qrows.append({"q":q,"accuracy":float(acc.mean()),"trajectory_bootstrap95":boot_mean_ci(acc,rng)})
    result={"experiment":"OMEGA-DUAL-002B","status":"EXECUTED_LOCALLY","date":"2026-10-10","seed":SEED,
      "n_trajectories_per_sigma":N,"steps_per_trajectory":T,"burn_in":BURN,"bootstrap_resamples":BOOT,
      "noise_results":rows,"reliability_sweep_sigma_0_5":qrows,
      "scope":"Synthetic information-routing benchmark only; no universal or physical inference."}
    out=Path(__file__).resolve().parents[1]/"results"/"OMEGA-DUAL-002B_RESULTS_2026-10-10.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))

if __name__=="__main__": main()
