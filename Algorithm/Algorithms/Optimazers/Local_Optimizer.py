from Algorithm.Algorithms.Optimazers.Optimizer import Optimizer


class Local_Optimizer(Optimizer):

    def __restore_graph__(self, g, sol):
        for node in sol:
            g.nodes[node]['isGen'] = True

    def __local_optimization__(self, g, nodes_sol):
        if len(nodes_sol) == 1:  # Best Solution
            return nodes_sol


        # Optimize based in substitution 2x2
        for n1 in nodes_sol:
            for n2 in nodes_sol:
                if g.nodes[n1]['isGen'] and g.nodes[n2]['isGen']:
                    g.nodes[n1]['isGen'] = False
                    g.nodes[n2]['isGen'] = False
                    if not self.checker.check(g):
                        g.nodes[n1]['isGen'] = True
                        g.nodes[n2]['isGen'] = True

        nodes_sol_aux = [x for x in g.nodes if g.nodes[x]['isGen']]

        # Optimize based in substitution 1x1
        for n in nodes_sol_aux:
            g.nodes[n]['isGen'] = False
            if not self.checker.check(g):
                g.nodes[n]['isGen'] = True

        return [x for x in g.nodes if g.nodes[x]['isGen']]

    def optimize(self, solution, nodes):
        return self.__local_optimization__(solution.graph, nodes)