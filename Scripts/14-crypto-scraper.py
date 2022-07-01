import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style
import sys
import os

# Gather Prices
def get_price():
	
    # Data
	response = requests.get(url)
	soup = BeautifulSoup(response.content,'html.parser')

	# Currencies
	if asset == 'btc':
		price = soup.find('span',{'class':'price'}).text #bitcoin works faster with the price class
	else:
		price = soup.find('span',{'class':'woobJfK-Xb2EM1W1o8yoE'}).text #other altcoins only work with this class

	return float(price.replace(",",""))

# Asset
asset = input('Abbreviation of the asset: ')
url = 'https://cryptowat.ch/assets/' + asset

# Missing Currencies
try:
	price = get_price()
except AttributeError:
	print("The asset doesn't exist or it's not supported!")
	sys.exit()

# Display
if sys.platform == 'win32':
	os.system('cls')
else:
	os.system('clear')


price = 0

# Gather Prices
while True:

	last_price = price
	price = get_price()

	if price > last_price:
		color = Fore.GREEN
	elif last_price > price:
		color = Fore.RED
	else:
		color = Style.RESET_ALL

	print('$ ',end='')
	print(color + str(price) + Style.RESET_ALL)
    