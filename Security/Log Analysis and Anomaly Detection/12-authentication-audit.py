import re

def analyze_authentication_logs(log_file_path):
    failed_attempts = {}
    successful_logins = {}

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            if 'Failed login' in line:
                username = re.search('user=([^\s]+)', line).group(1)
                ip_address = re.search('src=([^\s]+)', line).group(1)

                if username in failed_attempts:
                    failed_attempts[username].append(ip_address)
                else:
                    failed_attempts[username] = [ip_address]
            elif 'Successful login' in line:
                username = re.search('user=([^\s]+)', line).group(1)
                ip_address = re.search('src=([^\s]+)', line).group(1)

                if username in successful_logins:
                    successful_logins[username].append(ip_address)
                else:
                    successful_logins[username] = [ip_address]

    print("=== Failed Login Attempts ===")
    for username, ips in failed_attempts.items():
        print(f"Username: {username}")
        print("IP Addresses:", ", ".join(ips))
        print()

    print("=== Successful Logins ===")
    for username, ips in successful_logins.items():
        print(f"Username: {username}")
        print("IP Addresses:", ", ".join(ips))
        print()

# Example usage
log_file_path = 'authentication.log'
analyze_authentication_logs(log_file_path)

