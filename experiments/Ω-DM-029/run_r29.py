"""Ω-DM-029: recover shell dimension from relations only."""
import numpy as np
from collections import deque

def build(n=101):
    def node(i,j,k): return (i*n+j)*n+k
    adj=[[] for _ in range(n**3)]
    for i in range(n):
      for j in range(n):
       for k in range(n):
        a=node(i,j,k)
        for di,dj,dk in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
         ii,jj,kk=i+di,j+dj,k+dk
         if 0<=ii<n and 0<=jj<n and 0<=kk<n: adj[a].append(node(ii,jj,kk))
    return adj

def run(seed,n=101):
    adj0=build(n); N=n**3
    rng=np.random.default_rng(seed); perm=rng.permutation(N); inv=np.empty(N,int); inv[perm]=np.arange(N)
    adj=[[] for _ in range(N)]
    for a in range(N):
        aa=inv[a]
        adj[aa]=[inv[b] for b in adj0[a]]
    src=inv[(n//2*n+n//2)*n+n//2]
    dist=np.full(N,-1,np.int16); dist[src]=0; q=deque([src])
    while q:
        a=q.popleft()
        for b in adj[a]:
            if dist[b]<0: dist[b]=dist[a]+1; q.append(b)
    r=np.arange(5,30)
    counts=np.array([(dist==x).sum() for x in r],dtype=float)
    p=np.polyfit(np.log(r),np.log(counts),1)[0]
    return p

if __name__=='__main__':
    vals=[run(s) for s in range(6)]
    print(vals)
    print('mean',np.mean(vals),'sd',np.std(vals,ddof=1))
