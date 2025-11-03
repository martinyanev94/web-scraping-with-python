class Crawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.throttle = Throttle(base_wait=2, randomness=1)

    def crawl(self):
        self.throttle.wait()
        try:
            response = requests.get(self.base_url, timeout=5)
            response.raise_for_status()  # Raise HTTPError for bad responses
            soup = BeautifulSoup(response.text, 'html.parser')
            items = soup.find_all(class_='product-item')
            for item in items:
                title = item.find(class_='product-title').text
                print(f"Product Title: {title}")
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.ConnectionError:
            print(f"Connection error. Please check your network.")
        except requests.exceptions.Timeout:
            print(f"Request timed out.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Instantiate the crawler
my_crawler = Crawler("https://example.com/products")
my_crawler.crawl()
