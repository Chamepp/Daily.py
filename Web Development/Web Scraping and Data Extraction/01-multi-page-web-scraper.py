import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    if response.status_code == 200:
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract data from the parsed HTML
        # Replace the following code with your specific data extraction logic
        titles = soup.find_all('h2', class_='title')
        for title in titles:
            print(title.text.strip())
        
        # Check if there are more pages to scrape
        next_page = soup.find('a', class_='next-page')
        if next_page:
            next_page_url = next_page['href']
            # Recursively call the scrape_data function for the next page
            scrape_data(next_page_url)
    else:
        print(f"Error accessing URL: {url}")

# Example usage
start_url = 'https://www.example.com/page1'
scrape_data(start_url)

