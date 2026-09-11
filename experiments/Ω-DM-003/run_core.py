"""Ω-DM-003 minimal relation-core executor.

Reconstructs the frozen R3 model deterministically, performs frozen single-edge
necessity tests, and runs training-only backward elimination under the
preregistered tau=0.01 rule for three deterministic order policies.
"""
import json, math, random, platform, sys
import numpy as np
from scipy.optimize import nnls

SEED=20260911; N=24; TRAIN=40; TEST=20; LENGTH=80
K=.05; GAMMA=.02; SIGMA=.005; EDGE_P=.12; TAU=.01
LAMBDAS=(.1,.3,1,3,10,30,100)
EDGES=np.array([(i,j) for i in range(N) for j in range(i+1,N)],int); P=len(EDGES)
B=np.zeros((N,P))
for e,(a,b) in enumerate(EDGES): B[a,e]=-1.; B[b,e]=1.

def graph(seed):
 r=random.Random(seed); W=np.zeros((N,N))
 for i in range(N):
  for j in range(i+1,N):
   if r.random()<EDGE_P: W[i,j]=W[j,i]=.2+.8*r.random()
 return W

def trajectory(W,seed):
 r=random.Random(seed); x=np.array([r.uniform(-1,1) for _ in range(N)]); v=np.array([r.uniform(-.2,.2) for _ in range(N)]); out=np.empty((LENGTH,N)); out[0]=x
 for t in range(LENGTH-1):
  c=W.sum(1)*x-W@x; x=x+v; v=v-K*c-GAMMA*v+np.array([r.gauss(0,SIGMA) for _ in range(N)]); out[t+1]=x
 return out

def stats(trs):
 D=np.vstack([tr[:-2,EDGES[:,0]]-tr[:-2,EDGES[:,1]] for tr in trs]); Y=np.vstack([(tr[2:]-2*tr[1:-1]+tr[:-2])+GAMMA*(tr[1:-1]-tr[:-2]) for tr in trs])
 G=(K*K)*(B.T@B)*(D.T@D); b=K*np.sum(D*(Y@B),axis=0); return G,b,float(np.sum(Y*Y)),len(Y)*N

def fit(G,b,yty,lam):
 vals,U=np.linalg.eigh(G); keep=vals>1e-10; A=np.sqrt(vals[keep])[:,None]*U[:,keep].T; q=(U[:,keep].T@(b-lam))/np.sqrt(vals[keep]); w,_=nnls(A,q,maxiter=100000); rss=float(yty-2*w@b+w@G@w); return w,rss

def fit_r3(trs):
 G,b,yty,n=stats(trs); best=None; grid=[]
 for lam in LAMBDAS:
  w,r=fit(G,b,yty,lam); k=int(np.count_nonzero(w>1e-8)); bic=n*math.log(max(r/n,1e-300))+2*k; row={'lambda':lam,'rss':r,'active_edges':k,'bic_like':bic}; grid.append(row)
  if best is None or bic<best['bic_like']: best={**row,'weights':w}
 W=np.zeros((N,N))
 for (a,b),v in zip(EDGES,best['weights']): W[a,b]=W[b,a]=v
 return W,best,grid

def rmse1(W,trs):
 se=0
 for tr in trs:
  x=tr[1:-1]; v=tr[1:-1]-tr[:-2]; Lx=x*W.sum(1)-x@W.T; d=x+v-K*Lx-GAMMA*v-tr[2:]; se+=float(np.sum(d*d))
 return math.sqrt(se/(len(trs)*(LENGTH-2)*N))

def rollout_rmse(W,trs,h):
 se=c=0
 for tr in trs:
  for t in range(1,LENGTH-h):
   p,q=tr[t-1],tr[t]
   for _ in range(h):
    v=q-p; q=q+v-K*(W.sum(1)*q-W@q)-GAMMA*v; p=tr[t] if False else p
   d=q-tr[t+h]; se+=float(d@d); c+=N
 return math.sqrt(se/c)

def deletion_table(W,test,active_edges):
 base=[rollout_rmse(W,test,h) for h in (1,2,5,10)]; rows=[]
 for idx,(a,b) in enumerate(active_edges):
  wd=W.copy(); wd[a,b]=wd[b,a]=0; vals=[rollout_rmse(wd,test,h) for h in (1,2,5,10)]
  rows.append({'edge_id':idx,'a':int(a),'b':int(b),'delta_h1':vals[0]-base[0],'delta_h2':vals[1]-base[1],'delta_h5':vals[2]-base[2],'delta_h10':vals[3]-base[3],'provisionally_necessary':bool(vals[0]-base[0]>TAU)})
 return base,rows

def backward_core(W,train,active_edges,policy):
 C=W.copy(); current=rmse1(C,train); log=[]
 while True:
  cand=[]
  for idx,(a,b) in enumerate(active_edges):
   if C[a,b]<=1e-8: continue
   wd=C.copy(); wd[a,b]=wd[b,a]=0; loss=rmse1(wd,train)
   if loss<=current+TAU: cand.append((idx,loss))
  if not cand: break
  if policy=='ascending_edge_id': idx,loss=min(cand,key=lambda z:z[0])
  elif policy=='descending_edge_id': idx,loss=max(cand,key=lambda z:z[0])
  else: idx,loss=min(cand,key=lambda z:z[1])
  a,b=active_edges[idx]; C[a,b]=C[b,a]=0; log.append({'edge_id':idx,'a':int(a),'b':int(b),'train_rmse_after':loss,'delta_train':loss-current}); current=loss
 return C,log

if __name__=='__main__':
 trueW=graph(SEED); train=[trajectory(trueW,SEED+1000+i) for i in range(TRAIN)]; test=[trajectory(trueW,SEED+2000+i) for i in range(TEST)]
 W,best,grid=fit_r3(train); active=EDGES[np.flatnonzero(W[np.triu_indices(N,1)]>1e-8)]
 base,table=deletion_table(W,test,active)
 cores={}
 for policy in ('ascending_edge_id','descending_edge_id','smallest_training_loss_increase'):
  C,log=backward_core(W,train,active,policy); cores[policy]={'size':int(np.count_nonzero(np.triu(C,1)>1e-8)),'steps':len(log),'test_rmse':[rollout_rmse(C,test,h) for h in (1,2,5,10)],'train_rmse':rmse1(C,train),'log':log}
 out={'status':'EXECUTED','config':{'seed':SEED,'N':N,'train':TRAIN,'test':TEST,'length':LENGTH,'K':K,'gamma':GAMMA,'sigma':SIGMA,'edge_p':EDGE_P,'tau':TAU,'lambda_grid':LAMBDAS},'runtime':{'python':sys.version,'numpy':np.__version__,'scipy':__import__('scipy').__version__,'platform':platform.platform()},'r3_selected':{'lambda':best['lambda'],'active_edges':best['active_edges']},'frozen_full_test_rmse':base,'frozen_deletion':table,'cores':cores,'acceptance':{'reduced_core_obtained':all(v['size']<best['active_edges'] for v in cores.values()),'all_frozen_edges_necessary':any(r['provisionally_necessary'] for r in table),'core_beats_baseline':{p:all(v['test_rmse'][i]<base[i] for i in range(4)) for p,v in cores.items()}}}
 print(json.dumps(out,indent=2))
