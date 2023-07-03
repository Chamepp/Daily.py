import os
import shutil
import datetime

# Configuration
backup_dir = '/path/to/backup/directory'
max_backups = 5  # Maximum number of backups to retain

def perform_backup(source_dir, destination_dir):
    # Create a backup directory with the current timestamp
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_path = os.path.join(destination_dir, f'backup_{timestamp}')

    # Perform the backup
    shutil.copytree(source_dir, backup_path)
    print(f'Successfully created backup: {backup_path}')

def cleanup_backups(destination_dir):
    # Get a list of existing backups sorted by creation time
    backups = sorted([entry for entry in os.listdir(destination_dir) if entry.startswith('backup_')])

    # Calculate the number of backups to remove
    num_backups_to_remove = max(0, len(backups) - max_backups)

    # Remove the oldest backups exceeding the retention policy
    for i in range(num_backups_to_remove):
        backup_to_remove = os.path.join(destination_dir, backups[i])
        shutil.rmtree(backup_to_remove)
        print(f'Removed backup: {backup_to_remove}')

# Example usage
source_directory = '/path/to/source/directory'

# Perform the backup
perform_backup(source_directory, backup_dir)

# Cleanup backups based on retention policy
cleanup_backups(backup_dir)

