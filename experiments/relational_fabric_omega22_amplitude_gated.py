"""Ω-22 amplitude-gated signed-relation stability test. Requires NumPy.
See preregistration in EXPERIMENTS/. This script computes 40 paired seeds.
"""
import json
import numpy as np
N, J, EPS = 160, 0.85, 0.20
SEEDS = range(20262200, 20262240)
MODES = ("adaptive_live","frozen_learned","permuted_learned","fixed_original","no_coupling")

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

def evolve(x,e,w,s,steps,adapt=False,target=None):
    x=x.copy(); w=w.copy(); s=s.copy(); a,b=e[:,0],e[:,1]
    for _ in range(steps):
        xn=np.tanh(.35*x+J*field(x,e,w,s))
        if adapt:
            compat=x[a]*x[b]*s
            w=np.clip(w+.025*(compat-.15*w)-.008*(w-1),.1,1.3)
            if target is not None: w=np.clip(w*(target/w.mean()),.1,1.3)
            flip=(compat<-.35)&(w<.35); s[flip]*=-1
        x=xn
    return x,w,s

def gated_relation(x,e,s):
    a,b=e[:,0],e[:,1]; valid=(np.abs(x[a])>=EPS)&(np.abs(x[b])>=EPS)
    if not valid.any(): return {"score":None,"coverage":0.0,"valid_edges":0}
    relation=np.where(x[a]*x[b]>=0,1.,-1.)
    return {"score":float(np.mean(relation[valid]==s[valid])),
            "coverage":float(valid.mean()),"valid_edges":int(valid.sum())}

def gated_retention(x0,x1,e):
    a,b=e[:,0],e[:,1]
    valid=(np.abs(x0[a])>=EPS)&(np.abs(x0[b])>=EPS)&(np.abs(x1[a])>=EPS)&(np.abs(x1[b])>=EPS)
    if not valid.any(): return {"score":None,"coverage":0.0}
    r0=np.where(x0[a]*x0[b]>=0,1.,-1.); r1=np.where(x1[a]*x1[b]>=0,1.,-1.)
    return {"score":float(np.mean(r0[valid]==r1[valid])),"coverage":float(valid.mean())}

def state_recovery(x0,x1):
    den=np.sqrt(np.mean(x0*x0))
    if den<1e-10: return None
    return float(1-np.sqrt(np.mean((x1-x0)**2))/(2*den))

def run_seed(seed):
    rng=np.random.default_rng(seed); e=make_graph(seed)
    x0=rng.normal(0,.15,N); w0=rng.uniform(.7,1.3,len(e))
    s0=np.where(rng.random(len(e))<.5,1.,-1.)
    xcommon,wlearn,slearn=evolve(x0,e,w0,s0,100,True,float(w0.mean()))
    wlearn=np.clip(wlearn*(w0.mean()/wlearn.mean()),.1,1.3)
    xpert=xcommon.copy(); xpert[:int(.1*N)]*=-1
    wperm=np.random.default_rng(seed+700000).permutation(wlearn)
    rows=[]
    for mode in MODES:
        if mode=="adaptive_live": xpost,_,sp=evolve(xpert,e,wlearn,slearn,100,True,float(w0.mean()))
        elif mode=="frozen_learned": xpost,_,sp=evolve(xpert,e,wlearn,slearn,100)
        elif mode=="permuted_learned": xpost,_,sp=evolve(xpert,e,wperm,slearn,100)
        elif mode=="fixed_original": xpost,_,sp=evolve(xpert,e,w0,s0,100)
        else:
            xpost=xpert.copy()
            for _ in range(100): xpost=np.tanh(.35*xpost)
            sp=s0
        metric=gated_relation(xpost,e,sp); ret=gated_retention(xcommon,xpost,e)
        rows.append({"seed":int(seed),"mode":mode,"primary_score":metric["score"],
          "coverage":metric["coverage"],"valid_edges":metric["valid_edges"],
          "retention":ret["score"],"retention_coverage":ret["coverage"],
          "state_recovery":state_recovery(xcommon,xpost),
          "pre_rms":float(np.sqrt(np.mean(xcommon*xcommon))),
          "post_rms":float(np.sqrt(np.mean(xpost*xpost)))})
    return rows

def main():
    rows=[r for seed in SEEDS for r in run_seed(seed)]
    summary={}
    for mode in MODES:
        rr=[r for r in rows if r["mode"]==mode]; summary[mode]={}
        for k in ("primary_score","coverage","retention","retention_coverage","state_recovery","pre_rms","post_rms"):
            vals=np.array([r[k] for r in rr if r[k] is not None],dtype=float)
            summary[mode][k]={"n":int(len(vals)),"mean":float(vals.mean()) if len(vals) else None,
              "sd":float(vals.std(ddof=1)) if len(vals)>1 else None}
        summary[mode]["fraction_coverage_ge_50pct"]=float(np.mean([r["coverage"]>=.5 for r in rr]))
    rng=np.random.default_rng(20262299); paired={}
    for control in ("permuted_learned","fixed_original"):
        paired[control]={}
        for metric in ("primary_score","retention","state_recovery"):
            d=np.array([next(r[metric] for r in rows if r["seed"]==s and r["mode"]=="frozen_learned")-
              next(r[metric] for r in rows if r["seed"]==s and r["mode"]==control) for s in SEEDS
              if next(r[metric] for r in rows if r["seed"]==s and r["mode"]=="frozen_learned") is not None
              and next(r[metric] for r in rows if r["seed"]==s and r["mode"]==control) is not None])
            boot=d[rng.integers(0,len(d),size=(10000,len(d)))].mean(axis=1)
            paired[control][metric]={"n":len(d),"mean_difference":float(d.mean()),
              "positive":int((d>0).sum()),"negative":int((d<0).sum()),"ties":int((d==0).sum()),
              "ci95":[float(np.quantile(boot,.025)),float(np.quantile(boot,.975))]}
    print(json.dumps({"experiment":"Ω-22 amplitude-gated signed-relation stability",
      "protocol":{"n_seeds":len(list(SEEDS)),"nodes":N,"J":J,"epsilon":EPS,
        "train_steps":100,"post_perturbation_steps":100,"bootstrap_resamples":10000,
        "bootstrap_seed":20262299},"summary":summary,"paired":paired,"runs":rows},indent=2))
if __name__=="__main__": main()
