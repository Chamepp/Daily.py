import pandas as pd

def data_discretization(data, column, num_bins):
    # Perform data discretization using equal-width binning
    bin_labels = range(1, num_bins + 1)
    data['bin'] = pd.cut(data[column], num_bins, labels=bin_labels)
    return data

# Example usage
data = pd.read_csv('your_data_file.csv')  # Replace with your data file path
column_to_discretize = 'your_column_name'  # Replace with the column to discretize
num_bins = 5  # Replace with the desired number of bins

discretized_data = data_discretization(data, column_to_discretize, num_bins)

# Print the discretized data
print(discretized_data)

