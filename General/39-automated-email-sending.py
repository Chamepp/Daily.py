import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender and recipient information
sender_email = "your_email@example.com"
recipient_email = "recipient_email@example.com"
password = "your_email_password"

# Create message object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = "Automated Email"

# Add email body
body = "Hello, this is an automated email!"
message.attach(MIMEText(body, "plain"))

# SMTP server configuration (Gmail example)
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Establish connection to SMTP server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Enable TLS encryption
    server.login(sender_email, password)
    server.sendmail(sender_email, recipient_email, message.as_string())

print("Email sent successfully!")
