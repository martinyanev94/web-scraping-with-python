import requests

def check_robots_txt(url):
    if url.endswith('/'):
        robots_url = url + 'robots.txt'
    else:
        robots_url = url + '/robots.txt'
    
    response = requests.get(robots_url)
    if response.status_code == 200:
        print("Robots.txt:")
        print(response.text)
    else:
        print("Robots.txt not found.")

check_robots_txt("https://example.com")
