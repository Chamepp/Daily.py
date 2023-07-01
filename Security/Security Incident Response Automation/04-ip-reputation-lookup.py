import requests

def check_ip_reputation(ip_address):
    url = f"https://api.example.com/ip/reputation/{ip_address}"  # Replace with the appropriate API endpoint
    headers = {
        "Authorization": "Bearer YOUR_API_KEY"  # Replace with your actual API key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        reputation = response.json()["reputation"]
        print(f"The reputation of IP address {ip_address} is: {reputation}")
    else:
        print(f"Error occurred while checking IP reputation: {response.status_code}")


# Example usage
ip_address = input("Enter the IP address to check reputation: ")
check_ip_reputation(ip_address)

