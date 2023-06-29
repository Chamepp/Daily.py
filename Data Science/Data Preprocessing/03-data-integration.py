import pandas as pd

# Example datasets
data1 = pd.DataFrame({'ID': [1, 2, 3],
                      'Name': ['John', 'Alice', 'Bob'],
                      'Age': [25, 30, 35]})

data2 = pd.DataFrame({'ID': [3, 4, 5],
                      'Salary': [5000, 6000, 7000]})

# Merge the datasets based on the 'ID' column
merged_data = pd.merge(data1, data2, on='ID', how='inner')

# Concatenate the datasets vertically
concatenated_data = pd.concat([data1, data2])

# Display the merged data
print("Merged Data:")
print(merged_data)

print("\nConcatenated Data:")
print(concatenated_data)

