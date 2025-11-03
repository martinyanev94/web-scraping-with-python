import time

for i in range(5):
    response = requests.get(url, headers=headers)
    print(f'Response code: {response.status_code}')
    time.sleep(2)  # Wait for 2 seconds before the next request
