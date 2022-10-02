from enum import Enum
import random, math

#Random Distribution
#Crate Exponential Distributed Variables
def exponential(lambd):
    r = random.random()
    return -(1 / lambd) * math.log(1 - r,math.e)


class Algorithms(Enum):
    FIFO = 1
    SJF = 2


class Duration():
    A1 = 5
    A2 = 10
    B1 = 15
    B2 = 30
    C1 = 40
    C2 = 50


class Interval():
    A1 = 10
    A2 = 20
    B1 = 30
    B2 = 40
    C1 = 50
    C2 = 60