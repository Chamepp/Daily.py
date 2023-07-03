import shutil
import gzip

def compress_backup(source_file, destination_file):
    try:
        with open(source_file, 'rb') as source:
            with gzip.open(destination_file, 'wb') as destination:
                shutil.copyfileobj(source, destination)
        print("Backup compressed successfully!")
    except Exception as e:
        print("An error occurred while compressing the backup:", str(e))

# Example usage
source_file = 'backup_file.tar'
destination_file = 'compressed_backup_file.tar.gz'

compress_backup(source_file, destination_file)

