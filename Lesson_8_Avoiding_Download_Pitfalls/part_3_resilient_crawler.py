class ResilientCrawler(Crawler):
    def crawl(self, url, current_depth=0):
        if current_depth > self.max_depth or url in self.visited:
            return

        self.visited.add(url)
        print(f"Crawling: {url} at depth {current_depth}")

        try:
            links = self.fetch_links(url)
        except Exception as e:
            print(f"Failed to fetch links from {url}: {e}")
            return  # Exit this crawl attempt and move on

        for link in links:
            self.crawl(link, current_depth + 1)

resilient_crawler = ResilientCrawler(max_depth=3)
resilient_crawler.crawl("http://example.com")
