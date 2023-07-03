import shutil
import os
import datetime

# Directory paths for configuration files and backup destination
config_directory = "/etc"
backup_directory = "/path/to/backup"

# Create a backup directory with the current date and time
backup_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_path = os.path.join(backup_directory, backup_timestamp)
os.makedirs(backup_path)

# List of configuration files to backup
config_files = [
    "apache2/apache2.conf",
    "nginx/nginx.conf",
    "iptables/rules.v4",
    "iptables/rules.v6",
    # Add more configuration files as needed
]

# Perform backup for each configuration file
for config_file in config_files:
    source_path = os.path.join(config_directory, config_file)
    destination_path = os.path.join(backup_path, config_file)

    try:
        shutil.copy2(source_path, destination_path)
        print(f"Backup successful: {config_file}")
    except Exception as e:
        print(f"Backup failed: {config_file}\nError: {str(e)}")

print("Backup process completed!")

