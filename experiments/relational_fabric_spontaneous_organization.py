"""Ω-18: spontaneous organization from random initial states.

NumPy required. Same graph and random initial state are paired across modes.
No domains are preset. This is a toy-network falsification test, not physics.
"""
import json
import numpy as np

N, K, REWIRE = 160, 4, 0.03
SEEDS = range(20261200, 20261240)
MODES = ("adaptive_live", "frozen_learned", "permuted_learned",
         "fixed_original", "no_coupling")

def make_graph(seed):
    rng=np.random.default_rng(seed); edges=set()
    for i in range(N):
        for d in range(1,K//2+1): edges.add(tuple(sorted((i,(i+d)%N))))
    for i in range(N):
        for d in range(1,K//2+1):
            old=tuple(sorted((i,(i+d)%N)))
            if old in edges and rng.random()<REWIRE:
                edges.remove(old)
                cand=[j for j in range(N) if j!=i and tuple(sorted((i,j))) not in edges]
                if cand: edges.add(tuple(sorted((i,int(rng.choice(cand))))))
    return np.asarray(sorted(edges),dtype=int)

def evolve(x,edges,w,steps,adapt=False,target_mean=None):
    x,w=x.copy(),w.copy(); a,b=edges[:,0],edges[:,1]
    for _ in range(steps):
        sums,den=np.zeros(N),np.zeros(N)
        np.add.at(sums,a,w*x[b]); np.add.at(sums,b,w*x[a])
        np.add.at(den,a,w); np.add.at(den,b,w)
        avg=np.divide(sums,den,out=np.zeros_like(sums),where=den>0)
        xn=np.tanh(.45*x+1.65*avg)
        if adapt:
            w=np.clip(w+.03*(x[a]*x[b]-.1*w)-.01*(w-1),.1,2)
            if target_mean is not None: w=np.clip(w*(target_mean/w.mean()),.1,2)
        x=xn
    return x,w

def metrics(x,edges):
    sign=np.where(x>=0,1,-1); a,b=edges[:,0],edges[:,1]
    adj=[[] for _ in range(N)]
    for i,j in edges:
        if sign[i]==sign[j]: adj[i].append(j); adj[j].append(i)
    seen=set(); comps=0
    for i in range(N):
        if i not in seen:
            comps+=1; stack=[i]; seen.add(i)
            while stack:
                u=stack.pop()
                for v in adj[u]:
                    if v not in seen: seen.add(v); stack.append(v)
    return {"sign_agreement":float(np.mean(sign[a]==sign[b])),
            "plus_fraction":float(np.mean(sign>0)),
            "sign_components":comps,
            "state_rms":float(np.sqrt(np.mean(x*x))),
            "mean_abs_state":float(np.mean(np.abs(x)))}

def run(seed,mode):
    rng=np.random.default_rng(seed); edges=make_graph(seed)
    # Independent random Gaussian initial states; no preset domain pattern.
    x0=rng.normal(0,.15,N); w0=rng.uniform(.7,1.3,len(edges)); target=float(w0.mean())
    _,wlearn=evolve(x0,edges,w0,80,adapt=True,target_mean=target)
    wlearn=np.clip(wlearn*(target/wlearn.mean()),.1,2)
    rngp=np.random.default_rng(seed+500000)
    if mode=="adaptive_live": xe,we=evolve(x0,edges,w0,160,adapt=True,target_mean=target)
    elif mode=="frozen_learned": xe,we=evolve(x0,edges,wlearn,160)
    elif mode=="permuted_learned": xe,we=evolve(x0,edges,rngp.permutation(wlearn),160)
    elif mode=="fixed_original": xe,we=evolve(x0,edges,w0,160)
    else:
        xe=x0.copy()
        for _ in range(160): xe=np.tanh(.45*xe)
        we=w0.copy()
    return {"seed":seed,"mode":mode,**metrics(xe,edges),
            "initial_sign_agreement":metrics(x0,edges)["sign_agreement"],
            "initial_sign_components":metrics(x0,edges)["sign_components"],
            "weight_mean":float(we.mean()),"weight_std":float(we.std())}

if __name__=="__main__":
    runs=[run(s,m) for s in SEEDS for m in MODES]
    summary={}
    for mode in MODES:
        rr=[r for r in runs if r["mode"]==mode]
        summary[mode]={k:{"mean":float(np.mean([r[k] for r in rr])),
                          "sd":float(np.std([r[k] for r in rr],ddof=1))}
                       for k in ("sign_agreement","plus_fraction","sign_components",
                                 "state_rms","mean_abs_state","initial_sign_agreement",
                                 "initial_sign_components","weight_mean","weight_std")}
    print(json.dumps({"seeds":list(SEEDS),"runs":runs,"summary":summary},indent=2))
