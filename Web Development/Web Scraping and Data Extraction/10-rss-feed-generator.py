import feedparser
import requests
from bs4 import BeautifulSoup

def generate_rss_feed(url):
    # Fetch the webpage content
    response = requests.get(url)
    response.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find relevant elements on the webpage
    # Customize these lines based on the specific website structure
    article_elements = soup.find_all('article')
    title_elements = [article.find('h2') for article in article_elements]
    link_elements = [article.find('a')['href'] for article in article_elements]

    # Create an RSS feed using the extracted information
    feed = feedparser.FeedParserDict()
    feed['feed'] = {
        'title': 'Website RSS Feed',
        'link': url,
        'description': 'Automated RSS feed generated from the website',
    }
    feed_entries = []

    for title, link in zip(title_elements, link_elements):
        entry = {
            'title': title.get_text(),
            'link': link,
            'description': '',
        }
        feed_entries.append(entry)

    feed['entries'] = feed_entries

    # Generate the RSS feed in XML format
    rss_feed = feedparser.parse(feed)

    # Print the RSS feed
    print(rss_feed.to_xml())

# Example usage
url = input("Enter the URL of the website to generate the RSS feed: ")
generate_rss_feed(url)

