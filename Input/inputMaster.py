import Input.read_graph_input as read
import Input.generate_Graph as generate

def getInput(n):
    if n == 1:
        return read.readGraph()
    elif n == 2:
        return generate.generate_Barabasi_Albert_Graph()