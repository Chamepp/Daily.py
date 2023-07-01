import subprocess

def install_packages(packages):
    try:
        subprocess.check_call(['apt-get', 'update'])  # Update package lists
        subprocess.check_call(['apt-get', 'install', '-y'] + packages)  # Install packages
        print("Package installation completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Package installation failed with error: {e}")

# List of packages to install
packages_to_install = ['package1', 'package2', 'package3']

# Call the function to install the packages
install_packages(packages_to_install)

