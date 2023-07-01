import smtplib

def send_email(subject, body):
    sender_email = "your_email@example.com"
    receiver_email = "recipient_email@example.com"
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_username"
    password = "your_password"

    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(sender_email, receiver_email, message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

# Example usage
incident_id = "INC1234"
severity = "High"
description = "A security incident has been detected."

subject = f"Incident Escalation - {incident_id}"
body = f"Incident ID: {incident_id}\nSeverity: {severity}\nDescription: {description}"

send_email(subject, body)

