import subprocess

def create_user(username, password):
    # Execute the command to create a new user
    subprocess.run(['useradd', '-m', username])

    # Set the user password
    subprocess.run(['passwd', username], input=password.encode())

    print(f"User '{username}' has been created successfully.")

def delete_user(username):
    # Execute the command to delete the user
    subprocess.run(['userdel', '-r', username])

    print(f"User '{username}' has been deleted successfully.")

# Example usage
username = input("Enter the username: ")
password = input("Enter the password: ")

# Create a new user
create_user(username, password)

# Delete an existing user
# delete_user(username)

