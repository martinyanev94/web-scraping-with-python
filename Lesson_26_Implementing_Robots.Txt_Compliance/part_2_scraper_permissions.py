def is_allowed_to_scrape(url, robots_rules, user_agent):
    from urllib.parse import urlparse

    parsed_url = urlparse(url)
    path = parsed_url.path

    rules_for_agent = robots_rules.get(user_agent, rules_for_agent.get("*", []))
    
    for disallowed in rules_for_agent:
        if path.startswith(disallowed):
            return False  # Not allowed to scrape this URL
    return True  # Allowed to scrape

# Example use
url_to_scrape = f"{url}/private/data"
if is_allowed_to_scrape(url_to_scrape, robots_rules, user_agent):
    print(f"Scraping is allowed for: {url_to_scrape}")
else:
    print(f"Scraping is not allowed for: {url_to_scrape}")
