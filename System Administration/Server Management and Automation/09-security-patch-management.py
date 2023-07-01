import subprocess

def grant_access(username, permission):
    # Execute the command to grant access to a user
    command = f"usermod -aG {permission} {username}"
    subprocess.run(command, shell=True)

def revoke_access(username, permission):
    # Execute the command to revoke access from a user
    command = f"gpasswd -d {username} {permission}"
    subprocess.run(command, shell=True)

# Example usage
username = input("Enter the username: ")
permission = input("Enter the permission to grant/revoke: ")

grant_or_revoke = input("Do you want to grant or revoke access? (grant/revoke): ")

if grant_or_revoke == "grant":
    grant_access(username, permission)
    print(f"Access granted: {username} now has {permission} permission.")
elif grant_or_revoke == "revoke":
    revoke_access(username, permission)
    print(f"Access revoked: {username} no longer has {permission} permission.")
else:
    print("Invalid choice. Please enter 'grant' or 'revoke'.")

