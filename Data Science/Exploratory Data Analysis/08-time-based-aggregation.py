import pandas as pd

# Load the dataset
data = pd.read_csv('data.csv')

# Convert the 'timestamp' column to datetime format
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Set the 'timestamp' column as the index
data.set_index('timestamp', inplace=True)

# Resample and aggregate data on a daily basis
daily_data = data.resample('D').sum()

# Print the aggregated data
print(daily_data)

