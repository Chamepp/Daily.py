import requests
import os
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

def download_images(url, save_directory):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    image_tags = soup.find_all('img')

    for image in image_tags:
        image_url = image['src']
        if image_url.startswith('http'):
            image_filename = os.path.basename(urlparse(image_url).path)
            save_path = os.path.join(save_directory, image_filename)
            try:
                image_response = requests.get(image_url)
                with open(save_path, 'wb') as file:
                    file.write(image_response.content)
                print(f"Downloaded image: {image_url}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to download image: {image_url}")
                print(f"Error: {e}")

# Example usage
webpage_url = input("Enter the URL of the webpage: ")
save_directory = input("Enter the directory to save the images: ")

download_images(webpage_url, save_directory)

