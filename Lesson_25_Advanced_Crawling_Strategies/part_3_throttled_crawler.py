import time

class ThrottledCrawler:
    def __init__(self):
        self.visited_urls = set()

    def crawl_with_throttle(self, url):
        if url not in self.visited_urls:
            self.visited_urls.add(url)
            print(f"Fetching: {url}")
            response = requests.get(url)
            if response.status_code == 200:
                print("Page fetched successfully.")
                # Process the content
            else:
                print(f"Error fetching {url}: {response.status_code}")
            time.sleep(2)  # Throttle to 2 seconds between requests
        else:
            print(f"Already visited: {url}")
