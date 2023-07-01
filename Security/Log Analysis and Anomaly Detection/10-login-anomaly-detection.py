import datetime
import re

# Regular expression pattern for extracting IP address from log entry
ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

def is_login_anomaly(log_entry):
    # Extract the IP address from the log entry
    ip_address = re.search(ip_pattern, log_entry).group()

    # Get the current date and time
    current_time = datetime.datetime.now()

    # Get the hour of the day
    current_hour = current_time.hour

    # Check if the login time is outside the normal working hours (9 AM to 6 PM)
    if current_hour < 9 or current_hour > 18:
        return True

    # Check if the login location is outside the normal IP range
    if not is_normal_ip_range(ip_address):
        return True

    return False

def is_normal_ip_range(ip_address):
    # Replace this with your own logic to determine the normal IP range
    normal_ip_range = ["192.168.

