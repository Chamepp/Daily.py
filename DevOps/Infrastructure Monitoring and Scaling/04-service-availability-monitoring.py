import requests
import smtplib

# Define the URL of the service to monitor
service_url = "https://example.com"

# Define the email settings for sending notifications
sender_email = "your.email@example.com"
receiver_email = "recipient.email@example.com"
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_username = "your.email@example.com"
smtp_password = "your_password"

def send_email_notification(subject, body):
    message = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message)

def check_service_availability():
    try:
        response = requests.get(service_url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

# Main script
if __name__ == "__main__":
    if check_service_availability():
        print("Service is available.")
    else:
        print("Service is not available. Sending email notification...")
        subject = "Service Unavailable"
        body = "The monitored service is not available. Please investigate."
        send_email_notification(subject, body)

