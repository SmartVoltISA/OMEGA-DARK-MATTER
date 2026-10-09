#!/usr/bin/env python3
"""Ω-09: nonlinear domain formation vs single-well linear control.

1-D periodic field model. Requires Python 3 and NumPy.
The nonlinear double-well equation and the linear single-well control are
assumed models, not a derivation of matter from relations.
"""
import json, math
import numpy as np

def smooth_initial(N, L=80.0, amp=0.03, seed=20261009, cutoff_modes=40):
    rng = np.random.default_rng(seed)
    coeff = (rng.normal(size=cutoff_modes) + 1j*rng.normal(size=cutoff_modes))
    coeff = coeff / (np.arange(1, cutoff_modes+1)**1.2)
    x = np.arange(N)*L/N
    u = np.zeros(N)
    for m,c in enumerate(coeff, start=1):
        u += c.real*np.cos(2*np.pi*m*x/L) - c.imag*np.sin(2*np.pi*m*x/L)
    return amp*u/np.std(u)

def run(N=512, L=80., T=20., K=1., rho=1., lam=1., eta=1.,
        seed=20261009, cfl=0.2, nonlinear=True):
    dx=L/N
    c=math.sqrt(K/rho)
    dt=cfl*dx/c
    steps=round(T/dt)
    dt=T/steps
    u=smooth_initial(N,L,seed=seed)
    prev=u.copy()
    def energy(q,qd):
        grad=.5*K*np.sum((np.roll(q,-1)-q)**2/dx**2)*dx
        pot=(lam/4*np.sum((q*q-eta**2)**2)*dx) if nonlinear else .5*lam*np.sum(q*q)*dx
        kin=.5*rho*np.sum(qd*qd)*dx
        return float(grad+pot+kin)
    e0=energy(u,np.zeros_like(u))
    snaps={}
    targets={round(t/dt):t for t in (0,5,10,15,20)}
    for it in range(steps+1):
        if it in targets:
            s=np.sign(u); s[s==0]=1
            snaps[str(targets[it])] = {
                "sign_change_domain_proxy":int(np.sum(s!=np.roll(s,1))),
                "near_double_well_vacuum_fraction":float(np.mean(np.abs(np.abs(u)-eta)<0.2)),
                "rms":float(np.sqrt(np.mean(u*u))),
                "mean":float(np.mean(u))}
        if it==steps: break
        lap=(np.roll(u,-1)-2*u+np.roll(u,1))/dx**2
        if nonlinear:
            acc=(K*lap-lam*u*(u*u-eta**2))/rho
        else:
            acc=(K*lap-lam*u)/rho
        nxt=2*u-prev+dt**2*acc
        prev,u=u,nxt
    e1=energy(u,(u-prev)/dt)
    return {"N":N,"dx":dx,"dt":dt,"steps":steps,"seed":seed,
            "equation":"rho*u_tt=K*u_xx-lambda*u*(u^2-eta^2)" if nonlinear else "rho*u_tt=K*u_xx-lambda*u",
            "relative_energy_drift":(e1-e0)/e0,"snapshots":snaps}

if __name__=="__main__":
    out={"parameters":{"L":80,"T":20,"K":1,"rho":1,"lambda":1,"eta":1,
                       "amplitude":0.03,"seeded_fourier_modes":40,"cfl":0.2},
         "nonlinear_double_well_resolution_sweep":[run(N=n,nonlinear=True) for n in (256,512,1024)],
         "linear_single_well_control_resolution_sweep":[run(N=n,nonlinear=False) for n in (256,512,1024)],
         "nonlinear_seed_ensemble":[run(N=512,seed=s,nonlinear=True) for s in (20261009,20261010,20261011)],
         "caveats":[
             "Sign changes are only a domain proxy, not a particle count.",
             "The double-well potential explicitly assumes two preferred states; it is not derived from relation alone.",
             "The linear control's sign changes can occur in a tiny-amplitude oscillatory field, so sign count alone is not evidence of domain formation.",
             "The field equation does not derive physical c or establish a physical ontology."
         ]}
    print(json.dumps(out,indent=2))
