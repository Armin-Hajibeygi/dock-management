from main import Algorithms
from enum import Enum


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


class SimQueue:
    def __init__(self, simulation):
        self.waiting_customers = list()
        self.simulation = simulation


    def add_customer(self, customer):
        self.waiting_customers.append(customer)


    def start_service(self, clock, customer):
        #Duration of service
        if (customer.type == CustomerType.A1):
            duration = 1

        #Create end of service event
        self.simulation.fel_maker(EventType.END, clock + duration, customer)

        self.simulation.number_of_cashiers -= 1

        self.remove_from_waiting_customers(customer)
        customer.start_service(clock)


    def end_service(self, clock, customer):
        self.simulation.number_of_cashiers += 1
        customer.end_service(clock)

        #Create next service event
        next_customer = self.next_customer()
        self.simulation.fel_maker(EventType.SERVING, clock, next_customer)



    def next_customer(self):
        if self.simulation.algorithm == Algorithms.FIFO:
            next_customer = self.fifo()

        return next_customer


    def fifo(self):
        return self.waiting_customers[0]


    def remove_from_waiting_customers(self, customer):
        self.waiting_customers.remove(customer)
