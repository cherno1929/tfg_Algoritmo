from Algorithm.Algorithms.Checkers.Checker import Checker

class Prim(Checker):

    def __select_next_node__(self, distances, visited):
        best_item = None
        min_dist = float("inf")
        # Itarete until find the best node
        for i in range(len(distances)):
            if i not in visited and distances[i] < min_dist:
                best_item = i
                min_dist = distances[i]
        return best_item

    def __get_conection_to_new_node__(self,g,n,v,c):
        connected = False
        min_dist = float("inf")
        # Iterate to find lest distant connection
        for x, y in g.edges(n):
            cost = g.get_edge_data(x, y)['dist']
            error = g.get_edge_data(x, y)['isFail']
            # It's known that the connection is feassible
            if not error and y in v and cost < min_dist and cost + c[y] <= g.graph['l_max']:
                # If is a generator then the distance resets to 0
                min_dist = cost + c[y]
                if g.nodes[n]['isGen']:
                    c[n] = 0
                else:
                    c[n] = min_dist
                connected = True
        return connected  # So we know if the node conected

    def __get_viable_dist_to_network__(self, g, end, visited, costs):
        dist = float("inf")
        while dist > g.graph['l_max'] and visited:
            node = visited.pop()
            if g.has_edge(node, end):
                # Min dist and distance to network + cost of the visited node
                dist = min(dist, g.get_edge_data(node, end)['dist'] + costs[node])
        return dist

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
                    # Add visited node
                    visited.add(next_node)
                    # Update distances
                    for start, end in g.edges(next_node):
                        # Only no visited nodes are needed for distance update
                        if end not in visited:
                            # Get fist viable distance for next posible nodes
                            dist = self.__get_viable_dist_to_network__(g, end, list(visited),costs)
                            if dist <= g.graph['l_max']:
                                distances[end] = min(dist, distances[end])
                else:
                    distances[next_node] = float("inf")
                    n += 1
            else:
                break
            n -= 1

        # Starting node will allways have 0 distance
        distances[node] = 0
        return visited, distances

    def check_all_nodes(self, g):
        isValid = True
        i = 0
        while isValid and i < len(g.nodes):
            isValid = self.check(g, i)
            i += 1
        return isValid

    def check(self, g, node = None):
        # Get a node, get first generator if possible
        if node == None:
            nodes = [x for x in g.nodes if g.nodes[x]['isGen']]
            if len(nodes) > 0:
                node = nodes[0]
            else:
                return self.check_all_nodes(g)
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