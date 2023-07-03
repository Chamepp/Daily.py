import os
import shutil
import datetime

def perform_incremental_backup(source_dir, backup_dir):
    # Create a timestamped folder for the backup
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_folder = os.path.join(backup_dir, timestamp)

    # Copy new and modified files from the source directory to the backup directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            backup_path = os.path.join(backup_folder, os.path.relpath(source_path, source_dir))
            if not os.path.exists(backup_path) or os.stat(source_path).st_mtime > os.stat(backup_path).st_mtime:
                os.makedirs(os.path.dirname(backup_path), exist_ok=True)
                shutil.copy2(source_path, backup_path)

    print("Incremental backup complete. Files copied:", len(os.listdir(backup_folder)))

# Example usage
source_directory = "/path/to/source"
backup_directory = "/path/to/backup"

perform_incremental_backup(source_directory, backup_directory)

