pip install python-whois
import whois

def get_whois_info(domain):
    domain_info = whois.whois(domain)
    return domain_info

domain = 'example.com'
info = get_whois_info(domain)

print(f"Domain: {domain}")
print(f"Owner Name: {info.name}")
print(f"Owner Email: {info.email}")
print(f"Registration Date: {info.creation_date}")
