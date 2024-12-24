import copy

from Generators.Graph_Generator import Graph_Generator
from Algorithms.Solver_Master import Solve_Master
import Output.Out_Data_Graph as out

'''
-------------------------------------------
"read" will create an instance of graph and depending of the number you pass it will...
n = 1   -->     Read input from terminal
n = 2   -->     Generate Random graph (Barabasi_Albert) 
-------------------------------------------
"algorithm" will solve the problem
(For now gives a random solution)
-------------------------------------------
"referee" will check if the solution is correct and depending of the number you pass it will...
n = 1   -->     Check using Prim 
n = 2   -->     Check using Inner functions of NetworkX
n = 3   -->     Check using Floyd Warshall
'''

class Main:

    def __init__(self):
        self.graph_generator = Graph_Generator()
        self.solver_master = Solve_Master()

    def run(self):
        solution = self.graph_generator.generate_graph(10,0.35,8,2,7)
        sol_1 = copy.deepcopy(solution)
        sol_2 = copy.deepcopy(solution)
        sol_3 = copy.deepcopy(solution)
        self.solver_master.solve_optimal(sol_2)
        print("/////////////////////////")
        self.solver_master.solve_greedy(sol_1)
        print("/////////////////////////")
        self.solver_master.solver_random(sol_3)
        print("/////////////////////////")

        out.show_Graph(sol_1.graph, False)
        out.show_Graph(sol_2.graph, False)

main = Main()
main.run()

