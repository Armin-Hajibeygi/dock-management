from main import Algorithms

class Queue:
    def __init__(self):
        self.customers = list()
        self.waiting_customers = list()


    def add_customer(self, customer):
        self.customers.append(customer)
        self.waiting_customers.append(customer)


    def start_service(self, time, customer):
        self.simulation.number_of_cashiers -= 1
        self.remove_from_waiting_customers(customer)
        customer.start_serive(time)


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
