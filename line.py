from algorithms import Algorithms

class Line:
    def __init__(self) -> None:
        self.waiting_customers = list()


    def add_customer(self, customer):
        self.waiting_customers.append(customer)
    

    def remove_customer(self, customer):
        self.waiting_customers.remove(customer)
    
    
    def next_customer(self, algorithm):
        if algorithm == Algorithms.FIFO:
            next_customer = self.fifo()

        return next_customer


    def fifo(self):
        return self.waiting_customers[0]