import line
from customer import Customer, CustomerStatus
from enum import Enum
from consts import Duration, Interval


class CustomerType(Enum):
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

class Simulation:
    def __init__(self, simulation_time, algorithm, number_of_cashiers) -> None:
        self.simulation_time = simulation_time
        self.algorithm = algorithm
        self.number_of_cashiers = number_of_cashiers
        self.clock = 0
        self.customers = list()
        self.fel = list()
        self.main_line = line.Line()
        self.number_of_customers = ({"Total": 0, CustomerType.A1.name: 0, CustomerType.A2.name: 0, CustomerType.B1.name: 0, CustomerType.B2.name: 0, CustomerType.C1.name: 0, CustomerType.C2.name: 0 })
    

    def fel_maker(self, event_type, event_time, customer=None):
        self.fel.append({"Event Type": event_type, "Event Time": event_time, "Customer": customer})
    

    def next_event(self):
        sorted_fel = sorted(self.fel, key=lambda x: x['Event Time'])
        current_event = sorted_fel[0]
        event_type = current_event["Event Type"]
        event_time = current_event['Event Time']
        customer = current_event['Customer']

        self.fel.remove(current_event)

        return event_type, event_time, customer
    

    def event_processor(self):
        event_type, event_time, customer = self.next_event()

        #Nice Print of the Event
        try:
            print(str(event_type).ljust(30) + '\t' + str(round(event_time, 3)).ljust(15) + '\t' + ("Customer" + str(customer.id)).ljust(15))
        except:
            print(str(event_type).ljust(30) + '\t' + str(round(event_time, 3)).ljust(15))            

        #Forward Time to nearest event
        self.clock = event_time

        #End the simulation if time exceed simulation time
        if (self.clock >= self.simulation_time):
            self.fel.clear()
            return

        #Process the Event
        if (event_type == EventType.ARRIVAL):
            self.arrival(customer)
        elif (event_type == EventType.SERVING):
            self.start_service(customer)
        elif (event_type == EventType.END):
            self.end_service(customer)

        #Process the next event on Future_Event_List(FEL)
        if (len(self.fel) > 0):
            self.event_processor()
    

    def arrival(self, customer):
        #Add Customer
        self.customers.append(customer)
        customer.arrival(self.clock)
        self.number_of_customers["Total"] += 1
        self.number_of_customers[customer.type.name] += 1

        #If we have free cashiers, the service should begin
        if (self.number_of_cashiers > 0):
            self.fel_maker(EventType.SERVING, self.clock, customer)
        
        #If there is no cashiers, the customer should go to the queue
        else:
            self.main_line.add_customer(customer)
        
        #Interval between arrival of customers based on customer type
        if (customer.type == CustomerType.A1):
            interval = Interval.A1

        #Create Next Customer
        new_customer_type = customer.type
        new_customer = Customer(new_customer_type)

        #Create the next arrival event
        self.fel_maker(EventType.ARRIVAL, self.clock + interval, new_customer)
    
    
    def start_service(self, customer):
        customer.start_service(self.clock)
        self.number_of_cashiers -= 1

        #Duration of service
        if (customer.type == CustomerType.A1):
            duration = Duration.A1
        
        #Remove customer from the line if it's from the line
        if (customer in self.main_line.waiting_customers):
            self.main_line.remove_customer(customer)
        
        #Create end of service event
        self.fel_maker(EventType.END, self.clock + duration, customer)


    def end_service(self, customer):
        customer.end_service(self.clock)
        self.number_of_cashiers += 1

        #Create next service event
        if (len(self.main_line.waiting_customers) > 0):
            next_customer = self.main_line.next_customer(self.algorithm)
            self.fel_maker(EventType.SERVING, self.clock, next_customer)

    
    def total_customers(self):
        return len(self.customers)

    
    def total_served_customers(self):
        total_served_customers = 0
        for customer in self.customers:
            if (customer.status == CustomerStatus.END):
                total_served_customers += 1
        
        return total_served_customers