import urllib.parse
from html.parser import HTMLParser
import requests
requests.packages.urllib3.disable_warnings()

def shape_url(url, link):
    if '://' in link:
        return link
    else:
        return urllib.parse.urljoin(url, link)


class ParsePage(HTMLParser):
    def __init__(self, parent_url):
        super().__init__()
        self.parent_url = parent_url
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'a':
            for attr in attrs:
                if attr[0].lower() == 'href' and attr[-1] != '#':
                    self.links.append(shape_url(self.parent_url, attr[-1]))

visited = []
def scout(url):
    print(url)
    r = requests.get(url, verify=False)
    print(r.status_code)
    html = ParsePage(url)
    html.feed(r.text)
    print(f'  {len(html.links)} links')
    for link in html.links:
        if link not in visited and link.startswith('http'):
            visited.append(link)
            scout(link)

scout('http://www.zh.com.br')