from consts import Algorithms

class Line:
    def __init__(self) -> None:
        self.waiting_customers = list()


    def add_customer(self, customer):
        self.waiting_customers.append(customer)
    

    def remove_customer(self, customer):
        self.waiting_customers.remove(customer)
    
    
    def next_customer(self, algorithm, clock):
        if algorithm == Algorithms.FIFO:
            next_customer = self.fifo()
        
        elif algorithm == Algorithms.SJF:
            next_customer = self.sjf()

        elif algorithm == Algorithms.HRRN:
            next_customer = self.hrrn(clock)
        
        elif algorithm == Algorithms.SCALED_T:
            next_customer = self.scaled_t(clock)

        self.remove_customer(next_customer)

        return next_customer


    def fifo(self):
        return self.waiting_customers[0]

    
    def sjf(self):
        sort_by_sjf = min(self.waiting_customers, key= lambda customer: customer.duration)
        return sort_by_sjf

    
    def hrrn(self, clock):
        for customer in self.waiting_customers:
            customer.get_hrrn_score(clock)

        sort_by_hrrn = max(self.waiting_customers, key= lambda customer: customer.score)
        return sort_by_hrrn

    
    def scaled_t(self, clock):
        for customer in self.waiting_customers:
            customer.get_waiting_time(clock)
        
        min_waiting_time = min(self.waiting_customers, key= lambda customer: customer.waiting_time).waiting_time
        max_waiting_time = max(self.waiting_customers, key= lambda customer: customer.waiting_time).waiting_time

        for customer in self.waiting_customers:
            customer.get_scaled_t_score(min_waiting_time, max_waiting_time)

        
        sort_by_scaled_t = max(self.waiting_customers, key= lambda customer: customer.score)
        return sort_by_scaled_t
        
        