class Solution:

    def __init__(self, graph, best_nodes, prob_random = None, prob_destruction = None):
        # Graph from networkx
        self.graph = graph
        # Best nodes based on greedy criteria
        self.best_nodes = best_nodes
        # First Solution
        self.first_solution = None
        # Solution after first optimization
        self.first_local_solution = None
        # Final Solution
        self.best_solution = None
        # Time taken to solve the problem
        self.time_to_solve = None
        # % to activate node, when random algorithm
        self.random_node_activation = prob_random
        # % to destroy solution, when greedy algotithm
        self.greedy_destruction = prob_destruction

    # Lets the solution to transform into json
    def to_dict(self):
        return {
            'graph' : self.__graph_to_dict__(),
            'solution' : self.best_solution,
            'best_nodes' : self.best_nodes,
            'time_to_solve' : self.time_to_solve
        }

    # Transforms networkx graph into json
    def __graph_to_dict__(self):
        node_data = list(map(lambda x:self.graph.nodes[x], self.graph.nodes))
        link_data = []
        for x, y in self.graph.edges:
            link_data.append(self.graph.get_edge_data(x, y))

        return {
            'nodes' : node_data,
            'links' : link_data
        }
