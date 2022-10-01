from enum import Enum

class CustomerStatus(Enum):
    WAITING = 1
    SERVING = 2
    END = 3

class Customer:
    next_id = 1

    def __init__(self, type, queue, simulation):
        self.id = Customer.next_id
        self.type = type
        self.status = CustomerStatus.WAITING
        self.queue = queue
        self.simulation = simulation
        Customer.next_id += 1

    def start_service(self, clock):
        self.status = CustomerStatus.SERVING
        self.start_time = clock

    def end_service(self, clock):
        self.status = CustomerStatus.END
        self.end_time = clock

        #Calculate waiting times
        self.queue_waiting_time = self.start_time - self.arrival_time
        self.total_time = self.end_time - self.arrival_time