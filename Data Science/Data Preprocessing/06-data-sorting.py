import pandas as pd

# Sample data
data = {
    'Name': ['John', 'Alice', 'Bob', 'David'],
    'Age': [28, 24, 32, 30],
    'Salary': [50000, 60000, 45000, 70000]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Sort the DataFrame by 'Name' column in ascending order
sorted_df = df.sort_values('Name')

# Display the sorted DataFrame
print("Sorted by Name (Ascending):\n", sorted_df)

# Sort the DataFrame by 'Age' column in descending order
sorted_df = df.sort_values('Age', ascending=False)

# Display the sorted DataFrame
print("Sorted by Age (Descending):\n", sorted_df)

# Sort the DataFrame by multiple columns
sorted_df = df.sort_values(['Age', 'Salary'], ascending=[True, False])

# Display the sorted DataFrame
print("Sorted by Age (Ascending) and Salary (Descending):\n", sorted_df)

