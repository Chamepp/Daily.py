import paramiko

# Server details
servers = [
    {
        'hostname': 'server1.example.com',
        'username': 'admin',
        'password': 'password',
        'config_file': 'server1.conf'
    },
    {
        'hostname': 'server2.example.com',
        'username': 'admin',
        'password': 'password',
        'config_file': 'server2.conf'
    }
]

# Local configuration file
local_config_file = 'local.conf'

def copy_config_to_servers():
    for server in servers:
        hostname = server['hostname']
        username = server['username']
        password = server['password']
        config_file = server['config_file']

        # Establish SSH connection
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname, username=username, password=password)

        # Upload local configuration file to server
        sftp = ssh_client.open_sftp()
        sftp.put(local_config_file, config_file)
        sftp.close()

        print(f"Configuration file '{local_config_file}' copied to '{hostname}' as '{config_file}'")

        # Close SSH connection
        ssh_client.close()

# Example usage
copy_config_to_servers()

