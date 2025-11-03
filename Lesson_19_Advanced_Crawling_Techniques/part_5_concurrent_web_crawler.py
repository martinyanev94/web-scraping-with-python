from concurrent.futures import ThreadPoolExecutor

def concurrent_crawl(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(download, urls))
    return results

urls_to_crawl = [f"http://example.com/view/item-{i}" for i in range(1, 100)]
responses = concurrent_crawl(urls_to_crawl)
