import requests
import re

# Get Url
url = input('Enter a URL (include `http://`): ')

# Connect
website = requests.get(url)

# Read
html = website.text

# Grab Links
links = re.findall('"((http|ftp)s?://.*?)"', html)

# Output Links
for link in links:
    print(link[0])
    