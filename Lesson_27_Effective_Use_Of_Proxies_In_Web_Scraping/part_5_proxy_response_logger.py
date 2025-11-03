import time

def log_response_time(proxy):
    start_time = time.time()
    try:
        response = requests.get('http://example.com', proxies=proxy, timeout=5)
        end_time = time.time()
        return response.status_code, end_time - start_time
    except Exception as e:
        return None, None

for proxy in working_proxies:
    status, response_time = log_response_time({'http': proxy})
    if status is not None:
        print(f"Proxy: {proxy} | Status: {status} | Response Time: {response_time:.2f} seconds")
