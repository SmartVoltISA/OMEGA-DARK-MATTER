#!/usr/bin/env python3
"""Reproducible toy tests: kink perturbation persistence and kink-antikink approach/collision.

Model: u_tt = u_xx - u (u^2 - 1), in dimensionless units.
This is a phi^4 scalar-field toy model, not a derived model of physical matter.
"""
import json
import numpy as np

def energy_fixed(u, v, dx):
    ux = np.diff(u) / dx
    return float(np.sum(0.5 * ux**2) * dx
                 + np.sum(0.25 * (u**2 - 1)**2) * dx
                 + 0.5 * np.sum(v[1:-1]**2) * dx)

def kink_perturbation(N=1024, L=80.0, T=30.0, seed=20261012,
                      amplitude=0.01, velocity_amplitude=0.01, cfl=0.2):
    dx = L / N
    x = np.linspace(-L/2, L/2, N, endpoint=False)
    dt = cfl * dx
    steps = int(round(T / dt))
    dt = T / steps
    rng = np.random.default_rng(seed)
    a = np.sqrt(2.0)
    base = np.tanh(x / a)
    bump = np.exp(-(x / 3.0)**2)
    u = base + amplitude * bump * rng.normal(size=N)
    v = velocity_amplitude * bump * rng.normal(size=N)
    u[0], u[-1], v[0], v[-1] = -1.0, 1.0, 0.0, 0.0

    def center(field):
        ids = np.where(field[:-1] * field[1:] <= 0)[0]
        if not len(ids):
            return None
        i = ids[np.argmin(np.abs(x[ids]))]
        return float(x[i] - field[i] * dx / (field[i+1] - field[i] + 1e-30))

    def acceleration(field):
        acc = np.zeros(N)
        acc[1:-1] = ((field[2:] - 2*field[1:-1] + field[:-2]) / dx**2
                     - field[1:-1] * (field[1:-1]**2 - 1))
        return acc

    e0 = energy_fixed(u, v, dx)
    vh = v + 0.5 * dt * acceleration(u)
    targets = {round(steps*f): round(T*f, 6) for f in (0.1, 0.25, 0.5, 0.75, 1.0)}
    snapshots = {}
    for n in range(1, steps+1):
        un = u.copy()
        un[1:-1] = u[1:-1] + dt * vh[1:-1]
        un[0], un[-1] = -1.0, 1.0
        vh[1:-1] += dt * acceleration(un)[1:-1]
        u = un
        if n in targets:
            t = targets[n]
            snapshots[str(t)] = {
                "center": center(u),
                "energy": energy_fixed(u, vh, dx),
                "rms_difference_from_unperturbed_kink": float(np.sqrt(np.mean((u-base)**2)))
            }
    ef = energy_fixed(u, vh, dx)
    return {
        "test": "perturbed_single_kink_fixed_boundaries",
        "N": N, "L": L, "T": T, "dt": dt, "steps": steps, "seed": seed,
        "initial_energy": e0, "final_energy": ef,
        "relative_energy_drift": (ef-e0)/e0,
        "initial_kink_center": 0.0, "final_kink_center": center(u),
        "snapshots": snapshots
    }

def kink_antikink_collision(N=1024, L=80.0, T=50.0, x0=8.0,
                            inward_speed=0.2, cfl=0.2):
    dx = L/N
    x = np.linspace(-L/2, L/2, N, endpoint=False)
    dt = cfl*dx
    steps = int(round(T/dt))
    dt = T/steps
    a = np.sqrt(2.0)
    f = np.tanh((x+x0)/a)
    g = np.tanh((x-x0)/a)
    u = f*g
    fp = (1/a) / np.cosh((x+x0)/a)**2
    gp = (1/a) / np.cosh((x-x0)/a)**2
    v = -inward_speed*fp*g + inward_speed*f*gp

    def energy_periodic(field, vel):
        ux = (np.roll(field, -1)-np.roll(field, 1))/(2*dx)
        density = 0.5*vel**2 + 0.5*ux**2 + 0.25*(field**2-1)**2
        return float(np.sum(density)*dx)

    def wall_positions(field):
        ids = np.where(field*np.roll(field, -1) < 0)[0]
        walls = []
        for i in ids:
            x1 = x[i]
            x2 = x[(i+1) % N] + (L if i == N-1 else 0)
            z = x1 - field[i]*(x2-x1)/(np.roll(field, -1)[i]-field[i])
            if z >= L/2:
                z -= L
            walls.append(round(float(z), 5))
        return sorted(walls)

    e0 = energy_periodic(u, v)
    acc = (np.roll(u, -1)-2*u+np.roll(u, 1))/dx**2-u*(u*u-1)
    vh = v+0.5*dt*acc
    targets = (0, 10, 20, 30, 35, 40, 45, 50)
    snapshots = {"0": {"walls": wall_positions(u), "energy": e0,
                       "center_value": float(u[N//2])}}
    target_steps = {round(t/dt): t for t in targets if t > 0}
    for n in range(1, steps+1):
        u = u+dt*vh
        acc = (np.roll(u, -1)-2*u+np.roll(u, 1))/dx**2-u*(u*u-1)
        vh = vh+dt*acc
        if n in target_steps:
            t = target_steps[n]
            snapshots[str(t)] = {"walls": wall_positions(u),
                                 "energy": energy_periodic(u, vh),
                                 "center_value": float(u[N//2])}
    ef = energy_periodic(u, vh)
    return {
        "test": "periodic_kink_antikink_inward_motion",
        "N": N, "L": L, "T": T, "initial_wall_centers": [-x0, x0],
        "initial_inward_speed": inward_speed, "dt": dt, "steps": steps,
        "initial_energy": e0, "final_energy": ef,
        "relative_energy_drift": (ef-e0)/e0,
        "snapshots": snapshots,
        "measurement_warning": "Zero-crossing count is only a proxy; during collision the field can transiently have no zero crossings."
    }

if __name__ == "__main__":
    print(json.dumps({
        "model": "dimensionless phi^4 scalar field; not a physical-matter derivation",
        "kink_perturbation": kink_perturbation(),
        "kink_antikink_collision": kink_antikink_collision()
    }, indent=2))
