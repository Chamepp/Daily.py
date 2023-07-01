import subprocess
import smtplib
from email.mime.text import MIMEText

def check_server_health():
    # Perform server health check commands and store the output
    output = subprocess.run(['ping', '-c', '5', 'example.com'], capture_output=True, text=True)

    # Check the result and send an email notification if the server is down
    if output.returncode != 0:
        send_email_notification("Server is down!", str(output.stdout))
    else:
        print("Server is up and running.")

def send_email_notification(subject, body):
    # Email configurations
    sender_email = 'your_email@example.com'
    receiver_email = 'recipient_email@example.com'
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'

    # Create email message
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    # Send email notification
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# Run the server health check
check_server_health()

