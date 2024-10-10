#Get best nodes
from Referee.CheckAlgorithm.checkPrim import prim_1 as prim

def getBestNodes(g):
    bestNodes = []
    n = len(g.nodes)
    greed = []
    for node in range(n):
        g.nodes[node]['isGen'] = True
        visited,distances = prim(g,node)
        greed.append((len(visited), sum([x for x in distances if x != float("inf")]),g.degree(node),node))
        g.nodes[node]['isGen'] = False

    vorax_list = sorted(greed, key=lambda x:(x[0],-x[1],x[2]), reverse=True)

    for node in range(n):
        bestNodes.append(vorax_list[node][3])

    return bestNodes

