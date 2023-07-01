import requests
from bs4 import BeautifulSoup

def get_product_price(url):
    # Send a GET request to the product URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the element containing the price
    # Adjust the CSS selector based on the structure of the web page
    price_element = soup.select_one('.product-price')
    
    if price_element:
        return price_element.text.strip()
    else:
        return 'Price not found'

# List of e-commerce product URLs to track
product_urls = [
    'https://example.com/product1',
    'https://example.com/product2',
    'https://example.com/product3'
]

for url in product_urls:
    product_price = get_product_price(url)
    print(f'Price for {url}: {product_price}')
