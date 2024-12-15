from Algorithms.Checkers.Prim import Prim

class Solution:

    def __init__(self, graph, best_nodes):
        self.graph = graph
        self.best_nodes = best_nodes
        self.first_solution = None
        self.first_local_solution = None
        self.best_solution = None

