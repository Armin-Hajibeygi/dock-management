import customer, simulation
from consts import Algorithms

simulation_time = 8*60
dock_management = simulation.Simulation(simulation_time= simulation_time, algorithm= Algorithms.FIFO, number_of_cashiers= 3)

#Initial State
customer1 = customer.Customer(simulation.CustomerType.A1)
dock_management.fel_maker(simulation.EventType.ARRIVAL, 0, customer1)
dock_management.fel_maker("End of Simulation", simulation_time)


#Start Simulation with discrete event processing
dock_management.event_processor()

#Print Statistics from Simulation
print('-------------------------------------------------------------------------------------------------')
print(f"Total Customers in Simulation: {dock_management.total_customers()}")
print(f"Total Served Customers in Simulation: {dock_management.total_served_customers()}")
print('-------------------------------------------------------------------------------------------------')