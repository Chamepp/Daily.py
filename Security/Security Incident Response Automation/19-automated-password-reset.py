import random
import string

def generate_random_password(length=12):
    # Generate a random password with a combination of uppercase, lowercase, and digits
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def reset_password(username):
    # Simulate the password reset process for a given username
    new_password = generate_random_password()
    
    # Here, you would implement the actual logic to reset the password for the user account
    # This could involve interacting with your user management system or directory service

    # For demonstration purposes, we will print the new password
    print(f"Password for user {username} has been reset to: {new_password}")

# Example usage
username = input("Enter the username to reset the password: ")
reset_password(username)

