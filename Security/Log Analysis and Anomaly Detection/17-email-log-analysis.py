import re

# Regular expression pattern for identifying suspicious email activity
suspicious_pattern = r'(phish|spam|suspicious|fraud)'

def analyze_email_logs(log_file):
    suspicious_emails = []
    with open(log_file, 'r') as file:
        for line in file:
            if re.search(suspicious_pattern, line, re.IGNORECASE):
                suspicious_emails.append(line.rstrip('\n'))
    
    return suspicious_emails

# Example usage
log_file = 'email_logs.txt'  # Replace with the path to your email server logs

suspicious_emails = analyze_email_logs(log_file)

if len(suspicious_emails) > 0:
    print("Suspicious emails found:")
    for email in suspicious_emails:
        print(email)
else:
    print("No suspicious emails found.")

