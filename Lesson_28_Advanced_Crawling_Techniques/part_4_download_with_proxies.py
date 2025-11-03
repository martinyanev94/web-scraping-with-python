import requests

def download(url, proxies=None):
    response = requests.get(url, proxies=proxies)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to download: {url} with status code: {response.status_code}")
        return None
proxies = {
    'http': 'http://your_proxy:port',
    'https': 'http://your_proxy:port',
}
html_content = download('http://example.com', proxies)
