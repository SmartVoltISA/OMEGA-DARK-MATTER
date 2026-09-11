"""Ω-DM-021 — Conservation of Relational Flux
Minimal reproducible runner. Requires numpy and scipy.
"""
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.stats import linregress


def run(N=31, mu=0.0):
    n = N**3
    I = lambda i,j,k: (i*N+j)*N+k
    boundary=np.zeros(n,bool)
    for i in range(N):
      for j in range(N):
       for k in range(N):
        boundary[I(i,j,k)] = i in (0,N-1) or j in (0,N-1) or k in (0,N-1)
    interior=np.where(~boundary)[0]
    mp=-np.ones(n,int); mp[interior]=np.arange(len(interior))
    rows=[]; cols=[]; vals=[]
    for i in range(1,N-1):
      for j in range(1,N-1):
       for k in range(1,N-1):
        g=I(i,j,k); q=mp[g]
        rows.append(q); cols.append(q); vals.append(6+mu)
        for di,dj,dk in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
          h=I(i+di,j+dj,k+dk)
          if mp[h]>=0:
            rows.append(q); cols.append(mp[h]); vals.append(-1)
    A=sp.csr_matrix((vals,(rows,cols)),shape=(len(interior),)*2)
    b=np.zeros(len(interior)); b[mp[I(N//2,N//2,N//2)]]=1
    x=spla.spsolve(A,b); full=np.zeros(n); full[interior]=x
    xyz=np.indices((N,N,N)).reshape(3,-1).T
    c=np.array([N//2]*3); rd=np.linalg.norm(xyz-c,axis=1)
    shell=np.array([(r,full[(rd>=r-.5)&(rd<r+.5)].mean()) for r in range(2,N//2-3)])
    rg=shell[1:-1,0]
    grad=-(shell[2:,1]-shell[:-2,1])/2
    fit=(rg>=4)&(rg<=10)&(grad>0)
    p=-linregress(np.log(rg[fit]),np.log(grad[fit])).slope
    edges=[]
    for i in range(N-1):
      for j in range(N):
       for k in range(N): edges.append((I(i,j,k),I(i+1,j,k)))
    for i in range(N):
      for j in range(N-1):
       for k in range(N): edges.append((I(i,j,k),I(i,j+1,k)))
    for i in range(N):
      for j in range(N):
       for k in range(N-1): edges.append((I(i,j,k),I(i,j,k+1)))
    flux=[]
    for R in range(3,N//2-3):
      q=0.0
      for g,h in edges:
        if (rd[g]<R and rd[h]>=R) or (rd[h]<R and rd[g]>=R):
          inn=g if rd[g]<R else h; out=h if rd[g]<R else g
          q += full[inn]-full[out]
      flux.append(q)
    flux=np.array(flux)
    return p, flux

if __name__ == '__main__':
    for mu in (0.0,0.02):
        p,flux=run(31,mu)
        cv=np.std(flux[1:-1])/abs(np.mean(flux[1:-1]))
        print(f'mu={mu:g} p={p:.6f} flux_mean={np.mean(flux):.6f} flux_CV={cv:.6g}')
        print('flux=',np.array2string(flux,precision=6))
