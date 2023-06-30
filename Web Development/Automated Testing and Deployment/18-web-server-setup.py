import subprocess

def install_dependencies():
    # Install necessary packages for the web server (e.g., Apache, Nginx)
    subprocess.call(['apt', 'update'])
    subprocess.call(['apt', 'install', '-y', 'apache2'])

def configure_server():
    # Configure the web server settings (e.g., virtual hosts, ports)
    subprocess.call(['cp', '/etc/apache2/sites-available/000-default.conf', '/etc/apache2/sites-available/my-website.conf'])
    subprocess.call(['sed', '-i', 's/80/8080/g', '/etc/apache2/sites-available/my-website.conf'])
    subprocess.call(['a2ensite', 'my-website.conf'])
    subprocess.call(['a2dissite', '000-default.conf'])
    subprocess.call(['a2enmod', 'rewrite'])
    subprocess.call(['systemctl', 'restart', 'apache2'])

def main():
    print("Web Server Setup Script")
    print("=======================")
    
    # Step 1: Install dependencies
    print("Installing dependencies...")
    install_dependencies()
    print("Dependencies installed successfully.")
    
    # Step 2: Configure the server
    print("Configuring the web server...")
    configure_server()
    print("Web server configured successfully.")
    
    print("Web server setup completed!")

if __name__ == '__main__':
    main()

