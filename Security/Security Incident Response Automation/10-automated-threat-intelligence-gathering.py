import requests

def gather_threat_intelligence():
    # List of threat intelligence sources
    sources = [
        "https://example.com/threat-intel-source1",
        "https://example.com/threat-intel-source2",
        "https://example.com/threat-intel-source3"
    ]

    threat_intelligence = []

    # Iterate through each source
    for source in sources:
        try:
            # Fetch threat intelligence data from the source
            response = requests.get(source)
            data = response.json()

            # Extract relevant information from the data
            relevant_info = data["relevant_info"]

            # Append the relevant information to the threat intelligence list
            threat_intelligence.extend(relevant_info)
        except Exception as e:
            print(f"Error fetching threat intelligence from {source}: {str(e)}")

    return threat_intelligence

# Example usage
intelligence = gather_threat_intelligence()

# Print the gathered threat intelligence
print("Threat Intelligence:")
for info in intelligence:
    print(info)

