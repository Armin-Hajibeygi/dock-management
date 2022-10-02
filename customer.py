from enum import Enum

class CustomerStatus(Enum):
    ARRIVED = 1
    SERVING = 2
    END = 3


class Customer:
    customer_id = 1
    
    def __init__(self, type) -> None:
        self.id = Customer.customer_id
        Customer.customer_id += 1
        self.type = type


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