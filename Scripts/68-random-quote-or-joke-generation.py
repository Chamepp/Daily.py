import requests
import random

def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        quote = response.json()
        return quote["content"]
    else:
        return "Unable to fetch a random quote at the moment."

def main():
    quote = get_random_quote()
    print("Random Quote:")
    print(quote)

if __name__ == "__main__":
    main()
