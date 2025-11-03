pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('http://example-angularjs-site.com')

time.sleep(3)  # Wait for the page to fully render JS content

page_content = driver.page_source
print(page_content)

driver.quit()
