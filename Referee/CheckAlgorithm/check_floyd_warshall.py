#Check using Floyd_WarShall

def getEdgeMatrix(g):
    n = len(g.nodes)
    matrix = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if g.has_edge(i,j):
                matrix[i].append(g.get_edge_data(i,j)['dist'])
            elif i == j:
                matrix[i].append(0)
            else:
                matrix[i].append(float("inf"))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if g.nodes[k]['isGen'] and matrix[i][k] <= g.graph['l_max']:
                    matrix[i][k] = 0
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    return matrix

def printMatrix(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            print("\t", m[i][j], end=" ")
        print()

def check(g):
    isValid = True
    n = len(g.nodes)

    for x, y in g.edges:
        edgeToFailData = g.get_edge_data(x, y)
        g.remove_edge(x,y)
        distances = getEdgeMatrix(g)
        for i in range(n):
            for j in range(n):
                if distances[i][j] > g.graph['l_max']:
                    isValid = False
                    break
            if not isValid:
                break
        g.add_edge(x,y, **edgeToFailData)
        if not isValid:
            break

    return isValid