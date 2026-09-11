"""Ω-DM-031 runner.
Coordinate-free local rewiring; measurement uses graph distance only.
"""
import numpy as np
import networkx as nx


def make_graph(n, seed, kind):
    rng=np.random.default_rng(seed)
    if kind=='er':
        while True:
            G=nx.gnp_random_graph(n,0.045,seed=int(rng.integers(1<<30)))
            if nx.is_connected(G): break
    elif kind=='regular':
        G=nx.random_regular_graph(6,n,seed=int(rng.integers(1<<30)))
    else:
        G=nx.watts_strogatz_graph(n,6,0.15,seed=int(rng.integers(1<<30)))
        if not nx.is_connected(G):
            G=nx.connected_watts_strogatz_graph(n,6,0.15,seed=int(rng.integers(1<<30)))
    return G


def relax(G, steps=60, radius=2):
    G=G.copy(); n=len(G)
    for _ in range(steps):
        nodes=list(G.nodes())
        deg=dict(G.degree())
        common={}
        # local candidate edges at distance two
        adds=[]
        for i in nodes:
            for j in nx.single_source_shortest_path_length(G,i,cutoff=2):
                if i>=j or G.has_edge(i,j) or j==i: continue
                c=len(set(G.neighbors(i)) & set(G.neighbors(j)))
                if c>=2: adds.append((c,i,j))
        adds.sort(reverse=True)
        dels=[]
        for i,j in G.edges():
            c=len(set(G.neighbors(i)) & set(G.neighbors(j)))
            if c==0: dels.append((deg[i]+deg[j],i,j))
        # bounded local rewiring; degree target emerges from regularization, not dimension
        changed=0
        for _,i,j in adds[:max(1,n//8)]:
            if not G.has_edge(i,j) and deg[i]<8 and deg[j]<8:
                G.add_edge(i,j); deg[i]+=1; deg[j]+=1; changed+=1
        for _,i,j in dels[:max(1,n//8)]:
            if G.has_edge(i,j) and G.degree(i)>3 and G.degree(j)>3:
                G.remove_edge(i,j); changed+=1
        if changed==0: break
    return G


def shell_dimension(G, sources):
    vals=[]
    for s in sources:
        d=nx.single_source_shortest_path_length(G,s)
        c=np.bincount(list(d.values()))
        r=np.arange(len(c))
        mask=(r>=2)&(r<=min(12,len(c)-1))&(c>0)
        if mask.sum()>=4:
            p=np.polyfit(np.log(r[mask]),np.log(c[mask]),1)[0]
            vals.append(float(p))
    return np.mean(vals),np.std(vals,ddof=1) if len(vals)>1 else 0.0


def run():
    rows=[]
    for kind in ['er','regular','smallworld']:
        for seed in range(6):
            G=relax(make_graph(500,seed,kind))
            rng=np.random.default_rng(10000+seed)
            src=rng.choice(list(G.nodes()),8,replace=False)
            p,sd=shell_dimension(G,src)
            rows.append((kind,seed,p,sd,G.number_of_edges(),np.mean([d for _,d in G.degree()]),np.std([d for _,d in G.degree()])))
    for r in rows: print(r)
    return rows

if __name__=='__main__': run()
