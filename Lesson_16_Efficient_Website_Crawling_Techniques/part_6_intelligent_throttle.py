import time
import random

class IntelligentThrottle:
    def __init__(self, base_wait=1, randomness=0.5):
        self.base_wait = base_wait
        self.randomness = randomness
    
    def wait(self):
        wait_time = self.base_wait + random.uniform(0, self.randomness)
        time.sleep(wait_time)

# Example usage
throttler = IntelligentThrottle(base_wait=2, randomness=1)

for _ in range(5):
    print("Crawling...")
    throttler.wait()
