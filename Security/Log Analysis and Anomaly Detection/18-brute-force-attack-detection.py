import collections

# Function to detect brute-force attacks
def detect_brute_force(logs, threshold):
    failed_login_counts = collections.defaultdict(int)

    for log in logs:
        if log["status"] == "failed":
            ip_address = log["ip_address"]
            failed_login_counts[ip_address] += 1

    for ip_address, count in failed_login_counts.items():
        if count >= threshold:
            print(f"Brute-force attack detected from {ip_address} with {count} failed login attempts.")

# Example usage
logs = [
    {"ip_address": "192.168.1.100", "status": "failed"},
    {"ip_address": "192.168.1.101", "status": "failed"},
    {"ip_address": "192.168.1.100", "status": "failed"},
    {"ip_address": "192.168.1.102", "status": "failed"},
    {"ip_address": "192.168.1.100", "status": "failed"},
    {"ip_address": "192.168.1.103", "status": "failed"},
    {"ip_address": "192.168.1.101", "status": "failed"},
]

threshold = 3

detect_brute_force(logs, threshold)

