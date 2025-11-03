import time
import random

def fetch_page_with_delay(url):
    time.sleep(random.uniform(1, 3))  # Random delay between 1 to 3 seconds
    return fetch_page(url)

with ThreadPoolExecutor(max_workers=5) as executor:
    html_pages = list(executor.map(fetch_page_with_delay, urls))
