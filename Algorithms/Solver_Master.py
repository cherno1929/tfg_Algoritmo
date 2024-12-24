from Algorithms.Solvers.First_Solution_Solver import First_Solution_Solver
from Algorithms.Optimazers.Iterative_Greedy_Optimazer import Iterative_Greedy_Optimazer
from Algorithms.Solvers.Optimal_Solver import Optimal_Solver
from Algorithms.Solvers.Random_Solver import Random_Solver
from Algorithms.Checkers.Prim import Prim

class Solve_Master:

    def __init__(self):
        self.check = Prim()
        self.fist_solution_solver = First_Solution_Solver()
        self.iterative_greedy_optimizer = Iterative_Greedy_Optimazer()
        self.optimal_solver = Optimal_Solver()
        self.random_solver = Random_Solver()


    def solve_greedy(self, g):
        g.first_solution = self.fist_solution_solver.solve(g)
        if g.first_solution != None:
            g.first_local_solution = self.iterative_greedy_optimizer.local_optimizer.optimize(g, g.first_solution)
            g.best_solution = self.iterative_greedy_optimizer.optimize(g)

        return g

    def solve_optimal(self, g):
        solution = self.optimal_solver.solve(g)
        if solution != None:
            print(solution)
            print(self.check.check(g.graph, g.best_nodes[0]))
        else:
            print("There is no solution")
        return g

    def solver_random(self, g):
        solution = self.random_solver.solve(g)
        print(solution)
        return g