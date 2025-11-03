def get_whois_info_with_privacy_check(domain):
    domain_info = whois.whois(domain)
    if domain_info.name == "Privacy Protect, LLC":
        return f"The owner of {domain} has opted for privacy protection, details are not publicly available."
    return domain_info

domain = 'example.com'
info = get_whois_info_with_privacy_check(domain)

if isinstance(info, str):
    print(info)
else:
    print(f"Domain: {domain}")
    print(f"Owner Name: {info.name}")
    print(f"Owner Email: {info.email}")
    print(f"Registration Date: {info.creation_date}")
