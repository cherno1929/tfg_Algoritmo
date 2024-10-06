#Check if solution is feasible

def select_next_node(distances, visited):
    bestItem = None
    minDist = float("inf")
    for i in range(len(distances)):
        if i not in visited and distances[i] < minDist:
            bestItem = i
            minDist = distances[i]
    return bestItem

def getConectionToNewNode(g,n,v,c):
    connected = False
    minDist = float("inf")
    for x,y in g.edges(n):
        cost = g.get_edge_data(x,y)['dist']
        error = g.get_edge_data(x,y)['isFail']
        if not error and y in v and cost < minDist and cost + c[y] <= g.graph['l_max']:
            if g.nodes[n]['isGen']:
                c[n] = 0
            else:
                c[x] = cost + c[y]
            connected = True
    return connected #So we know if the node conected

def prim_1(g, node):
    n = len(g.nodes)

    distances = [float("inf")] * n
    costs = [0] * n

    for start, end in g.edges(node):
        distances[end] = g.get_edge_data(start,end)['dist']

    visited = {node}

    while(n > 0):
        next_node = select_next_node(distances, visited)
        if next_node != None :
            if getConectionToNewNode(g,next_node,visited,costs):
                for start, end in g.edges(next_node):
                    dist = g.get_edge_data(start,end)['dist']
                    error = g.get_edge_data(start, end)['isFail']
                    if not error and end not in visited and costs[next_node] + dist <= g.graph['l_max']:
                        distances[end] = min(dist, distances[end])
                visited.add(next_node)
            else:
                distances[next_node] = float("inf")
                n += 1
        else:
            break
        n -= 1
    return visited

def check(g):
    isSol = True
    checkSet = set(g.nodes)
    for x,y in g.edges:
        g.get_edge_data(x,y)['isFail'] = True
        for nodeToTest in range(len(g.nodes)):
            visitedNodes = prim_1(g,nodeToTest)
            isSol = visitedNodes == checkSet
            if not isSol:
                break
        if not isSol:
            break
        g.get_edge_data(x,y)['isFail'] = False
    return isSol