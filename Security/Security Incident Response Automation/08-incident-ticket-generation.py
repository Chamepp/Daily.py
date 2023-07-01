import requests

def generate_incident_ticket(incident_details):
    # Prepare the incident ticket payload with relevant details
    ticket_payload = {
        'title': incident_details['title'],
        'description': incident_details['description'],
        'severity': incident_details['severity'],
        'assignee': incident_details['assignee'],
        'category': incident_details['category'],
        # Additional fields can be added based on your ticketing system's requirements
    }

    # Send a POST request to the ticketing system's API endpoint
    ticketing_api_url = 'https://your-ticketing-system-api.com/tickets'
    response = requests.post(ticketing_api_url, json=ticket_payload)

    # Check the response status code for success
    if response.status_code == 201:
        print('Incident ticket created successfully!')
        ticket_id = response.json().get('ticket_id')
        print(f'Ticket ID: {ticket_id}')
    else:
        print('Failed to create incident ticket.')
        print('Response:', response.text)

# Example usage
incident = {
    'title': 'Security Incident: Unauthorized Access Attempt',
    'description': 'A suspicious login attempt was detected from an unknown IP address.',
    'severity': 'High',
    'assignee': 'securityteam@example.com',
    'category': 'Security Incident',
}

generate_incident_ticket(incident)

