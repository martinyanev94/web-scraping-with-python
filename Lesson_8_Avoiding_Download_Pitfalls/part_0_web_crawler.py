class Crawler:
    def __init__(self, max_depth):
        self.max_depth = max_depth
        self.visited = set()

    def crawl(self, url, current_depth=0):
        if current_depth > self.max_depth:
            return  # Stop if we've reached max crawl depth
        if url in self.visited:
            return  # Avoid revisiting the same page

        self.visited.add(url)  # Mark this URL as visited
        print(f"Crawling: {url} at depth {current_depth}")

        # Imagine we fetch links from the current URL
        links = self.fetch_links(url)
        for link in links:
            self.crawl(link, current_depth + 1)

    def fetch_links(self, url):
        # For illustration, mocking the response; you would fetch actual links here
        return ["http://example.com/page1", "http://example.com/page2"]

crawler = Crawler(max_depth=3)
crawler.crawl("http://example.com")
