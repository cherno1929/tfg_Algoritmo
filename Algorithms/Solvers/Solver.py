from Algorithms.Checkers.Prim import Prim

class Solver:

    def __init__(self, checker = None):
        if checker != None:
            self.checker = checker
        else:
            self.checker = Prim()

    def solve(self):
        pass
