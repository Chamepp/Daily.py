import requests
from bs4 import BeautifulSoup

# URL to scrape data from
url = "https://example.com"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find specific elements on the webpage using CSS selectors
# Replace "css-selector" with the actual CSS selector for the desired element
elements = soup.select("css-selector")

# Process and display the scraped data
for element in elements:
    data = element.text.strip()  # Extract the text from the element
    print(data)

# Save the scraped data to a file
with open("scraped_data.txt", "w") as file:
    for element in elements:
        data = element.text.strip()
        file.write(data + "\n")
