import time
import requests

def scrape_with_exponential_backoff(url, max_retries=5):
    delay = 1  # Start with 1 second
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Will raise an HTTPError for bad responses
            print(f"Successfully scraped: {url} with status code: {response.status_code}")
            return response.text
        except requests.HTTPError as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
            delay *= 2  # Double the delay for the next attempt
    print(f"Failed to scrape {url} after {max_retries} attempts.")

scrape_with_exponential_backoff("https://example.com")
