from enum import Enum
import customer, queue, simulation
from simulation import EventType

class Algorithms(Enum):
    FIFO = 1


def nice_print(current_state, current_event, current_customer):
    print(str(current_event['Event Type']).ljust(30) + '\t' + str(round(current_event['Event Time'], 3)).ljust(15) + '\t' + str(current_customer).ljust(15))


dock_management = simulation.Simulation(time= 100, algorithm= Algorithms.FIFO, number_of_cashiers=3)

#Initial State
dock_management.fel
