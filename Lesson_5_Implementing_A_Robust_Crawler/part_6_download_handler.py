def download(url, user_agent='wswp', num_retries=2):
    ...
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        if isinstance(e, urllib2.HTTPError):
            code = e.code
            if code == 404:
                print 'Page not found, skipping:', url
            elif code == 403:
                print 'Access denied, skipping:', url
            elif 500 <= code < 600:
                print 'Server error, retrying:', url
                if num_retries > 0:
                    return download(url, user_agent, num_retries-1)
        return None
