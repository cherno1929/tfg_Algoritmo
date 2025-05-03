import time

from Algorithm.Algorithms.Solvers.Solver import Solver
import random

class Random_Solver(Solver):

    def __restore_graph__(self, g, sol):
        for node in sol:
            g.nodes[node]['isGen'] = True

    # Gives a random solution
    def __random_solve__(self, g):
        graph = g.graph
        sol = []
        start_time = time.time()
        is_sol = False
        while not is_sol and (time.time() - start_time) < 300:
            self.__restore_graph__(graph, sol)
            sol = []
            for n in graph.nodes:
                if random.randint(1, 100) <= g.random_node_activation:
                    graph.nodes.get(n)['isGen'] = True
                    sol.append(n)
            is_sol = self.checker.check(graph)
        if is_sol:
            return sol
        else:
            return None

    def solve(self, g):
        return self.__random_solve__(g)
