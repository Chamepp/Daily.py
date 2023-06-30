import pandas as pd

# Sample data
data = {
    'Date': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Category': ['A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Perform data pivoting and reshaping
pivot_df = df.pivot(index='Date', columns='Category', values='Value')

# Display the pivoted DataFrame
print(pivot_df)

