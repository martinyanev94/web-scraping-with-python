from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # or use webdriver.Firefox() for Firefox

# Navigate to the target page
driver.get("https://example.com")

# Wait for the page to load completely
driver.implicitly_wait(10)  # wait for a maximum of 10 seconds

# Extract titles from the page after JavaScript has rendered the content
titles = driver.find_elements(By.TAG_NAME, 'h1')
for title in titles:
    print(title.text)

driver.quit()  # close the browser window
