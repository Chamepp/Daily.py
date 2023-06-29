import pandas as pd

def data_discretization(data, column, num_bins):
    # Create a new column to store the discretized values
    discretized_column = column + '_discretized'
    
    # Calculate bin boundaries using equal-width binning
    min_val = data[column].min()
    max_val = data[column].max()
    bin_width = (max_val - min_val) / num_bins
    bins = [min_val + i*bin_width for i in range(num_bins+1)]
    
    # Perform discretization based on bin boundaries
    data[discretized_column] = pd.cut(data[column], bins=bins, labels=False, include_lowest=True)
    
    return data

# Example usage
# Assuming you have a DataFrame called 'df' with a continuous column 'age'

# Discretize the 'age' column into 5 bins
num_bins = 5
df = data_discretization(df, 'age', num_bins)

# Display the discretized data
print(df[['age', 'age_discretized']].head())

