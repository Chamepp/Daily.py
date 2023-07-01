import subprocess

def install_nginx():
    # Update package manager and install Nginx
    subprocess.run(['apt', 'update'])
    subprocess.run(['apt', 'install', '-y', 'nginx'])

def configure_nginx():
    # Configure Nginx
    nginx_config = '''
    server {
        listen 80;
        server_name example.com;

        location / {
            proxy_pass http://localhost:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
    '''

    # Write Nginx configuration to a file
    with open('/etc/nginx/sites-available/default', 'w') as config_file:
        config_file.write(nginx_config)

    # Restart Nginx to apply the configuration
    subprocess.run(['systemctl', 'restart', 'nginx'])

def main():
    install_nginx()
    configure_nginx()
    print("Nginx setup completed successfully!")

if __name__ == '__main__':
    main()

