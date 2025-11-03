import time
import random

class Throttle:
    def __init__(self, base_wait=1, randomness=0.5):
        self.base_wait = base_wait
        self.randomness = randomness

    def wait(self):
        wait_time = self.base_wait + random.uniform(0, self.randomness)
        print(f"Sleeping for {wait_time} seconds")
        time.sleep(wait_time)
