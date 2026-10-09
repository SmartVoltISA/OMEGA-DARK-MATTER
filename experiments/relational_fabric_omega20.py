"""Ω-20 exploratory signed-link perturbation model. Requires NumPy.
See preregistration and report in EXPERIMENTS/. The protocol caveat in the report
must be considered: adaptive and frozen branches have different state histories.
"""
import json
import numpy as np
N=160; J=.85; SEEDS=range(20262000,20262040)
MODES=("adaptive_signed","frozen_learned_signed","permuted_learned_signed",
       "fixed_unsigned","adaptive_unsigned","no_coupling")
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
def field(x,e,w,sgn):
    a,b=e[:,0],e[:,1]; sums=np.zeros(N); den=np.zeros(N); vals=w*sgn
    np.add.at(sums,a,vals*x[b]); np.add.at(sums,b,vals*x[a])
    np.add.at(den,a,w); np.add.at(den,b,w)
    return np.divide(sums,den,out=np.zeros_like(sums),where=den>0)
def evolve(x,e,w,sgn,steps,adapt=False,target=None,unsigned=False):
    x=x.copy(); w=w.copy(); sgn=np.ones(len(e)) if unsigned else sgn.copy()
    a,b=e[:,0],e[:,1]
    for _ in range(steps):
        xn=np.tanh(.35*x+J*field(x,e,w,sgn))
        if adapt:
            compat=x[a]*x[b]*sgn
            w=np.clip(w+.025*(compat-.15*w)-.008*(w-1),.1,1.3)
            flip=(compat<-.35)&(w<.35); sgn[flip]*=-1
            if target is not None: w=np.clip(w*(target/w.mean()),.1,1.3)
        x=xn
    return x,w,sgn
def relation_score(x,e,s):
    a,b=e[:,0],e[:,1]; return float(np.mean((np.where(x[a]*x[b]>=0,1.,-1.))==s))
def retention(x0,x1,e,s):
    a,b=e[:,0],e[:,1]
    p=np.where(x0[a]*x0[b]>=0,1,-1)*s
    q=np.where(x1[a]*x1[b]>=0,1,-1)*s
    return float(np.mean(p==q))
def recovery(x0,x1):
    den=np.sqrt(np.mean(x0*x0))
    return 0. if den<1e-10 else float(1-np.sqrt(np.mean((x1-x0)**2))/(2*den))
def run_seed(seed):
    rng=np.random.default_rng(seed); e=make_graph(seed)
    x0=rng.normal(0,.15,N); w0=rng.uniform(.7,1.3,len(e))
    s0=np.where(rng.random(len(e))<.5,1.,-1.)
    xt,wl,sl=evolve(x0,e,w0,s0,100,True,float(w0.mean()))
    wl=np.clip(wl*(w0.mean()/wl.mean()),.1,1.3)
    rp=np.random.default_rng(seed+700000); wp=rp.permutation(wl)
    rows=[]
    for mode in MODES:
        if mode=="adaptive_signed": xpre,wpre,spre=evolve(x0,e,w0,s0,100,True,float(w0.mean()))
        elif mode=="frozen_learned_signed": xpre,wpre,spre=evolve(xt,e,wl,sl,100)
        elif mode=="permuted_learned_signed": xpre,wpre,spre=evolve(xt,e,wp,sl,100)
        elif mode=="fixed_unsigned": xpre,wpre,spre=evolve(x0,e,w0,np.ones(len(e)),200,unsigned=True)
        elif mode=="adaptive_unsigned": xpre,wpre,spre=evolve(x0,e,w0,np.ones(len(e)),200,True,float(w0.mean()),True)
        else:
            xpre=x0.copy()
            for _ in range(200): xpre=np.tanh(.35*xpre)
            wpre=w0.copy(); spre=np.ones(len(e))
        xpert=xpre.copy(); xpert[:int(.1*N)]*=-1
        xpost,_,_=evolve(xpert,e,wpre,spre,100,mode in ("adaptive_signed","adaptive_unsigned"),float(w0.mean()),mode=="adaptive_unsigned")
        rows.append({"seed":seed,"mode":mode,"pre_relation_score":relation_score(xpre,e,spre),
            "post_relation_score":relation_score(xpost,e,spre),"relation_retention":retention(xpre,xpost,e,spre),
            "state_recovery":recovery(xpre,xpost),"pre_rms":float(np.sqrt(np.mean(xpre*xpre))),
            "post_rms":float(np.sqrt(np.mean(xpost*xpost)))})
    return rows
if __name__=="__main__":
    rows=[r for seed in SEEDS for r in run_seed(seed)]
    summary={}
    for mode in MODES:
        rr=[r for r in rows if r["mode"]==mode]; summary[mode]={}
        for k in ("pre_relation_score","post_relation_score","relation_retention","state_recovery","pre_rms","post_rms"):
            summary[mode][k]={"mean":float(np.mean([r[k] for r in rr])),"sd":float(np.std([r[k] for r in rr],ddof=1))}
    print(json.dumps({"seed_count":len(SEEDS),"rows":rows,"summary":summary},indent=2))
