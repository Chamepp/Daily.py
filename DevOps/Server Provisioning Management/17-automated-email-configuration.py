import subprocess

def configure_postfix():
    # Install Postfix package
    subprocess.run(['apt', 'install', '-y', 'postfix'])

    # Configure Postfix
    subprocess.run(['dpkg-reconfigure', 'postfix'])

    print("Postfix configuration complete.")

# Run the script
configure_postfix()

