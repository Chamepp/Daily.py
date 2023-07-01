import requests

def update_firewall_rules(rule_list):
    # API endpoint for updating firewall rules
    api_url = 'https://api.example.com/firewall/rules'

    for rule in rule_list:
        # Construct the payload for the API request
        payload = {
            'action': rule['action'],
            'source_ip': rule['source_ip'],
            'destination_ip': rule['destination_ip'],
            'protocol': rule['protocol'],
            'port': rule['port']
        }

        try:
            # Send a PUT request to update the firewall rule
            response = requests.put(api_url, json=payload)
            response.raise_for_status()

            print(f"Firewall rule updated: {rule}")

        except requests.exceptions.RequestException as e:
            print(f"Error updating firewall rule: {rule}")
            print(e)

# Example usage
firewall_rules = [
    {
        'action': 'allow',
        'source_ip': '192.168.1.10',
        'destination_ip': '10.0.0.5',
        'protocol': 'tcp',
        'port': 80
    },
    {
        'action': 'deny',
        'source_ip': '192.168.2.20',
        'destination_ip': '10.0.0.8',
        'protocol': 'udp',
        'port': 443
    }
]

update_firewall_rules(firewall_rules)

