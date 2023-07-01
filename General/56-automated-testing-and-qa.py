import subprocess

def check_network_connection():
    try:
        # Ping a reliable IP address to test network connectivity
        subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
        print("Network connection is active.")
    except subprocess.CalledProcessError:
        print("No network connection.")

def check_internet_speed():
    try:
        # Use Speedtest CLI to measure internet speed
        speedtest_output = subprocess.check_output(["speedtest", "--simple"]).decode("utf-8")
        for line in speedtest_output.split("\n"):
            if "Ping" in line:
                ping = line.split(":")[1].strip()
                print("Ping:", ping)
            elif "Download" in line:
                download = line.split(":")[1].strip()
                print("Download Speed:", download)
            elif "Upload" in line:
                upload = line.split(":")[1].strip()
                print("Upload Speed:", upload)
    except FileNotFoundError:
        print("Speedtest CLI not found. Install it using 'pip install speedtest-cli'.")

# Check network connection
check_network_connection()

# Check internet speed
check_internet_speed()
