import re

def analyze_web_logs(log_file):
    suspicious_patterns = [r"SELECT\s.+\sFROM", r"<script>", r"eval\(", r"document\.write\("]

    with open(log_file, 'r') as file:
        for line in file:
            for pattern in suspicious_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    print("Suspicious pattern found:")
                    print(line)

# Example usage
log_file = "web_server_logs.txt"
analyze_web_logs(log_file)

