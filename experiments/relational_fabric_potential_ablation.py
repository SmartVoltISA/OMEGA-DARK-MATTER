#!/usr/bin/env python3
"""Compare spontaneous pattern formation across three scalar-field potentials.

Dimensionless 1D periodic wave equation u_tt = u_xx - dV/du.
Potentials:
  double_well: V=(u^2-1)^2/4, so u=0 is linearly unstable.
  single_well: V=u^2/2, so u=0 is stable.
  quartic_soft: V=0.025*u^4, also stable near u=0 but with no quadratic mass term.
This is a toy-model control study, not a physical model of matter.
"""
import json
import numpy as np

def run(kind, N=512, L=80.0, T=20.0, seed=20261013, modes=40, cfl=0.2):
    dx=L/N
    x=np.arange(N)*dx-L/2
    dt=cfl*dx
    steps=round(T/dt)
    dt=T/steps
    rng=np.random.default_rng(seed)
    coeff=rng.normal(size=modes)+1j*rng.normal(size=modes)
    u=np.zeros(N)
    for m,c in enumerate(coeff, start=1):
        u += c.real*np.cos(2*np.pi*m*x/L)-c.imag*np.sin(2*np.pi*m*x/L)
    u=u/np.sqrt(np.mean(u*u))*0.03
    v=np.zeros(N)
    def force(q):
        lap=(np.roll(q,-1)-2*q+np.roll(q,1))/dx**2
        if kind=="double_well": return lap-q*(q*q-1)
        if kind=="single_well": return lap-q
        if kind=="quartic_soft": return lap-0.1*q**3
        raise ValueError(kind)
    def energy(q,p):
        ux=(np.roll(q,-1)-np.roll(q,1))/(2*dx)
        if kind=="double_well": pot=0.25*(q*q-1)**2
        elif kind=="single_well": pot=0.5*q*q
        else: pot=0.025*q**4
        return float(np.sum(0.5*p*p+0.5*ux*ux+pot)*dx)
    def metrics(q):
        return {"rms":float(np.sqrt(np.mean(q*q))),
                "mean":float(np.mean(q)),
                "sign_crossings":int(np.sum(q*np.roll(q,-1)<0)),
                "near_pm1_fraction":float(np.mean(np.abs(np.abs(q)-1)<0.2)) if kind=="double_well" else None,
                "min":float(q.min()),"max":float(q.max())}
    e0=energy(u,v)
    vh=v+0.5*dt*force(u)
    snapshots={"0":{"energy":e0,**metrics(u)}}
    targets={round(t/dt):t for t in [5,10,15,20]}
    for n in range(1,steps+1):
        u=u+dt*vh
        vh=vh+dt*force(u)
        if n in targets:
            t=targets[n]
            snapshots[str(t)]={"energy":energy(u,vh),**metrics(u)}
    ef=energy(u,vh)
    return {"kind":kind,"N":N,"L":L,"T":T,"dt":dt,"steps":steps,"seed":seed,
            "initial_energy":e0,"final_energy":ef,"relative_energy_drift":(ef-e0)/e0,
            "snapshots":snapshots}

if __name__=="__main__":
    results=[run(k,N=n) for k in ("double_well","single_well","quartic_soft") for n in (256,512,1024)]
    print(json.dumps({"model_note":"Dimensionless toy model; not evidence for relational matter.","results":results},indent=2))
