import shutil
import os
import datetime

def backup_directory(source_dir, destination_dir):
    # Create a backup folder with the current date and time
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_folder = os.path.join(destination_dir, f"backup_{timestamp}")

    # Copy the contents of the source directory to the backup folder
    try:
        shutil.copytree(source_dir, backup_folder)
        print(f"Backup created successfully at {backup_folder}")
    except OSError as e:
        print(f"Backup creation failed: {e}")

# Example usage
source_directory = "/path/to/source/directory"
destination_directory = "/path/to/destination/directory"

backup_directory(source_directory, destination_directory)

