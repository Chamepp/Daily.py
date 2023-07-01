import subprocess

def deploy_application(server_ip, application_path):
    # Connect to the server using SSH
    ssh_command = f"ssh username@{server_ip}"

    # Change to the application directory
    change_directory_command = f"cd {application_path}"

    # Pull the latest code from the Git repository
    git_pull_command = "git pull"

    # Build and compile the application
    build_command = "make build"

    # Restart the application server
    restart_command = "sudo systemctl restart application"

    # Execute the commands on the remote server
    try:
        subprocess.check_call(f"{ssh_command} '{change_directory_command}; {git_pull_command}; {build_command}; {restart_command}'", shell=True)
        print("Application deployment successful!")
    except subprocess.CalledProcessError:
        print("Error occurred during application deployment.")

# Example usage
server_ip = "123.456.789.0"
application_path = "/path/to/application"

deploy_application(server_ip, application_path)

