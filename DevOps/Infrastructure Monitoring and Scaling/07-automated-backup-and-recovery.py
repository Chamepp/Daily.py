import os
import shutil
import datetime

def backup_files(source_dir, backup_dir):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_folder = os.path.join(backup_dir, f"backup_{timestamp}")
    
    try:
        shutil.copytree(source_dir, backup_folder)
        print(f"Backup created successfully at {backup_folder}")
    except Exception as e:
        print(f"Error creating backup: {str(e)}")

def recover_files(source_dir, backup_dir):
    latest_backup = max([f for f in os.listdir(backup_dir) if f.startswith("backup_")])
    backup_folder = os.path.join(backup_dir, latest_backup)
    
    try:
        shutil.rmtree(source_dir)
        shutil.copytree(backup_folder, source_dir)
        print(f"Recovery successful. Restored files from {backup_folder} to {source_dir}")
    except Exception as e:
        print(f"Error recovering files: {str(e)}")

# Example usage
source_directory = "/path/to/source/directory"
backup_directory = "/path/to/backup/directory"

# Backup files
backup_files(source_directory, backup_directory)

# Simulate changes in the source directory (e.g., add, modify, or delete files)

# Recover files from the latest backup
recover_files(source_directory, backup_directory)

