# Define incident response playbooks
playbooks = {
    'Malware Incident': ['Isolate affected system', 'Perform malware analysis', 'Remediate infected files'],
    'Unauthorized Access': ['Change compromised user account passwords', 'Disable affected user accounts'],
    'Data Breach': ['Identify compromised data', 'Contain the breach', 'Notify appropriate stakeholders'],
    # Add more playbooks as needed
}

def execute_playbook(playbook_name):
    if playbook_name in playbooks:
        print(f"Executing playbook for {playbook_name}:")
        for step in playbooks[playbook_name]:
            print(f"- {step}")
        print("Playbook executed successfully.")
    else:
        print("Playbook not found.")

# Example usage
incident_type = input("Enter the type of incident: ")
execute_playbook(incident_type)

