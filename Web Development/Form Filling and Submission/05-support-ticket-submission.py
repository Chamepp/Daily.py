import requests
from bs4 import BeautifulSoup

def opt_out_subscription(url, form_data):
    # Send a GET request to the opt-out form page
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the opt-out form on the page
        form = soup.find('form')

        # Extract the form action URL
        form_action = form.get('action')

        # Build the complete URL for the opt-out form submission
        submit_url = url + form_action

        # Extract the input fields from the form
        input_fields = form.find_all('input')

        # Prepare the form data with the provided values
        form_data.update({field.get('name'): field.get('value') for field in input_fields})

        # Send a POST request to submit the opt-out form
        response = requests.post(submit_url, data=form_data)

        if response.status_code == 200:
            print("Successfully opted out of the subscription!")
        else:
            print("Failed to opt out of the subscription. Please check the form submission.")

    else:
        print("Failed to access the opt-out form page. Please check the URL.")

# Example usage
url = 'https://example.com/opt-out'
form_data = {
    'email': 'your_email@example.com',
    'reason': 'unsubscribe',
    'comments': 'Please remove me from your subscription list.'
}

opt_out_subscription(url, form_data)

