#Generate random solution
import random

def random_Sol(g):
    for n in g.nodes:
        if bool(random.getrandbits(1)):
            g.nodes.get(n)['isGen'] = True