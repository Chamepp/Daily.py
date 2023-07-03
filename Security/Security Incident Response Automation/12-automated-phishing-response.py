import re

def is_phishing_email(email_subject):
    # Perform pattern matching to detect potential phishing indicators
    phishing_patterns = ['urgent', 'verify', 'account', 'security', 'suspicious']
    for pattern in phishing_patterns:
        if re.search(pattern, email_subject, re.IGNORECASE):
            return True
    return False

def send_response(email_sender):
    # Send an automated response to the sender of the phishing email
    response = """Dear {},
    
Thank you for your email. We appreciate your vigilance in reporting potential phishing emails. Our security team will investigate the matter accordingly.

Best regards,
Your Organization""".format(email_sender)
    # Code to send the response email goes here (implementation depends on your email sending method)

# Example usage
email_subject = input("Enter the subject of the email: ")
email_sender = input("Enter the sender of the email: ")

if is_phishing_email(email_subject):
    send_response(email_sender)
    print("Automated response sent to the sender.")
else:
    print("This email is not identified as a phishing attempt.")

