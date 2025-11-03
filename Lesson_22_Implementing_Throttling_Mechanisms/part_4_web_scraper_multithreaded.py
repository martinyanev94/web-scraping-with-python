import time
import requests
from queue import Queue
from threading import Thread

def worker(q):
    while not q.empty():
        url = q.get()
        try:
            response = requests.get(url)
            print(f"Scraped: {url} with status code: {response.status_code}")
        finally:
            q.task_done()
            time.sleep(2)  # Throttle the request rate

url_queue = Queue()
urls_to_scrape = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

for url in urls_to_scrape:
    url_queue.put(url)

for _ in range(3):  # Number of worker threads
    thread = Thread(target=worker, args=(url_queue,))
    thread.start()

url_queue.join()  # Wait for all tasks to complete
