from main import Algorithms
from simulation import CustomerType, EventType
class Queue:
    def __init__(self):
        self.waiting_customers = list()


    def add_customer(self, customer):
        self.waiting_customers.append(customer)


    def start_service(self, time, customer):
        #Duration of service
        if (customer.type == CustomerType.A1):
            duration = 1

        #Create end of service event
        self.fel_maker(EventType.END, time + duration, customer)

        self.simulation.number_of_cashiers -= 1

        self.remove_from_waiting_customers(customer)
        customer.start_service(time)


    def end_service(self, customer):
        self.simulation.number_of_cashiers += 1
        customer.end_service()


    def next_customer(self):
        if self.simulation.algorithm == Algorithms.FIFO:
            next_customer = self.fifo()

        return next_customer


    def fifo(self):
        return self.waiting_customers[0]


    def remove_from_waiting_customers(self, customer):
        self.waiting_customers.remove(customer)
