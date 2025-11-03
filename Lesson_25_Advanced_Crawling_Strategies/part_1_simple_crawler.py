import requests

class SimpleCrawler:
    def __init__(self):
        self.visited_urls = set()

    def crawl(self, url):
        if url in self.visited_urls:
            print(f"Already visited: {url}")
            return
        self.visited_urls.add(url)
        
        print(f"Fetching: {url}")
        response = requests.get(url)

        if response.status_code == 200:
            print("Page fetched successfully.")
            # Process the page content here
        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")

# Usage
crawler = SimpleCrawler()
crawler.crawl("http://example.com")
crawler.crawl("http://example.com")  # This will be detected as a duplicate
