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
    CREATED = 0
    ARRIVED = 1
    SERVING = 2
    END = 3


class Algorithms(Enum):
    FIFO = 1
    SJF = 2
    HRRN = 3
    SCALED_T = 4

#Duration Parameters for Exponential Function
class Duration():
    A1 = 0.291
    A2 = 0.083
    B1 = 0.256
    B2 = 0.054
    C1 = 0.231
    C2 = 0.059

#Interval Parameters for Exponential Function
class Interval():
    A1 = 0.241
    A2 = 0.145
    B1 = 0.240
    B2 = 0.403
    C1 = 0.008
    C2 = 0.009


class CustomerWeight():
    A1 = 45
    A2 = 35
    B1 = 25
    B2 = 15
    C1 = 5
    C2 = 0