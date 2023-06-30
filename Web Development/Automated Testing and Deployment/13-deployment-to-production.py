import subprocess

def deploy_to_production():
    # Pull the latest code changes from the repository
    subprocess.call(["git", "pull"])

    # Run any necessary build or compilation steps
    subprocess.call(["npm", "install"])  # Example: Install dependencies using npm
    subprocess.call(["npm", "run", "build"])  # Example: Build the web application

    # Stop the running web server or services
    subprocess.call(["sudo", "systemctl", "stop", "my-web-server.service"])

    # Copy the built application to the production directory
    subprocess.call(["cp", "-r", "dist/", "/var/www/my-web-app/"])

    # Restart the web server or services
    subprocess.call(["sudo", "systemctl", "start", "my-web-server.service"])

    # Perform any necessary post-deployment tasks
    subprocess.call(["python", "manage.py", "migrate"])  # Example: Apply database migrations

    print("Deployment to production completed successfully.")

# Example usage
deploy_to_production()

