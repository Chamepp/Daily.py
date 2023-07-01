import smtplib

def send_email(subject, body):
    # Email configuration
    sender_email = "your-email@example.com"
    receiver_email = "recipient-email@example.com"
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_username = "your-username"
    smtp_password = "your-password"

    # Create message headers
    message = f"Subject: {subject}\n\n{body}"

    try:
        # Connect to SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Start TLS encryption
            server.starttls()

            # Log in to the SMTP server
            server.login(smtp_username, smtp_password)

            # Send the email
            server.sendmail(sender_email, receiver_email, message)

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error sending email: {str(e)}")

# Example usage
subject = "Security Alert: Unauthorized Access Attempt"
body = "An unauthorized access attempt has been detected on your network. Please take appropriate action."

send_email(subject, body)

