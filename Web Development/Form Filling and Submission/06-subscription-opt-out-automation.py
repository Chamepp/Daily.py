import requests
from bs4 import BeautifulSoup

def opt_out_subscription(form_url, form_data):
    # Send a GET request to the opt-out form URL
    response = requests.get(form_url)
    
    if response.status_code == 200:
        # Parse the HTML content of the form page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the form on the page
        form = soup.find('form')
        
        if form:
            # Extract the form action URL
            action_url = form.get('action')
            
            # Construct the complete form action URL
            if action_url.startswith('/'):
                action_url = response.url + action_url
                
            # Extract the form inputs and their corresponding names
            form_inputs = form.find_all('input')
            payload = {}
            
            # Fill in the form data
            for input_field in form_inputs:
                input_name = input_field.get('name')
                
                if input_name in form_data:
                    payload[input_name] = form_data[input_name]
                else:
                    payload[input_name] = input_field.get('value', '')
            
            # Submit the form with the opt-out payload
            response = requests.post(action_url, data=payload)
            
            if response.status_code == 200:
                print("Successfully opted out of the subscription.")
            else:
                print("Error occurred while submitting the opt-out form.")
        else:
            print("No opt-out form found on the page.")
    else:
        print("Error occurred while accessing the opt-out form page.")

# Example usage
form_url = "https://example.com/opt-out"
form_data = {
    'email': 'your_email@example.com',
    'reason': 'I no longer wish to receive emails.'
}

opt_out_subscription(form_url, form_data)

