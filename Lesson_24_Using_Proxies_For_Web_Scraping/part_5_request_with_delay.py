import time

def make_request_with_delay(url, delay=3):
    response = make_request(url)
    if response:
        print(response.status_code)
        print(response.content)
    time.sleep(delay)  # Wait before next request

# Example scraping loop
for _ in range(5):  # Let's assume we want to make 5 requests
    make_request_with_delay('https://example.com')
