import numpy as np
import pandas as pd
import random
from City import City
from Fitness import Fitness


def route(cityList):
    route = random.sample(cityList, len(cityList))
    return route

# creating initial population, first generation


def initialPop(popSize, cityList):
    population = []
    for i in range(0, popSize):
        population.append(route(cityList))
    return population