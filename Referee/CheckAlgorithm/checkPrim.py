#Check if solution is feasible

def select_next_node(distances, visited):
    bestItem = None
    minDist = float("inf")
    for i in range(len(distances)):
        if i not in visited and distances[i] < minDist:
            bestItem = i
            minDist = distances[i]
    return bestItem

'''
"getConectionToNewNode" In order to get the next feasible node, it is needed that the "nextNode" knows with witch
node is gonna connect, so it search of each visited node and asks if node have edge with it && is the best option?
'''

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

'''
"prim_1" will use Prim expansión and search for every graph that
can connect with, and will return the set of nodes connected
'''

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
    distances[node] = 0
    return visited, distances

'''
"check" will check if any node can connect with any other node and will try-cach
every posible link failure until it catches a failure of conection
'''

def check(g):
    isSol = True
    checkSet = set(g.nodes)
    for x,y in g.edges:
        g.get_edge_data(x,y)['isFail'] = True
        for nodeToTest in range(len(g.nodes)):
            visitedNodes, _ = prim_1(g,nodeToTest)
            isSol = visitedNodes == checkSet
            if not isSol:
                break
        if not isSol:
            break
        g.get_edge_data(x,y)['isFail'] = False
    return isSol
