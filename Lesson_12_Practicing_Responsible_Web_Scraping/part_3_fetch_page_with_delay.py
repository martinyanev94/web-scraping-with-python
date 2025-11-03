import time
import random

def fetch_page(url):
    time_delay = random.uniform(1, 5)  # Random delay between requests
    print(f"Waiting for {time_delay:.2f} seconds before fetching {url}...")
    time.sleep(time_delay)
    # Include your request logic here
