import psutil

def detect_suspicious_processes():
    suspicious_processes = []
    
    for process in psutil.process_iter(attrs=['name', 'exe']):
        process_name = process.info['name']
        process_path = process.info['exe']
        
        # Add conditions to identify suspicious processes
        if process_name == 'unknown_process':
            suspicious_processes.append((process_name, process_path))
        
    return suspicious_processes

# Example usage
suspicious_processes = detect_suspicious_processes()

if len(suspicious_processes) > 0:
    print("Suspicious processes found:")
    for process_name, process_path in suspicious_processes:
        print("Process Name:", process_name)
        print("Process Path:", process_path)
        print("----------------------")
else:
    print("No suspicious processes found.")

