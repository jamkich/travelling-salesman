import operator

import numpy as np
import pandas as pd
import random
from City import City
from Fitness import Fitness
DATA_LOCATION = '../berlin52.tsp'
popSize = 52


# cityList data read
def data_read():
    with open(DATA_LOCATION, 'r') as file:
        Name = file.readline().strip().split()[1]  # NAME
        FileType = file.readline().strip().split()[1]  # TYPE
        Comment = file.readline().strip().split()[1]  # COMMENT
        Dimension = file.readline().strip().split()[1]  # DIMENSION
        EdgeWeightType = file.readline().strip().split()[1]  # EDGE_WEIGHT_TYPE
        file.readline()
        cities = []
        coordinates = []
        # Reading and writing data to cities list and coordinates list, each entry in coordinates relates to city
        for i in range(int(Dimension)):
            info = file.readline()
            info = info.split(' ')
            index = info[0]
            x = int(float(info[1]))
            y = int(float(info[2]))
            cities.append(index)
            coordinates.append((x, y))
        return coordinates, cities


# creating individual of our population
def route(cityList):
    route = random.sample(cityList, len(cityList))
    return route


# creating initial population, first generation
def initialPop(popSize, cityList):
    population = []
    for i in range(0, popSize):
        population.append(route(cityList))
    return population

# creating new objects of fitness class for every city from created pupulation,
# adding them to dict and sorting in reverse based on the route
def rankRoutes(population):
    fitnessGrades = {}
    for i in range(len(population)):
        fitnessGrades[i] = Fitness(population[i]).fitness()
    return sorted(fitnessGrades.items(), key=operator.itemgetter(1), reverse= True)