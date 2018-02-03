from time import time

class RPSCounter:
    def __init__(self):
        self.start_time = time()
        self.total_requests = 1
        self.previous_datavector = None
        self.timer = [0, 0]
        self.timer_index = 0

    def get(self):
        self.total_requests += 1
        self.timer[self.timer_index] += 1
        self.elapsed = time() - self.start_time

        if self.elapsed > 1:
            self.start_time = time()
            self.timer_index = 1
            self.timer[0] = (self.timer[0] + self.timer[1]) / 2  
            self.timer[1] = 0

        rps = self.timer[0]

        return rps