import shutil
import os
import datetime
import time

# Source directory to be backed up
source_directory = "/path/to/source/directory"

# Destination directory to store the backups
destination_directory = "/path/to/destination/directory"

# Interval between backups in seconds (e.g., 24 hours = 24 * 60 * 60)
backup_interval = 24 * 60 * 60

def perform_backup():
    # Create a timestamp for the backup
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Create a new directory in the destination with the timestamp
    backup_directory = os.path.join(destination_directory, f"backup_{timestamp}")
    os.makedirs(backup_directory)
    
    # Copy all files and directories from the source to the backup directory
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(backup_directory, os.path.relpath(source_path, source_directory))
            shutil.copy2(source_path, destination_path)
    
    print(f"Backup created: {backup_directory}")

# Continuously perform backups at the specified interval
while True:
    perform_backup()
    time.sleep(backup_interval)

