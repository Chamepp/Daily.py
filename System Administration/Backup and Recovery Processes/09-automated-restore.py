import shutil

def restore_backup(backup_path, restore_location):
    try:
        # Copy the backup files to the restore location
        shutil.copytree(backup_path, restore_location)
        print("Backup successfully restored to:", restore_location)
    except Exception as e:
        print("Error occurred during backup restoration:", str(e))

# Example usage
backup_path = "/path/to/backup"
restore_location = "/path/to/restore/location"

restore_backup(backup_path, restore_location)

