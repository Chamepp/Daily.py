import paramiko

def provision_server(hostname, username, password, commands):
    # Connect to the server
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)

    try:
        # Execute the provisioning commands
        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')

            if output:
                print(f"Command: {command}\nOutput: {output.strip()}\n")
            if error:
                print(f"Command: {command}\nError: {error.strip()}\n")

        print("Server provisioning completed successfully.")

    except Exception as e:
        print("An error occurred during server provisioning:", str(e))

    finally:
        # Close the SSH connection
        ssh.close()

# Example usage
hostname = 'your_server_hostname'
username = 'your_username'
password = 'your_password'

# List of provisioning commands
commands = [
    'sudo apt update',
    'sudo apt upgrade -y',
    'sudo apt install nginx -y',
    'sudo systemctl enable nginx',
    'sudo systemctl start nginx'
]

# Call the function to provision the server
provision_server(hostname, username, password, commands)

