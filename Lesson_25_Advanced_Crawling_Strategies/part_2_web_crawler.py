from collections import deque

class Crawler:
    def __init__(self):
        self.visited_urls = set()

    def depth_first_search(self, url):
        if url not in self.visited_urls:
            print(f"Visiting: {url}")
            self.visited_urls.add(url)
            # Fetch and extract links, then recurse
            # Here we assume `get_links` fetches links from the page
            for link in get_links(url):
                self.depth_first_search(link)

    def breadth_first_search(self, starting_url):
        queue = deque([starting_url])
        while queue:
            current_url = queue.popleft()
            if current_url not in self.visited_urls:
                print(f"Visiting: {current_url}")
                self.visited_urls.add(current_url)
                # Fetch and extract links, then add to queue
                for link in get_links(current_url):
                    if link not in self.visited_urls:
                        queue.append(link)

# Assuming get_links is defined to extract links from pages
