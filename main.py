import Input.inputMaster as read
import Algorithms.random_Graph as algorithm
import Referee.refereeMaster as referee
import Output.Out_Data_Graph as write

'''
-------------------------------------------
"read" will create an instance of graph and depending of the number you pass it will...
n = 1   -->     Read input from terminal
n = 2   -->     Generate Random graph (Barabasi_Albert) 
-------------------------------------------
"algorithm" will solve the problem
(For now gives a random solution)
-------------------------------------------
"referee" will check if the solution is correct and depending of the number you pass it will...
n = 1   -->     Check using Prim 
n = 2   -->     Check using Inner functions of NetworkX
'''

def run():
    g = read.getInput(2)
    algorithm.random_Sol(g)
    print(referee.check(g, 1))
    print(referee.check(g, 2))
    write.show_Graph(g)

run()