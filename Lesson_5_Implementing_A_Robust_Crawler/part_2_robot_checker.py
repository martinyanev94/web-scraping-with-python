import robotparser

def check_robot(url, user_agent):
    rp = robotparser.RobotFileParser()
    rp.set_url(url + '/robots.txt')
    rp.read()
    return rp.can_fetch(user_agent, url)
if check_robot(url, user_agent):
    html = download(url)
else:
    print 'Blocked by robots.txt:', url
