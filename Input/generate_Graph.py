import networkx as nx
import random

n = 200 #Number of nodes
m = 7 #Number of edges per node

def generate_Barabasi_Albert_Graph():
    # Create graph
    g = nx.barabasi_albert_graph(n, m)
    # Assign maximum distance travel
    g.graph['l_max'] = 8
    # Give attributes to every link and node
    for (u, v) in g.edges():
        g.edges[u, v]['dist'] = random.randint(1, 6)
        g.edges[u, v]['isFail'] = False
    for node in g.nodes():
        g.nodes[node]['isGen'] = False
    return g