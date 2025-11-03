import requests
import random

# Create a list of proxy IPs
proxy_list = [
    'http://proxy1_ip:port',
    'http://proxy2_ip:port',
    'http://proxy3_ip:port',
    # Add more proxies as needed
]

# Function to get a random proxy
def get_random_proxy():
    return random.choice(proxy_list)

# Example of sending a request using a random proxy
proxy = get_random_proxy()
response = requests.get('https://example.com', proxies={'http': proxy, 'https': proxy})

print(response.status_code)
print(response.content)
