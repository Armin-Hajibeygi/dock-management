import math, random
import sim_queue
from customer import Customer

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
        self.queue = sim_queue.SimQueue(self)
        self.number_of_customers = ({"Total": 0, sim_queue.CustomerType.A1.name: 0, sim_queue.CustomerType.A2.name: 0, sim_queue.CustomerType.B1.name: 0, sim_queue.CustomerType.B2.name: 0,sim_queue.CustomerType.C1.name: 0, sim_queue.CustomerType.C2.name: 0 })


    def fel_maker(self, event_type, event_time, customer=None):
        self.fel.append({"Event Type": event_type, "Event Time": event_time, "Customer": customer})

    
    def event_processor(self):
        event_type, event_time, customer = self.next_event()

        #Nice Print of the Event
        print(str(event_type).ljust(30) + '\t' + str(round(event_time, 3)).ljust(15) + '\t' + ("Customer" + str(customer.id)).ljust(15))

        #Forward Time to nearest event
        self.clock = event_time

        if (self.clock > self.time):
            self.fel.clear()
            return

        if (event_type == sim_queue.EventType.ARRIVAL):
            self.arrival(customer)
            customer.arrival_time = self.clock
        elif (event_type == sim_queue.EventType.SERVING):
            self.queue.start_service(self.clock, customer)
        elif (event_type == sim_queue.EventType.END):
            pass

        if (len(self.fel) > 0):
            self.event_processor()


    def next_event(self):
        sorted_fel = sorted(self.fel, key=lambda x: x['Event Time'])
        current_event = sorted_fel[0]
        event_type = current_event["Event Type"]
        event_time = current_event['Event Time']
        customer = current_event['Customer']

        self.fel.remove(current_event)

        return event_type, event_time, customer


    def arrival(self, customer):
        #Add Customer
        self.number_of_customers["Total"] += 1
        self.number_of_customers[customer.type.name] += 1

        #If we have free cashiers, the service should begin
        if (self.number_of_cashiers > 0):
            self.queue.start_service(self.clock, customer)
            self.fel_maker(sim_queue.EventType.SERVING, self.clock, customer)
        
        #If there is no cashiers, the customer should go to the queue
        else:
            self.queue.add_customer(customer)
        
        #Interval between arrival of customers based on customer type
        if (customer.type == sim_queue.CustomerType.A1):
            interval = 0.1

        #Create Next Customer
        new_customer_type = customer.type
        new_customer = Customer(new_customer_type, self.queue, self)
        self.customers.append(new_customer)

        #Create the next arrival event
        self.fel_maker(sim_queue.EventType.ARRIVAL, self.clock + interval, new_customer)
