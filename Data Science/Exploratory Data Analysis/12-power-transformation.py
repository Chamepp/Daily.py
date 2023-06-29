import numpy as np

def power_transform(data, power):
    transformed_data = np.power(data, power)
    return transformed_data

# Example usage
# Assuming 'data' is your numerical dataset stored in a numpy array or pandas DataFrame

# Specify the desired power for the transformation
power = 0.5

# Perform power transformation
transformed_data = power_transform(data, power)

# Print the transformed data
print(transformed_data)

