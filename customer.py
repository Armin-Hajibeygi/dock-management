from enum import Enum
from consts import Duration, CustomerType, CustomerStatus, CustomerWeight

class Customer:
    customer_id = 1
    
    def __init__(self, type) -> None:
        self.id = Customer.customer_id
        Customer.customer_id += 1
        self.type = type

        if (self.type == CustomerType.A1):
            self.duration = Duration.A1
        elif (self.type == CustomerType.A2):
            self.duration = Duration.A2
        elif (self.type == CustomerType.B1):
            self.duration = Duration.B1
        elif (self.type == CustomerType.B2):
            self.duration = Duration.B2
        elif (self.type == CustomerType.C1):
            self.duration = Duration.C1
        elif (self.type == CustomerType.C2):
            self.duration = Duration.C2


    def arrival(self, clock):
        self.arrival_time = clock
        self.status = CustomerStatus.ARRIVED


    def start_service(self, clock):
        self.start_time = clock
        self.status = CustomerStatus.SERVING


    def end_service(self, clock):
        self.end_time = clock
        self.status = CustomerStatus.END

        #Calculate waiting times
        self.queue_waiting_time = self.start_time - self.arrival_time
        self.total_time = self.end_time - self.arrival_time

    
    def get_served(self):
        if (self.status == CustomerStatus.END):
            return True
        return False

    
    def get_waiting_time(self, clock):
        self.waiting_time = clock - self.arrival_time

    
    def get_hrrn_score(self, clock):
        self.get_waiting_time(clock)
        self.score = 1 + (self.waiting_time / self.duration)

    
    def get_scaled_t_score(self, min, max):
        t_score = 100 * ((self.waiting_time - min) / (max - min))
        
        if (self.type == CustomerType.A1):
            w_score = CustomerWeight.A1
        elif (self.type == CustomerType.A2):
            w_score = CustomerWeight.A2
        elif (self.type == CustomerType.B1):
            w_score = CustomerWeight.B1
        elif (self.type == CustomerType.B2):
            w_score = CustomerWeight.B2
        elif (self.type == CustomerType.C1):
            w_score = CustomerWeight.C1
        elif (self.type == CustomerType.C2):
            w_score = CustomerWeight.C2

        self.score =  t_score + w_score