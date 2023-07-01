import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_incident_report(subject, body):
    # Email configuration
    sender_email = 'sender@example.com'
    sender_password = 'password'
    recipient_email = 'recipient@example.com'
    smtp_server = 'smtp.example.com'
    smtp_port = 587

    # Create email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    # Add body to the email
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)

# Example usage
incident_subject = 'Security Incident Report - Unauthorized Access'
incident_body = '''Dear Security Team,

We would like to report a security incident that occurred today regarding unauthorized access to the company's internal network. 

Summary of Incident:
- Incident Type: Unauthorized Access
- Date and Time: July 1, 2023, 10:30 AM
- Description: An external IP address was found attempting to gain unauthorized access to our network resources. We have initiated the necessary actions to mitigate the threat.

Please let us know if you require any additional information or if there are further steps we need to take.

Best regards,
Your Team'''

send_incident_report(incident_subject, incident_body)

