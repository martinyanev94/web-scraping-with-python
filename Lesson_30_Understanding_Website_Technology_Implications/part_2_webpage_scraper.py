from selenium import webdriver

url = 'https://www.example.com'
driver = webdriver.Chrome()  # Make sure you have the Chrome WebDriver installed
driver.get(url)

content = driver.page_source
driver.quit()

print(content)
