from enum import Enum
import customer, simulation


class Algorithms(Enum):
    FIFO = 1

dock_management = simulation.Simulation(simulation_time= 8*60, algorithm= Algorithms.FIFO, number_of_cashiers= 3)

#Initial State
customer1 = customer.Customer(simulation.CustomerType.A1)
dock_management.fel_maker(simulation.EventType.ARRIVAL, 0, customer1)


#Start Simulation with discrete event processing
dock_management.event_processor()