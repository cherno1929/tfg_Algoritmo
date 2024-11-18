import Referee.refereeMaster as referee
import Algorithms.algorithm_Master as master
import Algorithms.Optimazers.optimazer_proto_1 as solution_Optimizer

def solve_v1(g):
    bestNodes = master.getBestNodes(g)
    justNodes = [x for (x,_) in bestNodes]
    print(f"Best nodes : {[x for (x,y) in bestNodes]}")

    if referee.check(g,1):
        return []

    sol = []

    for node in justNodes:
        g.nodes[node]['isGen'] = True
        sol.append(node)
        if referee.check(g, 1, sol[0]):
            print(f"First solution : {sol}")
            return solution_Optimizer.optimaze(g, sol)

    return None

def solve_v2(g):
    bestNodes = master.getBestNodes(g)
    print(f"Best nodes : {[x for (x,_) in bestNodes]}")

    if referee.check(g, 1):
        return ()

    sol = []

    totalVisited = set()

    isSol = False

    while bestNodes and not isSol:
        node, setVisited = bestNodes.pop(0)
        g.nodes[node]['isGen'] = True
        sol.append(node)
        totalVisited.update(setVisited)
        isSol = referee.check(g,1,sol[0])
        if isSol:
             return solution_Optimizer.optimaze(g, sol)

        # Regroup the nodes
        bestNodes = master.getDiffNodes(bestNodes, totalVisited)

    if isSol:
        return solution_Optimizer.optimaze(g, sol)
    else:
        return None
