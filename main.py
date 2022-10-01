import customer, simulation
from consts import Algorithms

simulation_time = 8*60
dock_management = simulation.Simulation(simulation_time= simulation_time, algorithm= Algorithms.FIFO, number_of_cashiers= 3)

#Initial State
customer1 = customer.Customer(simulation.CustomerType.A1)
customer2 = customer.Customer(simulation.CustomerType.A2)
customer3 = customer.Customer(simulation.CustomerType.B1)
customer4 = customer.Customer(simulation.CustomerType.B2)
customer5 = customer.Customer(simulation.CustomerType.C1)
customer6 = customer.Customer(simulation.CustomerType.C2)

dock_management.fel_maker(simulation.EventType.ARRIVAL, 0, customer1)
dock_management.fel_maker(simulation.EventType.ARRIVAL, 0, customer2)
dock_management.fel_maker(simulation.EventType.ARRIVAL, 0, customer3)
dock_management.fel_maker(simulation.EventType.ARRIVAL, 0, customer4)
dock_management.fel_maker(simulation.EventType.ARRIVAL, 0, customer5)
dock_management.fel_maker(simulation.EventType.ARRIVAL, 0, customer6)

dock_management.fel_maker("End of Simulation", simulation_time)


#Start Simulation with discrete event processing
dock_management.event_processor()

#Print Statistics from Simulation
print('-------------------------------------------------------------------------------------------------')
print(f"Total Customers in Simulation: {dock_management.total_customers()}")
print(f"Total Served Customers in Simulation: {dock_management.total_served_customers()}")
print('-------------------------------------------------------------------------------------------------')
for k, v in dock_management.number_of_customers.items():
    print(f"Number of {k} Customers: {v}")
print('-------------------------------------------------------------------------------------------------')