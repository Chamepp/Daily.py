import csv
import requests

# Read data from CSV file
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        name = row[0]
        email = row[1]
        phone = row[2]
        
        # Send POST request to the form endpoint
        response = requests.post('https://example.com/submit', data={'name': name, 'email': email, 'phone': phone})
        
        # Check if the request was successful
        if response.status_code == 200:
            print(f"Data for {name} successfully submitted.")
        else:
            print(f"Error submitting data for {name}.")
