import shutil
import os

def selective_backup(source_dir, destination_dir, included_dirs=[], excluded_dirs=[]):
    """
    Performs a selective backup of files from source directory to destination directory.
    
    Args:
        source_dir (str): Path to the source directory.
        destination_dir (str): Path to the destination directory where files will be backed up.
        included_dirs (list): List of directories to be included in the backup (default: []).
        excluded_dirs (list): List of directories to be excluded from the backup (default: []).
    """
    for root, dirs, files in os.walk(source_dir):
        # Exclude directories specified in excluded_dirs
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        
        for file in files:
            file_path = os.path.join(root, file)
            
            # Include only files from included_dirs, if specified
            if included_dirs and root not in included_dirs:
                continue
            
            # Create the corresponding directory structure in the destination directory
            dest_path = os.path.join(destination_dir, os.path.relpath(root, source_dir))
            os.makedirs(dest_path, exist_ok=True)
            
            # Copy the file to the destination directory
            shutil.copy2(file_path, dest_path)
            print(f"File {file} backed up successfully.")

# Example usage
source_directory = "/path/to/source/directory"
destination_directory = "/path/to/destination/directory"
included_directories = ["/path/to/source/directory/subdirectory1", "/path/to/source/directory/subdirectory2"]
excluded_directories = ["/path/to/source/directory/excluded_directory"]

selective_backup(source_directory, destination_directory, included_directories, excluded_directories)

