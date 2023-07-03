import os
import shutil

def backup_files(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get the list of files in the source directory
    files = os.listdir(source_dir)

    # Copy each file from the source directory to the destination directory
    for file in files:
        source_file = os.path.join(source_dir, file)
        destination_file = os.path.join(destination_dir, file)
        shutil.copy2(source_file, destination_file)

    print("Backup completed successfully!")

# Example usage
source_directory = "/path/to/source/directory"
destination_directory = "/path/to/destination/directory"

backup_files(source_directory, destination_directory)

