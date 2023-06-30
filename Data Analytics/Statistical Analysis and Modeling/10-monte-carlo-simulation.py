import pandas as pd
from statsmodels.tsa.seasonal import STL

# Load the time series data into a pandas DataFrame
data = pd.read_csv('time_series_data.csv', parse_dates=['date'], index_col='date')

# Perform time series decomposition using STL
stl = STL(data, seasonal=13)  # Seasonal period set to 13 for monthly data
result = stl.fit()

# Retrieve the components: trend, seasonal, and residuals
trend = result.trend
seasonal = result.seasonal
residuals = result.resid

# Print the components or perform further analysis
print("Trend:\n", trend)
print("Seasonal:\n", seasonal)
print("Residuals:\n", residuals)

