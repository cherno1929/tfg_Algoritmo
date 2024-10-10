#Show data of graphs
import matplotlib.pyplot as plt
import networkx as nx

def show_Graph(g):
    pos = nx.spring_layout(g)
    node_colors = ['red' if g.nodes[node]['isGen'] else 'pink' for node in g.nodes()]
    nx.draw(g, pos, with_labels=True, node_color = node_colors)
    edge_labels = {(u, v): f"{attr['dist']:.2f}" for u, v, attr in g.edges(data=True)}
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
    plt.show()