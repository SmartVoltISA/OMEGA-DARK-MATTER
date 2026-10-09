#!/usr/bin/env python3
"""Ω-10 follow-up: phi^4 collision convergence and speed scan.

Dimensionless equation: u_tt = u_xx - u*(u^2 - 1).
Toy scalar-field model with an explicit double-well potential.
"""
import json
import numpy as np

def run_pair(N=512, L=80.0, T=50.0, x0=8.0, speed=0.2, cfl=0.1):
    dx=L/N; x=np.arange(N)*dx-L/2; dt=cfl*dx
    steps=round(T/dt); dt=T/steps; a=np.sqrt(2.0)
    f,g=np.tanh((x+x0)/a),np.tanh((x-x0)/a); u=f*g
    fp=(1/a)/np.cosh((x+x0)/a)**2; gp=(1/a)/np.cosh((x-x0)/a)**2
    v=-speed*fp*g+speed*f*gp
    def acc(q): return (np.roll(q,-1)-2*q+np.roll(q,1))/dx**2-q*(q*q-1)
    def energy(q,p):
        grad=(np.roll(q,-1)-q)/dx
        return float(dx*np.sum(.5*p*p+.5*grad*grad+.25*(q*q-1)**2))
    def walls(q):
        ids=np.where(q*np.roll(q,-1)<0)[0]; out=[]
        for i in ids:
            j=(i+1)%N; x1=x[i]; x2=x[j]+(L if j==0 else 0)
            z=x1-q[i]*(x2-x1)/(q[j]-q[i]); out.append(float(((z+L/2)%L)-L/2))
        return sorted(out)
    e0=energy(u,v); a0=acc(u)
    targets=[0,10,20,25,30,32,34,35,36,38,40,45,50]
    target_steps={round(t/dt):t for t in targets if t>0 and t<=T}
    snaps={"0":{"walls":walls(u),"energy":e0,"center":float(u[np.argmin(abs(x))]),
        "umin":float(u.min()),"umax":float(u.max())}}
    for n in range(1,steps+1):
        un=u+dt*v+.5*dt*dt*a0; an=acc(un); vn=v+.5*dt*(a0+an)
        u,v,a0=un,vn,an
        if n in target_steps:
            t=target_steps[n]; snaps[str(t)]={"walls":walls(u),"energy":energy(u,v),
                "center":float(u[np.argmin(abs(x))]),"umin":float(u.min()),"umax":float(u.max())}
    ef=energy(u,v)
    return {"N":N,"L":L,"T":T,"x0":x0,"inward_speed":speed,"cfl":cfl,"dx":dx,
        "dt":dt,"steps":steps,"initial_energy":e0,"final_energy":ef,
        "relative_energy_drift":(ef-e0)/e0,"snapshots":snaps}

def speed_scan(N=512,L=80.0,x0=8.0,speed=.2,cfl=.1):
    T=2*x0/speed+8; dx=L/N; x=np.arange(N)*dx-L/2
    dt=cfl*dx; steps=round(T/dt); dt=T/steps; a=np.sqrt(2.)
    f,g=np.tanh((x+x0)/a),np.tanh((x-x0)/a); u=f*g
    fp=(1/a)/np.cosh((x+x0)/a)**2; gp=(1/a)/np.cosh((x-x0)/a)**2
    v=-speed*fp*g+speed*f*gp
    def acc(q): return (np.roll(q,-1)-2*q+np.roll(q,1))/dx**2-q*(q*q-1)
    def energy(q,p):
        gr=(np.roll(q,-1)-q)/dx
        return float(dx*np.sum(.5*p*p+.5*gr*gr+.25*(q*q-1)**2))
    def count(q): return int(np.count_nonzero(q*np.roll(q,-1)<0))
    e0=energy(u,v); a0=acc(u); rows=[]; stride=max(1,round(.25/dt))
    for n in range(1,steps+1):
        un=u+dt*v+.5*dt*dt*a0; an=acc(un); v=v+.5*dt*(a0+an); u=un; a0=an
        if n%stride==0: rows.append((n*dt,float(u[np.argmin(abs(x))]),count(u),energy(u,v)))
    arr=np.array(rows); no=arr[:,2]==0; times=arr[no,0]; ef=energy(u,v)
    return {"N":N,"L":L,"x0":x0,"speed":speed,"T":T,"dt":dt,"steps":steps,
        "initial_energy":e0,"final_energy":ef,"relative_energy_drift":(ef-e0)/e0,
        "min_center":float(arr[:,1].min()),"max_center":float(arr[:,1].max()),
        "first_sample_no_walls":float(times[0]) if len(times) else None,
        "last_sample_no_walls":float(times[-1]) if len(times) else None,
        "wall_count_at_final":count(u)}

if __name__ == "__main__":
    sweep=[run_pair(N=n,cfl=c) for n in (512,1024) for c in (.2,.1,.05)]
    scan=[speed_scan(speed=s) for s in (.1,.2,.3)]
    print(json.dumps({"model":"dimensionless phi^4 toy model",
        "resolution_timestep_sweep":sweep,"inward_speed_scan":scan},indent=2))
