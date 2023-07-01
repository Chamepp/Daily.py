import os
import shutil
import datetime

# Source directory to backup
source_dir = '/path/to/source'

# Destination directory for backups
backup_dir = '/path/to/backup'

# Create backup directory if it doesn't exist
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Generate backup file name with timestamp
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
backup_file = f'backup_{timestamp}.tar.gz'

# Create a compressed backup archive
backup_path = os.path.join(backup_dir, backup_file)
shutil.make_archive(backup_path, 'gztar', source_dir)

print(f'Backup created: {backup_file}')

