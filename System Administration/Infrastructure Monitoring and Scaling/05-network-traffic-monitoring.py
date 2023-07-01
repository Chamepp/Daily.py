import psutil
import time

def monitor_network_traffic(interval):
    while True:
        # Get network usage statistics
        network_stats = psutil.net_io_counters()
        bytes_sent = network_stats.bytes_sent
        bytes_received = network_stats.bytes_recv

        # Convert bytes to megabytes
        mb_sent = bytes_sent / (1024 * 1024)
        mb_received = bytes_received / (1024 * 1024)

        # Display network traffic information
        print(f"Sent: {mb_sent:.2f} MB | Received: {mb_received:.2f} MB")

        time.sleep(interval)

# Example usage with interval of 5 seconds
monitor_network_traffic(5)

