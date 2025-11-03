import random

class Throttle:
    ...
    def wait(self, domain):
        with self.lock:
            current_time = time.time()
            if domain in self.last_accessed:
                elapsed_time = current_time - self.last_accessed[domain]
                if elapsed_time < self.delay:
                    # Adding a randomization factor
                    sleep_time = self.delay + random.uniform(1, 3)  # Random add-on of 1 to 3 seconds
                    print(f"Throttling request to {domain}. Waiting for {sleep_time:.2f} seconds.")
                    time.sleep(sleep_time)
            self.last_accessed[domain] = time.time()
