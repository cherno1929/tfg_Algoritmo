import Referee.refereeMaster as referee
import Algorithms.algorithm_Master as master

def optimaze(g,nodes_sol):
    '''
    #Eliminate no needed nodes from solution
    node = 0
    while node < len(nodes_sol):
        g.nodes[nodes_sol[node]]['isGen'] = False
        if referee.check(g,1):
            nodes_sol.pop(node)
        else:
            g.nodes[nodes_sol[node]]['isGen'] = True
            node += 1



    #Try to substitute 2 nodes for 1 (Only nodes in solution)

    '''

    print(f"First solution {nodes_sol}")

    if len(nodes_sol) <= 2:  # Best Solution
        return nodes_sol

    for n1 in nodes_sol:
        for n2 in nodes_sol:
            if g.nodes[n1]['isGen'] and g.nodes[n2]['isGen']: #If generator off, then there was an previous case of optimization
                g.nodes[n1]['isGen'] = False
                if not referee.check(g,1): #Means n1 is needed
                    g.nodes[n1]['isGen'] = True
                    g.nodes[n2]['isGen'] = False
                    if not referee.check(g,1): #Means n1 && n2 are needed
                        g.nodes[n1]['isGen'] = True
                        g.nodes[n2]['isGen'] = True


    return [x for x in g.nodes if g.nodes[x]['isGen']]


