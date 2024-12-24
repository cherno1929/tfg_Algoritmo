from Algorithms.Checkers.Prim import Prim
from Algorithms.Optimazers.Optimizer import Optimizer
from Algorithms.Optimazers.Local_Optimizer import Local_Optimizer
import math
import random

class Iterative_Greedy_Optimazer(Optimizer):

    def __init__(self, checker = None):
        if checker != None:
            super.__init__(checker)
        else:
            super().__init__(Prim())
        self.local_optimizer = Local_Optimizer(self.checker)
        # % destruction of solution, no more than 50%
        self.betta = 35
        # Counter of upgrades
        self.delta = 0
        # Value got to be low (5-10 according to teacher)
        self.lim_upgrade = 5

    # This algorithm is based on destroying part of the solution and adding
    def __destruct_sol__(self, g, sol):  # Destroy n random nodes of solution
        # Numbers of nodes to deactivate
        num_Nodes_To_Destroy = math.ceil((self.betta / 100) * len(sol))

        # Set of used nodes to avoid duplication
        deactivated = set()

        # Elimination of random nodes of solution nodes
        while (num_Nodes_To_Destroy > 0):
            rand_Node = random.choice(sol)
            if not rand_Node in deactivated:
                num_Nodes_To_Destroy -= 1
                deactivated.add(rand_Node)
                g.nodes[rand_Node]['isGen'] = False

        return list(set(sol) - deactivated)

    def __reconstruct_solution__(self, solution, part_sol):  # Reconstruct solution based on greedy criterium
        # Add bestNodes until feasible solution
        bestNodesAux = solution.best_nodes[:]
        isSol = False
        # Stop when it's a solution, or the new solution is bigger than the current one
        while not isSol and bestNodesAux:
            node = bestNodesAux.pop(0)
            part_sol.append(node)
            solution.graph.nodes[node]['isGen'] = True
            isSol = self.checker.check(solution.graph, part_sol[0])
        # Optimize when solution if is valid
        if isSol:
            return self.local_optimizer.optimize(solution, part_sol)
        return solution.first_local_solution

    def __restore_sol__(self, g, actualSol, nodesRestore):
        for node in actualSol:
            if not node in nodesRestore:
                g.nodes[node]['isGen'] = False
            else:
                nodesRestore.remove(node)
        for node in nodesRestore:
            g.nodes[node]['isGen'] = True

    def __iterational_greedy__(self, solution):
        sol = solution.first_local_solution
        if len(sol) > 1:  # No upgrade needed
            while self.delta < self.lim_upgrade and len(sol) > 1:  # Not more upgrades posible
                partical_sol = self.__destruct_sol__(solution.graph, sol)
                newSolution = self.__reconstruct_solution__(solution, partical_sol)
                # Update solution ,if the new solution is better than the old one
                if len(newSolution) < len(sol) and self.checker.check(solution.graph,newSolution[0]):
                    sol = newSolution
                    self.delta = 0
                # If not restore the old solution
                else:
                    self.delta += 1
                    self.__restore_sol__(solution.graph, newSolution, set(sol))
        return sol

    def optimize(self, solution):
        return self.__iterational_greedy__(solution)

