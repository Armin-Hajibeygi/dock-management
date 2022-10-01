from enum import Enum
import simulation

class CustomerStatus(Enum):
    WAITING = 1
    SERVING = 2
    END = 3

class Customer:
    def __init__(self, id, type, arrival_time, queue, simulation):
        self.id = id
        self.type = type
        self.arrival_time = arrival_time
        self.status = CustomerStatus.WAITING
        self.queue = queue
        self.simulation = simulation
        self.work_duration = simulation.exponential()

    def start_service(self, time):
        self.status = CustomerStatus.SERVING
        self.start_service = time
        self.end_time = self.start_service + self.work_duration
        self.simulation.fel_maker(simulation.EventType.END, self.end_time, self.id)  

    def end_service(self):
        self.status = CustomerStatus.END