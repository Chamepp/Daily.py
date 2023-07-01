import paramiko

def setup_ssh_key(server_ip, username, password, public_key_path):
    # Connect to the server using SSH
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(server_ip, username=username, password=password)

    try:
        # Read the contents of the public key file
        with open(public_key_path, 'r') as file:
            public_key = file.read().strip()

        # Append the public key to the authorized_keys file
        ssh_client.exec_command('echo "{}" >> ~/.ssh/authorized_keys'.format(public_key))

        print("SSH key setup completed successfully.")
    except Exception as e:
        print("Error occurred while setting up SSH key:", str(e))
    finally:
        # Close the SSH connection
        ssh_client.close()

# Example usage
server_ip = input("Enter the server IP: ")
username = input("Enter the SSH username: ")
password = input("Enter the SSH password: ")
public_key_path = input("Enter the path to the public key file: ")

setup_ssh_key(server_ip, username, password, public_key_path)

