import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Load your time series data into a pandas DataFrame or Series
# Assuming the time series data is stored in a CSV file
data = pd.read_csv('your_data.csv')

# Assuming the time series data is in a column named 'value'
time_series = data['value']

# Compute autocorrelation and partial autocorrelation
lags = 50  # Number of lags to consider
acf_values = pd.Series(plot_acf(time_series, lags=lags, alpha=0.05))
pacf_values = pd.Series(plot_pacf(time_series, lags=lags, alpha=0.05))

# Plot autocorrelation function (ACF)
plt.figure(figsize=(12, 6))
plt.stem(acf_values.index, acf_values.values, use_line_collection=True)
plt.title('Autocorrelation Function (ACF)')
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.show()

# Plot partial autocorrelation function (PACF)
plt.figure(figsize=(12, 6))
plt.stem(pacf_values.index, pacf_values.values, use_line_collection=True)
plt.title('Partial Autocorrelation Function (PACF)')
plt.xlabel('Lag')
plt.ylabel('Partial Autocorrelation')
plt.show()

