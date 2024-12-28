#Show data of graphs
import matplotlib.pyplot as plt
import networkx as nx

def getInputOfGraph(g):
    print(f"{len(g.nodes)} {len(g.edges)}")
    for x,y in g.edges:
        print(f"{x} {y} {g.get_edge_data(x, y)['dist']}")
    print([nodo for nodo in g.nodes if g.nodes[nodo]['isGen']])

def show_Graph(g,getInp):
    pos = nx.spring_layout(g)
    node_colors = ['red' if g.nodes[node]['isGen'] else 'pink' for node in g.nodes()]
    nx.draw(g, pos, with_labels=True, node_color = node_colors)
    edge_labels = {(u, v): f"{attr['dist']:.2f}" for u, v, attr in g.edges(data=True)}
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
    plt.show()
    if getInp:
        getInputOfGraph(g)