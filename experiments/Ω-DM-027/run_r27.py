"""Ω-DM-027 audit runner.
No gravity law is inserted. This runner evaluates the geometric minimality
identity behind the conserved-flux p=d-1 scaling used in Ω-DM-021/024.
"""
import numpy as np

def shell_measure(r, d):
    # S_d(r) is the surface measure scaling of an isotropic d-dimensional sphere.
    # Constants cancel in ratios, so only r**(d-1) is required.
    return r ** (d - 1)

def run():
    rows=[]
    for d in (1,2,3):
        r=np.linspace(1.0,100.0,1000)
        Q=np.ones_like(r)
        G=Q/shell_measure(r,d)
        p=-np.polyfit(np.log(r),np.log(G),1)[0]
        rows.append((d,p,d-1))
    # Leakage control: Q(r) decreases exponentially, so the response is not
    # a pure power law. This demonstrates why conservation is essential.
    r=np.linspace(1.0,20.0,500)
    Q=np.exp(-0.08*r)
    G=Q/r**2
    p=-np.polyfit(np.log(r),np.log(G),1)[0]
    return rows,p

if __name__ == '__main__':
    rows,p=run()
    for row in rows: print(row)
    print('leaky_local_log_slope_fit=',p)
