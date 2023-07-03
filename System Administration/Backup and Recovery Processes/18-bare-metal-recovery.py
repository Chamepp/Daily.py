import os
import shutil

def perform_bare_metal_recovery(backup_dir, restore_dir):
    # Check if the backup directory exists
    if not os.path.exists(backup_dir):
        print("Backup directory does not exist.")
        return

    # Check if the restore directory exists
    if os.path.exists(restore_dir):
        print("Restore directory already exists. Please choose a different location.")
        return

    try:
        # Create the restore directory
        os.makedirs(restore_dir)

        # Copy all files from the backup directory to the restore directory
        for root, dirs, files in os.walk(backup_dir):
            for file in files:
                src_path = os.path.join(root, file)
                dest_path = os.path.join(restore_dir, os.path.relpath(src_path, backup_dir))
                shutil.copy2(src_path, dest_path)

        print("Bare metal recovery completed successfully.")
    except Exception as e:
        print("An error occurred during bare metal recovery:", str(e))

# Example usage
backup_directory = "/path/to/backup"
restore_directory = "/path/to/restore"

perform_bare_metal_recovery(backup_directory, restore_directory)

