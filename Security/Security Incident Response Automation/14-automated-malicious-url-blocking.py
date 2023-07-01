import requests
import re
import subprocess

# List of known malicious URLs
malicious_urls = [
    "http://example.com/malware",
    "https://malicious-site.com/phishing",
    "http://infected-website.net/virus",
    # Add more malicious URLs to the list
]

def block_malicious_urls():
    # Fetch the current list of blocked URLs from the firewall
    blocked_urls = subprocess.run(["firewall-command", "get-blocked-urls"], capture_output=True, text=True).stdout

    for url in malicious_urls:
        if url not in blocked_urls:
            # Block the URL using the firewall command
            subprocess.run(["firewall-command", "block-url", url])
            print(f"Blocked URL: {url}")
        else:
            print(f"URL already blocked: {url}")

# Example usage
block_malicious_urls()

