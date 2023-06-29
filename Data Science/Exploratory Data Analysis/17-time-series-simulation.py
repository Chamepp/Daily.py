import numpy as np
import matplotlib.pyplot as plt

# Parameters for the synthetic time series
num_points = 1000
trend_coeff = 0.05
seasonal_amplitude = 10
noise_std = 2

# Generate synthetic time series data
time = np.arange(num_points)
trend = trend_coeff * time
seasonal = seasonal_amplitude * np.sin(2 * np.pi * time / 365)
noise = np.random.normal(0, noise_std, size=num_points)
time_series = trend + seasonal + noise

# Plot the synthetic time series
plt.figure(figsize=(10, 6))
plt.plot(time, time_series)
plt.title('Synthetic Time Series')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()

