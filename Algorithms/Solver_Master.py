from Algorithms.Solvers.First_Solution_Solver import First_Solution_Solver
from Algorithms.Optimazers.Iterative_Greedy_Optimazer import Iterative_Greedy_Optimazer

class Solve_Master:

    def __init__(self):
        self.fist_solution_solver = First_Solution_Solver()
        self.iterative_greedy_optimizer = Iterative_Greedy_Optimazer()


    def solve_greedy(self, g):
        g.first_solution = self.fist_solution_solver.solve(g)
        if g.first_solution != None:
            g.first_local_solution = self.iterative_greedy_optimizer.local_optimizer.optimize(g, g.first_solution)
            g.best_solution = self.iterative_greedy_optimizer.optimize(g)

        print(g.first_solution)
        print(g.first_local_solution)
        print(g.best_solution)

        return g
