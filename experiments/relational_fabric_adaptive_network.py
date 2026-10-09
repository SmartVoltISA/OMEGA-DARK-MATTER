#!/usr/bin/env python3
"""Adaptive relational coupling test without a double-well potential."""
import json
import numpy as np

def run(seed=20261014, n=64, steps=5000, dt=0.01, eta=0.3, decay=0.3,
        mu=0.1, noise=0.03, adaptive=True, sigma=0.01):
    rng=np.random.default_rng(seed)
    A=np.zeros((n,n),float)
    for i in range(n):
        A[i,(i+1)%n]=A[(i+1)%n,i]=1
        A[i,(i+2)%n]=A[(i+2)%n,i]=1
    for _ in range(n*2):
        i,j=rng.integers(0,n,size=2)
        if i!=j: A[i,j]=A[j,i]=1
    np.fill_diagonal(A,0)
    mask=np.triu(A,1).astype(bool)
    W=A*0.05
    x=rng.normal(0,0.01,n)
    snapshots={}
    targets={0,100,500,1000,2500,4999}
    def metrics():
        w=W[mask]
        products=np.abs(x[:,None]*x[None,:])[A.astype(bool)]
        weights=W[A.astype(bool)]
        corr=float(np.corrcoef(products,weights)[0,1]) if np.std(products)>1e-12 and np.std(weights)>1e-12 else None
        return {"state_rms":float(np.sqrt(np.mean(x*x))),
                "state_std":float(np.std(x)),
                "mean_abs_edge_difference":float(np.mean(np.abs(x[:,None]-x[None,:])[A.astype(bool)])),
                "weight_mean":float(w.mean()),"weight_std":float(w.std()),
                "fraction_zero_weights":float(np.mean(w<1e-5)),
                "fraction_saturated_weights":float(np.mean(w>0.499)),
                "abs_coproduct_weight_correlation":corr}
    for t in range(steps):
        if t in targets: snapshots[str(t)]=metrics()
        deg=A.sum(axis=1)
        flow=(W*(x[None,:]-x[:,None])).sum(axis=1)/(deg+1e-9)
        xnew=x+dt*(-mu*x+flow+noise*rng.normal(size=n))
        if adaptive:
            coactivity=np.tanh((x[:,None]*x[None,:])/(sigma*sigma))
            W=np.clip(W+dt*(eta*coactivity-decay*(W-0.05)),0,0.5)*A
            np.fill_diagonal(W,0)
        x=xnew
    snapshots[str(steps)]=metrics()
    return {"seed":seed,"adaptive":adaptive,"snapshots":snapshots}

if __name__=="__main__":
    print(json.dumps([run(seed=s,adaptive=a) for a in (True,False)
                      for s in (20261014,20261015,20261016)],indent=2))
