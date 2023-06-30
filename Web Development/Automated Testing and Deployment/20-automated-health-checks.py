import requests
import smtplib
from email.mime.text import MIMEText

def check_website_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def send_email_notification(sender, recipient, subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # SMTP server configuration
    smtp_server = 'your_smtp_server'
    smtp_port = 587
    smtp_username = 'your_smtp_username'
    smtp_password = 'your_smtp_password'

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
    except smtplib.SMTPException as e:
        print("Failed to send email notification:", e)

# List of websites to check
websites = [
    'https://example1.com',
    'https://example2.com',
    'https://example3.com'
]

# Email configuration
sender_email = 'your_sender_email@example.com'
recipient_email = 'your_recipient_email@example.com'

# Iterate through the websites and check their health
for website in websites:
    if check_website_health(website):
        print(website, "is healthy.")
    else:
        print(website, "is down. Sending email notification...")
        subject = 'Website Down Alert'
        message = f"The website {website} is currently down. Please investigate."
        send_email_notification(sender_email, recipient_email, subject, message)

