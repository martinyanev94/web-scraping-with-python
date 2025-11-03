import requests

def scrape_website(url, throttle):
    domain = url.split('/')[2]  # Extract the domain from the URL
    throttle.wait(domain)  # Wait if necessary
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Successfully retrieved data from {url}")
        return response.text
    else:
        print(f"Failed to retrieve data from {url}")
        return None

if __name__ == "__main__":
    throttle = Throttle(delay=5)  # 5 seconds delay
    urls_to_scrape = [
        "http://example.com/page1",
        "http://example.com/page2",
        "http://example.com/page3"
    ]
    
    for url in urls_to_scrape:
        data = scrape_website(url, throttle)
