import Referee.refereeMaster as referee
import Algorithms.algorithm_Master as master

def restore_Graph(g,sol):
    for node in sol:
        g.nodes[node]['isGen'] = True

def optimaze(g,nodes_sol):

    if len(nodes_sol) == 1:  # Best Solution
        return nodes_sol

    set_nodes_solution = set(nodes_sol)

    # Optimize based in substitution 2x1
    i = 0
    while i < len(nodes_sol) and set_nodes_solution:
        j = 0
        while j < len(nodes_sol) and set_nodes_solution:
            if i != j and nodes_sol[i] in set_nodes_solution and nodes_sol[j] in set_nodes_solution:
                g.nodes[nodes_sol[i]]['isGen'] = False
                g.nodes[nodes_sol[j]]['isGen'] = False
                set_nodes_solution.remove(nodes_sol[i])
                set_nodes_solution.remove(nodes_sol[j])
                if not referee.check(g,1):
                    g.nodes[nodes_sol[i]]['isGen'] = True
                    set_nodes_solution.add(nodes_sol[i])
                    if not referee.check(g,1):
                        g.nodes[nodes_sol[i]]['isGen'] = False
                        g.nodes[nodes_sol[j]]['isGen'] = True
                        set_nodes_solution.remove(nodes_sol[i])
                        set_nodes_solution.add(nodes_sol[j])
                        if not referee.check(g,1):
                            g.nodes[nodes_sol[i]]['isGen'] = True
                            set_nodes_solution.add(nodes_sol[i])
            j += 1
        i += 1
    # Problem!!! -> Sometimes this doble loop cancels all generator nodes
    # This if it's just a temporal solution
    if len(set_nodes_solution) == 0:
        restore_Graph(g,nodes_sol)
        return nodes_sol

    return list(set_nodes_solution)


