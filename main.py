import Input.read_graph_input as read
import Algorithms.random_Graph as algorithm
import Referee.refereeMaster as referee
import Output.Out_Data_Graph as write


def run():
    g = read.getInput()
    algorithm.random_Sol(g)
    #print(referee.check(g))
    print(referee.check(g, 1))
    print(referee.check(g, 2))
    write.show_Graph(g)

run()