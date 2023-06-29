import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Load time series data into a DataFrame
data = pd.read_csv('time_series_data.csv', parse_dates=['Date'], index_col='Date')

# Perform seasonal decomposition
decomposition = seasonal_decompose(data, model='additive')

# Extract components
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# Plot original, trend, seasonal, and residual components
plt.figure(figsize=(10, 8))
plt.subplot(411)
plt.plot(data, label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(seasonal, label='Seasonal')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(residual, label='Residual')
plt.legend(loc='best')

# Show the plot
plt.tight_layout()
plt.show()

