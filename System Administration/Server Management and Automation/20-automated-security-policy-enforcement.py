import paramiko

def enforce_security_policy(server_ip, username, password):
    # Connect to the server using SSH
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server_ip, username=username, password=password)

    # Define the security policy commands
    security_commands = [
        "firewall-cmd --zone=public --add-port=80/tcp --permanent",
        "firewall-cmd --zone=public --add-port=443/tcp --permanent",
        "firewall-cmd --reload",
        "setsebool -P httpd_can_network_connect on",
        "setsebool -P httpd_can_sendmail on",
        # Add more security commands as needed
    ]

    # Execute the security policy commands
    for command in security_commands:
        stdin, stdout, stderr = client.exec_command(command)
        # Optionally, you can check the command output or handle any errors

    # Close the SSH connection
    client.close()

# Example usage
server_ip = "192.168.0.1"
username = "admin"
password = "password"

enforce_security_policy(server_ip, username, password)

