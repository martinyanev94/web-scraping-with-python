import time
import random

class PoliteCrawler(Crawler):
    def crawl(self, url, current_depth=0):
        if current_depth > self.max_depth or url in self.visited:
            return

        self.visited.add(url)
        print(f"Crawling: {url} at depth {current_depth}")

        # Simulate varying delay before fetching links
        delay = random.uniform(1, 3)  # Random wait between 1 and 3 seconds
        print(f"Waiting for {delay:.2f} seconds before the next request.")
        time.sleep(delay)

        links = self.fetch_links(url)
        for link in links:
            self.crawl(link, current_depth + 1)

polite_crawler = PoliteCrawler(max_depth=3)
polite_crawler.crawl("http://example.com")
