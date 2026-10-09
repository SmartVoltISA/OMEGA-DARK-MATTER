#!/usr/bin/env python3
"""Ω-15: paired local perturbation recovery in adaptive/fixed/shuffled networks.
Run with NumPy: python experiments/relational_fabric_local_recovery.py
Toy network model only; not a physical theory of matter.
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
    for ei,(a,b) in enumerate(edges): adj[a].append((b,ei)); adj[b].append((a,ei))
    return edges,adj

def run_one(mode,seed,n=160,k=4,steps_pre=80,steps_post=80,patch_size=8,eta=0.03,decay=0.01):
    rng=np.random.default_rng(seed); edges,adj=build_graph(n,k,0.03,rng); m=len(edges)
    w0=rng.uniform(0.7,1.3,size=m); w=w0.copy(); sector=n//4
    x=np.ones(n); x[sector:2*sector]=-1; x[3*sector:]=-1
    x=x+0.03*rng.normal(size=n); degree=np.array([len(z) for z in adj])
    def step(state,weights):
        if mode=="adaptive": used=weights
        elif mode=="fixed": used=w0
        elif mode=="shuffled": used=w0[rng.permutation(m)]
        else: raise ValueError(mode)
        inp=np.zeros(n)
        for e,(a,b) in enumerate(edges):
            inp[a]+=used[e]*state[b]; inp[b]+=used[e]*state[a]
        inp/=np.maximum(degree,1)
        new=np.tanh(0.45*state+1.65*inp)
        if mode=="adaptive":
            for e,(a,b) in enumerate(edges):
                corr=new[a]*new[b]
                weights[e]=np.clip(weights[e]+eta*(corr-0.1*weights[e])-decay*(weights[e]-1.0),0.1,2.0)
        return new
    for _ in range(steps_pre): x=step(x,w)
    baseline=x.copy(); wbase=w.copy(); patch=np.arange(sector//2,sector//2+patch_size)
    pert=baseline.copy(); pert[patch]=-pert[patch]; wp=wbase.copy()
    for _ in range(steps_post):
        baseline=step(baseline,wbase); pert=step(pert,wp)
    bs=np.sign(baseline); ps=np.sign(pert)
    target=np.ones(n); target[sector:2*sector]=-1; target[3*sector:]=-1
    boundaries=lambda q:int(np.sum(np.sign(q)!=np.roll(np.sign(q),1)))
    return {"mode":mode,"seed":seed,"N":n,"edge_count":m,"patch_size":patch_size,
        "patch_recovery":float(np.mean(ps[patch]==bs[patch])),
        "global_recovery":float(np.mean(ps==bs)),
        "domain_label_retention":float(np.mean(ps==target)),
        "baseline_boundaries":boundaries(baseline),"perturbed_boundaries":boundaries(pert),
        "weight_std_final":float(np.std(w)) if mode=="adaptive" else float(np.std(w0))}

def main():
    modes=("adaptive","fixed","shuffled")
    runs=[run_one(mode,20261030+i) for mode in modes for i in range(20)]
    summary={}
    for mode in modes:
        rr=[r for r in runs if r["mode"]==mode]; summary[mode]={}
        for key in ("patch_recovery","global_recovery","domain_label_retention","baseline_boundaries","perturbed_boundaries","weight_std_final"):
            vals=np.array([r[key] for r in rr])
            summary[mode][key]={"mean":float(vals.mean()),"sd":float(vals.std(ddof=1)),"min":float(vals.min()),"max":float(vals.max())}
    print(json.dumps({"note":"Toy model only; not physical evidence.","runs_per_mode":20,"summary":summary,"runs":runs},indent=2))
if __name__=="__main__": main()
