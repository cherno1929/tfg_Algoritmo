

class Prim:

    def __select_next_node__(self, distances, visited):
        bestItem = None
        minDist = float("inf")
        # Itarete until find the best node
        for i in range(len(distances)):
            if i not in visited and distances[i] < minDist:
                bestItem = i
                minDist = distances[i]
        return bestItem

    def __get_conection_to_new_node__(self,g,n,v,c):
        connected = False
        minDist = float("inf")
        # Iterate to find lest distant connection
        for x, y in g.edges(n):
            cost = g.get_edge_data(x, y)['dist']
            error = g.get_edge_data(x, y)['isFail']
            # It's known that the connection is feassible
            if not error and y in v and cost < minDist and cost + c[y] <= g.graph['l_max']:
                # If is a generator then the distance resets to 0
                if g.nodes[n]['isGen']:
                    c[n] = 0
                else:
                    c[x] = cost + c[y]
                connected = True
        return connected  # So we know if the node conected

    def prim(self, g, node, len_g = float("inf")):
        n = len(g.nodes)
        # Its needed a list of distances of every node from regenerator to them
        distances = [float("inf")] * n
        costs = [0] * n

        # The distances are still not known
        for start, end in g.edges(node):
            distances[end] = g.get_edge_data(start, end)['dist']

        visited = {node}

        while n > 0 and len(visited) < len_g:
            # Select the next best node
            next_node = self.__select_next_node__(distances, visited)
            if next_node != None:
                # Establish connection between new_node -- graph
                if self.__get_conection_to_new_node__(g, next_node, visited, costs):
                    # Update distances
                    for start, end in g.edges(next_node):
                        dist = g.get_edge_data(start, end)['dist']
                        if end not in visited and costs[next_node] + dist <= g.graph['l_max']:
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

    def check(self, g, node):
        isSol = True
        nodesInGraph = set(g.nodes)
        len_nodes_in_graph = len(nodesInGraph)
        # Check every possible link fail scenario
        for x, y in g.edges:
            # Break link
            edgeToFailData = g.get_edge_data(x, y)
            g.remove_edge(x, y)
            # Check if works
            visited, dist = self.prim(g, node, len_nodes_in_graph)
            isSol = visited == nodesInGraph
            # Rebuild link
            g.add_edge(x, y, **edgeToFailData)
            if not isSol:
                break
        return isSol