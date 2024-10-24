import Algorithms.Solvers.greedy_Nodes as greedN
import Algorithms.Solvers.random_Graph as randomG
import Algorithms.Solvers.optimalSolver as optm
import Algorithms.Solvers.greedSolver as greed

def solveGraph(g,n):
    if n == 1:
        return randomG.random_Sol(g)
    elif n == 2:
        return optm.optimalSolve(g)
    elif n == 3:
        return greed.solve_v1(g)
    elif n == 4:
        return greed.solve_v2(g)


def getBestNodes(g):
    return greedN.getBestNodes(g)

def getGenInput(g):
    genNodes = list(map(int,input().strip().split()))
    for node in genNodes:
        g.nodes[node]['isGen'] = True

def getDiffNodes(listNodes, visited):
    return sorted(listNodes, key=lambda s: len(s[1] ^ visited), reverse=True)

