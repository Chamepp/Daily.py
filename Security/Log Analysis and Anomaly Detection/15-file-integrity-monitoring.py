import os
import hashlib

def calculate_hash(file_path):
    """Calculate the hash (SHA-256) of a file."""
    hash_object = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def monitor_files(directory):
    """Monitor files in a directory for changes in their integrity."""
    file_hashes = {}

    # Calculate initial hashes for all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = calculate_hash(file_path)

    print("File integrity monitoring started...")
    
    # Continuously monitor files for changes
    while True:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                current_hash = calculate_hash(file_path)
                
                if file_path in file_hashes:
                    if current_hash != file_hashes[file_path]:
                        print(f"File '{file_path}' has been modified!")
                else:
                    print(f"New file detected: '{file_path}'")
                    file_hashes[file_path] = current_hash

        # Wait for a specified interval before checking again
        time.sleep(60)  # Adjust the interval as needed

# Example usage
directory_to_monitor = "/path/to/directory"
monitor_files(directory_to_monitor)

