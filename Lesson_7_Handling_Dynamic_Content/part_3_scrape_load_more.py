def scrape_with_load_more(url):
    options = Options()
    options.headless = True
    service = Service('path_to_chromedriver')
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)

    # Click on the 'Load More' button until it's no longer available
    while True:
        try:
            load_more_button = driver.find_element(By.XPATH, "//button[text()='Load More']")
            load_more_button.click()
            time.sleep(2)  # Allow time for the new content to load
        except Exception as e:
            print("No more 'Load More' button found or error occurred.")
            break

    # Now you can scrape the fully loaded page content
    content = driver.find_elements(By.CLASS_NAME, 'dynamic')
    for item in content:
        print(item.text)

    driver.quit()

scrape_with_load_more('https://example.com')
