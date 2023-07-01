import requests

# Data
message = input('Enter a Message: ')
number = input('Enter the phone number: ')

# Sending Payload
payload = {'number': number, 'message': message}
r = requests.post("http://textbelt.com/text", data=payload)

# Confirmation
if r.json()['success']:
    print('Success!')
else:
    print('Error!')
    