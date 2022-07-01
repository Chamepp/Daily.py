import sys
import json
import yaml


# Json Data
json_data = json.loads(open(sys.argv[1]).read())

# Convert Data
converted_json_data = json.dumps(json_data)

# Get Output
print(yaml.dump(yaml.load(converted_json_data), default_flow_style=False))
