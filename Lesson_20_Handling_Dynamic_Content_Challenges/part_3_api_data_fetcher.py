import time
import random

for i in range(10):
    response = requests.get('http://example-angularjs-site.com/api/data')
    print(response.json())
    time.sleep(random.uniform(1, 5))  # Sleep for a random time between 1 and 5 seconds
