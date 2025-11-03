pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def scrape_dynamic_content(url):
    options = Options()
    options.headless = True  # Set to False to see the browser
    service = Service('path_to_chromedriver')  # Specify the path to your ChromeDriver
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(3)  # Wait for JavaScript to load the content

    # Assuming the dynamic content we want is within an element with class 'dynamic'
    content = driver.find_element(By.CLASS_NAME, 'dynamic').text

    print(content)
    driver.quit()

scrape_dynamic_content('https://example.com')
