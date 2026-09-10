"""Ω-DM-002 — hidden relation reconstruction, stdlib only.

The generating topology is never supplied to the inference routine. Training
trajectories expose x(t) only. Candidate edges are scored from observed
accelerations using a fixed least-squares statistic, then selected by a fixed
sparsity threshold chosen before test evaluation.
"""
from __future__ import annotations
import json, math, random, hashlib

SEED = 20260911
N = 24
TRAIN_TRAJ = 40
TEST_TRAJ = 20
LENGTH = 80
K = 0.05
GAMMA = 0.02
SIGMA = 0.005
EDGE_P = 0.12
TRUE_W_MIN = 0.2
TRUE_W_MAX = 1.0
LAMBDA = 1.0
SPARSITY_THRESHOLD = 0.002


def matrix_hash(W):
    raw = json.dumps(W, separators=(",", ":"), sort_keys=True).encode()
    return hashlib.sha256(raw).hexdigest()


def graph(n, p, seed):
    rng = random.Random(seed)
    W = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < p:
                W[i][j] = W[j][i] = TRUE_W_MIN + (TRUE_W_MAX-TRUE_W_MIN)*rng.random()
    return W


def permuted_graph(W, seed):
    rng = random.Random(seed)
    n = len(W)
    pairs = [(i,j) for i in range(n) for j in range(i+1,n) if W[i][j] > 0]
    weights = [W[i][j] for i,j in pairs]
    rng.shuffle(weights)
    rng.shuffle(pairs)
    out = [[0.0]*n for _ in range(n)]
    for (i,j),w in zip(pairs,weights): out[i][j]=out[j][i]=w
    return out


def step(x,v,W,rng):
    n=len(x); a=[0.0]*n
    for i in range(n):
        coupling=sum(W[i][j]*(x[i]-x[j]) for j in range(n))
        a[i]=-K*coupling-GAMMA*v[i]
    x2=[x[i]+v[i] for i in range(n)]
    v2=[v[i]+a[i]+rng.gauss(0,SIGMA) for i in range(n)]
    return x2,v2


def trajectory(W,seed):
    rng=random.Random(seed); x=[rng.uniform(-1,1) for _ in W]
    v=[rng.uniform(-.2,.2) for _ in W]; out=[x[:]]
    for _ in range(LENGTH-1): x,v=step(x,v,W,rng); out.append(x[:])
    return out


def observed_acceleration(tr):
    # From x(t+1)=x(t)+v(t), estimate v(t)=x(t+1)-x(t).
    # Then a(t)=v(t+1)-v(t).  Noise is retained as part of observations.
    return [[tr[t+2][i]-2*tr[t+1][i]+tr[t][i]
             for i in range(N)] for t in range(len(tr)-2)]


def edge_score(trajs,i,j):
    # For the true law, acceleration contains -K*W_ij*(x_i-x_j).
    # Score is normalized covariance between observed acceleration residual
    # and pairwise difference. Other edges contribute correlated nuisance.
    num=den=0.0
    for tr in trajs:
        acc=observed_acceleration(tr)
        for t,a in enumerate(acc):
            d=tr[t][i]-tr[t][j]
            num += (-a[i])*d
            den += d*d
    return num/den if den else 0.0


def reconstruct(trajs):
    W=[[0.0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            # Fixed pre-registered threshold; no test data involved.
            s=edge_score(trajs,i,j)
            w=max(0.0,s/K)
            if w >= SPARSITY_THRESHOLD:
                W[i][j]=W[j][i]=w
    return W


def predict_step(x_prev,x_now,W):
    # v(t)=x(t)-x(t-1); x(t+1)=x(t)+v(t)+a(t)
    v=[x_now[i]-x_prev[i] for i in range(N)]
    out=[]
    for i in range(N):
        coupling=sum(W[i][j]*(x_now[i]-x_now[j]) for j in range(N))
        a=-K*coupling-GAMMA*v[i]
        out.append(x_now[i]+v[i]+a)
    return out


def rollout_rmse(trajs,W):
    se=0.0; c=0
    for tr in trajs:
        for t in range(1,len(tr)-1):
            pred=predict_step(tr[t-1],tr[t],W)
            for a,b in zip(pred,tr[t+1]): se+=(a-b)**2; c+=1
    return math.sqrt(se/max(c,1))


def zero_graph(): return [[0.0]*N for _ in range(N)]


def evaluate(seed=SEED, null=False, permute=False):
    W=graph(N,EDGE_P,seed)
    genW=zero_graph() if null else W
    train=[trajectory(genW,seed+1000+i) for i in range(TRAIN_TRAJ)]
    test=[trajectory(genW,seed+2000+i) for i in range(TEST_TRAJ)]
    candidate=reconstruct(train)
    if permute:
        candidate=permuted_graph(candidate,seed+9000)
    return {"baseline_rmse":rollout_rmse(test,zero_graph()),
            "relation_rmse":rollout_rmse(test,candidate),
            "true_edges":len([(i,j) for i in range(N) for j in range(i+1,N) if W[i][j]>0]),
            "recovered_edges":len([(i,j) for i in range(N) for j in range(i+1,N) if candidate[i][j]>0]),
            "true_hash":matrix_hash(genW),
            "candidate_hash":matrix_hash(candidate)}


def main():
    main_run=evaluate(SEED)
    null_runs=[evaluate(SEED+100+k,null=True) for k in range(20)]
    perm_runs=[evaluate(SEED+200+k,permute=True) for k in range(20)]
    out={"status":"EXECUTABLE_RECONSTRUCTION",
         "config":{"seed":SEED,"N":N,"train_trajectories":TRAIN_TRAJ,
                   "test_trajectories":TEST_TRAJ,"length":LENGTH,"K":K,
                   "gamma":GAMMA,"sigma":SIGMA,"edge_probability":EDGE_P,
                   "sparsity_threshold":SPARSITY_THRESHOLD},
         "main":main_run,"null":null_runs,"permutation":perm_runs}
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
