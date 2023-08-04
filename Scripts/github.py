import requests

username = input("Enter the github username : ")
url = f'https://api.github.com/users/{username}'
response = requests.get(url)

if response.status_code == 200 and requests.codes.ok:
  
    data = response.json()
    for i in data:
        print(f'[+] {i} : ',data[i])

