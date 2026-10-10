#!/usr/bin/env python3
"""Ω-I-EXP-005 exploratory lineage-feature benchmark. Python + numpy + scikit-learn."""
import json
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, balanced_accuracy_score
from sklearn.model_selection import GroupShuffleSplit

SEED=20261010
N_FAMILIES=500
T=80
D=8

def build_data():
    families=[]
    for f in range(N_FAMILIES):
        r=np.random.default_rng(SEED+f)
        A=np.eye(D)*.65+r.normal(0,.035,(D,D))
        eig=max(abs(np.linalg.eigvals(A)))
        A=A/max(1.0,float(eig)/.88)
        x=np.zeros((T,D)); x[0]=r.normal(size=D)
        for t in range(T-1):
            x[t+1]=A@x[t]+r.normal(scale=.35,size=D)
        families.append((x,A))
    rows=[]; labels=[]; groups=[]
    for f,(x,A) in enumerate(families):
        r=np.random.default_rng(SEED+100000+f)
        for j in range(4):
            t=int(r.integers(20,40)); lag=int(r.integers(3,8))
            xa,xb=x[t],x[t+lag]
            ha=x[t-4:t+1].mean(axis=0); hb=x[t+lag-4:t+lag+1].mean(axis=0)
            ra=np.mean(np.diff(x[t-4:t+1],axis=0),axis=0)
            rb=np.mean(np.diff(x[t+lag-4:t+lag+1],axis=0),axis=0)
            rows.append([np.linalg.norm(xa-xb),0.0,np.linalg.norm(ha-hb),np.linalg.norm(ra-rb)])
            labels.append(1); groups.append(f)
        for j in range(4):
            t=int(r.integers(20,40)); x0=x[t].copy(); branches=[]
            for b in range(2):
                z=np.zeros((8,D)); z[0]=x0
                rr=np.random.default_rng(SEED+200000+f*100+j*2+b)
                for k in range(7):
                    z[k+1]=A@z[k]+rr.normal(scale=.35,size=D)
                branches.append(z)
            a,b=branches
            ha=a[-5:].mean(axis=0); hb=b[-5:].mean(axis=0)
            ra=np.mean(np.diff(a[-5:],axis=0),axis=0)
            rb=np.mean(np.diff(b[-5:],axis=0),axis=0)
            rows.append([np.linalg.norm(a[-1]-b[-1]),0.0,np.linalg.norm(ha-hb),np.linalg.norm(ra-rb)])
            labels.append(0); groups.append(f)
    return np.array(rows),np.array(labels),np.array(groups)

def main():
    X,y,groups=build_data()
    tr,te=next(GroupShuffleSplit(n_splits=1,test_size=.30,random_state=SEED).split(X,y,groups))
    feature_sets={"PRESENT_ONLY":[0],"ORGANIZATION":[0,1],"HISTORY_AWARE":[0,1,2,3]}
    metrics={}; preds={}
    for name,cols in feature_sets.items():
        m=make_pipeline(StandardScaler(),LogisticRegression(C=1.0,max_iter=2000,random_state=SEED))
        m.fit(X[tr][:,cols],y[tr]); p=m.predict_proba(X[te][:,cols])[:,1]; preds[name]=p
        metrics[name]={"auc":float(roc_auc_score(y[te],p)),
                       "balanced_accuracy":float(balanced_accuracy_score(y[te],p>=.5))}
    test_groups=groups[te]; unique=np.unique(test_groups)
    id_to_indices={g:np.where(test_groups==g)[0] for g in unique}
    brng=np.random.default_rng(SEED+1234); diffs=[]; hist_auc=[]; cur_auc=[]
    for _ in range(2000):
        sampled=brng.choice(unique,size=len(unique),replace=True)
        ix=np.concatenate([id_to_indices[g] for g in sampled])
        if len(np.unique(y[te][ix]))<2: continue
        ah=roc_auc_score(y[te][ix],preds["HISTORY_AWARE"][ix])
        ac=roc_auc_score(y[te][ix],preds["PRESENT_ONLY"][ix])
        hist_auc.append(ah); cur_auc.append(ac); diffs.append(ah-ac)
    perm_auc=[]
    for seed in range(100):
        py=np.random.default_rng(SEED+9000+seed).integers(0,2,size=len(tr))
        m=make_pipeline(StandardScaler(),LogisticRegression(C=1.0,max_iter=2000,random_state=SEED))
        m.fit(X[tr],py); perm_auc.append(float(roc_auc_score(y[te],m.predict_proba(X[te])[:,1])))
    result={"experiment":"Ω-I-EXP-005","status":"exploratory; not preregistered before execution",
      "n_families":N_FAMILIES,"n_pairs":len(y),"train_pairs":len(tr),"test_pairs":len(te),
      "feature_order":["current_state_distance","organization_distance","history_mean_distance","transition_signature_distance"],
      "metrics":metrics,
      "bootstrap_95_ci":{"history_auc":[float(np.quantile(hist_auc,.025)),float(np.quantile(hist_auc,.975))],
                         "present_auc":[float(np.quantile(cur_auc,.025)),float(np.quantile(cur_auc,.975))],
                         "auc_difference_history_minus_present":[float(np.quantile(diffs,.025)),float(np.quantile(diffs,.975))]},
      "shuffled_label_control_auc":{"median":float(np.median(perm_auc)),"mean":float(np.mean(perm_auc)),
                                    "percentile_2_5":float(np.quantile(perm_auc,.025)),
                                    "percentile_97_5":float(np.quantile(perm_auc,.975))},
      "feature_means":{"same_lineage":[float(v) for v in X[y==1].mean(axis=0)],
                       "independent_branches":[float(v) for v in X[y==0].mean(axis=0)]},
      "caveat":"Labels are simulator lineage metadata; history helps infer this operational label but cannot establish universal identity criteria."}
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()
