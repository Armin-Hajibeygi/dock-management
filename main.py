from enum import Enum
import customer, queue, simulation
from simulation import EventType

class Algorithms(Enum):
    FIFO = 1


dock_management = simulation.Simulation(time= 100, algorithm= Algorithms.FIFO, number_of_cashiers=3)

#Initial State
