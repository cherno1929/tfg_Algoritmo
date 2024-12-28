import copy
import time
from Generators.Graph_Generator import Graph_Generator
from Algorithms.Solver_Master import Solve_Master
import Output.Out_Data_Graph as out


class Main:

    def __init__(self):
        # Generator of graphs
        self.graph_generator = Graph_Generator()

        # Solver of graph
        self.solver_master = Solve_Master()

    def run(self):
        solution = self.graph_generator.generate_graph(20,0.3,8,3,6)
        start_time = time.time()
        self.solver_master.solve_greedy(solution)
        end_time = time.time()

        # Gets how many time in seconds it needed
        print(f"Time required :: {end_time - start_time}")

        # Show graphic of the graph
        out.show_Graph(solution.graph, False)


main = Main()
main.run()

