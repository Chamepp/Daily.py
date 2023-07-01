import subprocess

def deploy_application(server_ip, application_path):
    try:
        # Connect to the server via SSH and execute deployment commands
        ssh_command = f'ssh user@{server_ip} "cd {application_path} && git pull origin main && ./deploy.sh"'
        subprocess.run(ssh_command, shell=True, check=True)
        print("Application deployed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error deploying application: {str(e)}")

# Example usage
server_ip = "123.456.789.0"  # Replace with the actual server IP
application_path = "/path/to/application"  # Replace with the actual application path on the server

deploy_application(server_ip, application_path)

