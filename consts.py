from enum import Enum
import random, math

#Random Distribution
#Crate Exponential Distributed Variables
def exponential(lambd):
    r = random.random()
    return -(1 / lambd) * math.log(1 - r,math.e)


class Algorithms(Enum):
    FIFO = 1


class Duration():
    A1 = 90
    A2 = 2
    B1 = 3
    B2 = 4
    C1 = 5
    C2 = 6


class Interval():
    A1 = 10
    A2 = 2
    B1 = 3
    B2 = 4
    C1 = 5
    C2 = 6