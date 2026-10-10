#!/usr/bin/env python3
"""Reproduce Ω-I-EXP-007 synthetic intervention benchmark.
Requires Python 3, numpy, scikit-learn. No external data."""
import json
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import roc_auc_score, balanced_accuracy_score

CONDS=["AR1","IID","SWITCH","OSC"]
def make_base(cond,seed,T=240,d=8):
    rng=np.random.default_rng(seed); x=np.zeros((T,d)); x[0]=rng.normal(size=d)
    A=np.eye(d)*.55+rng.normal(scale=.025,size=(d,d))
    for t in range(T-1):
        if cond=="IID": x[t+1]=rng.normal(size=d)
        elif cond=="SWITCH": x[t+1]=(0.65 if t<T//2 else -0.65)*x[t]+rng.normal(size=d)
        elif cond=="OSC":
            if t>=1: x[t+1,:d//2]=1.25*x[t,:d//2]-.55*x[t-1,:d//2]+rng.normal(scale=.45,size=d//2)
            x[t+1,d//2:]=.6*x[t,d//2:]+rng.normal(size=d-d//2)
        else: x[t+1]=A@x[t]+rng.normal(size=d)
    return x,x+rng.normal(scale=.6,size=x.shape),A
def org(o):
    cov=np.cov(o[-60:].T)
    return np.array([np.mean(np.diag(cov)),np.mean(np.abs(cov-np.diag(np.diag(cov))))])
def features(o1,o2):
    cur=np.linalg.norm(o1[-1]-o2[-1])
    hist=np.mean(np.linalg.norm(o1[-6:]-o2[-6:],axis=1))
    tr=np.mean(np.linalg.norm(np.diff(o1[-8:],axis=0)-np.diff(o2[-8:],axis=0),axis=1))
    od=np.linalg.norm(org(o1)-org(o2))
    return [cur,hist,tr,od]
def main():
    rows=[]
    for ci,cond in enumerate(CONDS):
        for i in range(250):
            x,o,A=make_base(cond,20261010+ci*10000+i)
            rng=np.random.default_rng(20261010+500000+ci*10000+i); start=x[119].copy()
            def tail(inter):
                z=np.zeros((120,8)); z[0]=start
                for t in range(119):
                    if cond=="IID": z[t+1]=rng.normal(size=8)
                    elif cond=="SWITCH": z[t+1]=(-.65 if 119+t>=120 else .65)*z[t]+rng.normal(size=8)
                    elif cond=="OSC": z[t+1]=.6*z[t]+rng.normal(size=8)
                    else: z[t+1]=A@z[t]+rng.normal(size=8)
                if inter=="FUNCTION_PERTURB": z[1:]+=rng.normal(scale=.9,size=z[1:].shape)
                return z,z+rng.normal(scale=.6,size=z.shape)
            for inter in ["CONTINUATION","SNAPSHOT_CLONE","ELEMENT_REPLACEMENT","FUNCTION_PERTURB"]:
                xa,oa=tail("CONTINUATION"); xb,ob=tail(inter)
                label=int(inter in ("CONTINUATION","ELEMENT_REPLACEMENT"))
                rows.append((features(oa,ob),label,cond,i))
    X=np.array([r[0] for r in rows]); y=np.array([r[1] for r in rows])
    conds=np.array([r[2] for r in rows]); fam=np.array([r[3] for r in rows])
    tr=np.zeros(len(y),bool); te=np.zeros(len(y),bool)
    for c in CONDS:
        ids=np.unique(fam[conds==c]); tr|=(conds==c)&np.isin(fam,ids[:175]); te|=(conds==c)&np.isin(fam,ids[175:])
    metrics={}
    for name,cols in {"present":[0],"present_history":[0,1],"present_history_transition":[0,1,2],"full":[0,1,2,3]}.items():
        m=make_pipeline(StandardScaler(),LogisticRegression(C=1,max_iter=3000,random_state=1))
        m.fit(X[tr][:,cols],y[tr]); p=m.predict_proba(X[te][:,cols])[:,1]
        metrics[name]={"roc_auc":float(roc_auc_score(y[te],p)),"balanced_accuracy":float(balanced_accuracy_score(y[te],m.predict(X[te][:,cols])))}
    print(json.dumps({"experiment":"Ω-I-EXP-007","metrics":metrics,"rows":len(y),"train":int(tr.sum()),"test":int(te.sum())},indent=2))
if __name__=="__main__": main()
