pip install fake-useragent
from fake_useragent import UserAgent

def download_with_user_agent(url):
    ua = UserAgent()
    user_agent = ua.random
    headers = {'User-Agent': user_agent}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to download: {url} with status code: {response.status_code}")
        return None
