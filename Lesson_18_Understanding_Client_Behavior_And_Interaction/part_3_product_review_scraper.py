import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class ProductReviewScraper:
    def __init__(self, product_url):
        self.product_url = product_url

    def scrape_reviews(self):
        reviews_data = []

        # Assume we have logic here to paginate through multiple review pages 
        response = requests.get(self.product_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        reviews = soup.find_all(class_='review-item')

        for review in reviews:
            date_str = review.find(class_='review-date').text
            review_date = datetime.strptime(date_str, "%Y-%m-%d")
            review_text = review.find(class_='review-text').text
            reviews_data.append({"date": review_date, "text": review_text})

        return pd.DataFrame(reviews_data)

product_url = "https://example.com/product/reviews"
review_scraper = ProductReviewScraper(product_url)
reviews_df = review_scraper.scrape_reviews()

print(reviews_df.head())
