import requests
from bs4 import BeautifulSoup

# Specify the URL of the webpage to scrape
url = "https://example.com"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find specific elements on the page using CSS selectors
    # Extract the desired data from the elements
    data = soup.find("div", class_="example-class").text

    # Print the extracted data
    print("Extracted data:")
    print(data)
else:
    print("Error: Failed to retrieve the webpage.")
