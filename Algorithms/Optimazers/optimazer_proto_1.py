import Referee.refereeMaster as referee
import Algorithms.algorithm_Master as master

def restore_Graph(g,sol):
    for node in sol:
        g.nodes[node]['isGen'] = True

def optimaze(g,nodes_sol):

    if len(nodes_sol) == 1:  # Best Solution
        return nodes_sol

    nodes_set = set(nodes_sol)

    # Optimize based in substitution 2x1
    for n1 in nodes_sol:
        for n2 in reversed(nodes_sol):
            if n1 != n2 and g.nodes[n1]['isGen'] and g.nodes[n2]['isGen']: #If generator off, then there was an previous case of optimization
                g.nodes[n1]['isGen'] = False
                g.nodes[n2]['isGen'] = False
                nodes_set.remove(n1)
                nodes_set.remove(n2)
                if not referee.check(g,1,next(iter(nodes_set))): # Check if n1 & n2 aren't needed
                    nodes_set.add(n1)
                    g.nodes[n1]['isGen'] = True
                    if not referee.check(g,1,next(iter(nodes_set))): # Check if only n1 is needed
                        nodes_set.add(n2)
                        nodes_set.remove(n1)
                        g.nodes[n1]['isGen'] = False
                        g.nodes[n2]['isGen'] = True
                        if not referee.check(g, 1, next(iter(nodes_set))): # Check if only n2 is needed
                            nodes_set.add(n1)
                            g.nodes[n1]['isGen'] = True
            # Problem!!! -> Sometimes this doble loop cancels all generator nodes
            # This if it's just a temporal solution
            if len(nodes_set) == 0:
                restore_Graph(g,nodes_sol)
                return nodes_sol

    return list(nodes_set)


