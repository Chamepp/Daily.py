import time
from pyfiglet import Figlet
from getpass import getpass
import new_token


fig_type = Figlet(font='graffiti')
print(fig_type.renderText('Token Manager'))


# Script Menu
print(
        '\n[1] New Token \n'
        '[2] Edit Token \n'
        '[3] Delete Token \n'
        '[4] Exit\n\n\n'
     )

user_selection = input('[?] What Type Of Service Are You Looking For ? ')

if user_selection == '1':
    print("Starting New Token Configurations ...")
    gather_token = new_token.get_token()

elif user_selection == '2':
    print("Starting Tokens Data Edit Mode...")

elif user_selection == '3':
    print("Fetching Tokens List and Data ...")
    exit()

elif user_selection == '4':
    print("Exiting The Store ...")
    exit()

else:
    print("Unknown Menu Value !")
    exit()