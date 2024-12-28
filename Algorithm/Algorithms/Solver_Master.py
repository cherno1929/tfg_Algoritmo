from Algorithm.Algorithms.Solvers.First_Solution_Solver import First_Solution_Solver
from Algorithm.Algorithms.Optimazers.Iterative_Greedy_Optimazer import Iterative_Greedy_Optimazer
from Algorithm.Algorithms.Solvers.Optimal_Solver import Optimal_Solver
from Algorithm.Algorithms.Solvers.Random_Solver import Random_Solver
from Algorithm.Algorithms.Checkers.Prim import Prim

class Solve_Master:

    def __init__(self):
        # Create checker for all attributes to save memory
        prim = Prim()
        self.fist_solution_solver = First_Solution_Solver(prim)
        self.iterative_greedy_optimizer = Iterative_Greedy_Optimazer(prim)
        self.optimal_solver = Optimal_Solver(prim)
        self.random_solver = Random_Solver(prim)


    def solve_greedy(self, g):
        g.first_solution = self.fist_solution_solver.solve(g)
        if g.first_solution != None:
            g.first_local_solution = self.iterative_greedy_optimizer.local_optimizer.optimize(g, g.first_solution)
            g.best_solution = self.iterative_greedy_optimizer.optimize(g)
        return g

    def solve_optimal(self, g):
        g.best_solution = self.optimal_solver.solve(g)
        return g

    def solver_random(self, g):
        g.best_solution = self.random_solver.solve(g)
        return g