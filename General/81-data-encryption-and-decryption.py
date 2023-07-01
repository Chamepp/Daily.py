import requests

def get_currency_exchange_rate(base_currency, target_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        exchange_rate = data['rates'][target_currency]
        return exchange_rate
    
    return None

# Example usage
base_currency = 'USD'
target_currency = 'EUR'
exchange_rate = get_currency_exchange_rate(base_currency, target_currency)

if exchange_rate:
    print(f"The exchange rate from {base_currency} to {target_currency} is: {exchange_rate}")
else:
    print("Failed to retrieve the exchange rate. Please try again later.")
