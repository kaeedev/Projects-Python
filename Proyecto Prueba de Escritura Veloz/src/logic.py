import timeit

class TypingSpeedTest:
    def __init__(self):
        self.phrase = ""
        self.start_time = None
        self.end_time = None

    def start_timer(self):
        self.start_time = timeit.default_timer()

    def stop_timer(self):
        self.end_time = timeit.default_timer()

    def get_time(self):
        return round(self.end_time - self.start_time, 2)

    def check_accuracy(self, user_input):
        return user_input == self.phrase
