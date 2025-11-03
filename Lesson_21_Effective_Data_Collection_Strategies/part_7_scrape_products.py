import pandas as pd

data = {
    'Product Name': [],
    'Price': []
}

for product in products:
    data['Product Name'].append(product.find('h2', class_='product-name').text)
    data['Price'].append(product.find('span', class_='product-price').text)

df = pd.DataFrame(data)
df.to_csv('products.csv', index=False)
