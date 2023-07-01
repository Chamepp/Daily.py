import subprocess

def isolate_endpoint(endpoint_ip):
    # Execute the command to isolate the endpoint using firewall rules or network access control
    command = f"your_isolation_command {endpoint_ip}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Check the command execution result
    if result.returncode == 0:
        print(f"Endpoint {endpoint_ip} has been successfully isolated.")
    else:
        print(f"Failed to isolate endpoint {endpoint_ip}. Error: {result.stderr}")

# Example usage
endpoint_ip = input("Enter the IP address of the endpoint to isolate: ")
isolate_endpoint(endpoint_ip)

