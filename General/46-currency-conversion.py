from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount

# Example usage:
amount = 100  # Amount to convert
from_currency = 'USD'  # Currency to convert from
to_currency = 'EUR'  # Currency to convert to

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f'{amount} {from_currency} is equal to {converted_amount} {to_currency}')
