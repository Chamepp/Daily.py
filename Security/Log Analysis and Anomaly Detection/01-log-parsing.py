import re

def parse_logs(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()

    parsed_logs = []
    for log in logs:
        # Customize the regular expression pattern based on your log format
        pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\w+): (.*)'
        match = re.search(pattern, log)
        
        if match:
            timestamp = match.group(1)
            source = match.group(2)
            log_level = match.group(3)
            message = match.group(4)

            parsed_logs.append({
                'timestamp': timestamp,
                'source': source,
                'log_level': log_level,
                'message': message
            })

    return parsed_logs

# Example usage
log_file = 'security.log'
parsed_logs = parse_logs(log_file)

for log in parsed_logs:
    print(log)

