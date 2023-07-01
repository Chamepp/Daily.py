import time

def monitor_logs():
    log_file = "/var/log/security.log"  # Path to the security log file
    previous_size = 0  # Variable to store the size of the log file
    
    while True:
        # Open the log file in read-only mode
        with open(log_file, "r") as file:
            # Move the file pointer to the previous end of the file
            file.seek(previous_size)
            
            # Read the new log entries
            new_logs = file.read()
            
            # Process the new log entries (e.g., perform analysis, raise alerts, etc.)
            process_logs(new_logs)
            
            # Update the previous size to the current end of the file
            previous_size = file.tell()
        
        # Wait for a specific duration before checking for new logs again
        time.sleep(5)  # Adjust the duration as per your requirements

def process_logs(logs):
    # Perform analysis or raise alerts based on the log entries
    # Example: Print the new log entries
    print(logs)

# Start monitoring logs
monitor_logs()

