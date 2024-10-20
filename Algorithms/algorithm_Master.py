import Algorithms.greedy_Nodes as greedN
import Algorithms.random_Graph as randomG
import Algorithms.greed_Graph as greedG

def solveGraph(g,n):
    if n == 1:
        return randomG.random_Sol(g)
    elif n == 2:
        return greedG.greedSolve(g)


def getBestNodes(g):
    return greedN.getBestNodes(g)

def getGenInput(g):
    genNodes = list(map(int,input().strip().split()))
    for node in genNodes:
        g.nodes[node]['isGen'] = True

