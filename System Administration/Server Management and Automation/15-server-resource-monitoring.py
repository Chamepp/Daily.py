import psutil
import smtplib
from email.mime.text import MIMEText

# Set the threshold values for CPU and memory usage (in percentage)
cpu_threshold = 80
memory_threshold = 80

def send_email(subject, message):
    # Sender and receiver email addresses
    sender = 'your_email@example.com'
    receiver = 'recipient_email@example.com'

    # SMTP server configuration
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_email@example.com'
    smtp_password = 'your_password'

    # Create the email message
    email_message = MIMEText(message)
    email_message['Subject'] = subject
    email_message['From'] = sender
    email_message['To'] = receiver

    # Send the email using SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender, receiver, email_message.as_string())

# Get current CPU and memory usage
cpu_usage = psutil.cpu_percent()
memory_usage = psutil.virtual_memory().percent

# Check if CPU or memory usage exceeds the thresholds
if cpu_usage > cpu_threshold or memory_usage > memory_threshold:
    # Create an alert message
    alert_subject = 'Server Resource Alert'
    alert_message = f"CPU Usage: {cpu_usage}%\nMemory Usage: {memory_usage}%\n"

    # Send the alert email
    send_email(alert_subject, alert_message)

