import os
import random
import string

def generate_secret_key(length=16):
    """Generate a random secret key for 2FA."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_qr_code_url(account_name, secret_key):
    """Generate a QR code URL for 2FA setup."""
    url = f'https://api.qrserver.com/v1/create-qr-code/?data=otpauth://totp/{account_name}?secret={secret_key}&issuer=MyApp'
    return url

def save_secret_key(account_name, secret_key):
    """Save the secret key to a file for future reference."""
    with open(f'{account_name}_secret.txt', 'w') as file:
        file.write(secret_key)

# Example usage
account_name = input("Enter your account name: ")

# Generate a secret key
secret_key = generate_secret_key()

# Save the secret key to a file
save_secret_key(account_name, secret_key)

# Generate the QR code URL
qr_code_url = generate_qr_code_url(account_name, secret_key)

print("Two-Factor Authentication (2FA) Setup:")
print(f"Account Name: {account_name}")
print(f"Secret Key: {secret_key}")
print(f"QR Code URL: {qr_code_url}")

