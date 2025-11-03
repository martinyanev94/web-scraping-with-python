import requests

# Specify the proxy
proxies = {
    'http': 'http://your_proxy_ip:port',
    'https': 'http://your_proxy_ip:port',
}

# Sending a request through the proxy
response = requests.get('https://example.com', proxies=proxies)

print(response.status_code)
print(response.content)
