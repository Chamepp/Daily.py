import paramiko

# Configuration parameters
host = 'example.com'
username = 'your_username'
password = 'your_password'
config_file = 'config.txt'

def configure_server():
    # Establish SSH connection
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    
    try:
        # Upload configuration file
        sftp = client.open_sftp()
        sftp.put(config_file, f'/home/{username}/{config_file}')
        sftp.close()
        
        # Execute configuration commands
        command = f'sudo cp /home/{username}/{config_file} /etc/myapp/config.txt && sudo service myapp restart'
        stdin, stdout, stderr = client.exec_command(command)
        
        # Check for errors during execution
        error = stderr.read().decode().strip()
        if error:
            print(f'Error executing configuration commands: {error}')
        else:
            print('Server configuration completed successfully!')
    
    finally:
        # Close SSH connection
        client.close()

# Call the function to initiate configuration management
configure_server()

