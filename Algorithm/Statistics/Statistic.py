
class Statistic:

    def __init__(self, algorithm = 'g'):
        # Saves solutions x number of nodes
        self.solutions = dict()
        self.algorithm = algorithm

    def to_dict(self):
        data = dict()
        for key in self.solutions.keys():
            data[key] = list(map(lambda x : x.to_dict(), self.solutions[key]))
        data[-1] = self.algorithm
        return data
