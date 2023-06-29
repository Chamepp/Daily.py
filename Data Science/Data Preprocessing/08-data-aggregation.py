import pandas as pd

# Sample data
data = {
    'Category': ['A', 'A', 'B', 'B', 'A'],
    'Value': [10, 15, 20, 25, 30]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group data by 'Category' and calculate sum and average
grouped_data = df.groupby('Category').agg({'Value': ['sum', 'mean']})

# Print the grouped data
print(grouped_data)

