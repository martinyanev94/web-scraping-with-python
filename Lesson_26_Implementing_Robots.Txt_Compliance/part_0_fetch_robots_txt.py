import requests

def fetch_robots_txt(url):
    robots_url = url + '/robots.txt'
    response = requests.get(robots_url)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch robots.txt: {response.status_code}")
        return None

# Example use
url = "http://example.com"
robots_txt = fetch_robots_txt(url)
if robots_txt:
    print(robots_txt)
