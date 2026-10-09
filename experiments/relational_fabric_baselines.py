import numpy as np

def solve(N, cfl=0.4, T=0.2, c=1.0):
    dx = 4/(N-1)
    dt = cfl*dx/c
    steps = round(T/dt)
    dt = T/steps
    x = np.linspace(-2, 2, N)
    f = lambda z: np.exp(-(z/0.12)**2)
    u0 = f(x)
    up = u0.copy()
    lap = (np.roll(u0,-1)-2*u0+np.roll(u0,1))/dx**2
    u = u0 + 0.5*(c*dt)**2*lap
    u[[0,-1]] = 0
    up[[0,-1]] = 0
    for _ in range(1, steps):
        lap = (np.roll(u,-1)-2*u+np.roll(u,1))/dx**2
        un = 2*u-up+(c*dt)**2*lap
        un[[0,-1]] = 0
        up, u = u, un
    exact = 0.5*(f(x-c*T)+f(x+c*T))
    mask = np.abs(x) < 1.5
    rmse = float(np.sqrt(np.mean((u[mask]-exact[mask])**2)))
    return dx, steps, dt, rmse, float(np.max(np.abs(u)))

def stability(cfl, N=401, steps=500):
    dx = 1/(N-1)
    dt = cfl*dx
    x = np.linspace(0,1,N)
    u0 = np.exp(-((x-0.5)/0.04)**2)
    up = u0.copy()
    lap = (np.roll(u0,-1)-2*u0+np.roll(u0,1))/dx**2
    u = u0 + 0.5*dt**2*lap
    u[[0,-1]] = 0
    up[[0,-1]] = 0
    maxamp = max(float(np.max(np.abs(up))), float(np.max(np.abs(u))))
    for i in range(1,steps):
        lap = (np.roll(u,-1)-2*u+np.roll(u,1))/dx**2
        un = 2*u-up+dt**2*lap
        un[[0,-1]] = 0
        up,u = u,un
        maxamp = max(maxamp,float(np.max(np.abs(u))))
        if not np.isfinite(maxamp) or maxamp > 1e6:
            return False,maxamp,i
    return True,maxamp,steps

if __name__ == "__main__":
    print("EXP-01 convergence")
    for n in [201,401,801,1601]:
        print(n, solve(n))
    print("EXP-02 CFL stability")
    for r in [0.25,0.5,0.9,1.0,1.05,1.2]:
        print(r, stability(r))
    print("EXP-03 conventional-chain theoretical speed, a=M=1")
    for K in [0.25,1.0,4.0]:
        print(K, (K**0.5))
