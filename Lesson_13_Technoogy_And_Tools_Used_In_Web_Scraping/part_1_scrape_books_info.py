from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('http://example.com/books')
books = driver.find_elements(By.CLASS_NAME, 'book')

for book in books:
    title = book.find_element(By.CLASS_NAME, 'title').text
    author = book.find_element(By.CLASS_NAME, 'author').text
    print(f'Title: {title}, Author: {author}')

driver.quit()
