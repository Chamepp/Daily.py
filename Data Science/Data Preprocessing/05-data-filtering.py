import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
    'Age': [25, 32, 28, 21, 29],
    'City': ['New York', 'London', 'Paris', 'New York', 'Paris']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Filter data based on a condition
filtered_data = df[df['Age'] > 25]

# Print the filtered data
print(filtered_data)

