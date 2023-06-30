import requests
from bs4 import BeautifulSoup
import time

def monitor_web_content(url):
    # Retrieve the initial content of the webpage
    response = requests.get(url)
    initial_content = response.content

    while True:
        # Wait for a specific interval before checking for changes
        time.sleep(60)  # Adjust the interval as needed

        # Retrieve the updated content of the webpage
        response = requests.get(url)
        updated_content = response.content

        # Compare the initial and updated content
        if initial_content != updated_content:
            print("Content has changed!")
            # Perform additional actions like sending a notification or executing a specific task
            # You can also compare specific sections or elements of the content if needed

        # Update the initial content for the next iteration
        initial_content = updated_content

# Example usage
url = "https://example.com"  # Replace with the URL of the webpage you want to monitor
monitor_web_content(url)

