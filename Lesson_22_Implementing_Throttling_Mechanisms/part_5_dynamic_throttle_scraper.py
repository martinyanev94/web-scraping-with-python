import time
import requests
import logging

logging.basicConfig(level=logging.INFO)

def dynamic_throttle_scrape(url, base_delay=2):
    while True:
        start_time = time.time()
        try:
            response = requests.get(url)
            response.raise_for_status()
            logging.info(f"Scraped: {url} with status code: {response.status_code}")
            elapsed_time = time.time() - start_time
            logging.info(f"Time taken: {elapsed_time:.2f}s")
            
            # Adjust delay based on last request time
            if elapsed_time < base_delay:
                time.sleep(base_delay - elapsed_time)
            break
        except requests.HTTPError:
            logging.error(f"Failed to scrape {url}, retrying...")
            time.sleep(base_delay)

dynamic_throttle_scrape("https://example.com")
