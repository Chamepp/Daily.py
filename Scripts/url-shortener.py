import sys
import argparse
import requests
from bs4 import BeautifulSoup

# Colors
RED_COLOR = "\033[1;31m"
GREEN_COLOR = "\033[1;32m"
NO_COLOR = "\033[0m"

API_URL = "https://www.shorturl.at/shortener.php"
API_PARAM = "u"

# Run The API
class API:

    def __init__(self):
        # Initializing
        self.__long_url = ""

    def set_url(self, url):
        self.__long_url = url

    def get_short_url(self):
        return self.__short_url

    def request_short_url(self):

        prarams = {API_PARAM: self.__long_url}

        try:
            result = requests.post(API_URL, data = prarams)
        except ConnectionError as err:
            return -1, err

        return 1, result.text

    # Extracting Data
    def extract_data_from_html(self, html_page):

        soup = BeautifulSoup(html_page, 'html.parser')
        input_tag = soup.find("input", attrs={"id": "shortenurl"})

        try:
            self.__short_url = input_tag.attrs["value"]
            return 1
        except:
            return -1

# Shortening The Url
def main():

    if args.url == '' or args.url is None:
        args.url = input("Enter the url> ")

    api_manager = API()

    api_manager.set_url(args.url)
    response_stauts, result = api_manager.request_short_url() # Sends the request to the API

    if response_stauts == -1:
        print(f"[{RED_COLOR}-{NO_COLOR}] Error in connecting to the API server...")
        ans = input("Do you want to know the error? [Y/n] ") # For more information about thr error
        if ans.lower() != 'n':
            print(result)

        sys.exit(1)
        return

    if api_manager.extract_data_from_html(result) == -1:
        print(f"[{RED_COLOR}-{NO_COLOR}] Error in parsing the response...")
        sys.exit(1)
        return

    print("----------------------------")
    print(GREEN_COLOR + api_manager.get_short_url() + NO_COLOR)
    print("----------------------------")

    sys.exit(0)
    return

# Arguments and Execution
if __name__ == '__main__':
    global args

    parser = argparse.ArgumentParser(description="URL Shortener")

    # -u | --url URL
    parser.add_argument(
        '-u',
        '--url',
        metavar='url',
        type=str,
        default='',
        help='the URL'
    )

    args = parser.parse_args()

    main()
