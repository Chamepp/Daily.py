# This script demonstrates automated auto-scaling policies based on workload patterns

import time

# Simulated workload metrics (requests per minute)
workload_metrics = [100, 150, 200, 300, 400, 250, 180, 120, 100, 80, 100, 150, 200]

# Auto-scaling thresholds
upper_threshold = 300  # Scale up when workload exceeds this threshold
lower_threshold = 150  # Scale down when workload drops below this threshold

# Initial number of instances
num_instances = 2

def scale_up():
    global num_instances
    num_instances += 1
    print(f'Scaling up: Number of instances increased to {num_instances}.')

def scale_down():
    global num_instances
    if num_instances > 1:
        num_instances -= 1
        print(f'Scaling down: Number of instances decreased to {num_instances}.')
    else:
        print('Cannot scale down further. Minimum number of instances reached.')

# Simulate workload
for index, workload in enumerate(workload_metrics):
    print(f'Workload at minute {index+1}: {workload}')
    
    if workload > upper_threshold:
        scale_up()
    elif workload < lower_threshold:
        scale_down()
    
    time.sleep(1)  # Simulating a one-minute interval between workload measurements

