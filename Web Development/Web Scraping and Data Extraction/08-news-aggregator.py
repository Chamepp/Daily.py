import requests
from bs4 import BeautifulSoup

def scrape_product_prices(products):
    prices = {}
    
    for product, url in products.items():
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract the price element based on the HTML structure of the website
            price_element = soup.find('span', class_='product-price')
            
            if price_element:
                price = price_element.text.strip()
                prices[product] = price
            else:
                prices[product] = 'Price not available'
        else:
            prices[product] = 'Failed to retrieve price'
    
    return prices

# Example usage
product_urls = {
    'Product A': 'https://www.example.com/product-a',
    'Product B': 'https://www.example.com/product-b',
    'Product C': 'https://www.example.com/product-c'
}

product_prices = scrape_product_prices(product_urls)

# Print the scraped prices
for product, price in product_prices.items():
    print(f'{product}: {price}')

