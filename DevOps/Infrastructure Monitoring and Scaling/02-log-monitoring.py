import re

# Define the log file path
log_file_path = "/var/log/application.log"

# Define the pattern to search for in the logs
pattern = r"ERROR"

def monitor_logs(log_file_path, pattern):
    try:
        # Open the log file in read mode
        with open(log_file_path, "r") as log_file:
            # Read the contents of the log file
            log_contents = log_file.read()

            # Search for the pattern using regular expressions
            matches = re.findall(pattern, log_contents)

            # Check if any matches are found
            if matches:
                print("Alert: Errors detected in the log file!")
                print("Number of occurrences:", len(matches))
                print("Detailed error lines:")
                for match in matches:
                    print(match)

    except FileNotFoundError:
        print("Log file not found.")

# Call the function to monitor logs
monitor_logs(log_file_path, pattern)

