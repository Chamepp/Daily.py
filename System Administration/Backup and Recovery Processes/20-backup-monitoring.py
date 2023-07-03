import subprocess
import smtplib
from email.message import EmailMessage

# Define backup command or script to be monitored
backup_command = "python backup_script.py"

# Define email parameters
smtp_server = "your_smtp_server"
smtp_port = 587
smtp_username = "your_username"
smtp_password = "your_password"
sender_email = "sender@example.com"
receiver_email = "receiver@example.com"

def send_email(subject, body):
    # Create email message
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

def monitor_backup_process():
    try:
        # Run the backup command or script
        process = subprocess.run(backup_command, shell=True, capture_output=True, text=True)

        # Check the process exit code
        if process.returncode == 0:
            print("Backup process completed successfully!")
        else:
            # Backup process failed, send an email notification
            subject = "Backup Process Failed!"
            body = f"The backup process encountered an error.\n\nError message: {process.stderr}"
            send_email(subject, body)
            print("Backup process failed. Email notification sent.")
    except Exception as e:
        # An exception occurred, send an email notification
        subject = "Backup Process Error!"
        body = f"An error occurred during the backup process.\n\nError message: {str(e)}"
        send_email(subject, body)
        print("An error occurred during the backup process. Email notification sent.")

# Run the backup process monitoring
monitor_backup_process()

