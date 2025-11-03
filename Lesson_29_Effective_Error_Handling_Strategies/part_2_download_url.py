def download(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        elif response.status_code == 404:
            print(f"Error 404: Page not found for URL: {url}")
        elif response.status_code == 500:
            print(f"Error 500: Server error occurred for URL: {url}")
        else:
            print(f"Received unexpected status code: {response.status_code} for URL: {url}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    return None
