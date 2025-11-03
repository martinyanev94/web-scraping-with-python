from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_dynamic_content(url):
    options = Options()
    options.headless = True
    service = Service('path_to_chromedriver')
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)

    try:
        # Wait for the dynamic content to be present
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'dynamic'))
        WebDriverWait(driver, 10).until(element_present)
        
        content = driver.find_element(By.CLASS_NAME, 'dynamic').text
        print(content)
    finally:
        driver.quit()

scrape_dynamic_content('https://example.com')
