import time
import psutil
import smtplib
from email.mime.text import MIMEText

# Configure the email settings
SMTP_SERVER = 'your_smtp_server'
SMTP_PORT = 587
SMTP_USERNAME = 'your_username'
SMTP_PASSWORD = 'your_password'
SENDER_EMAIL = 'sender@example.com'
RECIPIENT_EMAIL = 'recipient@example.com'

# Define the threshold for CPU usage (in percentage)
CPU_THRESHOLD = 80

def send_email_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'Infrastructure Alert'
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
            print('Alert email sent!')
    except Exception as e:
        print('Failed to send email alert:', str(e))

def monitor_cpu_usage():
    while True:
        cpu_percent = psutil.cpu_percent()
        print('Current CPU usage:', cpu_percent)

        if cpu_percent > CPU_THRESHOLD:
            message = f'High CPU usage detected! Current usage: {cpu_percent}%'
            send_email_alert(message)

        time.sleep(5)  # Sleep for 5 seconds before checking CPU usage again

# Start monitoring CPU usage
monitor_cpu_usage()

