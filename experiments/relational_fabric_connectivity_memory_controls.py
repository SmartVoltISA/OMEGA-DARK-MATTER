#!/usr/bin/env python3
"""Ω-17: topology-specific learned weights vs distribution-matched controls.

NumPy only. The trained weight vector is rescaled to the original mean before
controls, so learned-vs-permuted comparisons preserve its exact weight distribution
and mean. All conditions share the same graph and trained node state per seed.
"""
import json
import numpy as np

def build_graph(n=160,k=4,rewiring=0.03,rng=None):
    rng=np.random.default_rng() if rng is None else rng
    edges=set()
    for i in range(n):
        for d in range(1,k//2+1): edges.add(tuple(sorted((i,(i+d)%n))))
    out=set()
    for a,b in sorted(edges):
        if rng.random()<rewiring:
            candidates=[v for v in range(n) if v!=a and tuple(sorted((a,v))) not in out]
            if candidates: b=int(rng.choice(candidates))
        if a!=b: out.add(tuple(sorted((a,b))))
    edges=sorted(out); adj=[[] for _ in range(n)]
    for ei,(a,b) in enumerate(edges): adj[a].append((b,ei));adj[b].append((a,ei))
    return edges,adj

def run_seed(seed,n=160,k=4,train_steps=80,recovery_steps=80,patch_size=8,eta=0.03,decay=0.01):
    rng=np.random.default_rng(seed); edges,adj=build_graph(n,k,0.03,rng)
    m=len(edges); deg=np.array([len(z) for z in adj])
    w0=rng.uniform(0.7,1.3,m); w=w0.copy()
    sector=n//4; x=np.ones(n); x[sector:2*sector]=-1; x[3*sector:]=-1
    x+=0.03*rng.normal(size=n)
    def step(q,ww,adapt=False):
        inp=np.zeros(n)
        for e,(a,b) in enumerate(edges): inp[a]+=ww[e]*q[b]; inp[b]+=ww[e]*q[a]
        inp/=np.maximum(deg,1)
        qn=np.tanh(0.45*q+1.65*inp); wn=ww.copy()
        if adapt:
            for e,(a,b) in enumerate(edges):
                corr=qn[a]*qn[b]
                wn[e]=np.clip(ww[e]+eta*(corr-0.1*ww[e])-decay*(ww[e]-1),0.1,2.0)
        return qn,wn
    for _ in range(train_steps): x,w=step(x,w,True)
    trained_x=x.copy()
    # Normalize learned weights to original mean; keeps learned ranking/distribution shape.
    wlearn=w*(np.mean(w0)/np.mean(w))
    wperm=wlearn[rng.permutation(m)]
    bins={}
    for e,(a,b) in enumerate(edges): bins.setdefault(tuple(sorted((deg[a],deg[b]))),[]).append(e)
    wbin=wlearn.copy()
    for ids in bins.values():
        if len(ids)>1: wbin[ids]=wlearn[rng.permutation(ids)]
    sector_target=np.ones(n); sector_target[sector:2*sector]=-1; sector_target[3*sector:]=-1
    controls={"frozen_learned_norm":wlearn,"permuted_learned_norm":wperm,
              "degreebin_permuted_norm":wbin,"fixed_original":w0}
    out=[]
    for mode,weights in controls.items():
        base=trained_x.copy(); pert=trained_x.copy()
        patch=np.arange(sector//2,sector//2+patch_size); pert[patch]=-pert[patch]
        for _ in range(recovery_steps):
            base,_=step(base,weights,False); pert,_=step(pert,weights,False)
        bs=np.sign(base); ps=np.sign(pert)
        out.append({"mode":mode,"seed":seed,"N":n,"edges":m,"train_steps":train_steps,
            "recovery_steps":recovery_steps,"patch_recovery":float(np.mean(ps[patch]==bs[patch])),
            "global_recovery":float(np.mean(ps==bs)),"domain_retention":float(np.mean(ps==sector_target)),
            "boundaries":int(np.sum(ps!=np.roll(ps,1))),"weight_mean":float(np.mean(weights)),
            "weight_std":float(np.std(weights))})
    return out

def summarize(runs):
    result={}
    keys=("patch_recovery","global_recovery","domain_retention","boundaries","weight_mean","weight_std")
    for mode in sorted(set(r["mode"] for r in runs)):
        rr=[r for r in runs if r["mode"]==mode]; result[mode]={}
        for key in keys:
            vals=np.array([r[key] for r in rr])
            result[mode][key]={"mean":float(vals.mean()),"sd":float(vals.std(ddof=1)),
                               "min":float(vals.min()),"max":float(vals.max())}
    return result

def paired(runs,a,b,key,boot_seed=20261199,nboot=10000):
    aa={r["seed"]:r[key] for r in runs if r["mode"]==a}
    bb={r["seed"]:r[key] for r in runs if r["mode"]==b}
    ds=np.array([aa[s]-bb[s] for s in sorted(aa)])
    rng=np.random.default_rng(boot_seed)
    boots=np.array([rng.choice(ds,size=len(ds),replace=True).mean() for _ in range(nboot)])
    return {"mean_difference":float(ds.mean()),"positive_pairs":int((ds>0).sum()),
            "negative_pairs":int((ds<0).sum()),"ties":int((ds==0).sum()),
            "bootstrap_95ci":[float(np.quantile(boots,.025)),float(np.quantile(boots,.975))]}

def main():
    runs=[r for i in range(40) for r in run_seed(20261100+i)]
    pairs={
      "learned_minus_permuted_domain_retention":paired(runs,"frozen_learned_norm","permuted_learned_norm","domain_retention"),
      "learned_minus_degreebin_domain_retention":paired(runs,"frozen_learned_norm","degreebin_permuted_norm","domain_retention"),
      "learned_minus_original_domain_retention":paired(runs,"frozen_learned_norm","fixed_original","domain_retention"),
      "learned_minus_permuted_patch_recovery":paired(runs,"frozen_learned_norm","permuted_learned_norm","patch_recovery")
    }
    print(json.dumps({"experiment":"Omega-17","runs_per_condition":40,"summary":summarize(runs),"paired_comparisons":pairs,"runs":runs},indent=2))
if __name__=="__main__": main()
