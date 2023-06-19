import feedparser
import smtplib
from email.mime.text import MIMEText

def convert_rss_to_email(feed_url, recipient_email):
    # Parse the RSS feed
    feed = feedparser.parse(feed_url)

    # Create the email message
    message = MIMEText(f"Latest news from {feed.feed.title}:\n\n")
    message['Subject'] = f"RSS Feed Update: {feed.feed.title}"
    message['From'] = 'your_email@example.com'
    message['To'] = recipient_email

    # Add the feed entries to the email body
    for entry in feed.entries:
        message_text = f"{entry.title}: {entry.link}\n"
        message.attach(MIMEText(message_text))

    # Send the email
    smtp_server = 'your_smtp_server'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(message['From'], message['To'], message.as_string())

# Example usage
rss_feed_url = 'https://example.com/rss_feed.xml'
recipient_email = 'recipient@example.com'
convert_rss_to_email(rss_feed_url, recipient_email)
