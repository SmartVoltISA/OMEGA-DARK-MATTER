"""Ω-DM-002 R3 convergent executor.

Preserves the preregistered objective: minimize RSS + 2*lambda*sum(w)
subject to w >= 0, with the fixed lambda grid and training-only BIC_like.
The solver uses sufficient statistics and an exact quadratic factorization;
NNLS solves the resulting non-negative quadratic program. No standardization
or intercept is used.
"""
import json, math, random, platform, sys
import numpy as np
from scipy.optimize import nnls

SEED=20260911; N=24; TRAIN_TRAJ=40; TEST_TRAJ=20; LENGTH=80
K=.05; GAMMA=.02; SIGMA=.005; EDGE_P=.12
LAMBDAS=(.1,.3,1,3,10,30,100)
EDGES=np.array([(i,j) for i in range(N) for j in range(i+1,N)],dtype=np.int16); P=len(EDGES)
B=np.zeros((N,P))
for e,(a,b) in enumerate(EDGES): B[a,e]=-1.; B[b,e]=1.

def graph(n,p,seed):
 r=random.Random(seed); W=np.zeros((n,n))
 for i in range(n):
  for j in range(i+1,n):
   if r.random()<p: W[i,j]=W[j,i]=.2+.8*r.random()
 return W

def trajectory(W,seed):
 r=random.Random(seed); x=np.array([r.uniform(-1,1) for _ in range(N)]); v=np.array([r.uniform(-.2,.2) for _ in range(N)]); out=np.empty((LENGTH,N)); out[0]=x
 for t in range(LENGTH-1):
  c=((x[:,None]-x[None,:])*W).sum(axis=1)
  x=x+v; v=v-K*c-GAMMA*v+np.array([r.gauss(0,SIGMA) for _ in range(N)])
  out[t+1]=x
 return out

def sufficient_stats(trajs):
 D=[]; Y=[]
 for tr in trajs:
  D.append(tr[:-2,EDGES[:,0]]-tr[:-2,EDGES[:,1]])
  Y.append((tr[2:]-2*tr[1:-1]+tr[:-2])+GAMMA*(tr[1:-1]-tr[:-2]))
 D=np.vstack(D); Y=np.vstack(Y)
 G=(K*K)*(B.T@B)*(D.T@D); b=K*np.sum(D*(Y@B),axis=0); yty=float(np.sum(Y*Y))
 return G,b,yty,len(Y)*N

def fit_lambda(G,b,yty,lam):
 vals,U=np.linalg.eigh(G); keep=vals>1e-10
 A=np.sqrt(vals[keep])[:,None]*U[:,keep].T
 c=b-lam; q=(U[:,keep].T@c)/np.sqrt(vals[keep])
 w,_=nnls(A,q,maxiter=100000)
 rss=float(yty-2*w@b+w@G@w)
 grad=G@w-b+lam
 kkt=max(float(np.max(np.abs(grad[w>1e-8]))) if np.any(w>1e-8) else 0., float(np.max(np.maximum(0.,-grad[w<=1e-8]))) if np.any(w<=1e-8) else 0.)
 return w,rss,{'success':kkt<=1e-7,'kkt_residual':kkt,'iterations':0,'lipschitz':float(vals[-1])}

def fit_select(train):
 G,b,yty,n=sufficient_stats(train); out=[]
 for lam in LAMBDAS:
  w,r,info=fit_lambda(G,b,yty,lam); active=int(np.count_nonzero(w>1e-8)); bic=n*math.log(max(r/n,1e-300))+2*active
  out.append({'lambda':lam,'rss':r,'active_edges':active,'bic_like':bic,**info})
 best=min(out,key=lambda z:z['bic_like']); wbest,_,_=fit_lambda(G,b,yty,best['lambda']); W=np.zeros((N,N))
 for (a,b),v in zip(EDGES,wbest): W[a,b]=W[b,a]=v
 return best,W,sorted(out,key=lambda z:LAMBDAS.index(z['lambda']))

def rmse(trajs,W,h):
 se=0.; c=0
 for tr in trajs:
  for t in range(1,len(tr)-h):
   prev=tr[t-1]; cur=tr[t]
   for _ in range(h):
    v=cur-prev; cc=((cur[:,None]-cur[None,:])*W).sum(axis=1); nxt=cur+v-K*cc-GAMMA*v; prev,cur=cur,nxt
   d=cur-tr[t+h]; se+=float(d@d); c+=N
 return math.sqrt(se/c)

def evaluate(seed,null=False,temporal_perm=False):
 trueW=graph(N,EDGE_P,seed); gen=np.zeros((N,N)) if null else trueW
 train=[trajectory(gen,seed+1000+i) for i in range(TRAIN_TRAJ)]; test=[trajectory(gen,seed+2000+i) for i in range(TEST_TRAJ)]
 if temporal_perm:
  for i,tr in enumerate(train):
   rr=random.Random(seed+5000+i); idx=list(range(len(tr))); rr.shuffle(idx); train[i]=tr[idx]
 best,W,grid=fit_select(train); Z=np.zeros((N,N))
 return {'baseline_h1':rmse(test,Z,1),'baseline_h2':rmse(test,Z,2),'baseline_h5':rmse(test,Z,5),'baseline_h10':rmse(test,Z,10),'selected_h1':rmse(test,W,1),'selected_h2':rmse(test,W,2),'selected_h5':rmse(test,W,5),'selected_h10':rmse(test,W,10),'lambda':best['lambda'],'active_edges':best['active_edges'],'true_edges':int(np.count_nonzero(np.triu(trueW,1))),'grid':grid,'edge_precision':float(np.sum((W>1e-8)&(trueW>0))/max(np.sum(W>1e-8),1)),'edge_recall':float(np.sum((W>1e-8)&(trueW>0))/max(np.sum(trueW>0),1))}

if __name__=='__main__':
 print(json.dumps({'implementation':'run_r3_convergent.py','runtime':{'python':sys.version,'numpy':np.__version__,'scipy':__import__('scipy').__version__,'platform':platform.platform()},'main':evaluate(SEED)},indent=2))
