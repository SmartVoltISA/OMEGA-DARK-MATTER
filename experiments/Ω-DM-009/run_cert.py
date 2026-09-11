import numpy as np
from scipy.optimize import curve_fit

rng=np.random.default_rng(20260911)
objs=[]
for k in range(24):
    n=5+(k%8)
    A=rng.uniform(.2,1.0,(n,n)); A=(A+A.T)/2; np.fill_diagonal(A,0)
    L=np.diag(A.sum(1))-A
    eig=np.linalg.eigvalsh(L)
    C=float(np.trace(L))
    r=np.array([3.,4.,5.,6.,8.,10.])
    flux=(C/(4*np.pi*r**2))*(4*np.pi*r**2)
    qhat=float(np.mean(flux/(4*np.pi*r**2)*(4*np.pi*r**2)))
    pinv=np.linalg.pinv(L+1e-9*np.eye(n))
    f=np.zeros(n); f[0]=1; f[1]=-1
    compliance=float(f@pinv@f)
    mhat=float(n/max(compliance,1e-12))
    objs.append((C,qhat,mhat,n,eig[1]))
C=np.array([x[0] for x in objs]); q=np.array([x[1] for x in objs]); m=np.array([x[2] for x in objs])
lin=np.polyfit(m,q,1); pred=np.polyval(lin,m); r2=1-np.sum((q-pred)**2)/np.sum((q-q.mean())**2)
def power(x,a,p): return a*np.maximum(x,1e-12)**p
popt,_=curve_fit(power,m,q,p0=(1,1),maxfev=10000)
logcorr=np.corrcoef(np.log(m),np.log(q))[0,1]
rng2=np.random.default_rng(20261911)
sh=[]
for k in range(10):
    perm=rng2.permutation(len(q)); sh.append(float(np.corrcoef(np.log(m),np.log(q[perm]))[0,1]))
print('objects',len(objs)); print('logcorr',logcorr); print('power_a',popt[0]); print('power_p',popt[1]); print('linear_R2',r2); print('ratio_median',np.median(q/m)); print('ratio_CV',np.std(q/m)/np.mean(q/m)); print('shuffle_mean',np.mean(sh)); print('shuffle_sd',np.std(sh))
