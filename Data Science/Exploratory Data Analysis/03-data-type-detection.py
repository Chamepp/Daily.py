import pandas as pd

def data_type_detection(dataset):
    types = dataset.dtypes
    type_mapping = {
        'int64': 'integer',
        'float64': 'float',
        'object': 'string',
        'bool': 'boolean',
        'datetime64': 'datetime'
    }
    result = {}
    
    for col, dtype in types.items():
        result[col] = type_mapping.get(str(dtype), 'unknown')
    
    return result

# Example usage
data = pd.read_csv('your_dataset.csv')  # Replace with your dataset filename or path
data_types = data_type_detection(data)

# Print the detected data types for each column
for col, dtype in data_types.items():
    print(f"Column '{col}': {dtype}")

