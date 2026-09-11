"""Ω-DM-026 local runner.
Random 3D point cloud + Delaunay local graph + nonlinear antisymmetric exchange.
"""
import numpy as np
from scipy.spatial import Delaunay
from scipy.optimize import minimize


def run(seed, N=1000, alpha=2.0, source_amp=5.0):
    rng = np.random.default_rng(seed)
    pts = []
    while len(pts) < N:
        z = rng.uniform(-1, 1, (N * 2, 3))
        z = z[np.sum(z*z, axis=1) <= 1]
        pts.extend(z.tolist())
    pts = np.array(pts[:N])
    tri = Delaunay(pts)
    edges = set()
    for s in tri.simplices:
        for a, b in ((s[0],s[1]),(s[0],s[2]),(s[0],s[3]),
                     (s[1],s[2]),(s[1],s[3]),(s[2],s[3])):
            if a > b: a, b = b, a
            edges.add((a,b))
    edges = np.array(list(edges), dtype=int)
    d = np.linalg.norm(pts[edges[:,0]] - pts[edges[:,1]], axis=1)
    w = 1.0 / (d + 0.03)
    r = np.linalg.norm(pts, axis=1)
    boundary = r > 0.90
    free = np.where(~boundary)[0]
    pos = {int(v): i for i, v in enumerate(free)}
    e0, e1 = edges.T
    fi = np.array([pos.get(int(v), -1) for v in e0])
    fj = np.array([pos.get(int(v), -1) for v in e1])
    src = int(np.argmin(r))

    def fg(u):
        dd = np.zeros(len(edges))
        both = (fi >= 0) & (fj >= 0)
        onei = (fi >= 0) & (fj < 0)
        onej = (fi < 0) & (fj >= 0)
        dd[both] = u[fi[both]] - u[fj[both]]
        dd[onei] = u[fi[onei]]
        dd[onej] = -u[fj[onej]]
        z = alpha * dd
        E = np.sum(w * (np.logaddexp(z, -z) - np.log(2.0)) / alpha**2)
        q = w * np.tanh(z) / alpha
        g = np.zeros(len(u))
        np.add.at(g, fi[fi >= 0], q[fi >= 0])
        np.add.at(g, fj[fj >= 0], -q[fj >= 0])
        g[pos[src]] -= source_amp
        return E - source_amp*u[pos[src]], g

    res = minimize(lambda u: fg(u), np.zeros(len(free)), jac=True,
                   method='L-BFGS-B', options={'maxiter':2500,'ftol':1e-12,'gtol':1e-8})
    u = np.zeros(N); u[free] = res.x

    bins = np.linspace(0.10, 0.82, 18)
    rb, ub = [], []
    for a, b in zip(bins[:-1], bins[1:]):
        m = (r >= a) & (r < b) & (~boundary)
        if m.sum() >= 10:
            rb.append(r[m].mean()); ub.append(u[m].mean())
    rb, ub = np.array(rb), np.array(ub)
    m = (ub > 0) & (rb > 0.18) & (rb < 0.75)
    qexp = -np.polyfit(np.log(rb[m]), np.log(ub[m]), 1)[0]
    p = qexp + 1.0

    flux, radii = [], []
    for R in np.linspace(0.20, 0.75, 8):
        ra, rb2 = r[e0], r[e1]
        mask = ((ra <= R) & (rb2 > R)) | ((rb2 <= R) & (ra > R))
        if not mask.any(): continue
        jj = w[mask] * np.tanh(alpha*(u[e0[mask]]-u[e1[mask]])) / alpha
        sign = np.where(ra[mask] <= R, 1.0, -1.0)
        flux.append(np.sum(jj*sign)); radii.append(R)
    flux = np.array(flux)
    return {'seed':seed,'N':N,'edges':len(edges),'alpha':alpha,'source_amp':source_amp,
            'success':bool(res.success),'max_grad':float(np.max(np.abs(res.jac))),
            'q':float(qexp),'p':float(p),'flux_mean':float(np.mean(flux)),
            'flux_cv':float(np.std(flux)/abs(np.mean(flux))), 'fluxes':flux.tolist()}

if __name__ == '__main__':
    for amp in (5.0, 50.0, 200.0):
        rows = [run(s, source_amp=amp) for s in range(6)]
        ps = [x['p'] for x in rows]
        print('amp', amp, 'p', ps, 'mean', np.mean(ps), 'sd', np.std(ps, ddof=1))
        print('flux_cv', [x['flux_cv'] for x in rows])
