def crawl(seed_url, link_regex, delay):
    throttle = Throttle(delay)
    crawl_queue = [seed_url]
    seen = set()

    while crawl_queue:
        url = crawl_queue.pop()
        if url in seen:
            continue
        seen.add(url)

        throttle.wait(url)
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex, link):
                crawl_queue.append(urlparse.urljoin(seed_url, link))
