import time
import requests

def scrape_with_throttling(url, delay):
    response = requests.get(url)
    print(f"Scraped: {url} with status code: {response.status_code}")
    time.sleep(delay)

urls_to_scrape = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

for url in urls_to_scrape:
    scrape_with_throttling(url, delay=2)  # Delay for 2 seconds
