import time

def download(url, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Attempt {attempt + 1}/{retries}: HTTP error {response.status_code} for URL: {url}")
        except requests.exceptions.RequestException as req_err:
            print(f"Attempt {attempt + 1}/{retries}: An error occurred: {req_err}")
        time.sleep(delay)  # Wait before the next attempt
    return None
