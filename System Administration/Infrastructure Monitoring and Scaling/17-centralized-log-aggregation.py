import os
import shutil

# Define the source directory where log files are located
log_directory = "/path/to/logs"

# Define the destination directory for centralized log aggregation
centralized_log_directory = "/path/to/centralized/logs"

# Check if the source directory exists
if not os.path.exists(log_directory):
    print(f"Source directory '{log_directory}' does not exist.")
    exit()

# Check if the destination directory exists, create if it doesn't
if not os.path.exists(centralized_log_directory):
    os.makedirs(centralized_log_directory)
    print(f"Created destination directory '{centralized_log_directory}'.")

# Iterate over the files in the source directory
for filename in os.listdir(log_directory):
    source_file = os.path.join(log_directory, filename)
    destination_file = os.path.join(centralized_log_directory, filename)

    # Check if the file is a regular file (not a directory)
    if os.path.isfile(source_file):
        # Copy the log file to the destination directory
        shutil.copy2(source_file, destination_file)
        print(f"Log file '{filename}' copied to centralized log directory.")

print("Log aggregation completed successfully.")

