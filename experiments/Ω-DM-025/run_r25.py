"""Ω-DM-025: primitive antisymmetric local exchange.
The conservation rule is implemented as an elementary pair exchange:
Delta u_i=-J, Delta u_j=+J. No Laplacian is constructed as a primitive rule.
"""
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

N=21; C=N//2

def idx(x,y,z): return (x*N+y)*N+z

def run(seed=0, amplitude=1.0, leak=0.0):
    rng=np.random.default_rng(seed); n=N**3
    rows=[]; cols=[]; data=[]; edges=[]
    for x in range(N-1):
      for y in range(N-1):
       for z in range(N-1):
        i=idx(x,y,z)
        for dx,dy,dz in ((1,0,0),(0,1,0),(0,0,1)):
          j=idx(x+dx,y+dy,z+dz); w=float(np.exp(rng.normal(0,.25)))
          rows += [i,j,i,j]; cols += [i,j,j,i]; data += [w,w,-w,-w]
          edges.append((i,j,w))
    A=coo_matrix((data,(rows,cols)),shape=(n,n)).tocsr()
    if leak: A=A+leak*coo_matrix((np.full(n,1.0),(np.arange(n),np.arange(n))),shape=(n,n))
    b=np.zeros(n); b[idx(C,C,C)]=amplitude
    A=A.tolil()
    for x in range(N):
      for y in range(N):
       for z in range(N):
        if x in (0,N-1) or y in (0,N-1) or z in (0,N-1):
          i=idx(x,y,z); A.rows[i]=[i]; A.data[i]=[1.0]; b[i]=0.0
    u=spsolve(A.tocsr(),b)
    coords=np.indices((N,N,N)).reshape(3,-1).T; rad=np.linalg.norm(coords-C,axis=1)
    rs=np.arange(3,8); flux=[]; grad=[]
    for r in rs:
      q=0.0
      for i,j,w in edges:
        if rad[i]<r<=rad[j]: q+=w*(u[i]-u[j])
        elif rad[j]<r<=rad[i]: q+=w*(u[j]-u[i])
      m0=u[(rad>=r)&(rad<r+1)].mean(); m1=u[(rad>=r+1)&(rad<r+2)].mean()
      flux.append(q); grad.append(abs(m0-m1))
    p=-np.polyfit(np.log(rs+.5),np.log(np.array(grad)+1e-300),1)[0]
    return p,np.array(flux)

if __name__=='__main__':
  for s in range(6):
    p,q=run(s); print('conserved',s,'p=',p,'flux=',q.mean(),'CV=',q.std()/abs(q.mean()))
  for a in (.5,1,2):
    p,q=run(0,a); print('amplitude',a,'p=',p,'flux=',q.mean())
  for s in range(3):
    p,q=run(s,1,.01); print('leak',s,'p=',p,'flux=',q.mean(),'CV=',q.std()/abs(q.mean()))
