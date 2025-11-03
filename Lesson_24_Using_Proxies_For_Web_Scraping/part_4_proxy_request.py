import requests

# Proxy with authentication
proxies = {
    'http': 'http://username:password@your_proxy_ip:port',
    'https': 'http://username:password@your_proxy_ip:port',
}

response = requests.get('https://example.com', proxies=proxies)

print(response.status_code)
print(response.content)
