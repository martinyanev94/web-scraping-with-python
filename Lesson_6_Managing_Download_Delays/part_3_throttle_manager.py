class Throttle:
    def __init__(self, default_delay, specific_delays=None):
        self.default_delay = default_delay
        self.specific_delays = specific_delays or {}
        self.domains = {}

    def wait(self, url):
        domain = urlparse(url).netloc
        delay = self.specific_delays.get(domain, self.default_delay)
        last_accessed = self.domains.get(domain)

        if last_accessed is not None:
            sleep_secs = delay - (datetime.datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)

        self.domains[domain] = datetime.datetime.now()
