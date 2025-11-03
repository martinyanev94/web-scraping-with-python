import requests

proxy = {
    'http': 'http://username:password@proxyserver.com:port',
    'https': 'http://username:password@proxyserver.com:port',
}

response = requests.get('http://example.com', proxies=proxy)
print(response.text)
