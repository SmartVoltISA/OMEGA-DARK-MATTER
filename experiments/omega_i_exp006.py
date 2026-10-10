#!/usr/bin/env python3
"""Reproduce Ω-I-EXP-006 symmetric lineage identifiability test."""
import json
import numpy as np
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, balanced_accuracy_score

SEED=20261010; N=10000; TPRE=20; TPOST=12; D=8
def main():
    X=[]; y=[]; groups=[]
    for i in range(N):
        r=np.random.default_rng(SEED+i)
        A=np.eye(D)*.65+r.normal(0,.03,(D,D))
        eig=max(abs(np.linalg.eigvals(A))); A=A/max(1.0,float(eig)/.88)
        pre=np.zeros((TPRE,D)); pre[0]=r.normal(size=D)
        for t in range(TPRE-1):
            pre[t+1]=A@pre[t]+r.normal(scale=.3,size=D)
        x0=pre[-1].copy(); branches=[]
        for b in range(2):
            rr=np.random.default_rng(SEED+500000+i*2+b)
            z=np.zeros((TPOST,D)); z[0]=x0
            for t in range(TPOST-1):
                z[t+1]=A@z[t]+rr.normal(scale=.3,size=D)
            branches.append(z+rr.normal(scale=.2,size=z.shape))
        original=int(r.integers(0,2))
        for b,obs in enumerate(branches):
            X.append(np.concatenate([obs[-1],obs[-5:].mean(axis=0),
                                     np.mean(np.diff(obs[-5:],axis=0),axis=0),A.flatten()]))
            y.append(1 if b==original else 0); groups.append(i)
    X=np.asarray(X); y=np.asarray(y); groups=np.asarray(groups)
    tr,te=next(GroupShuffleSplit(n_splits=1,test_size=.30,random_state=SEED).split(X,y,groups))
    model=make_pipeline(StandardScaler(),LogisticRegression(C=1.0,max_iter=2000,random_state=SEED))
    model.fit(X[tr],y[tr]); pred=model.predict_proba(X[te])[:,1]
    pair_idx={}
    for j,idx in enumerate(te): pair_idx.setdefault(groups[idx],[]).append(j)
    correct=[]
    for _,ii in pair_idx.items():
        if len(ii)==2:
            correct.append(int((pred[ii[0]]>pred[ii[1]]) == (y[te][ii[0]]==1)))
    acc=float(np.mean(correct)); n=len(correct); se=(acc*(1-acc)/n)**.5
    out={"experiment":"Ω-I-EXP-006","trials":N,"samples":len(y),
         "train_samples":len(tr),"test_samples":len(te),
         "heldout_auc":float(roc_auc_score(y[te],pred)),
         "balanced_accuracy":float(balanced_accuracy_score(y[te],pred>=.5)),
         "paired_branch_choice_accuracy":acc,
         "paired_accuracy_normal_95_ci":[max(0,acc-1.96*se),min(1,acc+1.96*se)],
         "n_heldout_pairs":n,
         "interpretation":"Lineage label is independent of observations; chance-level results are expected."}
    print(json.dumps(out,indent=2))
if __name__=="__main__": main()
