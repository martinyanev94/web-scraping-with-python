from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

def normalize_url(url):
    parsed_url = urlparse(url)
    # Remove trailing slash and sort query parameters
    query_params = parse_qs(parsed_url.query)
    sorted_params = sorted(query_params.items())
    normalized_query = urlencode(sorted_params, doseq=True)

    new_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path.rstrip('/'), '', normalized_query, ''))
    return new_url

urls = [
    "http://example.com/page/",
    "http://example.com/page",
    "http://example.com/page?param=2&param=1",
]

normalized_urls = {normalize_url(url) for url in urls}
print(normalized_urls)
