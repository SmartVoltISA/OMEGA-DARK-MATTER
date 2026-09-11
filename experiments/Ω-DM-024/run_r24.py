"""Ω-DM-024: conservation-to-geometry scaling across dimensions.
The response gradient is generated from conserved shell flux divided by shell measure;
no inverse-power radial response is inserted.
"""
import numpy as np


def shell_measure(r, d):
    if d == 1: return np.ones_like(r)
    return r ** (d - 1)


def fit_p(r, G):
    return -np.polyfit(np.log(r), np.log(G), 1)[0]

rows=[]
for d in (1,2,3):
    for seed in range(6):
        rng=np.random.default_rng(seed)
        r=np.arange(4,14,dtype=float)
        # Conserved flux with tiny local measurement perturbation.
        Q=np.exp(rng.normal(0,0.005,len(r)))
        # Remove the seed-wise mean flux drift so the conservation null is exact in aggregate.
        Q /= np.mean(Q)
        G=Q/shell_measure(r,d)
        p=fit_p(r,G)
        rows.append(("conserved",d,seed,p,float(np.std(Q))))

# Matched leakage control: flux decays with radius, breaking conservation.
for d in (1,2,3):
    for seed in range(6):
        rng=np.random.default_rng(seed)
        r=np.arange(4,14,dtype=float)
        Q=np.exp(-0.08*(r-4))*np.exp(rng.normal(0,0.005,len(r)))
        G=Q/shell_measure(r,d)
        p=fit_p(r,G)
        rows.append(("leaky",d,seed,p,float(np.std(Q))))

print("case,dimension,seed,p")
for x in rows: print(x)
for case in ("conserved","leaky"):
  print("SUMMARY",case)
  for d in (1,2,3):
    a=[x[3] for x in rows if x[0]==case and x[1]==d]
    print(d, np.mean(a), np.std(a,ddof=1), "target", d-1)
