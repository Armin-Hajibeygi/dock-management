from consts import Algorithms

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
        
        elif algorithm == Algorithms.SJF:
            next_customer = self.sjf()

        return next_customer


    def fifo(self):
        return self.waiting_customers[0]

    
    def sjf(self):
        sort_by_sjf = sorted(self.waiting_customers, key= lambda customer: customer.type)
        return sort_by_sjf[0]