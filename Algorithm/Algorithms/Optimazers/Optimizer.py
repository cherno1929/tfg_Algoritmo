from Algorithm.Algorithms.Checkers.Prim import Prim

class Optimizer:

    # All optimizers need a checker
    def __init__(self, checker=None):
        if checker != None:
            self.checker = checker
        else:
            self.checker = Prim()


    # Common function of all Optimizers
    def optimize(self):
        pass
