import pandas as pd

# Sample data
data = {
    'Category': ['A', 'A', 'B', 'B', 'A'],
    'Value': [10, 15, 20, 25, 30]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Perform groupby aggregation
grouped = df.groupby('Category').agg({
    'Value': ['sum', 'mean', 'max', 'min', 'count']
})

# Print the aggregated results
print(grouped)

