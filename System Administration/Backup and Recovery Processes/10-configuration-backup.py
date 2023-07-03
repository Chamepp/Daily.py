import shutil
import os

# Source directory containing configuration files
source_directory = "/etc/"

# Destination directory for backups
backup_directory = "/path/to/backup/"

# List of configuration files to be backed up
configuration_files = [
    "apache2/apache2.conf",
    "nginx/nginx.conf",
    "iptables/rules.v4",
    "iptables/rules.v6",
    # Add more configuration files as needed
]

# Create the backup directory if it doesn't exist
os.makedirs(backup_directory, exist_ok=True)

# Iterate over the configuration files and perform the backup
for file in configuration_files:
    source_path = os.path.join(source_directory, file)
    backup_path = os.path.join(backup_directory, file)

    # Check if the source file exists
    if os.path.isfile(source_path):
        # Create the backup by copying the source file to the backup directory
        shutil.copy2(source_path, backup_path)
        print(f"Backup created for {file}")
    else:
        print(f"Source file {file} does not exist. Skipping backup.")

print("Backup process completed.")

