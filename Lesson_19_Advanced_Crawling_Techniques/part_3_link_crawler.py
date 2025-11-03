def link_crawler(seed_url, max_depth=2):
    seen = {}
    crawl_queue = [(seed_url, 0)]  # store URLs with their depth
    while crawl_queue:
        url, depth = crawl_queue.pop()
        if depth >= max_depth:
            continue
        html = download(url)
        if html:
            links = get_links(html)  # function to extract links from the HTML
            for link in links:
                if link not in seen:
                    seen[link] = True
                    crawl_queue.append((link, depth + 1))
