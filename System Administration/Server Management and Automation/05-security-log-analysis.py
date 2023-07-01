import re

def analyze_security_logs(log_file):
    # Open the log file for reading
    with open(log_file, 'r') as file:
        # Read the log file line by line
        for line in file:
            # Perform pattern matching to extract relevant information
            # Here, we assume the log contains timestamps and log messages
            # You can customize the regular expressions based on your log format
            timestamp = re.search(r'\[(.*?)\]', line).group(1)
            log_message = re.search(r'\](.*)', line).group(1).strip()
            
            # Perform security log analysis based on specific patterns or keywords
            if re.search(r'access denied', log_message, re.IGNORECASE):
                print(f"[{timestamp}] ALERT: Access denied - {log_message}")
            elif re.search(r'failed login', log_message, re.IGNORECASE):
                print(f"[{timestamp}] ALERT: Failed login attempt - {log_message}")
            elif re.search(r'suspicious activity', log_message, re.IGNORECASE):
                print(f"[{timestamp}] ALERT: Suspicious activity detected - {log_message}")
            # Add more patterns or keywords to match specific security events
            
            # Perform additional analysis or actions based on the log entry
            
        # End of log file analysis

# Example usage
log_file = "security_logs.txt"  # Replace with the path to your security log file
analyze_security_logs(log_file)

