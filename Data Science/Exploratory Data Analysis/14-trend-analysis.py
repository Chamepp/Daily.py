import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load time series data
data = pd.read_csv('your_data_file.csv', parse_dates=['date_column'])
# Ensure the 'date_column' is in the proper datetime format

# Extract the relevant columns
dates = data['date_column']
values = data['value_column']

# Perform linear regression to estimate the trend
slope, intercept, _, _, _ = linregress(range(len(values)), values)
trend_line = intercept + slope * range(len(values))

# Plot the original time series data and the trend line
plt.figure(figsize=(10, 6))
plt.plot(dates, values, label='Original Data')
plt.plot(dates, trend_line, label='Trend Line')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Trend Analysis of Time Series')
plt.legend()
plt.show()

