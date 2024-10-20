import itertools
import Referee.refereeMaster as referee
import Algorithms.algorithm_Master as master

def greedSolve(g):
    listNodes = master.getBestNodes(g)

    print(f"Best Nodes : {listNodes}")

    if referee.check(g,1):
        return ()

    for node in listNodes:
        g.nodes[node]['isGen'] = True
        if referee.check(g,1):
            return (node)
        g.nodes[node]['isGen'] = False

    for n_node in range(2,len(listNodes)+1):
        comb = list(itertools.combinations(listNodes,n_node))
        for nodes in comb:
            for node in nodes:
                g.nodes[node]['isGen'] = True
            if referee.check(g,1):
                return nodes
            for node in nodes:
                g.nodes[node]['isGen'] = False

    return None
