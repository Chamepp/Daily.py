import pandas as pd

def data_binning(data, column, num_bins):
    # Compute bin edges based on the desired number of bins
    bin_edges = pd.cut(data[column], bins=num_bins, include_lowest=True)
    
    # Count the number of occurrences in each bin
    bin_counts = bin_edges.value_counts(sort=False)
    
    # Create a histogram-like representation of the binned data
    histogram = pd.DataFrame({'Bin Edges': bin_edges, 'Count': data[column]}).groupby('Bin Edges').count()
    
    return bin_counts, histogram

# Example usage
data = pd.read_csv('your_data.csv')  # Replace 'your_data.csv' with your actual data file
column_name = 'your_column'  # Replace 'your_column' with the column name to be binned
num_bins = 5  # Replace 5 with the desired number of bins

bin_counts, histogram = data_binning(data, column_name, num_bins)

print("Bin Counts:")
print(bin_counts)

print("\nHistogram:")
print(histogram)

