from Referee.CheckAlgorithm.checkPrim import check as prim
from Referee.CheckAlgorithm.checkNetworkx import check as native
from Referee.CheckAlgorithm.check_floyd_warshall import check as floyd_warshall

def check(g, n ,node = 0):
    if n == 1:
        return prim(g,node)
    elif n == 2:
        return native(g)
    elif n == 3:
        return floyd_warshall(g)
