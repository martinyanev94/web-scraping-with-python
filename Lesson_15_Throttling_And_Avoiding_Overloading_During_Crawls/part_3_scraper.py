def scrape_website(url, throttle):
    domain = url.split('/')[2]
    throttle.wait(domain)
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Successfully retrieved data from {url}")
        # Adjust the delay based on successful response
        throttle.delay = 2  
        return response.text
    else:
        print(f"Failed to retrieve data from {url}. Status: {response.status_code}")
        # Optional: Adjust the delay in case of failure
        throttle.delay += 2  # Perhaps the server is under stress, increment our wait time
        return None
