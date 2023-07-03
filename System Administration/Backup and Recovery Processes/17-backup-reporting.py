import os
import smtplib
from email.mime.text import MIMEText

def generate_backup_report(backup_directory):
    backup_files = os.listdir(backup_directory)
    num_files = len(backup_files)
    report_text = f"Backup Report:\n\nTotal backup files: {num_files}\n\nBackup files:\n"

    for file_name in backup_files:
        report_text += f"- {file_name}\n"

    return report_text

def send_email_report(sender_email, sender_password, recipient_email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print("Backup report email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Error sending backup report email: {str(e)}")

# Example usage
backup_directory = "/path/to/backup/folder"
sender_email = "your_email@gmail.com"
sender_password = "your_password"
recipient_email = "recipient_email@example.com"
subject = "Backup Report"
body = generate_backup_report(backup_directory)
send_email_report(sender_email, sender_password, recipient_email, subject, body)

