"""Ω-21 common-snapshot perturbation test. Requires NumPy.
Exploratory run: 40 seeds, six branches from one identical pre-perturbation state.
"""
import json
import numpy as np
N=160; J=.85
SEEDS=range(20262100,20262140)
MODES=("adaptive_live","frozen_learned","permuted_learned","fixed_original","adaptive_unsigned","no_coupling")
def make_graph(seed):
    rng=np.random.default_rng(seed); edges=set()
    for i in range(N):
        for d in (1,2): edges.add(tuple(sorted((i,(i+d)%N))))
    for i in range(N):
        for d in (1,2):
            old=tuple(sorted((i,(i+d)%N)))
            if old in edges and rng.random()<.03:
                edges.remove(old)
                cand=[j for j in range(N) if j!=i and tuple(sorted((i,j))) not in edges]
                if cand: edges.add(tuple(sorted((i,int(rng.choice(cand))))))
    return np.asarray(sorted(edges),dtype=int)
def field(x,e,w,s):
    a,b=e[:,0],e[:,1]; sums=np.zeros(N); den=np.zeros(N); vals=w*s
    np.add.at(sums,a,vals*x[b]); np.add.at(sums,b,vals*x[a])
    np.add.at(den,a,w); np.add.at(den,b,w)
    return np.divide(sums,den,out=np.zeros_like(sums),where=den>0)
def evolve(x,e,w,s,steps,adapt=False,target=None,unsigned=False):
    x=x.copy(); w=w.copy(); s=np.ones(len(e)) if unsigned else s.copy()
    a,b=e[:,0],e[:,1]
    for _ in range(steps):
        xn=np.tanh(.35*x+J*field(x,e,w,s))
        if adapt:
            compat=x[a]*x[b]*s
            w=np.clip(w+.025*(compat-.15*w)-.008*(w-1),.1,1.3)
            if target is not None: w=np.clip(w*(target/w.mean()),.1,1.3)
            flip=(compat<-.35)&(w<.35); s[flip]*=-1
        x=xn
    return x,w,s
def relation_score(x,e,s):
    a,b=e[:,0],e[:,1]
    return float(np.mean(np.where(x[a]*x[b]>=0,1.,-1.)==s))
def retention(x0,x1,e,s):
    a,b=e[:,0],e[:,1]
    p=np.where(x0[a]*x0[b]>=0,1,-1)*s
    q=np.where(x1[a]*x1[b]>=0,1,-1)*s
    return float(np.mean(p==q))
def state_recovery(x0,x1):
    den=np.sqrt(np.mean(x0*x0))
    return 0. if den<1e-10 else float(1-np.sqrt(np.mean((x1-x0)**2))/(2*den))
def run_seed(seed):
    rng=np.random.default_rng(seed); e=make_graph(seed)
    x0=rng.normal(0,.15,N); w0=rng.uniform(.7,1.3,len(e))
    s0=np.where(rng.random(len(e))<.5,1.,-1.)
    # One trained trajectory creates the common snapshot for all branches.
    xcommon,wlearn,slearn=evolve(x0,e,w0,s0,100,True,float(w0.mean()))
    wlearn=np.clip(wlearn*(w0.mean()/wlearn.mean()),.1,1.3)
    xpert=xcommon.copy(); xpert[:int(.1*N)]*=-1
    rp=np.random.default_rng(seed+700000); wperm=rp.permutation(wlearn)
    branches={
      "adaptive_live":(wlearn.copy(),slearn.copy(),True,False),
      "frozen_learned":(wlearn.copy(),slearn.copy(),False,False),
      "permuted_learned":(wperm.copy(),slearn.copy(),False,False),
      "fixed_original":(w0.copy(),s0.copy(),False,False),
      "adaptive_unsigned":(w0.copy(),np.ones(len(e)),True,True),
      "no_coupling":(w0.copy(),np.ones(len(e)),False,True)}
    rows=[]
    for mode,(w,s,adapt,unsigned) in branches.items():
        if mode=="no_coupling":
            xpost=xpert.copy()
            for _ in range(100): xpost=np.tanh(.35*xpost)
            seval=np.ones(len(e))
        else:
            xpost,_,_=evolve(xpert,e,w,s,100,adapt,float(w0.mean()),unsigned)
            seval=np.ones(len(e)) if unsigned else s
        rows.append({"seed":seed,"mode":mode,
          "common_pre_relation_score":relation_score(xcommon,e,seval),
          "post_relation_score":relation_score(xpost,e,seval),
          "relation_retention":retention(xcommon,xpost,e,seval),
          "state_recovery":state_recovery(xcommon,xpost),
          "pre_rms":float(np.sqrt(np.mean(xcommon*xcommon))),
          "post_rms":float(np.sqrt(np.mean(xpost*xpost)))})
    return rows
if __name__=="__main__":
    rows=[r for seed in SEEDS for r in run_seed(seed)]
    summary={}
    for mode in MODES:
        rr=[r for r in rows if r["mode"]==mode]; summary[mode]={}
        for k in ("common_pre_relation_score","post_relation_score","relation_retention","state_recovery","pre_rms","post_rms"):
            v=np.array([r[k] for r in rr])
            summary[mode][k]={"mean":float(v.mean()),"sd":float(v.std(ddof=1))}
    rng=np.random.default_rng(20262199); paired={}
    for control in ("frozen_learned","permuted_learned","fixed_original","adaptive_unsigned"):
        paired[control]={}
        for metric in ("relation_retention","state_recovery"):
            a=np.array([next(r[metric] for r in rows if r["seed"]==s and r["mode"]=="adaptive_live") for s in SEEDS])
            b=np.array([next(r[metric] for r in rows if r["seed"]==s and r["mode"]==control) for s in SEEDS])
            d=a-b; boot=d[rng.integers(0,len(d),size=(10000,len(d)))].mean(axis=1)
            paired[control][metric]={"mean_difference":float(d.mean()),"positive":int((d>0).sum()),
              "negative":int((d<0).sum()),"ties":int((d==0).sum()),
              "ci95":[float(np.quantile(boot,.025)),float(np.quantile(boot,.975))]}
    print(json.dumps({"experiment":"Ω-21 common-snapshot perturbation recovery",
      "n_seeds":len(list(SEEDS)),"runs":rows,"summary":summary,
      "paired_bootstrap_adaptive_live_minus_control":paired},indent=2))
