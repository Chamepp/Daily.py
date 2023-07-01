import subprocess
import os
import datetime

def generate_ssl_certificate(domain_name):
    # Generate SSL certificate for the specified domain using Let's Encrypt
    subprocess.run(['certbot', 'certonly', '--standalone', '--non-interactive', '--agree-tos', '--email', 'your_email@example.com', '-d', domain_name])

def renew_ssl_certificate():
    # Renew all existing SSL certificates that are due for renewal
    subprocess.run(['certbot', 'renew', '--non-interactive', '--agree-tos'])

def install_ssl_certificate(domain_name):
    # Install the SSL certificate on the server for the specified domain
    subprocess.run(['cp', '/etc/letsencrypt/live/' + domain_name + '/fullchain.pem', '/path/to/ssl/cert'])
    subprocess.run(['cp', '/etc/letsencrypt/live/' + domain_name + '/privkey.pem', '/path/to/ssl/key'])
    subprocess.run(['service', 'webserver', 'restart'])  # Restart the web server to apply the new certificate

def check_ssl_certificate_expiry(domain_name):
    # Check the expiry date of the SSL certificate for the specified domain
    cert_path = '/etc/letsencrypt/live/' + domain_name + '/cert.pem'
    if os.path.exists(cert_path):
        cert_expiry_date = subprocess.check_output(['openssl', 'x509', '-enddate', '-noout', '-in', cert_path])
        expiry_date = datetime.datetime.strptime(cert_expiry_date.decode().split('=')[1].strip(), "%b %d %H:%M:%S %Y %Z")
        days_left = (expiry_date - datetime.datetime.now()).days
        print(f"The SSL certificate for {domain_name} expires in {days_left} days.")
    else:
        print(f"No SSL certificate found for {domain_name}.")

# Example usage
domain_name = "example.com"

# Generate SSL certificate for a new domain (run this once for new domains)
generate_ssl_certificate(domain_name)

# Check SSL certificate expiry
check_ssl_certificate_expiry(domain_name)

# Renew SSL certificate (run this periodically to renew expiring certificates)
renew_ssl_certificate()

# Install the SSL certificate on the server
install_ssl_certificate(domain_name)

