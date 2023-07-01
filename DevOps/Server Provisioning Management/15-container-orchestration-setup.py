import subprocess

def install_docker():
    # Install Docker using the package manager (apt-get for Ubuntu)
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "docker.io"])

def configure_docker():
    # Start Docker service
    subprocess.run(["sudo", "systemctl", "start", "docker"])

    # Enable Docker service to start on system boot
    subprocess.run(["sudo", "systemctl", "enable", "docker"])

def main():
    print("Automating Docker installation and setup...")
    install_docker()
    configure_docker()
    print("Docker installation and setup completed successfully!")

if __name__ == "__main__":
    main()

