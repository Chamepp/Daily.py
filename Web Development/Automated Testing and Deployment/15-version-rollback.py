import os
import shutil

def rollback(deployment_directory, backup_directory):
    # Check if the backup directory exists
    if os.path.exists(backup_directory):
        # Remove the current deployment directory
        shutil.rmtree(deployment_directory)
        
        # Restore the backup directory to the deployment directory
        shutil.copytree(backup_directory, deployment_directory)
        
        print("Rollback successful. Restored to the previous version.")
    else:
        print("Rollback failed. Backup directory not found.")

# Example usage
deployment_directory = "/path/to/deployment_directory"
backup_directory = "/path/to/backup_directory"

rollback(deployment_directory, backup_directory)

