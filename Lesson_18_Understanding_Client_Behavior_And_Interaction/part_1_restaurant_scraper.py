import requests
from bs4 import BeautifulSoup

class RestaurantScraper:
    def __init__(self, url):
        self.url = url

    def scrape_data(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting restaurant details
        restaurants = soup.find_all(class_='restaurant-item')
        restaurant_data = []

        for restaurant in restaurants:
            name = restaurant.find(class_='restaurant-name').text
            location = restaurant.find(class_='restaurant-location').text
            reviews = restaurant.find(class_='restaurant-reviews').text
            restaurant_data.append((name, location, reviews))

        return restaurant_data

# Instantiate the scraper with a URL
scraper = RestaurantScraper("https://example.com/restaurants")
data = scraper.scrape_data()

for name, location, reviews in data:
    print(f"Restaurant: {name}, Location: {location}, Reviews: {reviews}")
