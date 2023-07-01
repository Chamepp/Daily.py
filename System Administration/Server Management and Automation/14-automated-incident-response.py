import smtplib

# Configure email settings
sender_email = "incidentresponse@example.com"
recipient_email = "admin@example.com"
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_username = "your_username"
smtp_password = "your_password"

def send_email(subject, message):
    # Compose the email
    email_message = f"Subject: {subject}\n\n{message}"

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to the SMTP server
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, email_message)

        # Disconnect from the SMTP server
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")

# Example usage
incident_subject = "Security Incident Alert"
incident_message = "We have detected a potential security breach. Please investigate immediately."

send_email(incident_subject, incident_message)

