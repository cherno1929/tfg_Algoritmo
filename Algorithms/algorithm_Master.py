import Algorithms.greedy_Nodes as greedN
import Algorithms.random_Graph as randomG

def solveGraph(g,n):
    randomG.random_Sol(g)

def getBestNodes(g):
    return greedN.getBestNodes(g)