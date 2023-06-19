import subprocess

def check_server_status(hostname):
    # Ping the server to check if it's reachable
    result = subprocess.run(['ping', '-c', '1', hostname], capture_output=True)
    
    if result.returncode == 0:
        print(f"Server {hostname} is reachable.")
    else:
        print(f"Server {hostname} is not reachable.")

# Specify the hostname or IP address of the server you want to monitor
server_hostname = "example.com"

# Call the function to check the server status
check_server_status(server_hostname)
