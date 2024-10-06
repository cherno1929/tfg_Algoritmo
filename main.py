import Input.read_graph_input as read
import Algorithms.random_Graph as algorithm
import Referee.check_random_sol as referee
import Output.Out_Data_Graph as write

def run():
    g = read.getInput()
    algorithm.random_Sol(g)
    print(referee.check(g))
    write.show_Graph(g)

run()