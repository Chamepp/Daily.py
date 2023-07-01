import os
import shutil

def aggregate_logs(log_directory, output_file):
    with open(output_file, 'w') as output:
        for root, dirs, files in os.walk(log_directory):
            for file in files:
                log_file = os.path.join(root, file)
                with open(log_file, 'r') as log:
                    shutil.copyfileobj(log, output)
                output.write('\n')

# Example usage
log_directory = '/path/to/logs'
output_file = '/path/to/aggregated_logs.txt'

aggregate_logs(log_directory, output_file)
print("Log aggregation complete. Aggregated logs saved to:", output_file)

