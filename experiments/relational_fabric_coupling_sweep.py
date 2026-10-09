"""Ω-19 coupling sweep; NumPy required. See preregistration in EXPERIMENTS/."""
import json
import numpy as np
N=160
JS=(0.25,0.60,1.00,1.65)
SEEDS=range(20261900,20261940)
MODES=("frozen_learned","permuted_learned","fixed_original","no_coupling")
def graph(seed):
    rng=np.random.default_rng(seed); edges=set()
    for i in range(N):
        for d in range(1,3): edges.add(tuple(sorted((i,(i+d)%N))))
    for i in range(N):
        for d in range(1,3):
            old=tuple(sorted((i,(i+d)%N)))
            if old in edges and rng.random()<.03:
                edges.remove(old)
                cand=[j for j in range(N) if j!=i and tuple(sorted((i,j))) not in edges]
                if cand: edges.add(tuple(sorted((i,int(rng.choice(cand))))))
    return np.asarray(sorted(edges),dtype=int)
def evolve(x,e,w,steps,J,adapt=False,target=None):
    x=x.copy(); w=w.copy(); a,b=e[:,0],e[:,1]
    for _ in range(steps):
        sums,den=np.zeros(N),np.zeros(N)
        np.add.at(sums,a,w*x[b]); np.add.at(sums,b,w*x[a])
        np.add.at(den,a,w); np.add.at(den,b,w)
        avg=np.divide(sums,den,out=np.zeros_like(sums),where=den>0)
        xn=np.tanh(.45*x+J*avg)
        if adapt:
            w=np.clip(w+.03*(x[a]*x[b]-.1*w)-.01*(w-1),.1,2)
            if target is not None: w=np.clip(w*(target/w.mean()),.1,2)
        x=xn
    return x,w
def metrics(x,e):
    s=np.where(x>=0,1,-1); a,b=e[:,0],e[:,1]
    adj=[[] for _ in range(N)]
    for i,j in e:
        if s[i]==s[j]: adj[i].append(j); adj[j].append(i)
    seen=set(); components=0
    for i in range(N):
        if i not in seen:
            components+=1; stack=[i]; seen.add(i)
            while stack:
                u=stack.pop()
                for v in adj[u]:
                    if v not in seen: seen.add(v); stack.append(v)
    return {"sign_agreement":float(np.mean(s[a]==s[b])),
            "sign_components":components,"state_rms":float(np.sqrt(np.mean(x*x))),
            "plus_fraction":float(np.mean(s>0))}
def run():
    out=[]
    for seed in SEEDS:
        rng=np.random.default_rng(seed); e=graph(seed)
        x=rng.normal(0,.15,N); w0=rng.uniform(.7,1.3,len(e)); target=float(w0.mean())
        for J in JS:
            _,wl=evolve(x,e,w0,80,J,True,target)
            wl=np.clip(wl*(target/wl.mean()),.1,2)
            rp=np.random.default_rng(seed+int(J*10000)+800000)
            for mode in MODES:
                if mode=="frozen_learned": xe,we=evolve(x,e,wl,160,J)
                elif mode=="permuted_learned": xe,we=evolve(x,e,rp.permutation(wl),160,J)
                elif mode=="fixed_original": xe,we=evolve(x,e,w0,160,J)
                else:
                    xe=x.copy()
                    for _ in range(160): xe=np.tanh(.45*xe)
                    we=w0
                out.append({"seed":seed,"J":J,"mode":mode,**metrics(xe,e)})
    return out
if __name__=="__main__":
    runs=run(); summary={}
    for J in JS:
        summary[str(J)]={}
        for mode in MODES:
            rr=[r for r in runs if r["J"]==J and r["mode"]==mode]
            summary[str(J)][mode]={k:{"mean":float(np.mean([r[k] for r in rr])),
                "sd":float(np.std([r[k] for r in rr],ddof=1))}
                for k in ("sign_agreement","sign_components","state_rms","plus_fraction")}
    rng=np.random.default_rng(20261999); paired={}
    for J in JS:
        paired[str(J)]={}
        for control in ("fixed_original","permuted_learned"):
            a=np.array([next(r["sign_agreement"] for r in runs if r["seed"]==s and r["J"]==J and r["mode"]=="frozen_learned") for s in SEEDS])
            b=np.array([next(r["sign_agreement"] for r in runs if r["seed"]==s and r["J"]==J and r["mode"]==control) for s in SEEDS])
            d=a-b; boot=d[rng.integers(0,len(d),size=(10000,len(d)))].mean(axis=1)
            paired[str(J)]["frozen_minus_"+control]={"mean":float(d.mean()),
                "positive":int((d>0).sum()),"negative":int((d<0).sum()),"ties":int((d==0).sum()),
                "ci95":[float(np.quantile(boot,.025)),float(np.quantile(boot,.975))]}
    print(json.dumps({"preregistration":"EXPERIMENTS/2026-10-09-relational-fabric-coupling-sweep-preregistration.md",
        "seed_count":len(SEEDS),"runs":runs,"summary":summary,"paired_bootstrap":paired},indent=2))
