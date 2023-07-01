import paramiko

# Server details
server_ip = "192.168.0.1"
server_username = "admin"
server_password = "password"
os_image_path = "/path/to/os_image.iso"

# SSH connection setup
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the server
ssh_client.connect(server_ip, username=server_username, password=server_password)

# Command to mount and install the OS image
mount_command = f"mount -o loop {os_image_path} /mnt"
install_command = "cd /mnt && ./install.sh"  # Replace with the actual installation command

# Execute the commands
stdin, stdout, stderr = ssh_client.exec_command(mount_command)
# Handle stdout and stderr if needed

stdin, stdout, stderr = ssh_client.exec_command(install_command)
# Handle stdout and stderr if needed

# Close the SSH connection
ssh_client.close()

