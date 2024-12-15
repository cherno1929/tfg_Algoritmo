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
        print("Nice")

main = Main()
main.run()

'''
def run():
    g = read.getInput(2)
    print(f"Nº Nodos : {len(g.nodes)} // Nº Aristas : {len(g.edges)}")
    print(f"Distancia maxima {g.graph['l_max']}")
    ini = time.time()
    sol = algorithms.solveGraph(g,3)
    print(f"Local Solución : {sol}")
    if sol != None:
        bestNodes = algorithms.getBestNodes(g)
        for n in sol: # Give back the nodes of solution yo the graph
            g.nodes[n]['isGen'] = True
        justNodes = [x for (x, _) in bestNodes]
        sol = itG_p1.iterationalGreedy(g,justNodes,sol)
        print(f"IG Solution : {sol}")
    else:
        print(f"No avalable IG solution")
    fin = time.time()
    print(f"Tiempo de ejecución en segundos : {fin-ini}")
    write.show_Graph(g,False)
'''