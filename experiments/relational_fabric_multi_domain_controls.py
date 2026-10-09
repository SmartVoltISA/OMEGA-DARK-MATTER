#!/usr/bin/env python3
"""Ω-14: noisy spin network, comparing adaptive/fixed/shuffled/absent couplings.

Requires NumPy. Outputs summary JSON to stdout. Toy model only, not physical matter.
"""
import json
import numpy as np

def make_graph(n=120, k=8, rewire_p=0.15, rng=None):
    edges=set()
    for i in range(n):
        for d in range(1,k//2+1): edges.add(tuple(sorted((i,(i+d)%n))))
    out=set()
    for a,b in sorted(edges):
        if rng.random()<rewire_p:
            candidates=[v for v in range(n) if v!=a and tuple(sorted((a,v)) not in out]
            if candidates: b=int(rng.choice(candidates))
        if a!=b: out.add(tuple(sorted((a,b))))
    edges=sorted(out); adj=[[] for _ in range(n)]
    for e,(a,b) in enumerate(edges): adj[a].append((b,e)); adj[b].append((a,e))
    return edges,adj

def components(s,adj):
    seen=set(); sizes=[]
    for i in range(len(s)):
        if i in seen: continue
        sign=int(s[i]); stack=[i]; seen.add(i); count=0
        while stack:
            u=stack.pop(); count+=1
            for v,e in adj[u]:
                if v not in seen and int(s[v])==sign: seen.add(v); stack.append(v)
        sizes.append(count)
    return sizes

def run(mode,seed):
    rng=np.random.default_rng(seed); n=120
    edges,adj=make_graph(rng=rng); m=len(edges)
    a=np.array([e[0] for e in edges]); b=np.array([e[1] for e in edges])
    w0=rng.uniform(.7,1.3,m); w=w0.copy()
    s=rng.choice([-1,1],n).astype(np.int8); degree=np.array([len(x) for x in adj],float)
    metrics=[]; history=[]
    for t in range(800):
        if mode=="adaptive": we=w
        elif mode=="fixed": we=w0
        elif mode=="shuffled": we=w0[rng.permutation(m)]
        elif mode=="none": we=None
        else: raise ValueError(mode)
        inp=np.zeros(n)
        if we is not None:
            np.add.at(inp,a,we*s[b]); np.add.at(inp,b,we*s[a])
            field=inp/np.maximum(degree,1)
            p=1/(1+np.exp(np.clip(-2*field/.45,-40,40)))
        else: p=np.full(n,.5)
        s=np.where(rng.random(n)<p,1,-1).astype(np.int8)
        if mode=="adaptive":
            corr=s[a]*s[b]
            w=np.clip(w+.008*(corr-.1*w)-.003*(w-1),.05,2)
        if t>=400 and t%20==0:
            cs=components(s,adj)
            metrics.append([np.mean(s[a]==s[b]),abs(np.mean(s)),max(cs)/n,len(cs),np.sum(s!=np.roll(s,1))])
            history.append(s.copy())
    mm=np.array(metrics); h=np.array(history)
    return {"mode":mode,"seed":seed,"edges":m,
        "edge_agreement_mean":float(mm[:,0].mean()),
        "polarization_mean":float(mm[:,1].mean()),
        "largest_component_mean":float(mm[:,2].mean()),
        "component_count_mean":float(mm[:,3].mean()),
        "ring_domain_count_mean":float(mm[:,4].mean()),
        "persistence_lag100":float(np.mean(h[5:]==h[:-5])),
        "final_weight_std":float(np.std(w)) if mode=="adaptive" else
          (float(np.std(w0)) if mode in ("fixed","shuffled") else None)}

def main():
    modes=("adaptive","fixed","shuffled","none")
    runs=[run(mode,20261020+i) for mode in modes for i in range(12)]
    summary={}
    for mode in modes:
        rr=[r for r in runs if r["mode"]==mode]; summary[mode]={}
        for key in ("edge_agreement_mean","polarization_mean","largest_component_mean",
                    "component_count_mean","ring_domain_count_mean","persistence_lag100"):
            vals=np.array([r[key] for r in rr])
            summary[mode][key]={"mean":float(vals.mean()),"sd":float(vals.std(ddof=1)),
                                "min":float(vals.min()),"max":float(vals.max())}
        summary[mode]["weight_std_mean"]=float(np.mean([r["final_weight_std"] for r in rr
            if r["final_weight_std"] is not None])) if mode!="none" else None
    print(json.dumps({"model":"noisy binary-spin network on a rewired ring",
        "warning":"Toy model only; not a physical model of matter.",
        "runs_per_mode":12,"summary":summary,"runs":runs},indent=2))
if __name__=="__main__": main()
