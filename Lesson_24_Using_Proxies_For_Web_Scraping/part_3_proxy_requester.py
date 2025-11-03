import requests
import random
from time import sleep

proxy_list = [
    'http://proxy1_ip:port',
    'http://proxy2_ip:port',
    'http://proxy3_ip:port',
]

def get_random_proxy():
    return random.choice(proxy_list)

def make_request(url, retries=3):
    for attempt in range(retries):
        proxy = get_random_proxy()
        try:
            response = requests.get(url, proxies={'http': proxy, 'https': proxy}, timeout=5)
            response.raise_for_status()  # Raise an error for bad responses
            return response
        except (requests.exceptions.RequestException, requests.exceptions.Timeout) as e:
            print(f"Attempt {attempt + 1} failed with proxy {proxy}. Retrying...")
            sleep(2)  # Wait before retrying
    print("All attempts failed. Please check your proxies.")
    return None

url = 'https://example.com'
response = make_request(url)

if response:
    print(response.status_code)
    print(response.content)
