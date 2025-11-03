import time
import requests
import random

def random_throttle_scrape(url):
    response = requests.get(url)
    print(f"Scraped: {url} with status code: {response.status_code}")
    delay = random.uniform(1, 5)  # Random delay between 1 to 5 seconds
    time.sleep(delay)

urls_to_scrape = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

for url in urls_to_scrape:
    random_throttle_scrape(url)
