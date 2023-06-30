import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def web_crawler(url, max_pages):
    visited_pages = set()
    pages_to_visit = [url]

    while len(visited_pages) < max_pages and pages_to_visit:
        current_url = pages_to_visit.pop(0)

        # Skip if the page has already been visited
        if current_url in visited_pages:
            continue

        try:
            # Send a GET request to the current URL
            response = requests.get(current_url)
            visited_pages.add(current_url)

            if response.status_code == 200:
                # Parse the HTML content of the page
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extract data from the page
                # Example: Extract all links on the page
                links = soup.find_all('a')
                for link in links:
                    href = link.get('href')
                    if href:
                        absolute_url = urljoin(current_url, href)
                        pages_to_visit.append(absolute_url)

                # Process or save the extracted data as needed
                # Example: Print the page title
                page_title = soup.title.string
                print(f"Page Title: {page_title}")

        except requests.exceptions.RequestException as e:
            print(f"Error accessing {current_url}: {str(e)}")

    print("Web crawling completed.")

# Example usage
start_url = "https://example.com"
max_pages_to_visit = 10

web_crawler(start_url, max_pages_to_visit)

