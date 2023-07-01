import random
import string

def generate_password(length=10):
    """Generate a random password of given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt user for password length
length = int(input("Enter the desired length of the password: "))

# Generate and print the password
password = generate_password(length)
print("Generated Password:", password)
