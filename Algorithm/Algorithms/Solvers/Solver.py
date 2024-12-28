from Algorithm.Algorithms.Checkers.Prim import Prim

class Solver:

    # All solvers need a checker
    def __init__(self, checker = None):
        if checker != None:
            self.checker = checker
        else:
            self.checker = Prim()

    # Common function of all solvers
    def solve(self):
        pass
