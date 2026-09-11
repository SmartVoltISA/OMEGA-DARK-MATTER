import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def run(N=31, seed=0):
    rng = np.random.default_rng(seed)
    c = N // 2
    idx = lambda x, y, z: (x * N + y) * N + z
    n = N**3
    A = lil_matrix((n, n))
    src = np.zeros(n)

    traits = np.exp(rng.normal(0, 0.7, (N, N, N)))
    edges = []
    for x in range(N):
        for y in range(N):
            for z in range(N):
                if x + 1 < N:
                    edges.append(((x, y, z), (x + 1, y, z)))
                if y + 1 < N:
                    edges.append(((x, y, z), (x, y + 1, z)))
                if z + 1 < N:
                    edges.append(((x, y, z), (x, y, z + 1)))

    for a, b in edges:
        wa, wb = traits[a], traits[b]
        w = np.sqrt(wa * wb) * (1 + 0.35 * np.sin(wa - wb))
        w = max(w, 0.05)
        ia, ib = idx(*a), idx(*b)
        A[ia, ia] += w
        A[ib, ib] += w
        A[ia, ib] -= w
        A[ib, ia] -= w

    boundary = []
    for x in range(N):
        for y in range(N):
            for z in range(N):
                if x in (0, N - 1) or y in (0, N - 1) or z in (0, N - 1):
                    boundary.append(idx(x, y, z))
    for i in boundary:
        A.rows[i] = [i]
        A.data[i] = [1.0]

    src[idx(c, c, c)] = 1.0
    u = spsolve(A.tocsr(), src)

    coords = np.indices((N, N, N))
    r = np.sqrt((coords[0] - c)**2 + (coords[1] - c)**2 + (coords[2] - c)**2)
    shell = []
    for rr in range(2, 13):
        mask = (r >= rr - 0.5) & (r < rr + 0.5)
        shell.append((rr, float(u[mask.ravel()].mean())))

    rs = np.array([a for a, _ in shell])
    us = np.array([b for _, b in shell])
    gradient = -np.gradient(us, rs)
    fitmask = (rs >= 3) & (rs <= 11) & (gradient > 0)
    p = -np.polyfit(np.log(rs[fitmask]), np.log(gradient[fitmask]), 1)[0]
    return p


if __name__ == '__main__':
    values = [run(seed=s) for s in range(6)]
    print('exponents:', ', '.join(f'{v:.9f}' for v in values))
    print(f'mean={np.mean(values):.9f}')
    print(f'std={np.std(values, ddof=1):.9f}')
