from Algorithms.Checkers.Prim import Prim

class Solution:

    def __init__(self, graph, best_nodes):
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

