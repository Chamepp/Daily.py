import subprocess

def install_docker():
    try:
        # Check if Docker is already installed
        subprocess.run(["docker", "--version"], check=True)
        print("Docker is already installed.")
    except subprocess.CalledProcessError:
        # Install Docker using the appropriate package manager based on the OS
        try:
            subprocess.run(["sudo", "apt-get", "update"], check=True)
            subprocess.run(["sudo", "apt-get", "install", "-y", "docker.io"], check=True)
            subprocess.run(["sudo", "systemctl", "start", "docker"], check=True)
            subprocess.run(["sudo", "systemctl", "enable", "docker"], check=True)
            print("Docker has been installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install Docker. Error: {e}")

if __name__ == "__main__":
    install_docker()

