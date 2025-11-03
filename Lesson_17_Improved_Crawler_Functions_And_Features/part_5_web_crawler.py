import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Crawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.throttle = Throttle(base_wait=2, randomness=1)

    def crawl_page(self, url):
        self.throttle.wait()
        logging.info(f"Crawling {url}")
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            extractor = DataExtractor(response.text)
            titles = extractor.extract_titles()
            for title in titles:
                logging.info(f"Found Product Title: {title}")
        except Exception as e:
            logging.error(f"An error occurred while crawling {url}: {e}")

    def crawl(self, pages):
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(self.crawl_page, pages)

# Instantiate the crawler and initiate the crawl
my_crawler = Crawler("https://example.com/products")
my_crawler.crawl(urls_to_crawl)
