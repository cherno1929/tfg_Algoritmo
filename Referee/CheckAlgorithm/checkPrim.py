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
"check" will get a regenerator node and will get all visited nodes, and this will happen inj every link failure scenario
until finding a conection failure 
'''

def check(g):
    isSol = True
    nodesInGraph = set(g.nodes)
    for x, y in g.edges:
        edgeToFailData = g.get_edge_data(x, y)
        g.remove_edge(x, y)
        genNode = next((n for n, attr in g.nodes(data=True) if attr.get('isGen') == True), None)
        if genNode == None:
            visited, dist = prim_1(g,0)
        else:
            visited, dist = prim_1(g, genNode)
        isSol = visited == nodesInGraph
        g.add_edge(x, y, **edgeToFailData)
        if not isSol:
            break
    return isSol
