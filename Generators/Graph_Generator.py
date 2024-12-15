import networkx as nx
import random
from Generators.Solution import Solution
from Algorithms.Checkers.Prim import Prim

class Graph_Generator:

    def __init__(self, checker = None):
        if checker == None:
            self.checker = Prim()
        else:
            self.checker = checker

    def __get_best_nodes__(self, graph):
        bestNodes = []
        n = len(graph.nodes)
        greed = []
        for node in range(n):
            graph.nodes[node]['isGen'] = True
            visited, distances = self.checker.prim(graph, node)
            greed.append(
                (len(visited), sum([x for x in distances if x != float("inf")]), graph.degree(node), node,
                 visited))
            graph.nodes[node]['isGen'] = False

        vorax_list = sorted(greed, key=lambda x: (x[0], -x[1], x[2]), reverse=True)

        return list(map(lambda x:x[3],vorax_list))

    def generate_graph(self, num_node, prob_edge, max_dist, min_edge, max_edge):
        g = nx.erdos_renyi_graph(num_node, prob_edge)
        g.graph['l_max'] = max_dist
        self.fill_graph_with_data(g, min_edge, max_edge)
        return Solution(g, self.__get_best_nodes__(g))


    def fill_graph_with_data(self, graph, min_edge, max_edge):
        for (u, v) in graph.edges():
            graph.edges[u, v]['dist'] = random.randint(min_edge, max_edge)
            graph.edges[u, v]['isFail'] = False
        for node in graph.nodes():
            graph.nodes[node]['isGen'] = False

