import requests
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.throttle = Throttle(base_wait=2, randomness=1)

    def crawl(self):
        self.throttle.wait()  # Add throttle here
        response = requests.get(self.base_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            items = soup.find_all(class_='product-item')
            for item in items:
                title = item.find(class_='product-title').text
                print(f"Product Title: {title}")
        else:
            print("Failed to retrieve data.")

# Instantiate the crawler
my_crawler = Crawler("https://example.com/products")
my_crawler.crawl()
