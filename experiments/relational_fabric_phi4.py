#!/usr/bin/env python3
"""Exploratory continuous-field tests for Ω relational-fabric research.

This is a 1-D nonlinear Klein-Gordon / phi^4 field model. It has no particle
nodes in its state representation, but it DOES assume a continuum field and
a local differential equation. It therefore tests a candidate continuous-field
analogue, not the ontological claim that relations alone constitute matter.
Requires Python 3 and NumPy.
"""
import math
import json
import numpy as np

def phi4_kink(N=801, L=40.0, T=8.0, cfl=0.35,
              K=1.0, rho=1.0, lam=1.0, eta=1.0):
    """Evolve a static kink under u_tt=(K/rho)u_xx-(lam/rho)u(u^2-eta^2)."""
    dx = L / (N - 1)
    c_characteristic = math.sqrt(K / rho)
    dt = cfl * dx / c_characteristic
    steps = round(T / dt)
    dt = T / steps
    x = np.linspace(-L / 2, L / 2, N)
    width = math.sqrt(2 * K / (lam * eta**2))
    u = eta * np.tanh(x / width)
    lap = (np.roll(u, -1) - 2*u + np.roll(u, 1)) / dx**2
    acc = (K * lap - lam*u*(u*u - eta**2)) / rho
    prev = u + 0.5 * dt**2 * acc
    prev[[0, -1]] = u[[0, -1]]

    def energy(q, qdot):
        grad = 0.5*K*np.sum(np.diff(q)**2/dx**2)*dx
        pot = lam/4*np.sum((q*q-eta**2)**2)*dx
        kin = 0.5*rho*np.sum(qdot*qdot)*dx
        return float(grad + pot + kin)

    e0 = energy(u, np.zeros_like(u))
    for _ in range(1, steps):
        lap = (np.roll(u, -1) - 2*u + np.roll(u, 1)) / dx**2
        acc = (K * lap - lam*u*(u*u - eta**2)) / rho
        nxt = 2*u - prev + dt**2*acc
        nxt[[0, -1]] = u[[0, -1]]
        prev, u = u, nxt
    qdot = (u - prev) / dt
    e1 = energy(u, qdot)
    crossings = np.where(u[:-1]*u[1:] <= 0)[0]
    if len(crossings):
        j = crossings[np.argmin(np.abs(x[crossings]))]
        center = float(x[j] - u[j]*(x[j+1]-x[j])/(u[j+1]-u[j]))
    else:
        center = None
    return {
        "N": N, "dx": dx, "dt": dt, "steps": steps,
        "c_characteristic": c_characteristic,
        "initial_energy": e0, "final_energy": e1,
        "relative_energy_drift": (e1-e0)/e0,
        "kink_center": center,
        "min_u": float(np.min(u)), "max_u": float(np.max(u))
    }

def pulse_arrival_test(N=1601, L=40.0, T=10.0, K=1.0, rho=1.0,
                       lam=1.0, eta=1.0, amp=0.05, sigma=0.3, cfl=0.4):
    """Threshold arrival times for a Gaussian perturbation around the +eta vacuum.

    This measures a threshold-dependent pulse feature, NOT the exact causal front.
    """
    dx = L/(N-1)
    c_char = math.sqrt(K/rho)
    dt = cfl*dx/c_char
    steps = round(T/dt)
    dt = T/steps
    x = np.linspace(-L/2, L/2, N)
    u = eta + amp*np.exp(-(x/sigma)**2)
    prev = u.copy()  # zero initial velocity
    locations = [3.0, 5.0, 7.0]
    arrivals = {str(xx): None for xx in locations}
    threshold = amp*0.03
    for it in range(1, steps+1):
        lap = (np.roll(u,-1)-2*u+np.roll(u,1))/dx**2
        acc = (K*lap-lam*u*(u*u-eta**2))/rho
        nxt = 2*u-prev+dt**2*acc
        nxt[[0,-1]] = eta
        prev, u = u, nxt
        t = it*dt
        for xx in locations:
            key = str(xx)
            if arrivals[key] is None:
                j = int(np.argmin(np.abs(x-xx)))
                if abs(u[j]-eta) > threshold:
                    arrivals[key] = t
    valid = [(float(k), v) for k,v in arrivals.items() if v is not None]
    speed = None
    if len(valid) >= 2:
        speed = float(np.polyfit([t for _,t in valid],
                                 [xx for xx,_ in valid], 1)[0])
    return {"N":N, "dx":dx, "dt":dt, "c_characteristic":c_char,
            "threshold":threshold, "arrivals":arrivals,
            "fitted_threshold_feature_speed":speed,
            "points_used":len(valid)}

def main():
    out = {
        "model": "1-D phi^4 nonlinear Klein-Gordon field",
        "equation": "rho*u_tt = K*u_xx - lambda*u*(u^2-eta^2)",
        "parameters_default": {"K":1.0,"rho":1.0,"lambda":1.0,"eta":1.0},
        "kink_resolution_sweep": [phi4_kink(N=n) for n in [201,401,801,1601]],
        "pulse_speed_parameter_sweep": [
            pulse_arrival_test(K=K,rho=rho)
            for K,rho in [(0.25,1.0),(1.0,1.0),(4.0,1.0),(1.0,4.0)]
        ],
        "interpretation": [
            "A stable localized kink exists in this chosen nonlinear field model.",
            "Its characteristic wave speed is sqrt(K/rho), derived from the equation's coefficients.",
            "The model assumes a continuum field and local dynamics; it does not derive the existence of that field from relation alone.",
            "The characteristic speed is not the physical speed of light unless independently calibrated and validated.",
            "Threshold arrival speed is not an exact causal-front speed; it depends on threshold, dispersion, and observation locations."
        ]
    }
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
