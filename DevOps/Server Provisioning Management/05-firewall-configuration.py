import subprocess

# Define the list of allowed ports and IP addresses
allowed_ports = ['22', '80', '443']
allowed_ip_addresses = ['192.168.0.1', '10.0.0.1']

def configure_firewall():
    # Flush existing firewall rules
    subprocess.run(['iptables', '-F'])

    # Set default policies to drop all incoming and outgoing traffic
    subprocess.run(['iptables', '-P', 'INPUT', 'DROP'])
    subprocess.run(['iptables', '-P', 'OUTPUT', 'DROP'])

    # Allow loopback traffic
    subprocess.run(['iptables', '-A', 'INPUT', '-i', 'lo', '-j', 'ACCEPT'])
    subprocess.run(['iptables', '-A', 'OUTPUT', '-o', 'lo', '-j', 'ACCEPT'])

    # Allow incoming connections on allowed ports
    for port in allowed_ports:
        subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', port, '-j', 'ACCEPT'])

    # Allow outgoing connections to allowed IP addresses
    for ip in allowed_ip_addresses:
        subprocess.run(['iptables', '-A', 'OUTPUT', '-d', ip, '-j', 'ACCEPT'])

    # Drop all other incoming and outgoing traffic
    subprocess.run(['iptables', '-A', 'INPUT', '-j', 'DROP'])
    subprocess.run(['iptables', '-A', 'OUTPUT', '-j', 'DROP'])

    # Save the firewall rules
    subprocess.run(['iptables-save', '>', '/etc/iptables/rules.v4'])

    print("Firewall configuration completed successfully.")

# Call the function to configure the firewall
configure_firewall()

