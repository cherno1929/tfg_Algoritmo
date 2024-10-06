#Generate random solution
import random

def random_Sol(g): #Give generator to random nose
    for n in g.nodes:
        if bool(random.getrandbits(1)):
            g.nodes.get(n)['isGen'] = True