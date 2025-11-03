import requests
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, base_url):
        self.base_url = base_url

    def crawl_category(self, category):
        response = requests.get(f"{self.base_url}/{category}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            items = soup.find_all(class_='product-item')
            for item in items:
                title = item.find(class_='product-title').text
                print(f"Product Title: {title}")
        else:
            print("Failed to retrieve category.")

# Instantiate the crawler and crawl the 'electronics' category
my_crawler = Crawler("https://example.com/products")
my_crawler.crawl_category("electronics")
