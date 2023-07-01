import shutil
import os
import datetime

def backup_directory(source_dir, destination_dir):
    # Create a new directory with the current date and time
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(destination_dir, f"backup_{current_time}")

    # Copy the contents of the source directory to the backup directory
    try:
        shutil.copytree(source_dir, backup_dir)
        print(f"Backup created successfully at: {backup_dir}")
    except shutil.Error as e:
        print(f"Backup failed: {e}")

# Set the source and destination directories
source_directory = "/path/to/source/directory"
destination_directory = "/path/to/destination/directory"

# Call the backup_directory function
backup_directory(source_directory, destination_directory)
