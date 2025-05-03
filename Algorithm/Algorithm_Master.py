import copy
import time
from Algorithm.Generators.Graph_Generator import Graph_Generator
from Algorithm.Algorithms.Solver_Master import Solve_Master
from Algorithm.Statistics.Statistic import Statistic
import Algorithm.Output.Out_Data_Graph as out


class Algorithm_Master:

    def __init__(self):
        # Generator of graphs
        self.graph_generator = Graph_Generator()

        # Solver of graph
        self.solver_master = Solve_Master()

    def solve_ftlrp_problem(self, data, is_data_transformed = False):
        if not is_data_transformed:
            data['n_node'] = int(data['n_node'])
            data['max_travel'] = int(data['max_travel'])
            data['min_dist'] = int(data['min_dist'])
            data['max_dist'] = int(data['max_dist'])
            data['prob_link'] = float(data['prob_link'])
            if 'ramdom_activation' in data:
                data['ramdom_activation'] = int(data['ramdom_activation'])
                data['greedy_destruction'] = None
            elif 'greedy_destruction' in data:
                data['greedy_destruction'] = int(data['greedy_destruction'])
                data['ramdom_activation'] = None
            else:
                data['greedy_destruction'] = None
                data['ramdom_activation'] = None
        solution = self.graph_generator.generate_graph(data['n_node'], data['prob_link'], data['max_travel'], data['min_dist'], data['max_dist'], data['ramdom_activation'], data['greedy_destruction'])
        if 'algorithm' not in data:
            data['algorithm'] = 'g'

        return self.run_ftlrp(solution, data['algorithm'][0])

    def run_benchmark(self, data):
        # Transform data
        data['n_ini_node'] = int(data['n_ini_node'])
        data['n_fin_node'] = int(data['n_fin_node'])
        data['prob_link'] = float(data['prob_link'])
        data['min_dist'] = int(data['min_dist'])
        data['max_dist'] = int(data['max_dist'])
        data['max_travel'] = int(data['max_travel'])
        data['n_sample'] = int(data['n_sample'])
        data['jump_node'] = int(data['jump_node'])
        if len(data['algorithm']) == 0:
            data['algorithm'] = 'g'
        if 'ramdom_activation' in data:
            data['ramdom_activation'] = int(data['ramdom_activation'])
            data['greedy_destruction'] = None
        elif 'greedy_destruction' in data:
            data['greedy_destruction'] = int(data['greedy_destruction'])
            data['ramdom_activation'] = None
        else:
            data['greedy_destruction'] = None
            data['ramdom_activation'] = None
        statistic = Statistic(data['algorithm'])


        for n_node in range(data['n_ini_node'], data['n_fin_node'] + 1, data['jump_node']):
            data['n_node'] = n_node
            n_sol = 0
            while n_sol < data['n_sample']:
                solution = self.solve_ftlrp_problem(data, True)
                if n_node in statistic.solutions:
                    statistic.solutions[n_node].append(solution)
                else:
                    statistic.solutions[n_node] = [solution]

                if solution.best_solution != None:
                    n_sol += 1

        return statistic

    def run_ftlrp(self, solution, algorithm = 'g'):
        start_time = time.time()
        if algorithm == 'o':
            self.solver_master.solve_optimal(solution)
        elif algorithm == 'r':
            self.solver_master.solver_random(solution)
        else:
            self.solver_master.solve_greedy(solution)
        end_time = time.time()
        solution.time_to_solve = end_time - start_time
        return solution

    def check_is_sol_client_req(self, graph_data):
        solution = self.graph_generator.transform_to_graph(graph_data)
        if self.solver_master.checker.check(solution.graph):
            return True
        else:
            for node in solution.graph.nodes:
                solution.graph.nodes[node]['isGen'] = False
            solution = self.run_ftlrp(solution)
            return solution.to_dict()