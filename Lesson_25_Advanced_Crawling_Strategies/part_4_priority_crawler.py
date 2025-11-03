import heapq

class PriorityCrawler:
    def __init__(self):
        self.visited_urls = set()
        self.priority_queue = []

    def add_to_queue(self, url, priority):
        heapq.heappush(self.priority_queue, (priority, url))

    def crawl(self):
        while self.priority_queue:
            priority, url = heapq.heappop(self.priority_queue)
            if url not in self.visited_urls:
                print(f"Visiting: {url} with priority {priority}")
                self.visited_urls.add(url)
                # Fetch and process the page
