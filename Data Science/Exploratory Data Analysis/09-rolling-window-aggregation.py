import pandas as pd

# Sample data
data = {
    'date': pd.date_range(start='2023-01-01', periods=10),
    'value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the window size
window_size = 3

# Perform rolling window aggregation
df['rolling_sum'] = df['value'].rolling(window=window_size).sum()
df['rolling_mean'] = df['value'].rolling(window=window_size).mean()

# Print the result
print(df)

