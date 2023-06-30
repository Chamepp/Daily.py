import subprocess

def renew_ssl_certificate(domain):
    try:
        # Run certbot command to renew SSL certificate
        subprocess.run(['certbot', 'certonly', '--agree-tos', '--non-interactive', '--keep-until-expiring',
                        '--cert-name', domain, '-d', domain], check=True)
        print("SSL certificate for", domain, "has been successfully renewed!")
    except subprocess.CalledProcessError as e:
        print("Failed to renew SSL certificate for", domain)
        print(e)

# Example usage
domain = input("Enter the domain for SSL certificate renewal: ")
renew_ssl_certificate(domain)

