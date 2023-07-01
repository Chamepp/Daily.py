import shutil
import os

def backup_files(source_dir, destination_dir):
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print("Source directory does not exist.")
        return

    # Create the destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Get the list of files in the source directory
    files = os.listdir(source_dir)

    # Copy each file from the source directory to the destination directory
    for file in files:
        source_file = os.path.join(source_dir, file)
        destination_file = os.path.join(destination_dir, file)
        shutil.copy2(source_file, destination_file)
        print(f"Copied {source_file} to {destination_file}")

    print("Backup completed successfully.")

# Example usage:
source_directory = "path/to/source/directory"
destination_directory = "path/to/destination/directory"

backup_files(source_directory, destination_directory)
