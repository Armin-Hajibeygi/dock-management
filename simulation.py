import line
from customer import Customer, CustomerStatus
from consts import exponential, Interval
from consts import CustomerType as CustomerType
from consts import EventType as EventType


class Simulation:
    def __init__(self, simulation_time, algorithm, number_of_cashiers) -> None:
        self.simulation_time = simulation_time
        self.algorithm = algorithm
        self.number_of_cashiers = number_of_cashiers
        self.clock = 0
        self.total_served_customers = 0
        self.max_queue_length = 0
        self.customers = list()
        self.fel = list()
        self.main_line = line.Line()
        self.number_of_customers = ({"Total": 0, CustomerType.A1.name: 0, CustomerType.A2.name: 0, CustomerType.B1.name: 0, CustomerType.B2.name: 0, CustomerType.C1.name: 0, CustomerType.C2.name: 0 })
    

    def fel_maker(self, event_type, event_time, customer=None):
        self.fel.append({"Event Type": event_type, "Event Time": event_time, "Customer": customer})
    

    def next_event(self):
        current_event = min(self.fel, key=lambda x: x['Event Time'])
        event_type = current_event["Event Type"]
        event_time = current_event['Event Time']
        customer = current_event['Customer']

        self.fel.remove(current_event)

        return event_type, event_time, customer
    

    def event_processor(self):
        event_type, event_time, customer = self.next_event()

        #Nice Print of the Event
        # try:
        #     try:
        #         print(str(event_type).ljust(30) + '\t' + str(round(event_time, 3)).ljust(15) + '\t' + ("Customer" + str(customer.id)).ljust(15) + '\t' + (customer.type.name).ljust(15) + '\t' + (str(round(customer.score, 3)).ljust(15)))
        #     except:
        #         print(str(event_type).ljust(30) + '\t' + str(round(event_time, 3)).ljust(15) + '\t' + ("Customer" + str(customer.id)).ljust(15) + '\t' + (customer.type.name).ljust(15))
        # except:
        #     print(str(event_type).ljust(30) + '\t' + str(round(event_time, 3)).ljust(15))            

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
            
            if (self.main_line.line_length() > self.max_queue_length):
                self.max_queue_length = self.main_line.line_length()
        
        #Interval between arrival of customers based on customer type
        if (customer.type == CustomerType.A1):
            interval = exponential(Interval.A1)
        elif (customer.type == CustomerType.A2):
            interval = exponential(Interval.A2)
        elif (customer.type == CustomerType.B1):
            interval = exponential(Interval.B1)
        elif (customer.type == CustomerType.B2):
            interval = exponential(Interval.B2)
        elif (customer.type == CustomerType.C1):
            interval = exponential(Interval.C1)
        elif (customer.type == CustomerType.C2):
            interval = exponential(Interval.C2)

        if (self.total_customers() <= 300):
            #Create Next Customer
            new_customer_type = customer.type
            new_customer = Customer(new_customer_type)

            #Create the next arrival event
            self.fel_maker(EventType.ARRIVAL, self.clock + interval, new_customer)
    
    
    def start_service(self, customer):
        customer.start_service(self.clock)
        self.number_of_cashiers -= 1

        #Duration of service        
        duration = customer.duration
        
        #Remove customer from the line if it's from the line
        if (customer in self.main_line.waiting_customers):
            self.main_line.remove_customer(customer)
        
        #Create end of service event
        self.fel_maker(EventType.END, self.clock + duration, customer)


    def end_service(self, customer):
        customer.end_service(self.clock)
        self.total_served_customers += 1
        self.number_of_cashiers += 1

        #Create next service event
        if (len(self.main_line.waiting_customers) > 0):
            next_customer = self.main_line.next_customer(self.algorithm, self.clock)
            self.fel_maker(EventType.SERVING, self.clock, next_customer)

    
    def total_customers(self):
        return len(self.customers)


    def simulation_data(self):
        simulation_data = dict()
        simulation_data["A1"] = {"Total": 0, "Served": 0, "Time in Queue": 0}
        simulation_data["A2"] = {"Total": 0, "Served": 0, "Time in Queue": 0}
        simulation_data["B1"] = {"Total": 0, "Served": 0, "Time in Queue": 0}
        simulation_data["B2"] = {"Total": 0, "Served": 0, "Time in Queue": 0}
        simulation_data["C1"] = {"Total": 0, "Served": 0, "Time in Queue": 0}
        simulation_data["C2"] = {"Total": 0, "Served": 0, "Time in Queue": 0}

        for customer in self.customers:
            simulation_data[customer.type.name]["Total"] += 1
            if (customer.get_served()):
                simulation_data[customer.type.name]["Served"] += 1
                simulation_data[customer.type.name]["Time in Queue"] += customer.get_queue_waiting_time()
            else:
                simulation_data[customer.type.name]["Time in Queue"] += customer.get_waiting_time(self.simulation_time)
            
        return simulation_data
    

    def get_max_queue_length(self):
        return self.max_queue_length
    
    
    def get_total_time_in_queue(self):
        total_time_in_queue = 0
        total_served = 0
        for customer in self.customers:
            if (customer.get_served()):
                total_time_in_queue += customer.get_queue_waiting_time()
                total_served += 1
                
        return (total_time_in_queue / total_served)