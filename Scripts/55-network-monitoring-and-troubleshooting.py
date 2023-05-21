import subprocess

def check_network(host):
    try:
        output = subprocess.check_output(["ping", "-c", "1", host])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    host = "www.google.com"  # Change to the desired host you want to ping
    if check_network(host):
        print("Network is up!")
    else:
        print("Network is down!")

if __name__ == "__main__":
    main()
