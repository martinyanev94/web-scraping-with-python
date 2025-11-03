import time
import threading

class Throttle:
    def __init__(self, delay):
        self.delay = delay
        self.last_accessed = {}
        self.lock = threading.Lock()

    def wait(self, domain):
        with self.lock:
            current_time = time.time()
            # If this domain was accessed recently
            if domain in self.last_accessed:
                elapsed_time = current_time - self.last_accessed[domain]
                if elapsed_time < self.delay:
                    time_to_wait = self.delay - elapsed_time
                    print(f"Throttling request to {domain}. Waiting for {time_to_wait:.2f} seconds.")
                    time.sleep(time_to_wait)
            self.last_accessed[domain] = time.time()
