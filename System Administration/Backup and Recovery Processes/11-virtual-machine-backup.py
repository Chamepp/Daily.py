import os
import shutil
import datetime

def backup_virtual_machine(vm_name, backup_path):
    # Generate a timestamp for the backup file
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create a backup directory for the virtual machine
    backup_dir = os.path.join(backup_path, vm_name + "_" + timestamp)
    os.makedirs(backup_dir)

    # Get the current virtual machine image path
    vm_image_path = get_virtual_machine_image_path(vm_name)

    # Copy the virtual machine image to the backup directory
    backup_image_path = os.path.join(backup_dir, os.path.basename(vm_image_path))
    shutil.copy2(vm_image_path, backup_image_path)

    print("Virtual machine backup created at:", backup_image_path)

def get_virtual_machine_image_path(vm_name):
    # Replace this with your own logic to retrieve the virtual machine image path
    # Example: For VMware, you can use the vmrun command to get the VMX file path
    vm_image_path = "/path/to/vm/" + vm_name + ".vmx"
    return vm_image_path

# Example usage
vm_name = input("Enter the name of the virtual machine: ")
backup_path = input("Enter the path to store the backup: ")

backup_virtual_machine(vm_name, backup_path)

