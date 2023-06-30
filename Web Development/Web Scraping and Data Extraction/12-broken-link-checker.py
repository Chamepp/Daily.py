import requests
from bs4 import BeautifulSoup

def check_broken_links(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to access the webpage.")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')
    
    print("Checking for broken links on:", url)
    print("========================================")
    
    for link in links:
        href = link.get('href')
        if href:
            link_response = requests.head(href)
            if link_response.status_code >= 400:
                print("Broken link found:", href)

    print("========================================")
    print("Link checking completed.")

# Example usage
website_url = input("Enter the URL of the webpage to check for broken links: ")
check_broken_links(website_url)

