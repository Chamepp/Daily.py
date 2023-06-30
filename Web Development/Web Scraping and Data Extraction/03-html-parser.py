import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage to scrape
url = 'https://example.com'

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(html_content, 'html.parser')

# Find and extract specific elements or attributes from the HTML
# Here's an example of extracting all <a> tags and their href attributes
links = soup.find_all('a')
for link in links:
    href = link.get('href')
    print(href)

