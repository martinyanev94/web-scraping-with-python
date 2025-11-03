def link_crawler(seed_url, link_regex, max_depth=2):
    crawl_queue = [seed_url]
    seen = {seed_url: 0}
    while crawl_queue:
        url = crawl_queue.pop()
        depth = seen[url]
        if depth < max_depth:
            html = download(url)
            for link in get_links(html):
                if re.match(link_regex, link):
                    link = urlparse.urljoin(seed_url, link)
                    if link not in seen:
                        seen[link] = depth + 1
                        crawl_queue.append(link)
