import numpy as np
from scipy.optimize import minimize


def relax_kink(N, k=1.0):
    grid = np.arange(N, dtype=float)
    center = (N - 1) / 2
    q0 = np.tanh((grid - center) / np.sqrt(2.0 * k))

    def energy(z):
        q = np.r_[-1.0, z, 1.0]
        return 0.5 * k * np.sum(np.diff(q) ** 2) + 0.25 * np.sum((q*q - 1.0) ** 2)

    res = minimize(energy, q0[1:-1], method='L-BFGS-B',
                   options={'maxiter': 3000, 'ftol': 1e-14})
    return np.r_[-1.0, res.x, 1.0]


def effective_metric(q, Xs):
    grid = np.arange(len(q), dtype=float)
    center = (len(q) - 1) / 2
    profiles = np.array([
        np.interp(grid - X + center, grid, q, left=-1.0, right=1.0)
        for X in Xs
    ])
    dq_dX = np.gradient(profiles, Xs, axis=0)
    M = np.sum(dq_dX * dq_dX, axis=1)
    return float(np.mean(M)), float(np.std(M))


def direct_center_metric(q, dx=0.1):
    """Independent central finite-difference check of sum_i (dq_i/dX)^2."""
    grid = np.arange(len(q), dtype=float)
    center = (len(q) - 1) / 2
    qp = np.interp(grid - (center + dx) + center, grid, q, left=-1.0, right=1.0)
    qm = np.interp(grid - (center - dx) + center, grid, q, left=-1.0, right=1.0)
    d = (qp - qm) / (2.0 * dx)
    return float(np.sum(d*d))


def main():
    rows = []
    for N in (101, 201, 401, 801):
        for k in (0.5, 1.0, 2.0):
            q = relax_kink(N, k)
            center = (N - 1) / 2
            Xs = np.linspace(center - 10.0, center + 10.0, 401)
            M, sd = effective_metric(q, Xs)
            Mc = direct_center_metric(q)
            rows.append((N, k, M, sd, Mc))
            print(f'N={N} k={k} M_E={M:.12f} SD={sd:.12f} M_center={Mc:.12f}')

    print('\nSUMMARY')
    print('runs=', len(rows))
    print('min_M_E=', min(r[2] for r in rows))
    print('max_M_E=', max(r[2] for r in rows))
    print('max_grid_spread=', max(r[2] for r in rows if r[0] == 101) - min(r[2] for r in rows if r[0] == 101))


if __name__ == '__main__':
    main()
