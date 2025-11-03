class HeuristicCrawler:
    def __init__(self):
        self.visited_urls = set()

    def score_link(self, link):
        # Placeholder scores based on some criteria, could be more complex
        score = 0
        if "important" in link:
            score += 10
        if "new" in link:
            score += 5
        return score

    def crawl(self, initial_url):
        links = get_links(initial_url)
        scored_links = [(self.score_link(link), link) for link in links]
        scored_links.sort(reverse=True)  # Sort by descending score
        
        for score, link in scored_links:
            if link not in self.visited_urls:
                print(f"Visiting {link} with score {score}")
                self.visited_urls.add(link)
                # Fetch and process the page
