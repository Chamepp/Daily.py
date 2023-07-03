import hashlib
import os

def calculate_checksum(file_path):
    """Calculate the checksum (SHA-256) of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        # Read the file in chunks to handle large files efficiently
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def verify_backup_integrity(backup_directory):
    """Verify the integrity of backup files in the given directory."""
    for root, dirs, files in os.walk(backup_directory):
        for file in files:
            file_path = os.path.join(root, file)
            checksum = calculate_checksum(file_path)
            print(f"Verifying {file_path}...")
            # Compare the calculated checksum with the stored checksum
            # (You would need to adjust this based on how your backups are stored)
            if checksum == get_stored_checksum(file_path):
                print("Integrity check passed!")
            else:
                print("Integrity check failed!")

# Example usage
backup_directory = "/path/to/backup/directory"
verify_backup_integrity(backup_directory)

