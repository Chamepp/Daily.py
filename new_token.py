import time
import json
from getpass import getpass

def get_token():
    data = {}
    user_token = getpass('Please Enter Your New Token  ')
    data['tokens'] = []
    if user_token.startswith('ghp'):
        print('Capturing Token ...')
        data['tokens'].append({
            'hash': user_token,
            'isValidated': True
        })
        with open('data.json', 'w') as write_dependencies:
            json.dump(data, write_dependencies)
    else:
        print('Unvalid Token !')
        quit()

