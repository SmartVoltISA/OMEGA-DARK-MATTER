"""Ω-DM-023 deterministic runner.
Directed local relational medium; balanced versus deliberately unbalanced controls.
No radial inverse-square kernel is used.
"""
import numpy as np
from scipy.sparse import lil_matrix, csr_matrix
from scipy.sparse.linalg import spsolve

N = 31
C = N // 2
seeds = range(6)
source_amplitudes = (0.5, 1.0, 2.0)


def idx(x,y,z): return (x*N + y)*N + z


def build(seed, balanced=True):
    rng = np.random.default_rng(seed)
    n = N**3
    # Positive directed local capacities.
    raw = {}
    for x in range(N):
      for y in range(N):
       for z in range(N):
        i = idx(x,y,z)
        if x==0 or y==0 or z==0 or x==N-1 or y==N-1 or z==N-1: continue
        for dx,dy,dz in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
          j = idx(x+dx,y+dy,z+dz)
          raw[(i,j)] = float(np.exp(rng.normal(0,0.35)))
    if balanced:
        # Sinkhorn-like local balancing is approximated globally on the directed graph.
        # Repeated row/column scaling preserves locality and positivity.
        for _ in range(80):
            rows = np.ones(n); cols = np.ones(n)
            for (i,j),w in raw.items(): rows[i]+=w; cols[j]+=w
            for k,(i,j) in enumerate(list(raw.keys())):
                raw[(i,j)] /= np.sqrt(rows[i]*cols[j])
    else:
        # Deliberately break balance with independent node gain factors.
        gain = np.exp(rng.normal(0,0.35,n))
        for key in list(raw): raw[key] *= gain[key[0]]
    A = lil_matrix((n,n))
    for (i,j),w in raw.items():
        A[i,i] += w; A[i,j] -= w
    A = csr_matrix(A)
    return A, raw


def run(seed, balanced, amp):
    A, raw = build(seed, balanced)
    b = np.zeros(N**3); b[idx(C,C,C)] = amp
    # Pin boundary by replacing boundary equations with u=0.
    A = A.tolil()
    for x in range(N):
      for y in range(N):
       for z in range(N):
        if x in (0,N-1) or y in (0,N-1) or z in (0,N-1):
          i=idx(x,y,z); A.rows[i]=[i]; A.data[i]=[1.0]; b[i]=0.0
    u=spsolve(A.tocsr(), b)
    flux=[]; grad=[]
    radii=range(4,14)
    for r in radii:
        q=0.0; vals=[]
        # Shell flux: sum directed currents crossing outward radial shell.
        for (i,j),w in raw.items():
            xi,yi,zi=np.unravel_index(i,(N,N,N)); xj,yj,zj=np.unravel_index(j,(N,N,N))
            ri=np.sqrt((xi-C)**2+(yi-C)**2+(zi-C)**2)
            rj=np.sqrt((xj-C)**2+(yj-C)**2+(zj-C)**2)
            if ri < r and rj >= r:
                q += w*(u[i]-u[j])
        # Shell means of u and finite radial gradient between adjacent shells.
        mask=[]
        for x in range(N):
         for y in range(N):
          for z in range(N):
           rr=np.sqrt((x-C)**2+(y-C)**2+(z-C)**2)
           if r <= rr < r+1: mask.append(u[idx(x,y,z)])
        m0=np.mean(mask)
        mask2=[]
        for x in range(N):
         for y in range(N):
          for z in range(N):
           rr=np.sqrt((x-C)**2+(y-C)**2+(z-C)**2)
           if r+1 <= rr < r+2: mask2.append(u[idx(x,y,z)])
        m1=np.mean(mask2)
        grad.append(abs(m0-m1)); flux.append(q)
    x=np.log(np.array(list(radii))+0.5); y=np.log(np.array(grad)+1e-300)
    p=-np.polyfit(x,y,1)[0]
    return p, np.array(flux), u

rows=[]
for balanced in (True,False):
  for seed in seeds:
    p,f,_=run(seed,balanced,1.0)
    rows.append((balanced,seed,p,float(np.mean(f)),float(np.std(f)/(abs(np.mean(f))+1e-300))))
print('balanced,seed,p,mean_flux,CV')
for row in rows: print(row)
print('source amplitude scaling:')
for amp in source_amplitudes:
  p,f,_=run(0,True,amp); print(amp,p,float(np.mean(f)))
