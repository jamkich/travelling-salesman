class Fitness():
    def __init__(self, route):
        self.distance = 0
        # This is chromosome of our algorithm, satisfies conditions
        self.route = route
        #
        self.fitness = 0.0

    def routeDistance(self):
        if self.distance == 0:
            pathDistance = 0
            for i in range(len(self.route)):
                fromCity = self.route[i]
                toCity = None
                # checking if there is any other city we haven't visited
                if i + 1 < len(self.route):
                    toCity = self.route[i + 1]
                # if not, go back to starting city
                else:
                    toCity = self.route[0]
                pathDistance += fromCity.distance(toCity)
            self.distance = pathDistance
        return self.distance

    def fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness