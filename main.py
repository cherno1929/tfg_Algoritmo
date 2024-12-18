from Generators.Graph_Generator import Graph_Generator
from Algorithms.Solver_Master import Solve_Master

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
        solution = self.graph_generator.generate_graph(20,0.35,8,2,7)
        solution = self.solver_master.solve_greedy(solution)

main = Main()
main.run()

