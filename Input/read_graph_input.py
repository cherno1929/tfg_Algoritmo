#Read input
import matplotlib.pyplot as plt
import networkx as nx

def readGraph():

    g = nx.Graph(l_max=2)

    n_node, n_edge = map(int, input().strip().split())
    for n in range(n_node):
        g.add_node(n, isFail=False, isGen=False)

    for _ in range(n_edge):
        a,b,d = map(int, input().strip().split())
        g.add_edge(a,b,dist=d,isFail=False)

    return g

