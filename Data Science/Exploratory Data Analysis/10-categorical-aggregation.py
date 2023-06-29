import pandas as pd

# Sample data
data = {
    'Category': ['A', 'B', 'A', 'B', 'C', 'C', 'A', 'B'],
    'Value': [10, 15, 20, 25, 30, 35, 40, 45]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Perform categorical aggregation
aggregated_data = df.groupby('Category').agg({
    'Value': ['sum', 'mean', 'count']
}).reset_index()

# Display the aggregated data
print(aggregated_data)

