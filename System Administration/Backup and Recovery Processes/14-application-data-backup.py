import shutil
import os
import datetime

# Source directory containing application data
source_directory = "/path/to/application/data"

# Destination directory to store backups
backup_directory = "/path/to/backup/directory"

# Backup filename format
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
backup_filename = f"backup_{timestamp}.zip"

# Create backup directory if it doesn't exist
os.makedirs(backup_directory, exist_ok=True)

# Compress and backup the application data
try:
    shutil.make_archive(os.path.join(backup_directory, backup_filename), 'zip', source_directory)
    print("Backup created successfully!")
except Exception as e:
    print(f"Backup creation failed: {str(e)}")

