import paramiko

def automate_security_hardening(server_ip, username, password):
    try:
        # Connect to the server using SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(server_ip, username=username, password=password)
        
        # Disable unused services
        disable_services = ["telnet", "ftp", "rsh"]
        for service in disable_services:
            command = f"sudo systemctl stop {service} && sudo systemctl disable {service}"
            stdin, stdout, stderr = ssh_client.exec_command(command)
            print(stdout.read().decode())
        
        # Apply security patches
        update_command = "sudo apt update && sudo apt upgrade -y"
        stdin, stdout, stderr = ssh_client.exec_command(update_command)
        print(stdout.read().decode())
        
        # Secure SSH configuration
        ssh_config_command = "sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config"
        stdin, stdout, stderr = ssh_client.exec_command(ssh_config_command)
        print(stdout.read().decode())
        
        # Restart SSH service
        restart_ssh_command = "sudo systemctl restart sshd"
        stdin, stdout, stderr = ssh_client.exec_command(restart_ssh_command)
        print(stdout.read().decode())
        
        print("Security hardening tasks completed successfully!")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        ssh_client.close()

# Example usage
server_ip = "192.168.0.100"
username = "admin"
password = "password123"

automate_security_hardening(server_ip, username, password)

