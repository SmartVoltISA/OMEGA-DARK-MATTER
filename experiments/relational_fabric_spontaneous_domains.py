#!/usr/bin/env python3
"""Spontaneous-domain test for the Ω relational-fabric candidate field.

Exploratory 1-D phi^4 continuum model. It starts from small random noise near
u=0 rather than a pre-seeded kink and tests whether domains near the two
potential minima and localized domain walls develop. This does not prove that
real matter is a relational fabric; the scalar field and PDE are assumed.
Requires Python 3 and NumPy.
"""
import json
import math
import numpy as np

def run(N=1024, L=80.0, T=20.0, K=1.0, rho=1.0,
        lam=1.0, eta=1.0, amplitude=0.03, seed=20261009, cfl=0.3):
    dx = L/N
    c_char = math.sqrt(K/rho)
    dt = cfl*dx/c_char
    steps = round(T/dt)
    dt = T/steps
    rng = np.random.default_rng(seed)
    u = amplitude*rng.normal(size=N)  # no seeded object/kink
    prev = u.copy()                    # zero initial velocity

    def energy(q, qdot):
        grad = 0.5*K*np.sum((np.roll(q,-1)-q)**2/dx**2)*dx
        pot = lam/4*np.sum((q*q-eta**2)**2)*dx
        kin = 0.5*rho*np.sum(qdot*qdot)*dx
        return float(grad+pot+kin)

    e0 = energy(u, np.zeros_like(u))
    for _ in range(1, steps+1):
        lap = (np.roll(u,-1)-2*u+np.roll(u,1))/dx**2
        acc = (K*lap-lam*u*(u*u-eta**2))/rho
        nxt = 2*u-prev+dt**2*acc
        prev,u = u,nxt
    qdot = (u-prev)/dt
    e1 = energy(u,qdot)
    signs = np.sign(u)
    signs[signs == 0] = 1
    walls = int(np.sum(signs != np.roll(signs,1)))  # periodic domain
    return {
        "N":N,"L":L,"T":T,"dx":dx,"dt":dt,"steps":steps,
        "K":K,"rho":rho,"lambda":lam,"eta":eta,
        "seed":seed,"initial_noise_amplitude":amplitude,
        "characteristic_speed_sqrt_K_over_rho":c_char,
        "initial_energy":e0,"final_energy":e1,
        "relative_energy_drift":(e1-e0)/e0,
        "periodic_sign_changes_domain_wall_proxy":walls,
        "fraction_near_vacuum_abs_abs_u_minus_eta_lt_0_2":
            float(np.mean(np.abs(np.abs(u)-eta)<0.2)),
        "min_u":float(np.min(u)),"max_u":float(np.max(u)),
        "mean_u":float(np.mean(u))
    }

if __name__ == "__main__":
    print(json.dumps({
        "model":"rho*u_tt = K*u_xx - lambda*u*(u^2-eta^2)",
        "runs":[run(seed=s) for s in [20261009,20261010,20261011]]
    }, indent=2))
