import datetime
import smtplib
from email.mime.text import MIMEText

def send_email_alert(recipient, subject, message):
    # Sender's email credentials
    sender_email = 'your_email@example.com'
    sender_password = 'your_email_password'

    # Create the email message
    email_message = MIMEText(message)
    email_message['Subject'] = subject
    email_message['From'] = sender_email
    email_message['To'] = recipient

    # Connect to the SMTP server and send the email
    with smtplib.SMTP('smtp.example.com', 587) as smtp_server:
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)
        smtp_server.send_message(email_message)

def check_certificate_expiry(domain, days_threshold):
    # Import the SSL library and connect to the domain
    import ssl
    ssl_context = ssl.create_default_context()
    with ssl.create_connection((domain, 443)) as sock:
        with ssl_context.wrap_socket(sock, server_hostname=domain) as ssock:
            # Get the certificate details
            cert = ssock.getpeercert()

    # Extract the certificate expiry date
    expiry_date = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
    days_left = (expiry_date - datetime.datetime.now()).days

    # Check if the certificate is within the threshold
    if days_left <= days_threshold:
        subject = f"SSL Certificate Expiry Alert: {domain}"
        message = f"The SSL certificate for {domain} is expiring in {days_left} days. Please renew it as soon as possible."
        send_email_alert('recipient@example.com', subject, message)

# Example usage
check_certificate_expiry('example.com', 30)

