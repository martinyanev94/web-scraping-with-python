class DataExtractor:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')

    def extract_titles(self):
        titles = []
        items = self.soup.find_all(class_='product-item')
        for item in items:
            title = item.find(class_='product-title').text
            titles.append(title)
        return titles

class Crawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.throttle = Throttle(base_wait=2, randomness=1)

    def crawl(self):
        self.throttle.wait()
        try:
            response = requests.get(self.base_url, timeout=5)
            response.raise_for_status()
            extractor = DataExtractor(response.text)
            titles = extractor.extract_titles()
            for title in titles:
                print(f"Product Title: {title}")
        except Exception as e:
            print(f"An error occurred: {e}")

# Instantiate the crawler
my_crawler = Crawler("https://example.com/products")
my_crawler.crawl()
