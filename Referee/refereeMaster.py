from Referee.CheckAlgorithm.checkPrim import check as prim
from Referee.CheckAlgorithm.checkNetworkx import check as native
def check(g,n):
    if n == 1:
        return prim(g)
    elif n == 2:
        return native(g)
