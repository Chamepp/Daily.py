import requests

def get_crypto_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    
    if crypto_id in data:
        price = data[crypto_id]["usd"]
        return price
    else:
        return None

# Set your desired cryptocurrency ID
crypto_id = "bitcoin"

# Get the price of the cryptocurrency
crypto_price = get_crypto_price(crypto_id)

if crypto_price is not None:
    print(f"The current price of {crypto_id} is ${crypto_price:.2f} USD.")
else:
    print("Unable to retrieve cryptocurrency price.")
