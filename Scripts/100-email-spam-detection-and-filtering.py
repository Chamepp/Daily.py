import re

# Regular expression patterns for spam keywords
spam_keywords = ['buy now', 'limited time offer', 'amazing deal', 'exclusive discount', 'money back guarantee']

def is_spam(email_subject):
    # Check if the email subject contains any spam keywords
    for keyword in spam_keywords:
        if re.search(keyword, email_subject, re.IGNORECASE):
            return True
    return False

# Example usage
email_subject = input("Enter the subject of the email: ")

if is_spam(email_subject):
    print("Warning: This email might be spam!")
else:
    print("This email is not spam.")
