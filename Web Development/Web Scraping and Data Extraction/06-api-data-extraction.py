import requests

def extract_data_from_api(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Process and extract the desired data from the JSON response
            # Example: extracting and printing user IDs and names
            for user in data:
                user_id = user['id']
                user_name = user['name']
                print(f"User ID: {user_id}, Name: {user_name}")
        else:
            print(f"Error: {response.status_code} - {response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage
api_url = "https://api.example.com/users"
extract_data_from_api(api_url)

