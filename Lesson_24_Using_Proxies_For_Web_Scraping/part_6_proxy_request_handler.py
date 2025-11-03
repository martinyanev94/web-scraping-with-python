import requests

service_url = 'https://api.proxyservice.com/get_proxy'
response = requests.get(service_url)

if response.status_code == 200:
    proxy_ip = response.json().get('proxy')
    print(f"Using proxy: {proxy_ip}")
    response = requests.get('https://example.com', proxies={'http': proxy_ip, 'https': proxy_ip})
    print(response.content)
else:
    print("Failed to retrieve proxy.")
