import datetime

def calculate_domain_age(domain_info):
    if isinstance(domain_info.creation_date, list):
        creation_date = domain_info.creation_date[0]  # Handle the case of multiple creation dates
    else:
        creation_date = domain_info.creation_date
    
    current_date = datetime.datetime.now()
    domain_age = current_date - creation_date
    return domain_age.days

domain = 'example.com'
info = get_whois_info(domain)
age_in_days = calculate_domain_age(info)

print(f"The domain {domain} has been active for {age_in_days} days.")
