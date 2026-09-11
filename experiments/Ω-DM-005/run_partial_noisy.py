"""Ω-DM-005 certified local runner.

Generator: Ω-DM-004 nonlinear bounded coupling.
Observation: 18/24 nodes, Gaussian measurement noise sigma_obs=0.01.
Inference: R3 symmetric non-negative reconstruction on observed nodes only.
"""
import math, random, json, platform, sys
import numpy as np
from scipy.optimize import nnls

N=24; OBS_N=18; TRAIN=40; TEST=20; LENGTH=80
K=.02; GAMMA=.02; SIGMA=.003; EDGE_P=.12; OBS_NOISE=.01
LAMBDAS=(.1,.3,1,3,10,30,100)
HORIZONS=(1,2,5,10)

def graph(seed):
    r=random.Random(seed); W=np.zeros((N,N))
    for i in range(N):
        for j in range(i+1,N):
            if r.random()<EDGE_P: W[i,j]=W[j,i]=.2+.8*r.random()
    return W

def trajectory(W,seed):
    r=random.Random(seed)
    x=np.array([r.uniform(-1,1) for _ in range(N)])
    v=np.array([r.uniform(-.2,.2) for _ in range(N)])
    out=np.empty((LENGTH,N)); out[0]=x
    for t in range(LENGTH-1):
        c=((x[:,None]-x[None,:])*W).sum(axis=1)
        x=x+v
        v=v-K*c-GAMMA*v+np.array([r.gauss(0,SIGMA) for _ in range(N)])
        out[t+1]=x
    return out

def fit_observed(train,obs):
    pairs=np.array([(a,b) for ii,a in enumerate(obs) for b in obs[ii+1:]],dtype=int)
    pos={int(a):i for i,a in enumerate(obs)}
    D=[]; Y=[]
    for tr in train:
        z=tr[:,obs]
        ia=np.array([pos[int(a)] for a,b in pairs]); ib=np.array([pos[int(b)] for a,b in pairs])
        D.append(z[:-2,ia]-z[:-2,ib])
        Y.append((z[2:]-2*z[1:-1]+z[:-2])+GAMMA*(z[1:-1]-z[:-2]))
    D=np.vstack(D); Y=np.vstack(Y); m=len(obs); p=len(pairs)
    B=np.zeros((m,p))
    for e,(a,b) in enumerate(pairs): B[pos[int(a)],e]=-1.; B[pos[int(b)],e]=1.
    G=(K*K)*(B.T@B)*(D.T@D); b=K*np.sum(D*(Y@B),axis=0)
    yty=float(np.sum(Y*Y)); n=Y.shape[0]*m
    vals,U=np.linalg.eigh(G); keep=vals>1e-10
    A=np.sqrt(vals[keep])[:,None]*U[:,keep].T
    results=[]
    for lam in LAMBDAS:
        q=(U[:,keep].T@(b-lam))/np.sqrt(vals[keep])
        w,_=nnls(A,q,maxiter=100000)
        rss=yty-2*w@b+w@G@w; active=int(np.count_nonzero(w>1e-8))
        bic=n*np.log(max(rss/n,1e-300))+2*active
        results.append((bic,lam,w,rss))
    _,lam,w,_=min(results,key=lambda z:z[0])
    W=np.zeros((N,N))
    for (a,bv),v in zip(pairs,w): W[a,bv]=W[bv,a]=v
    return W,lam,int(np.count_nonzero(w>1e-8))

def rmse(test,W,obs,h):
    Wobs=W[np.ix_(obs,obs)]; se=0.; count=0
    for tr in test:
        z=tr[:,obs]
        for t in range(1,len(z)-h):
            prev=z[t-1].copy(); cur=z[t].copy()
            for _ in range(h):
                vel=cur-prev; cc=((cur[:,None]-cur[None,:])*Wobs).sum(axis=1)
                nxt=cur+vel-K*cc-GAMMA*vel; prev,cur=cur,nxt
            d=cur-z[t+h]; se+=float(d@d); count+=len(obs)
    return math.sqrt(se/count)

def evaluate(seed,null=False,perm=False):
    trueW=np.zeros((N,N)) if null else graph(seed)
    train=[trajectory(trueW,seed+1000+i) for i in range(TRAIN)]
    test=[trajectory(trueW,seed+2000+i) for i in range(TEST)]
    rr=random.Random(seed+70000); obs=np.array(sorted(rr.sample(range(N),OBS_N)))
    noisy=[]
    for tr in train:
        noisy.append(tr+np.array([[rr.gauss(0,OBS_NOISE) for _ in range(N)] for _ in range(LENGTH)]))
    if perm:
        for i in range(len(noisy)):
            rp=random.Random(seed+5000+i); idx=list(range(LENGTH)); rp.shuffle(idx); noisy[i]=noisy[i][idx]
    W,lam,active=fit_observed(noisy,obs)
    vals=[]
    for h in HORIZONS:
        b=rmse(test,np.zeros((N,N)),obs,h); s=rmse(test,W,obs,h)
        vals.append({'h':h,'baseline_rmse':b,'selected_rmse':s,'relative_improvement':1-s/b})
    return {'seed':seed,'observed_nodes':obs.tolist(),'lambda':lam,'active_edges':active,'metrics':vals}

if __name__=='__main__':
    main=[evaluate(s) for s in range(20260911,20260931)]
    null=[evaluate(s,null=True) for s in range(20300911,20300921)]
    perm=[evaluate(s,perm=True) for s in range(20400911,20400921)]
    print(json.dumps({'runtime':{'python':sys.version,'numpy':np.__version__,'scipy':__import__('scipy').__version__,'platform':platform.platform()},'main':main,'null':null,'permutation':perm},indent=2))
