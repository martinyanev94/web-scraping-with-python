def get_extended_whois_info(domain):
    domain_info = whois.whois(domain)
    return f"""
    Domain: {domain}
    Owner Name: {domain_info.name}
    Owner Email: {domain_info.email}
    Registration Date: {domain_info.creation_date}
    Name Servers: {domain_info.name_servers}
    """

domain = 'example.com'
info = get_extended_whois_info(domain)
print(info)
