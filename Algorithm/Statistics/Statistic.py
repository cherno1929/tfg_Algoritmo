
class Statistic:

    def __init__(self):
        # Saves solutions x number of nodes
        self.solutions = dict()

    def to_dict(self):
        data = {}
        for key in self.solutions.keys():
            data[key] = list(map(lambda x : x.to_dict(), self.solutions[key]))
        return data
