import time

def measure_load_time(url):
    start_time = time.time()
    requests.get(url)
    end_time = time.time()
    load_time = end_time - start_time
    return load_time

load_time = measure_load_time(url)
print(f'Load time for {url}: {load_time:.2f} seconds')
