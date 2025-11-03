DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}

HTTP_PROXIES = [
    'http://proxy1:port',
    'http://proxy2:port',
]

def get_random_proxy():
    return random.choice(HTTP_PROXIES)
