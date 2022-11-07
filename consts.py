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
    A1 = 50
    A2 = 100
    B1 = 150
    B2 = 300
    C1 = 400
    C2 = 500


class Interval():
    A1 = 100
    A2 = 200
    B1 = 300
    B2 = 400
    C1 = 500
    C2 = 600


class CustomerWeight():
    A1 = 1
    A2 = 2
    B1 = 3
    B2 = 4
    C1 = 5
    C2 = 6