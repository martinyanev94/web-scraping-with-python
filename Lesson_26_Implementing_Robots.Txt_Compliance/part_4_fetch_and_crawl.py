def fetch_and_compliance_crawl(url):
    robots_txt = fetch_robots_txt(url)

    if robots_txt is None:  # No robots.txt found
        print(f"No robots.txt file found for {url}. Crawling with caution.")
        crawl(url)  # Optionally crawl, depending on the site's public content
    else:
        robots_rules = parse_robots_txt(robots_txt, user_agent)
        crawl(url)

# Try crawling a URL
fetch_and_compliance_crawl("http://example.com")
