from enum import Enum, IntEnum
import random, math

#Random Distribution
#Crate Exponential Distributed Variables
def exponential(lambd):
    r = random.random()
    return -(1 / lambd) * math.log(1 - r,math.e)

class CustomerType(IntEnum):
    A1 = 1
    A2 = 2
    B1 = 3
    B2 = 4
    C1 = 5
    C2 = 6


class EventType(Enum):
    ARRIVAL = 1
    SERVING = 2
    END = 3


class CustomerStatus(Enum):
    ARRIVED = 1
    SERVING = 2
    END = 3


class Algorithms(Enum):
    FIFO = 1
    SJF = 2
    HRRN = 3
    SCALED_T = 4


class Duration():
    A1 = 10
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


class CustomerWeight():
    A1 = 1
    A2 = 2
    B1 = 3
    B2 = 4
    C1 = 5
    C2 = 6