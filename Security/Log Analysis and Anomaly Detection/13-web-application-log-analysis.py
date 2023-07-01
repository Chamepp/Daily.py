import re

def analyze_web_logs(log_file_path):
    # Open the log file
    with open(log_file_path, 'r') as log_file:
        # Read each line in the log file
        for line in log_file:
            # Extract the request URL from the log entry using regex
            match = re.search(r'"(GET|POST) (.*?) HTTP', line)
            if match:
                request_url = match.group(2)
                
                # Check for potential web application attacks in the request URL
                if is_malicious_url(request_url):
                    print(f"Potential attack detected: {request_url}")

def is_malicious_url(url):
    # Add your custom logic here to detect potential malicious URLs
    # You can use regex or predefined attack patterns to identify attacks
    
    # Example: Check for SQL injection attacks
    if re.search(r'\b(SELECT|UNION|FROM|WHERE)\b', url, re.IGNORECASE):
        return True
    
    # Example: Check for cross-site scripting (XSS) attacks
    if re.search(r'<script>', url, re.IGNORECASE):
        return True
    
    return False

# Example usage
log_file_path = "webserver_logs.txt"  # Replace with the path to your web server log file
analyze_web_logs(log_file_path)

