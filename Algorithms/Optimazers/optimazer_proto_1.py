import Referee.refereeMaster as referee
import Algorithms.algorithm_Master as master

def optimaze(g,nodes_sol):

    if len(nodes_sol) == 1:  # Best Solution
        return nodes_sol

    for n1 in nodes_sol:
        for n2 in reversed(nodes_sol):
            if g.nodes[n1]['isGen'] and g.nodes[n2]['isGen']: #If generator off, then there was an previous case of optimization
                g.nodes[n1]['isGen'] = False
                if not referee.check(g,1): #Means n1 is needed
                    g.nodes[n1]['isGen'] = True
                    g.nodes[n2]['isGen'] = False
                    if not referee.check(g,1): #Means n1 && n2 are needed
                        g.nodes[n1]['isGen'] = True
                        g.nodes[n2]['isGen'] = True

    #Problem -> Sometimes this doble loop cancels all generator nodes
    return [x for x in g.nodes if g.nodes[x]['isGen']]


