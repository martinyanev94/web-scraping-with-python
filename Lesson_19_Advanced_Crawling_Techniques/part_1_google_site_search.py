import requests

def google_site_search(domain):
    url = f"https://www.google.com/search?q=site:{domain}"
    response = requests.get(url)
    return response.text  # You can process response to find indexed pages

print(google_site_search('example.webscraping.com'))
