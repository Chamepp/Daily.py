import requests

# Function to get the currency exchange rate
def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if target_currency in data["rates"]:
            exchange_rate = data["rates"][target_currency]
            return exchange_rate
        else:
            print(f"Currency '{target_currency}' is not supported.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    
    return None

# Get the exchange rate from USD to EUR
base_currency = "USD"
target_currency = "EUR"
exchange_rate = get_exchange_rate(base_currency, target_currency)

if exchange_rate is not None:
    print(f"The exchange rate from {base_currency} to {target_currency} is: {exchange_rate}")
