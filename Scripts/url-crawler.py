import requests
import re

# Import Further Libraries
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Compile Url
link_re = re.compile(r'href="(.*?)"')


def crawl(url):

    # Request Url
    req = requests.get(url)

    # Success Confirmation
    if(req.status_code != 200):
        return []

    # Find links
    links = link_re.findall(req.text)
    print("\nFound {} links".format(len(links)))

    # Search Links For Emails
    for link in links:

        # Get Url
        link = urljoin(url, link)
        print(link)

if __name__ == '__main__':
    crawl('http://www.sample.com')
