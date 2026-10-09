#!/usr/bin/env python3
"""Ω-13: adaptive vs fixed vs shuffled vs no-coupling network controls.

Run: python experiments/relational_fabric_network_controls.py
Only NumPy is required. Results are dimensionless model outputs, not physics evidence.
"""
import json
import numpy as np

def make_graph(n, k, rng, rewire_p=0.15):
    edges=set()
    for i in range(n):
        for d in range(1,k//2+1):
            edges.add(tuple(sorted((i,(i+d)%n))))
    new=set()
    for a,b in sorted(edges):
        if rng.random()<rewire_p:
            candidates=[v for v in range(n) if v!=a and tuple(sorted((a,v))) not in new]
            if candidates:
                b=int(rng.choice(candidates))
        if a!=b:
            new.add(tuple(sorted((a,b))))
    edges=sorted(new)
    adj=[[] for _ in range(n)]
    for e,(a,b) in enumerate(edges):
        adj[a].append((b,e)); adj[b].append((a,e))
    return edges,adj

def run_one(mode, seed, n=120, k=8, steps=500, noise=0.08, eta=0.015, decay=0.005):
    rng=np.random.default_rng(seed)
    edges,adj=make_graph(n,k,rng)
    m=len(edges)
    w0=rng.uniform(0.75,1.25,size=m)
    w=w0.copy()
    x=np.tanh(rng.normal(0,1,size=n))
    agreement=[]; polarization=[]; largest=[]; persistence=[]
    degree=np.array([len(z) for z in adj])
    def metrics(q):
        s=np.sign(q); s[s==0]=1
        agree=np.mean([s[a]==s[b] for a,b in edges])
        seen=set(); maxc=0
        for i in range(n):
            if i in seen: continue
            stack=[i]; seen.add(i); count=0
            while stack:
                u=stack.pop(); count+=1
                for v,e in adj[u]:
                    if v not in seen and s[v]==s[u]:
                        seen.add(v); stack.append(v)
            maxc=max(maxc,count)
        return float(agree),float(abs(np.mean(s))),float(maxc/n)
    for t in range(steps):
        if mode=="adaptive": w_use=w
        elif mode=="fixed": w_use=w0
        elif mode=="shuffled": w_use=w0[rng.permutation(m)]
        elif mode=="none": w_use=None
        else: raise ValueError(mode)
        inp=np.zeros(n)
        if w_use is not None:
            for e,(a,b) in enumerate(edges):
                inp[a]+=w_use[e]*x[b]; inp[b]+=w_use[e]*x[a]
            inp/=np.maximum(degree,1)
            xnew=np.tanh(0.45*x+1.1*inp+noise*rng.normal(size=n))
        else:
            xnew=np.tanh(0.65*x+noise*rng.normal(size=n))
        if mode=="adaptive":
            for e,(a,b) in enumerate(edges):
                corr=xnew[a]*xnew[b]
                w[e]=np.clip(w[e]+eta*(corr-0.15*w[e])-decay*(w[e]-1.0),0.1,2.0)
        if t>=steps//2:
            a,p,l=metrics(xnew)
            agreement.append(a); polarization.append(p); largest.append(l)
            persistence.append(float(np.mean(np.sign(xnew)==np.sign(x))))
        x=xnew
    return {
        "mode":mode,"seed":seed,"N":n,"edge_count":m,"steps":steps,
        "edge_sign_agreement_mean":float(np.mean(agreement)),
        "polarization_abs_mean_sign_mean":float(np.mean(polarization)),
        "largest_same_sign_component_fraction":float(np.mean(largest)),
        "sign_persistence_mean":float(np.mean(persistence)),
        "final_weight_std":float(np.std(w if mode=="adaptive" else w0)) if mode!="none" else None,
        "final_weight_mean":float(np.mean(w if mode=="adaptive" else w0)) if mode!="none" else None
    }

def main():
    modes=("adaptive","fixed","shuffled","none")
    runs=[run_one(mode,20261020+i) for mode in modes for i in range(20)]
    summary={}
    for mode in modes:
        rr=[r for r in runs if r["mode"]==mode]
        summary[mode]={}
        for key in ("edge_sign_agreement_mean","polarization_abs_mean_sign_mean",
                    "largest_same_sign_component_fraction","sign_persistence_mean"):
            vals=np.array([r[key] for r in rr])
            summary[mode][key]={"mean":float(vals.mean()),"std":float(vals.std(ddof=1)),
                                "min":float(vals.min()),"max":float(vals.max())}
        summary[mode]["final_weight_std_mean"]=float(np.mean([r["final_weight_std"] for r in rr if r["final_weight_std"] is not None])) if mode!="none" else None
    print(json.dumps({"model":"tanh node-state dynamics on a fixed small-world-like graph",
                      "note":"Toy model only; not a physical model of matter.",
                      "runs_per_mode":20,"summary":summary,"runs":runs},indent=2))
if __name__=="__main__": main()
