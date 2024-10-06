import networkx as nx
import random

n = 10 #Number of nodes
m = 3  #Number of edges

def generate_Barabasi_Albert_Graph():
    g = nx.barabasi_albert_graph(n, m)
    g.graph['l_max'] = 8
    for (u, v) in g.edges():
        g.edges[u, v]['dist'] = random.uniform(1, 10)
        g.edges[u, v]['isFail'] = False
    for node in g.nodes():
        g.nodes[node]['isFail'] = False
        g.nodes[node]['isGen'] = False
    return g