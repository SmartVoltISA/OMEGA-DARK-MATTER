#!/usr/bin/env python3
"""Ω-16: learned connectivity memory vs online adaptation.

Four modes:
- adaptive_live: adapt weights during preconditioning and recovery
- frozen_learned: learn weights during preconditioning, then freeze
- fixed_original: never learn weights
- shuffled_learned: randomly reassign learned weights during recovery
Python 3 + NumPy. Dimensionless toy network, not a physical model.
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

def run_one(mode,seed,n=160,k=4,train_steps=80,recovery_steps=80,patch_size=8,eta=0.03,decay=0.01):
    rng=np.random.default_rng(seed); edges,adj=build_graph(n,k,0.03,rng); m=len(edges)
    deg=np.array([len(z) for z in adj]); w0=rng.uniform(0.7,1.3,size=m); w=w0.copy()
    sector=n//4; x=np.ones(n); x[sector:2*sector]=-1; x[3*sector:]=-1
    x=x+0.03*rng.normal(size=n)
    def step(q,ww,adapt=False):
        inp=np.zeros(n)
        for e,(a,b) in enumerate(edges): inp[a]+=ww[e]*q[b]; inp[b]+=ww[e]*q[a]
        inp/=np.maximum(deg,1); qn=np.tanh(0.45*q+1.65*inp); wn=ww.copy()
        if adapt:
            for e,(a,b) in enumerate(edges):
                corr=qn[a]*qn[b]
                wn[e]=np.clip(ww[e]+eta*(corr-0.1*ww[e])-decay*(ww[e]-1),0.1,2.0)
        return qn,wn
    # IMPORTANT: train weights in both adaptive_live and frozen_learned.
    for _ in range(train_steps):
        if mode in ("adaptive_live","frozen_learned"): x,w=step(x,w,True)
        else: x,w=step(x,w0,False)
    trained_x=x.copy()
    learned_w=w.copy() if mode in ("adaptive_live","frozen_learned","shuffled_learned") else w0.copy()
    baseline=trained_x.copy(); pert=trained_x.copy()
    start=sector//2; patch=np.arange(start,start+patch_size); pert[patch]=-pert[patch]
    wb=learned_w.copy(); wp=learned_w.copy()
    for _ in range(recovery_steps):
        if mode=="adaptive_live":
            baseline,wb=step(baseline,wb,True); pert,wp=step(pert,wp,True)
        elif mode=="frozen_learned":
            baseline,_=step(baseline,learned_w,False); pert,_=step(pert,learned_w,False)
        elif mode=="fixed_original":
            baseline,_=step(baseline,w0,False); pert,_=step(pert,w0,False)
        elif mode=="shuffled_learned":
            baseline,_=step(baseline,learned_w[rng.permutation(m)],False)
            pert,_=step(pert,learned_w[rng.permutation(m)],False)
        else: raise ValueError(mode)
    base_sign=np.sign(baseline); pert_sign=np.sign(pert)
    target=np.ones(n); target[sector:2*sector]=-1; target[3*sector:]=-1
    return {"mode":mode,"seed":seed,"N":n,"edges":m,"train_steps":train_steps,"recovery_steps":recovery_steps,
        "patch_recovery":float(np.mean(pert_sign[patch]==base_sign[patch])),
        "global_recovery":float(np.mean(pert_sign==base_sign)),
        "domain_label_retention":float(np.mean(pert_sign==target)),
        "baseline_boundaries":int(np.sum(base_sign!=np.roll(base_sign,1))),
        "perturbed_boundaries":int(np.sum(pert_sign!=np.roll(pert_sign,1))),
        "learned_weight_std":float(np.std(learned_w)),"learned_weight_mean":float(np.mean(learned_w))}

def main():
    modes=("adaptive_live","frozen_learned","fixed_original","shuffled_learned")
    runs=[run_one(mode,20261040+i) for mode in modes for i in range(20)]
    summary={}
    for mode in modes:
        rr=[r for r in runs if r["mode"]==mode]; summary[mode]={}
        for key in ("patch_recovery","global_recovery","domain_label_retention","baseline_boundaries","perturbed_boundaries","learned_weight_std"):
            vals=np.array([r[key] for r in rr])
            summary[mode][key]={"mean":float(vals.mean()),"sd":float(vals.std(ddof=1)),"min":float(vals.min()),"max":float(vals.max())}
    print(json.dumps({"summary":summary,"runs":runs},indent=2))
if __name__=="__main__": main()
