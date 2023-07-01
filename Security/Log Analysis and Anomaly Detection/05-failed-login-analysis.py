import re

def analyze_failed_logins(log_file):
    suspicious_attempts = []
    
    with open(log_file, 'r') as file:
        for line in file:
            # Check if the line contains a failed login attempt
            if "Failed login" in line:
                # Extract relevant information like timestamp and IP address using regular expressions
                timestamp = re.search(r'\[(.*?)\]', line).group(1)
                ip_address = re.search(r'from ([\d.]+)', line).group(1)
                
                # Add the suspicious attempt to the list
                suspicious_attempts.append({'Timestamp': timestamp, 'IP Address': ip_address})
    
    return suspicious_attempts

# Example usage
log_file = 'auth.log'
suspicious_attempts = analyze_failed_logins(log_file)

# Print the suspicious attempts
for attempt in suspicious_attempts:
    print("Suspicious attempt at", attempt['Timestamp'], "from IP:", attempt['IP Address'])

