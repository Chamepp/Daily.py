import requests
import time

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def monitor_website(url, interval):
    while True:
        if check_website(url):
            print(f"{url} is up!")
        else:
            print(f"{url} is down!")
        time.sleep(interval)

# Example usage: monitor_website("https://www.example.com", 60)
