from Algorithms.Solvers.Solver import Solver
from Algorithms.Checkers.Prim import Prim

class First_Solution_Solver(Solver):

    def __fist_solution_solve(self, graph, best_nodes):

        if self.checker.check(graph, 1):
            return []

        sol = []

        # Add best-nodes until it finds a solution
        for node in best_nodes:
            graph.nodes[node]['isGen'] = True
            sol.append(node)
            if self.checker.check(graph, sol[0]):
                return sol

        # Graph doesnt have a solution
        return None

    def solve(self, solution):
        return self.__fist_solution_solve(solution.graph, solution.best_nodes)
