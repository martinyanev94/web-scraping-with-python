def extract_domain_details(domain_info):
    print(f"Domain Name: {domain_info.domain_name}")
    print(f"Registrar: {domain_info.registrar}")
    print(f"Whois Server: {domain_info.whois_server}")
    print(f"Creation Date: {domain_info.creation_date}")
    print(f"Expiration Date: {domain_info.expiration_date}")
    print(f"Emails: {domain_info.emails}")

if __name__ == "__main__":
    domain = "example.com"  # Replace with your domain
    info = get_domain_info(domain)
    extract_domain_details(info)
