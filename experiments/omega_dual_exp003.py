#!/usr/bin/env python3
"""Ω-DUAL-003. Requires NumPy. See preregistration for exact model."""
import json
from pathlib import Path
import numpy as np
SEED=20261010; N=300; T=240; BURN=40; BOOT=2000
SIGMAS=[0.2,0.6,1.0]
def signp(z): return np.where(z>=0,1,-1).astype(np.int8)
def boot_ci(v,rng):
    v=np.asarray(v); n=len(v)
    means=np.empty(BOOT)
    for i in range(BOOT): means[i]=v[rng.integers(0,n,n)].mean()
    return [float(np.quantile(means,.025)),float(np.quantile(means,.975))]
def main():
    rng=np.random.default_rng(SEED); rows=[]
    for sigma in SIGMAS:
        x=np.zeros((N,T,2)); eps=rng.normal(0,.3,(N,T,2))
        for t in range(1,T): x[:,t,:]=.82*x[:,t-1,:]+eps[:,t,:]
        weights=np.zeros((T,2)); weights[:120]=[.8,.2]; weights[120:]=[.2,.8]
        sl=slice(BURN,T)
        y=signp(np.sum(x*weights[None,:,:],axis=2))[:,sl]
        obs1=x[:,:,0]+rng.normal(0,sigma,(N,T))
        obs2=x[:,:,1]+rng.normal(0,sigma,(N,T))
        preds={
          "specialized":signp(weights[None,:,0]*obs1+weights[None,:,1]*obs2)[:,sl],
          "shared_aggregate":signp(
              (np.sum(x*weights[None,:,:],axis=2)+rng.normal(0,sigma,(N,T)))[:,sl]
              +(np.sum(x*weights[None,:,:],axis=2)+rng.normal(0,sigma,(N,T)))[:,sl]),
          "misallocated_specialists":signp(weights[::-1][None,:,0]*obs1+weights[::-1][None,:,1]*obs2)[:,sl]
        }
        rand2=rng.normal(0,1,(N,T))
        # Single aggregate sensor plus an independent random second channel.
        # The aggregate sensor is generated independently for this condition.
        preds["single_sensor_shared"]=signp(shared1[:,sl]+rand2[:,sl])
        # Shuffle partner observations within each trajectory across scored times.
        shuffled=np.empty_like(obs2)
        for i in range(N): shuffled[i]=rng.permutation(obs2[i])
        preds["shuffled_partner"]=signp(obs1[:,sl]+shuffled[:,sl])
        acc={k:(v==y).mean(axis=1) for k,v in preds.items()}
        conditions={}
        for k,v in acc.items(): conditions[k]={"accuracy":float(v.mean()),"trajectory_bootstrap95":boot_ci(v,rng)}
        diff=acc["specialized"]-acc["shared_aggregate"]
        conditions["paired_specialized_minus_shared"]={"mean_accuracy_difference":float(diff.mean()),"trajectory_bootstrap95":boot_ci(diff,rng)}
        regime_accuracy={}
        # Scored indices correspond to original t=40..239. Regime 1: original 40..119; regime 2: 120..239.
        for name,rs in [("regime1",slice(0,80)),("regime2",slice(80,200))]:
            regime_accuracy[name]={k:float((v[:,rs]==y[:,rs]).mean()) for k,v in preds.items()}
        rows.append({"sigma":sigma,"n_trajectories":N,"scored_steps":T-BURN,"conditions":conditions,"regime_accuracy":regime_accuracy})
    result={"experiment":"OMEGA-DUAL-003","status":"EXECUTED_LOCALLY","date":"2026-10-10","seed":SEED,
      "n_trajectories_per_sigma":N,"steps_per_trajectory":T,"burn_in":BURN,"bootstrap_resamples":BOOT,
      "results":rows,"scope":"Synthetic task-dependent sensor allocation benchmark only."}
    out=Path(__file__).resolve().parents[1]/"results"/"OMEGA-DUAL-003_RESULTS_2026-10-10.json"
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,indent=2)+"\\n",encoding="utf-8")
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()
