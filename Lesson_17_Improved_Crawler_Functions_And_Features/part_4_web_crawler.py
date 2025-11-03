from concurrent.futures import ThreadPoolExecutor

class Crawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.throttle = Throttle(base_wait=2, randomness=1)

    def crawl_page(self, url):
        self.throttle.wait()
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            extractor = DataExtractor(response.text)
            titles = extractor.extract_titles()
            for title in titles:
                print(f"Product Title: {title}")
        except Exception as e:
            print(f"An error occurred while crawling {url}: {e}")

    def crawl(self, pages):
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(self.crawl_page, pages)

# Instantiate the crawler with a list of URLs to crawl
urls_to_crawl = [
    "https://example.com/products/category1",
    "https://example.com/products/category2",
    "https://example.com/products/category3"
]
my_crawler = Crawler("https://example.com/products")
my_crawler.crawl(urls_to_crawl)
