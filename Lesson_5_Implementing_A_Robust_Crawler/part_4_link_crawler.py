def link_crawler(seed_url, link_regex, max_depth=3):
    crawl_queue = [seed_url]
    seen = {}
    depth = 0

    while crawl_queue:
        url = crawl_queue.pop()
        if url in seen:
            continue
        seen[url] = depth
        
        if depth > max_depth:
            continue
        
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex, link):
                crawl_queue.append(urlparse.urljoin(seed_url, link))
        
        depth += 1
