import subprocess
import datetime

def create_filesystem_snapshot(source_directory, snapshot_directory):
    # Create a timestamp for the snapshot
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Generate the snapshot directory path with the timestamp
    snapshot_path = f"{snapshot_directory}/{timestamp}"
    
    # Create the snapshot using rsync command
    try:
        subprocess.run(['rsync', '-a', '--delete', source_directory, snapshot_path], check=True)
        print(f"Filesystem snapshot created successfully at {snapshot_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating filesystem snapshot: {e}")

# Example usage
source_directory = "/path/to/source/directory"
snapshot_directory = "/path/to/snapshot/directory"

create_filesystem_snapshot(source_directory, snapshot_directory)

