"""Ω-24 activity-matched continuous relational alignment. Requires NumPy.
Run from repo root:
python experiments/relational_fabric_omega24_activity_matched.py > results/2026-10-09-relational-fabric-omega24.json
"""
import json
import numpy as np

N, J = 160, 0.85
SEEDS = range(20262400, 20262440)
MODES = ("adaptive_live", "frozen_learned", "permuted_learned", "fixed_original", "no_coupling")

def make_graph(seed):
    rng=np.random.default_rng(seed); edges=set()
    for i in range(N):
        for d in (1,2): edges.add(tuple(sorted((i,(i+d)%N))))
    for i in range(N):
        for d in (1,2):
            old=tuple(sorted((i,(i+d)%N)))
            if old in edges and rng.random()<.03:
                edges.remove(old)
                candidates=[j for j in range(N) if j!=i and tuple(sorted((i,j))) not in edges]
                if candidates: edges.add(tuple(sorted((i,int(rng.choice(candidates))))))
    return np.asarray(sorted(edges),dtype=int)

def field(x,e,w,s):
    a,b=e[:,0],e[:,1]; sums=np.zeros(N); den=np.zeros(N)
    np.add.at(sums,a,w*s*x[b]); np.add.at(sums,b,w*s*x[a])
    np.add.at(den,a,w); np.add.at(den,b,w)
    return np.divide(sums,den,out=np.zeros_like(sums),where=den>0)

def evolve(x,e,w,s,steps,adapt=False,target=None):
    x=x.copy(); w=w.copy(); a,b=e[:,0],e[:,1]
    for _ in range(steps):
        xn=np.tanh(.35*x+J*field(x,e,w,s))
        if adapt:
            compat=x[a]*x[b]*s
            w=np.clip(w+.025*(compat-.15*w)-.008*(w-1),.1,1.3)
            if target is not None: w=np.clip(w*(target/w.mean()),.1,1.3)
        x=xn
    return x,w

def metrics(x,e,s):
    a,b=e[:,0],e[:,1]; p=s*x[a]*x[b]
    A=float(np.mean(np.abs(x[a]*x[b]))); M=float(np.mean(p))
    return {"M":M,"A":A,"Q":M/(A+1e-12),"rms":float(np.sqrt(np.mean(x*x)))}

def recovery(x0,x1):
    d=np.sqrt(np.mean(x0*x0))
    return None if d<1e-12 else float(1-np.sqrt(np.mean((x1-x0)**2))/(2*d))

def main():
    runs=[]
    for seed in SEEDS:
        rng=np.random.default_rng(seed); e=make_graph(seed)
        x0=rng.normal(0,.15,N); w0=rng.uniform(.7,1.3,len(e))
        signs=np.where(rng.random(len(e))<.5,1.,-1.)
        xcommon,wlearn=evolve(x0,e,w0,signs,100,True,float(w0.mean()))
        wlearn=np.clip(wlearn*(w0.mean()/wlearn.mean()),.1,1.3)
        xpert=xcommon.copy(); xpert[:int(.1*N)]*=-1
        wperm=np.random.default_rng(seed+700000).permutation(wlearn)
        target_rms=float(np.sqrt(np.mean(xcommon*xcommon)))
        for mode in MODES:
            if mode=="adaptive_live": xpost,_=evolve(xpert,e,wlearn,signs,100,True,float(w0.mean()))
            elif mode=="frozen_learned": xpost,_=evolve(xpert,e,wlearn,signs,100)
            elif mode=="permuted_learned": xpost,_=evolve(xpert,e,wperm,signs,100)
            elif mode=="fixed_original": xpost,_=evolve(xpert,e,w0,signs,100)
            else:
                xpost=xpert.copy()
                for _ in range(100): xpost=np.tanh(.35*xpost)
            raw=metrics(xpost,e,signs)
            matched=None if raw["rms"]<1e-12 else metrics(xpost*(target_rms/raw["rms"]),e,signs)["M"]
            pre=metrics(xcommon,e,signs)
            runs.append({"seed":int(seed),"mode":mode,"target_rms":target_rms,
                "raw_M":raw["M"],"raw_A":raw["A"],"raw_Q":raw["Q"],"raw_rms":raw["rms"],
                "M_matched":matched,"state_recovery":recovery(xcommon,xpost),
                "pre_M":pre["M"],"pre_rms":pre["rms"]})
    summary={}
    for mode in MODES:
        rr=[r for r in runs if r["mode"]==mode]; summary[mode]={}
        for key in ("raw_M","raw_A","raw_Q","raw_rms","M_matched","state_recovery"):
            vals=np.array([r[key] for r in rr if r[key] is not None],float)
            summary[mode][key]={"n":len(vals),"mean":float(vals.mean()) if len(vals) else None,
                "sd":float(vals.std(ddof=1)) if len(vals)>1 else None}
    rng=np.random.default_rng(20262499); paired={}
    for control in ("permuted_learned","fixed_original"):
        paired[control]={}
        for key in ("M_matched","raw_M","raw_A","raw_Q","state_recovery"):
            d=np.array([next(r[key] for r in runs if r["seed"]==seed and r["mode"]=="frozen_learned")-
                next(r[key] for r in runs if r["seed"]==seed and r["mode"]==control) for seed in SEEDS
                if next(r[key] for r in runs if r["seed"]==seed and r["mode"]=="frozen_learned") is not None
                and next(r[key] for r in runs if r["seed"]==seed and r["mode"]==control) is not None])
            boot=d[rng.integers(0,len(d),size=(10000,len(d)))].mean(axis=1)
            paired[control][key]={"n":len(d),"mean_difference":float(d.mean()),
                "positive":int((d>0).sum()),"negative":int((d<0).sum()),
                "ci95":[float(np.quantile(boot,.025)),float(np.quantile(boot,.975))]}
    print(json.dumps({"experiment":"Ω-24 activity-matched continuous relational alignment",
        "status":"actual numerical execution in Python analysis session; script committed for reproduction, not run via GitHub Actions",
        "protocol":{"n_seeds":40,"seed_range":"20262400–20262439","evaluations":len(runs),"nodes":N,"J":J,
            "train_steps":100,"post_perturbation_steps":100,
            "primary_metric":"M_matched = mean(s_e*(c*x_i)*(c*x_j)) where c makes each branch RMS equal to common pre-perturbation RMS",
            "edge_signs_fixed":True,"bootstrap_resamples":10000,"bootstrap_seed":20262499},
        "summary":summary,"paired":paired,"runs":runs},indent=2))
if __name__=="__main__": main()
