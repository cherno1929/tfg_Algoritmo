#Show data of graphs
import matplotlib.pyplot as plt
import networkx as nx

def show_Graph(g):
    nx.draw(g, with_labels=True)
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()
    plt.show()