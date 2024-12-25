from Algorithms.Solvers.Solver import Solver
import random

class Random_Solver(Solver):

    # Gives a random solution
    def __random_solve__(self, g):
        sol = []
        for n in g.nodes:
            if bool(random.getrandbits(1)):
                g.nodes.get(n)['isGen'] = True
                sol.append(n)
        return sol

    def solve(self, g):
        return self.__random_solve__(g.graph)
