import numpy as np

def apply_transformation(data, transformation):
    if transformation == 'log':
        transformed_data = np.log(data)
    elif transformation == 'sqrt':
        transformed_data = np.sqrt(data)
    else:
        print("Invalid transformation. Please choose 'log' or 'sqrt'.")
        return None
    return transformed_data

# Example usage
data = [1, 2, 3, 4, 5]
transformation_type = 'log'

transformed_data = apply_transformation(data, transformation_type)
print("Original data:", data)
print("Transformed data:", transformed_data)

