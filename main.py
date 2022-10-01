from enum import Enum
import customer, sim_queue, simulation

class Algorithms(Enum):
    FIFO = 1


dock_management = simulation.Simulation(time= 100, algorithm= Algorithms.FIFO, number_of_cashiers=3)

#Initial State
customer1 = customer.Customer(sim_queue.CustomerType.A1, dock_management.queue, dock_management)
dock_management.fel_maker(sim_queue.EventType.ARRIVAL, 0, customer1)


#Start Simulation with discrete event processing
dock_management.event_processor()
