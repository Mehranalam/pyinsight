import random
import time

class LiveDataPlot:
    def __init__(self, update_interval=1):
        self.update_interval = update_interval
        self.data = []

    def start(self):
        print("Starting live data feed...")
        try:
            while True:
                new_data = random.randint(0, 100)
                self.data.append(new_data)
                print(f"New data: {new_data}")
                time.sleep(self.update_interval)
        except KeyboardInterrupt:
            print("Live data feed stopped.")
