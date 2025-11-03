import whois

def get_domain_info(domain):
    domain_info = whois.whois(domain)
    return domain_info

if __name__ == "__main__":
    domain = "example.com"  # Replace with your domain
    info = get_domain_info(domain)
    print(info)
