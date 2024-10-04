import json
import time

with open('settings.json', 'r') as file:
    data = json.load(file)
    
DEBUG = data["DEBUG"]

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def timer_start(self):
        if DEBUG:
            self.start_time = time.time()
            print("Timer started...")

    def timer_stop(self):
        if DEBUG:
            if self.start_time is None:
                print("Timer has not been started yet.")
                return
            
            self.end_time = time.time()
            elapsed_time = self.end_time - self.start_time
            print(f"Timer stopped. Elapsed time: {elapsed_time:.2f} seconds")
            return elapsed_time


my_timer = Timer()