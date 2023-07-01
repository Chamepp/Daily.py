import re

# Function to analyze network traffic logs
def analyze_traffic_logs(logs):
    suspicious_connections = []

    # Regular expression pattern to match suspicious IP addresses or domains
    suspicious_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|(example\.com)'

    # Iterate through the logs
    for log in logs:
        # Extract the source and destination IP addresses or domains
        match = re.search(suspicious_pattern, log)
        if match:
            suspicious_connections.append(log)

    return suspicious_connections

# Example usage
network_logs = [
    '2023-06-01 12:05:28 | Source: 192.168.1.10, Destination: 104.27.136.224',
    '2023-06-01 12:07:15 | Source: 192.168.1.20, Destination: example.com',
    '2023-06-01 12:10:42 | Source: 192.168.1.30, Destination: 172.16.0.12',
    '2023-06-01 12:12:55 | Source: 192.168.1.40, Destination: 10.0.0.5',
]

suspicious_connections = analyze_traffic_logs(network_logs)

if suspicious_connections:
    print("Suspicious connections found:")
    for connection in suspicious_connections:
        print(connection)
else:
    print("No suspicious connections found.")

