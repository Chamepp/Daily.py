import requests
from bs4 import BeautifulSoup
import smtplib

# URL of the webpage to monitor
url = "https://example.com"

# Function to check for webpage changes
def check_webpage():
    # Send a GET request to the webpage
    response = requests.get(url)
    content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Extract the desired content to compare
    # Here, we extract the text of all paragraphs on the webpage
    paragraphs = soup.find_all('p')
    current_content = [p.text for p in paragraphs]

    # Read the previously stored content from a file
    try:
        with open('previous_content.txt', 'r') as file:
            previous_content = file.read().splitlines()
    except FileNotFoundError:
        previous_content = []

    # Compare the current and previous content
    if current_content != previous_content:
        send_notification(current_content)
        save_content(current_content)

# Function to send an email notification
def send_notification(content):
    sender_email = "your_email@example.com"
    receiver_email = "recipient_email@example.com"
    password = "your_email_password"

    subject = "Webpage Change Notification"
    body = "The webpage at {} has been updated.\n\nNew content:\n{}".format(url, '\n'.join(content))

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

# Function to save the current content for future comparison
def save_content(content):
    with open('previous_content.txt', 'w') as file:
        file.write('\n'.join(content))

# Run the script to check for webpage changes
check_webpage()
