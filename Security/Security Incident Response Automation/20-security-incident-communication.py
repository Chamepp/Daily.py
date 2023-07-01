import smtplib

def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        # Establish a secure connection with the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Log in to the sender's email account
        server.login(sender_email, sender_password)

        # Compose the email message
        email_message = f"Subject: {subject}\n\n{message}"

        # Send the email
        server.sendmail(sender_email, recipient_email, email_message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")
    finally:
        # Close the connection with the SMTP server
        server.quit()

# Example usage
sender_email = "your_email@gmail.com"
sender_password = "your_password"
recipient_email = "recipient_email@example.com"
subject = "Security Incident Notification"
message = "Dear Team,\n\nWe have detected a security incident on our network. Please review the details and take appropriate action.\n\nRegards,\nSecurity Team"

send_email(sender_email, sender_password, recipient_email, subject, message)

