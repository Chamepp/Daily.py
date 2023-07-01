import time

def collect_metrics():
    # Simulate collecting infrastructure metrics
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_space = get_disk_space()
    network_traffic = get_network_traffic()

    return cpu_usage, memory_usage, disk_space, network_traffic

def display_dashboard(cpu_usage, memory_usage, disk_space, network_traffic):
    # Print the real-time dashboard
    print("Infrastructure Dashboard")
    print("-----------------------")
    print("CPU Usage: {:.2f}%".format(cpu_usage))
    print("Memory Usage: {:.2f}%".format(memory_usage))
    print("Disk Space: {:.2f} GB".format(disk_space))
    print("Network Traffic: {:.2f} Mbps".format(network_traffic))
    print()

# Simulated functions to get infrastructure metrics
def get_cpu_usage():
    return 70.5  # Example CPU usage value

def get_memory_usage():
    return 45.2  # Example memory usage value

def get_disk_space():
    return 256.8  # Example disk space value

def get_network_traffic():
    return 120.3  # Example network traffic value

# Main program
def main():
    while True:
        # Collect infrastructure metrics
        cpu_usage, memory_usage, disk_space, network_traffic = collect_metrics()

        # Display the real-time dashboard
        display_dashboard(cpu_usage, memory_usage, disk_space, network_traffic)

        # Wait for a specific interval (e.g., 5 seconds) before updating the dashboard
        time.sleep(5)

if __name__ == '__main__':
    main()

