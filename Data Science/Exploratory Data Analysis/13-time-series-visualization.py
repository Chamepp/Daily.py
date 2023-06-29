import pandas as pd
import matplotlib.pyplot as plt

# Read the time series data from a CSV file
data = pd.read_csv('your_data_file.csv', parse_dates=['date_column'], index_col='date_column')

# Plot the time series data
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['value_column'], color='blue')
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()

