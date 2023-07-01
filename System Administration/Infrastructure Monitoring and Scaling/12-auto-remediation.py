import subprocess

def ansible_playbook(playbook_path):
    """Execute an Ansible playbook."""
    command = ["ansible-playbook", playbook_path]
    subprocess.run(command, check=True)

# Example usage
playbook_path = "/path/to/your/playbook.yml"
ansible_playbook(playbook_path)

