url_template = 'http://example-ecommerce-site.com/products?page={}'

page_number = 1
while True:
    response = session.get(url_template.format(page_number))
    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = soup.find_all('div', class_='product')
    if not products:
        break  # Exit loop if there are no products
    
    for product in products:
        name = product.find('h2', class_='product-name').text
        price = product.find('span', class_='product-price').text
        print(f'Product Name: {name}, Price: {price}')
    
    page_number += 1
    time.sleep(2)
