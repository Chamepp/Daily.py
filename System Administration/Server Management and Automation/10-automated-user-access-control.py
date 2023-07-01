import subprocess

# Function to add a user with specified access level
def add_user(username, access_level):
    # Add user to the system
    subprocess.run(['useradd', username])
    
    # Set user access level
    subprocess.run(['setfacl', '-m', f'user:{username}:{access_level}', '/path/to/directory'])
    
    print(f"User {username} with access level {access_level} has been added.")

# Example usage
username = input("Enter the username: ")
access_level = input("Enter the access level (e.g., read, write, execute): ")

add_user(username, access_level)

