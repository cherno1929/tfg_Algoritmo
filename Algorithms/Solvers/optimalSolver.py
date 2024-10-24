import itertools
import Referee.refereeMaster as referee
import Algorithms.algorithm_Master as master

def optimalSolve(g):
    bestNodes = master.getBestNodes(g)

    justNodes = [x for (x,_) in bestNodes]

    print(f"Best Nodes : {justNodes}")

    if referee.check(g,1):
        return ()

    for node in justNodes:
        g.nodes[node]['isGen'] = True
        if referee.check(g,1):
            return (node)
        g.nodes[node]['isGen'] = False

    for n_node in range(2,len(justNodes)+1):
        comb = list(itertools.combinations(justNodes,n_node))
        for nodes in comb:
            for node in nodes:
                g.nodes[node]['isGen'] = True
            if referee.check(g,1):
                return nodes
            for node in nodes:
                g.nodes[node]['isGen'] = False

    return None
