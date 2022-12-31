import customer, simulation
from consts import Algorithms, exponential, Interval
import os, sys

os.system('clear')

simulation_time = 8 * 60
simulation_algorithm = Algorithms.SJF
number_of_cashiers = 3

average_served_customers = 0
average_total_customers = 0
average_waiting_time_in_queue = 0
max_queue_length = 0
total_number_of_customers = {"A1": 0, "A2": 0, "B1": 0, "B2": 0, "C1": 0, "C2": 0}
number_of_served_customers = {"A1": 0, "A2": 0, "B1": 0, "B2": 0, "C1": 0, "C2": 0}
percent_of_served_customers = {"A1": 0, "A2": 0, "B1": 0, "B2": 0, "C1": 0, "C2": 0}
queue_waiting_time = {"A1": 0, "A2": 0, "B1": 0, "B2": 0, "C1": 0, "C2": 0}

number_of_simulation = 1000


for i in range(number_of_simulation):
    
    sys.setrecursionlimit(simulation_time * 10000)

    dock_management = simulation.Simulation(simulation_time,simulation_algorithm, number_of_cashiers)

    #Initial State
    customer1 = customer.Customer(simulation.CustomerType.A1)
    customer2 = customer.Customer(simulation.CustomerType.A2)
    customer3 = customer.Customer(simulation.CustomerType.B1)
    customer4 = customer.Customer(simulation.CustomerType.B2)
    customer5 = customer.Customer(simulation.CustomerType.C1)
    customer6 = customer.Customer(simulation.CustomerType.C2)

    dock_management.fel_maker(simulation.EventType.ARRIVAL, exponential(Interval.A1), customer1)
    dock_management.fel_maker(simulation.EventType.ARRIVAL, exponential(Interval.A2), customer2)
    dock_management.fel_maker(simulation.EventType.ARRIVAL, exponential(Interval.B1), customer3)
    dock_management.fel_maker(simulation.EventType.ARRIVAL, exponential(Interval.B2), customer4)
    dock_management.fel_maker(simulation.EventType.ARRIVAL, exponential(Interval.C1), customer5)
    dock_management.fel_maker(simulation.EventType.ARRIVAL, exponential(Interval.C2), customer6)

    dock_management.fel_maker("End of Simulation", simulation_time)
    
    print(i)
    
    #Start Simulation with discrete event processing
    dock_management.event_processor()
    
    average_served_customers += (dock_management.total_served_customers / number_of_simulation)
    average_total_customers += (dock_management.total_customers() / number_of_simulation)
    average_waiting_time_in_queue += (dock_management.get_total_time_in_queue() / number_of_simulation)
    
    if (dock_management.get_max_queue_length() > max_queue_length):
        max_queue_length = dock_management.get_max_queue_length()
    
    for category, data in dock_management.simulation_data().items():
        try:
            number_of_served_customers[category] += (data['Served'] / number_of_simulation)
            total_number_of_customers[category] += (data['Total'] / number_of_simulation)
            percent_of_served_customers[category] += ((data['Served'] / data['Total']) / number_of_simulation )
            queue_waiting_time[category] += ((data['Time in Queue'] / data['Total']) / number_of_simulation)
        except:
            pass
        
       
print(f"Algorithm: {simulation_algorithm.name}")
print('-------------------------------------------------------------------------------------------------')
print(f"Average Total Customers: {average_total_customers}")
print(f"Average Served Customers: {int((average_served_customers / average_total_customers) * 100 )}%")
print(f"Average Total time in Queue: {average_waiting_time_in_queue}")
print(f"Max Queue Length: {max_queue_length}")
print('-------------------------------------------------------------------------------------------------')
print(f"Average Served A1 Customers: {int(percent_of_served_customers['A1'] * 100)}%")
print(f"Average Served A2 Customers: {int(percent_of_served_customers['A2'] * 100)}%")
print(f"Average Served B1 Customers: {int(percent_of_served_customers['B1'] * 100)}%")
print(f"Average Served B2 Customers: {int(percent_of_served_customers['B2'] * 100)}%")
print(f"Average Served C1 Customers: {int(percent_of_served_customers['C1'] * 100)}%")
print(f"Average Served C2 Customers: {int(percent_of_served_customers['C2'] * 100)}%")
print('-------------------------------------------------------------------------------------------------')
print(f"Average Time in Queue for A1: {queue_waiting_time['A1']}")
print(f"Average Time in Queue for A2: {queue_waiting_time['A2']}")
print(f"Average Time in Queue for B1: {queue_waiting_time['B1']}")
print(f"Average Time in Queue for B2: {queue_waiting_time['B2']}")
print(f"Average Time in Queue for C1: {queue_waiting_time['C1']}")
print(f"Average Time in Queue for C2: {queue_waiting_time['C2']}")
print('-------------------------------------------------------------------------------------------------')
print(f"Total number of customers A1: {total_number_of_customers['A1']} - Served: {number_of_served_customers['A1']}")
print(f"Total number of customers A2: {total_number_of_customers['A2']} - Served: {number_of_served_customers['A2']}")
print(f"Total number of customers B1: {total_number_of_customers['B1']} - Served: {number_of_served_customers['B1']}")
print(f"Total number of customers B2: {total_number_of_customers['B2']} - Served: {number_of_served_customers['B2']}")
print(f"Total number of customers C1: {total_number_of_customers['C1']} - Served: {number_of_served_customers['C1']}")
print(f"Total number of customers C2: {total_number_of_customers['C2']} - Served: {number_of_served_customers['C2']}")
