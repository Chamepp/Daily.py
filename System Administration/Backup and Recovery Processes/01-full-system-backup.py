import shutil
import datetime

def create_backup(backup_dir):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_folder = backup_dir + "/backup_" + timestamp
    
    try:
        shutil.copytree("/", backup_folder)
        print("Full system backup created successfully at:", backup_folder)
    except Exception as e:
        print("Error creating backup:", str(e))

# Specify the directory where backups will be stored
backup_directory = "/path/to/backup/directory"

# Create the backup
create_backup(backup_directory)

