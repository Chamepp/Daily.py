import psutil

def monitor_server_resources():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    print(f"CPU Usage: {cpu_percent}%")
    print(f"Memory Usage: {memory_percent}%")
    print(f"Disk Usage: {disk_usage}%")

# Run the monitoring function
monitor_server_resources()

