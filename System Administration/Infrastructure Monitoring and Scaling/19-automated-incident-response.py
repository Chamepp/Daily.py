import requests

def create_ticket(title, description, assignee):
    # API call to create a ticket in the incident management system
    ticket_url = "https://api.example.com/tickets"
    payload = {
        "title": title,
        "description": description,
        "assignee": assignee
    }

    response = requests.post(ticket_url, json=payload)

    if response.status_code == 201:
        print("Ticket created successfully!")
        ticket_id = response.json()["id"]
        return ticket_id
    else:
        print("Failed to create ticket. Error:", response.text)
        return None

def notify_team(ticket_id, team_emails):
    # Send notifications to the incident response team
    notification_url = "https://api.example.com/notifications"

    for email in team_emails:
        payload = {
            "ticket_id": ticket_id,
            "recipient": email,
            "message": "An incident has been reported. Please take action."
        }
        response = requests.post(notification_url, json=payload)

        if response.status_code == 200:
            print("Notification sent to:", email)
        else:
            print("Failed to send notification to:", email)

# Example usage
title = "Server Down Incident"
description = "One of the production servers is unresponsive."
assignee = "John Doe"
team_emails = ["team_member1@example.com", "team_member2@example.com"]

# Create a ticket
ticket_id = create_ticket(title, description, assignee)

if ticket_id:
    # Notify the incident response team
    notify_team(ticket_id, team_emails)

