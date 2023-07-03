import shutil
import datetime
import os

def create_versioned_backup(source_path, backup_directory):
    # Create a timestamp for the backup filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create the backup filename
    backup_filename = f"backup_{timestamp}.zip"

    # Construct the full backup file path
    backup_path = os.path.join(backup_directory, backup_filename)

    # Create a zip archive of the source directory
    shutil.make_archive(source_path, 'zip', source_path)

    # Move the zip archive to the backup directory
    shutil.move(f"{source_path}.zip", backup_path)

    print(f"Backup created: {backup_filename}")

# Example usage
source_directory = "/path/to/source/directory"
backup_directory = "/path/to/backup/directory"

create_versioned_backup(source_directory, backup_directory)

