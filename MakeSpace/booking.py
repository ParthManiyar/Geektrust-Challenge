class Booking:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def overlap(self, start_time, end_time):
        return((self.start_time <= start_time < self.end_time)
               or (self.start_time < end_time < self.end_time)
               or (start_time <= self.start_time < end_time)
               or (start_time < self.end_time < end_time))
