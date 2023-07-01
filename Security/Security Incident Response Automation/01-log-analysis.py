import re

def analyze_logs(log_file):
    suspicious_patterns = ['Unauthorized access', 'SQL injection', 'Brute force attack']

    with open(log_file, 'r') as file:
        logs = file.readlines()

        for line in logs:
            for pattern in suspicious_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    print(f"Potential security incident detected: {line}")

# Example usage
log_file = 'server_logs.txt'
analyze_logs(log_file)

