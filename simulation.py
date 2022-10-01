import math, random
from enum import Enum
from queue import Queue
from customer import Customer


class EventType(Enum):
    ARRIVAL = 1
    SERVING = 2
    END = 3


class CustomerType(Enum):
    A1 = 1
    A2 = 2
    B1 = 3
    B2 = 4
    C1 = 5
    C2 = 6


#Random Distribution
#Crate Exponential Distributed Variables
def exponential(lambd):
    r = random.random()
    return -(1 / lambd) * math.log(1 - r,math.e)


class Simulation:
    def __init__(self, time, algorithm, number_of_cashiers):
        self.time = time
        self.algorithm = algorithm
        self.number_of_cashiers = number_of_cashiers
        self.clock = 0
        self.customers = list()
        self.fel = list()
        self.queue = Queue()
        self.number_of_customers = ({"Total": 0, CustomerType.A1.name: 0, CustomerType.A2.name: 0, CustomerType.B1.name: 0, CustomerType.B2.name: 0, CustomerType.C1.name: 0, CustomerType.C2.name: 0 })


    def fel_maker(self, event_type, event_time, customer=None):
        self.fel.append({"Event Type": event_type, "Event Time": event_time, "Customer": customer})

    
    def event_processor(self):
        event_type, event_time, customer = self.next_event()

        if (event_type == EventType.ARRIVAL):
            self.arrival(customer)
        elif (event_type == EventType.SERVING):
            pass
        elif (event_type == EventType.END):
            pass

        #Forward Time to nearest event
        self.clock = event_time

    
    def next_event(self):
        sorted_fel = sorted(self.fel, key=lambda x: x['Event Time'])
        current_event = sorted_fel[0]
        event_type = current_event["Event Type"]
        event_time = current_event['Event Time']
        customer = current_event['Customer']

        return event_type, event_time, customer


    def arrival(self, customer):
        #Add Customer
        self.number_of_customers["Total"] += 1
        self.number_of_customers[customer.customer_type.name] += 1

        #If we have free cashiers, the service should begin
        if (self.number_of_cashiers > 0):
            customer.start_service(self.clock)
        
        #If there is no cashiers, the customer should go to the queue
        else:
            self.queue.add_customer(customer)
        
        #Interval between arrival of customers based on customer type
        if (customer.type == CustomerType.A1):
            interval = 1

        #Create Next Customer 
        new_customer_id = Customer.next_id
        new_customer_arrival_time = self.clock + interval
        new_customer_type = customer.type
        new_customer = Customer(new_customer_id, new_customer_type, new_customer_arrival_time, self.queue, self)
        self.customers.append(new_customer)

        #Create the next arrival event
        self.fel_maker(EventType.ARRIVAL, self.clock + interval, new_customer)


