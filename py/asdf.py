import numpy as np
import random

def data_read():
    with open("berlin52.tsp", 'r') as file:
       a = file[6:]
    return