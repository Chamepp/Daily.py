import paramiko

def configure_firewall(hostname, username, password, firewall_rules):
    # Establish SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)

    # Execute firewall configuration commands
    for rule in firewall_rules:
        command = f"sudo iptables {rule}"
        stdin, stdout, stderr = ssh.exec_command(command)
        # Add error handling or logging if desired

    # Close SSH connection
    ssh.close()

# Example usage
hostname = "your_server_hostname"
username = "your_username"
password = "your_password"
firewall_rules = [
    "-A INPUT -p tcp --dport 80 -j ACCEPT",
    "-A INPUT -p tcp --dport 443 -j ACCEPT",
    "-A INPUT -j DROP"
]

configure_firewall(hostname, username, password, firewall_rules)

