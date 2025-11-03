from bs4 import BeautifulSoup
import requests

url = 'http://example-ecommerce-site.com/products'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

products = soup.find_all('div', class_='product')  # Assuming each product is within a div with class 'product'

for product in products:
    name = product.find('h2', class_='product-name').text
    price = product.find('span', class_='product-price').text
    print(f'Product Name: {name}, Price: {price}')
