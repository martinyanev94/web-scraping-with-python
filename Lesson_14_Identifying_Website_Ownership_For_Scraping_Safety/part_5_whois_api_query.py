import requests

def get_whois_api_info(domain):
    api_key = "YOUR_API_KEY"  # Replace with your API key
    url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={api_key}&domainName={domain}&outputFormat=JSON"
    
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    domain = "example.com"  # Replace with your domain
    whois_data = get_whois_api_info(domain)
    print(whois_data)
