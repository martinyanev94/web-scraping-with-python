import random

proxies_list = [
    'http://username:password@proxy1.com:port',
    'http://username:password@proxy2.com:port',
    'http://username:password@proxy3.com:port',
]

def get_random_proxy(proxies):
    return {'http': random.choice(proxies), 'https': random.choice(proxies)}

for _ in range(10):  # Example: Attempt 10 requests
    proxy = get_random_proxy(proxies_list)
    response = requests.get('http://example.com', proxies=proxy)
    print(response.status_code)
