import subprocess

def run_security_scan(target_url):
    # Run OWASP ZAP security scan
    cmd = ['zap.sh', '-cmd', '-quickurl', target_url, '-quickout', 'report.html']
    subprocess.run(cmd, capture_output=True)

# Example usage
target_url = 'http://example.com'
run_security_scan(target_url)

