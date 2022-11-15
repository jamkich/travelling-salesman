import numpy as np
import pandas as pd
import random
from City import City
from Fitness import Fitness


def route(cityList):
    route = random.sample(cityList, len(cityList))
    return route