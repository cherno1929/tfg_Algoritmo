from Algorithms.Solvers.Solver import Solver
import itertools

class Optimal_Solver(Solver):

    def __solve_optimal__(self,g ,best_nodes):
        if self.checker.check(g, 0):
            return ()

        # Check if there is a solution activating only one node
        for node in best_nodes:
            g.nodes[node]['isGen'] = True
            if self.checker.check(g, node):
                return [node]
            g.nodes[node]['isGen'] = False

        # Checks every combination until it finds a solution
        for n_node in range(2, len(best_nodes) + 1):
            comb = list(itertools.combinations(best_nodes, n_node))
            for nodes in comb:
                for node in nodes:
                    g.nodes[node]['isGen'] = True
                if self.checker.check(g, nodes[0]):
                    return list(nodes)
                for node in nodes:
                    g.nodes[node]['isGen'] = False

        return None

    def solve(self, g):
        return self.__solve_optimal__(g.graph, g.best_nodes)
