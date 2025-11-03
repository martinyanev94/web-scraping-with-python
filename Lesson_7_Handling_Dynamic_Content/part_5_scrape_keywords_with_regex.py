import re

def scrape_with_regex(url):
    options = Options()
    options.headless = True
    service = Service('path_to_chromedriver')
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(3)

    # Get all paragraph elements and filter based on regex
    elements = driver.find_elements(By.TAG_NAME, 'p')
    
    for element in elements:
        if re.search(r'Specific Keyword', element.text):
            print(element.text)

    driver.quit()

scrape_with_regex('https://example.com')
