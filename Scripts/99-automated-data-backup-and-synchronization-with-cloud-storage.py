import os
import dropbox
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set up Dropbox API connection
dbx = dropbox.Dropbox(os.getenv("DROPBOX_ACCESS_TOKEN"))

# Local directory to be backed up
local_directory = "/path/to/local/directory"

# Dropbox directory for backup
dropbox_directory = "/path/to/dropbox/directory"

# Function to upload files to Dropbox
def upload_to_dropbox(local_file_path, dropbox_file_path):
    with open(local_file_path, "rb") as file:
        dbx.files_upload(file.read(), dropbox_file_path, mode=dropbox.files.WriteMode.overwrite)

# Function to recursively upload files in a directory
def upload_directory_to_dropbox(local_directory, dropbox_directory):
    for root, dirs, files in os.walk(local_directory):
        for file in files:
            local_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_file_path, local_directory)
            dropbox_file_path = os.path.join(dropbox_directory, relative_path)
            upload_to_dropbox(local_file_path, dropbox_file_path)

# Perform backup and synchronization
upload_directory_to_dropbox(local_directory, dropbox_directory)
print("Backup completed successfully.")
