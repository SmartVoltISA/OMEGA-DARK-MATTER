"""Ω-DM-002 R3 — joint nonnegative L1 reconstruction, stdlib only.

Training-only model selection over the preregistered lambda grid. The hidden
W is used by the generator only and is never supplied to reconstruction.
"""
from __future__ import annotations
import json, math, random, hashlib

SEED=20260911
N=24; TRAIN_TRAJ=40; TEST_TRAJ=20; LENGTH=80
K=.05; GAMMA=.02; SIGMA=.005; EDGE_P=.12
LAMBDAS=(.1,.3,1,3,10,30,100)
MAX_ITERS=600; TOL=1e-9


def graph(n,p,seed):
    r=random.Random(seed); W=[[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if r.random()<p: W[i][j]=W[j][i]=.2+.8*r.random()
    return W

def step(x,v,W,r):
    a=[]
    for i in range(N):
        c=sum(W[i][j]*(x[i]-x[j]) for j in range(N))
        a.append(-K*c-GAMMA*v[i])
    return [x[i]+v[i] for i in range(N)], [v[i]+a[i]+r.gauss(0,SIGMA) for i in range(N)]

def trajectory(W,seed):
    r=random.Random(seed); x=[r.uniform(-1,1) for _ in range(N)]; v=[r.uniform(-.2,.2) for _ in range(N)]; out=[x[:]]
    for _ in range(LENGTH-1): x,v=step(x,v,W,r); out.append(x[:])
    return out

def design_targets(trajs):
    # Each row predicts acceleration residual for one node. Feature e=(i,j)
    # contributes -K*(x_i-x_j) to node i and +K*(x_i-x_j) to node j.
    edges=[(i,j) for i in range(N) for j in range(i+1,N)]; rows=[]; ys=[]
    for tr in trajs:
        for t in range(len(tr)-2):
            acc=[tr[t+2][i]-2*tr[t+1][i]+tr[t][i] for i in range(N)]
            for i in range(N):
                y=acc[i]+GAMMA*(tr[t+1][i]-tr[t][i])
                row=[]
                for a,b in edges:
                    d=tr[t][a]-tr[t][b]
                    row.append(-K*d if i==a else (K*d if i==b else 0.0))
                rows.append(row); ys.append(y)
    return edges,rows,ys

def cd_nonneg_l1(X,y,lam,max_iter=MAX_ITERS):
    m=len(y); p=len(X[0]); w=[0.0]*p; colnorm=[sum(r[j]*r[j] for r in X) for j in range(p)]
    residual=y[:]
    for _ in range(max_iter):
        maxchg=0.0
        for j in range(p):
            old=w[j]
            if colnorm[j]==0: continue
            # residual currently = y-Xw. Add old contribution back, then solve
            rho=sum(X[r][j]*(residual[r]+X[r][j]*old) for r in range(m))
            nw=max(0.0,(rho-lam)/colnorm[j])
            if nw!=old:
                d=nw-old; w[j]=nw
                for r in range(m): residual[r]-=X[r][j]*d
                maxchg=max(maxchg,abs(d))
        if maxchg<TOL: break
    rss=sum(z*z for z in residual)
    return w,rss

def matrix_from(edges,w):
    W=[[0.0]*N for _ in range(N)]
    for (i,j),v in zip(edges,w): W[i][j]=W[j][i]=v
    return W

def predict(x0,x1,W,h=1):
    prev=x0[:]; cur=x1[:]
    for _ in range(h):
        v=[cur[i]-prev[i] for i in range(N)]
        nxt=[]
        for i in range(N):
            c=sum(W[i][j]*(cur[i]-cur[j]) for j in range(N))
            nxt.append(cur[i]+v[i]-K*c-GAMMA*v[i])
        prev,cur=cur,nxt
    return cur

def rmse(trajs,W,h=1):
    se=c=0
    for tr in trajs:
        for t in range(1,len(tr)-h):
            pred=predict(tr[t-1],tr[t],W,h)
            for a,b in zip(pred,tr[t+h]): se+=(a-b)**2; c+=1
    return math.sqrt(se/c)

def fit_select(train):
    edges,X,y=design_targets(train); rows=[]
    for lam in LAMBDAS:
        w,rss=cd_nonneg_l1(X,y,lam)
        active=sum(v>1e-8 for v in w)
        n=len(y); bic=n*math.log(max(rss/n,1e-300))+2*active
        rows.append({"lambda":lam,"rss":rss,"active_edges":active,"bic_like":bic,"weights":w})
    best=min(rows,key=lambda z:z["bic_like"])
    W=matrix_from(edges,best["weights"])
    return best,W,[{k:v for k,v in z.items() if k!="weights"} for z in rows]

def evaluate(seed, null=False, temporal_perm=False):
    trueW=graph(N,EDGE_P,seed); gen=[[0.0]*N for _ in range(N)] if null else trueW
    train=[trajectory(gen,seed+1000+i) for i in range(TRAIN_TRAJ)]
    test=[trajectory(gen,seed+2000+i) for i in range(TEST_TRAJ)]
    if temporal_perm:
        # Preserve each trajectory's states but permute temporal order before fitting.
        train=[random.Random(seed+5000+i).sample(tr,len(tr)) for i,tr in enumerate(train)]
    best,W,grid=fit_select(train)
    return {"baseline_h1":rmse(test,[[0.0]*N for _ in range(N)],1),"selected_h1":rmse(test,W,1),"selected_h2":rmse(test,W,2),"selected_h5":rmse(test,W,5),"selected_h10":rmse(test,W,10),"lambda":best["lambda"],"active_edges":best["active_edges"],"true_edges":sum(trueW[i][j]>0 for i in range(N) for j in range(i+1,N)),"grid":grid}

def main():
    main=evaluate(SEED); null=[evaluate(SEED+100+i,null=True) for i in range(5)]; perm=[evaluate(SEED+200+i,temporal_perm=True) for i in range(5)]
    print(json.dumps({"status":"EXECUTED_REFERENCE","config":{"seed":SEED,"N":N,"train":TRAIN_TRAJ,"test":TEST_TRAJ,"length":LENGTH,"K":K,"gamma":GAMMA,"sigma":SIGMA,"edge_p":EDGE_P,"lambda_grid":LAMBDAS},"main":main,"null":null,"temporal_permutation":perm},indent=2))
if __name__=='__main__': main()
