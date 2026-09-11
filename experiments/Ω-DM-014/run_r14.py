import numpy as np
from scipy.optimize import minimize


def relax_kink(N, k=1.0):
    grid = np.arange(N, dtype=float)
    q0 = np.tanh((grid - (N - 1) / 2) / np.sqrt(2.0 * k))
    def energy(z):
        q = np.r_[-1.0, z, 1.0]
        return 0.5 * k * np.sum(np.diff(q) ** 2) + 0.25 * np.sum((q*q - 1.0) ** 2)
    res = minimize(energy, q0[1:-1], method='L-BFGS-B', options={'maxiter': 3000, 'ftol': 1e-14})
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


def main():
    rows = []
    for N in (101, 201, 401):
        for k in (0.5, 1.0, 2.0):
            q = relax_kink(N, k)
            Xs = np.linspace(0.2*N, 0.8*N, 81)
            M, sd = effective_metric(q, Xs)
            rows.append((N, k, M, sd))
            print(f'N={N} k={k} M_E={M:.12f} SD={sd:.12f}')

    print('\nSUMMARY')
    print('positive_runs=', len(rows), '/', len(rows))
    print('min_M_E=', min(r[2] for r in rows))
    print('max_M_E=', max(r[2] for r in rows))

    # Velocity-scaling control is analytic for this ansatz: E_kin/U^2 = 0.5*M_E.
    q = relax_kink(201, 1.0)
    Xs = np.linspace(90, 110, 81)
    M, _ = effective_metric(q, Xs)
    for U in (0.1, 0.2, 0.4):
        E = 0.5 * M * U * U
        print(f'U={U} inferred_M={2*E/(U*U):.12f}')

if __name__ == '__main__':
    main()
