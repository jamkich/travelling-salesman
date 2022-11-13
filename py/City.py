import numpy as np
class City:
    def __init__(self, x, y):
        # These are genes of our algorithm
        self.x = x
        self.y = y

    def distance(self, city):
        xDistance = abs(self.x - city.x)
        yDistance = abs(self.y - city.y)
        distance = np.sqrt((xDistance ** 2) + (yDistance ** 2))
        print(distance)
        return distance

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
