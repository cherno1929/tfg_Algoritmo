import random
import math
import Referee.refereeMaster as referee
import Algorithms.Optimazers.optimazer_proto_1 as optimazer

#This algorithm is based on destroying part of the solution and adding
def destructSol(g,sol,betta): # Destroy n random nodes of solution
    # Numbers of nodes to deactivate
    num_Nodes_To_Destroy = math.ceil((betta / 100) * len(sol))

    # Set of used nodes to avoid duplication
    deactivated = set()

    # Elimination of random nodes of solution nodes
    while(num_Nodes_To_Destroy > 0):
        rand_Node = random.choice(sol)
        if not rand_Node in deactivated:
            num_Nodes_To_Destroy -= 1
            deactivated.add(rand_Node)
            g.nodes[rand_Node]['isGen'] = False

def reconstruct(g,bestNodes,lim_loop): # Reconstruct solution based on greedy criterium
    # Add bestNodes until feasible solution
    bestNodesAux = bestNodes
    sol_aux = [x for x in g.nodes if g.nodes[x]['isGen']]
    while not referee.check(g,1) and bestNodesAux and len(sol_aux) < lim_loop:
        node = bestNodesAux.pop(0)
        sol_aux.append(node)
        g.nodes[node]['isGen'] = True
    # Optimize solution
    return optimazer.optimaze(g,sol_aux)

def restoreSol(g,actualSol,nodesRestore):
    for node in actualSol:
        if not node in nodesRestore:
            g.nodes[node]['isGen'] = False
        else:
            nodesRestore.remove(node)
    for node in nodesRestore:
        g.nodes[node]['isGen'] = True

def iterationalGreedy(g,bestNode,sol):
    if len(sol) > 1: # No upgrade needed
        # Value got to be low (5-10 according to teacher)
        num_Upgrades = 5
        # Counter of upgrades
        delta = 0
        # % destruction of solution, no more than 50%
        betta = 50
        while delta < num_Upgrades and len(sol) > 1: # Not more upgrades posible
            destructSol(g,sol,betta)
            reconstruct(g,bestNode,len(sol))
            newSolution = [x for x in g.nodes if g.nodes[x]['isGen']]
            if len(newSolution) < len(sol):
                sol = newSolution
                delta = 0
            else:
                delta += 1
                restoreSol(g,newSolution,set(sol))
    return sol
