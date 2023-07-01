import subprocess

def install_monitoring_tools():
    # Install monitoring tool dependencies
    subprocess.run(['apt', 'update'])
    subprocess.run(['apt', 'install', '-y', 'python3-pip'])

    # Install monitoring tools using pip
    subprocess.run(['pip3', 'install', 'prometheus_client'])
    subprocess.run(['pip3', 'install', 'node_exporter'])

    # Configure and start monitoring services
    subprocess.run(['systemctl', 'start', 'node_exporter.service'])
    subprocess.run(['systemctl', 'enable', 'node_exporter.service'])

    print("Monitoring tools installation and configuration completed successfully.")

# Call the function to install and configure monitoring tools
install_monitoring_tools()

