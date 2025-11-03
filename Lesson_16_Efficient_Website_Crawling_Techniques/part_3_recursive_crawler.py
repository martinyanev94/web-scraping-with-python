class RecursiveCrawler:
    def __init__(self, base_url):
        self.base_url = base_url

    def crawl(self, url, depth):
        if depth == 0:
            return
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Data extraction logic
        product_titles = soup.find_all(class_='product-title')
        for title in product_titles:
            print(f"Found Product: {title.text}")

        # Recursively crawl deeper links
        links = soup.find_all('a', href=True)
        for link in links:
            full_url = link['href']
            if full_url.startswith("/"):  # if it's a relative link
                full_url = self.base_url + full_url
            self.crawl(full_url, depth - 1)

# Instantiate the recursive crawler and start from the homepage
recursive_crawler = RecursiveCrawler("https://example.com")
recursive_crawler.crawl("https://example.com", 2)  # Set depth to 2
