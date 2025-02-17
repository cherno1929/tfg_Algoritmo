import copy

import networkx as nx
import random
from Algorithm.Generators.Solution import Solution
from Algorithm.Algorithms.Checkers.Prim import Prim

class Graph_Generator:

    def __init__(self, checker = None):
        if checker == None:
            self.checker = Prim()
        else:
            self.checker = checker

    def __get_best_nodes__(self, graph):
        n = len(graph.nodes)
        greed = []
        # Get nodes visited, grade and distances of all nodes if they were regenerators
        for node in range(n):
            graph.nodes[node]['isGen'] = True
            # Get data of nodes and saving em
            visited, distances = self.checker.prim(graph, node)
            greed.append(
                (len(visited), sum([x for x in distances if x != float("inf")]), graph.degree(node), node,
                 visited))
            graph.nodes[node]['isGen'] = False

        # Sort nodes based on greed criteria
        vorax_list = sorted(greed, key=lambda x: (x[0], -x[1], x[2]), reverse=True)

        # Return list of nodes
        return list(map(lambda x:x[3],vorax_list))

    def generate_graph(self, num_node, prob_edge, max_dist, min_edge, max_edge):
        # Create a graph based on Erdos-Renyi
        g = nx.erdos_renyi_graph(num_node, prob_edge)
        g.graph['l_max'] = max_dist
        self.fill_graph_with_data(g, min_edge, max_edge)
        return Solution(g, self.__get_best_nodes__(g))


    def fill_graph_with_data(self, graph, min_edge, max_edge):
        # Data of edges
        for (u, v) in graph.edges():
            # Distance
            graph.edges[u, v]['dist'] = random.randint(min_edge, max_edge)
            # If its working
            graph.edges[u, v]['isFail'] = False
            # Nodes of edge
            graph.edges[u, v]['source'] = u
            graph.edges[u, v]['target'] = v
        for node in graph.nodes():
            # If its a regenerator
            graph.nodes[node]['isGen'] = False
            graph.nodes[node]['id'] = node

    def transform_to_graph(self, data):
        extracted_nodes = list(map(lambda x : int(x['id']), data['node']))
        extracted_links = list(map(lambda x : (int(x['source']['id']), int(x['target']['id'])), data['link']))
        g = nx.Graph()
        g.add_nodes_from(extracted_nodes)
        g.add_edges_from(extracted_links)
        g.graph['l_max'] = int(data['max_dist'])
        for node in data['node']:
            if bool(node['isGen']):
                g.nodes[int(node['id'])]['isGen'] = True
            else:
                g.nodes[int(node['id'])]['isGen'] = False
        for link in data['link']:
            source = int(link['source']['id'])
            target = int(link['target']['id'])
            g.edges[source, target]['dist'] = int(link['distance'])
            g.edges[source, target]['isFail'] = False
            g.edges[source, target]['source'] = source
            g.edges[source, target]['target'] = target
        return Solution(g, self.__get_best_nodes__(copy.deepcopy(g)))