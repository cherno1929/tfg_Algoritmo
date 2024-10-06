#Check using functions of networkx

'''
"check_NetworkX" will use horizontal expansión and search for every graph that
can connect with, and will return the set of nodes connected
'''
def check_NetworkX(g, nodeToTest):
    reachable_nodes = set()
    stack = [(nodeToTest, 0)]  # (current_node, current_distance)

    while stack:
        current_node, current_distance = stack.pop()
        if current_node not in reachable_nodes:
            reachable_nodes.add(current_node)
            for neighbor in g.neighbors(current_node):
                edge_weight = g[current_node][neighbor]['dist']
                new_distance = current_distance + edge_weight
                if new_distance <= g.graph['l_max'] or g.nodes[neighbor]['isGen']:
                    stack.append((neighbor, 0 if g.nodes[neighbor]['isGen'] else new_distance))

    return reachable_nodes

'''
"check" will check if any node can connect with any other node and will try-cach
every posible link failure until it catches a failure of conection
'''
def check(g):
    isSol = True
    checkSet = set(g.nodes)
    for x, y in g.edges:
        edgeToFailData = g.get_edge_data(x, y)
        g.remove_edge(x,y)
        for nodeToTest in range(len(g.nodes)):
            visitedNodes = check_NetworkX(g, nodeToTest)
            isSol = visitedNodes == checkSet
            if not isSol:
                break
        if not isSol:
            break
        g.add_edge(x,y, **edgeToFailData)
    return isSol