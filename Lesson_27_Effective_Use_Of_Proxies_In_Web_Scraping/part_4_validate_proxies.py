def validate_proxy(proxy):
    try:
        response = requests.get('http://example.com', proxies=proxy, timeout=5)
        return response.status_code == 200
    except Exception as e:
        return False

working_proxies = [proxy for proxy in proxies_list if validate_proxy({'http': proxy})]
print("Working Proxies:", working_proxies)
