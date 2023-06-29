import numpy as np
import pandas as pd

def detect_outliers_zscore(data, threshold=3):
    # Calculate Z-score for each data point
    z_scores = (data - data.mean()) / data.std()

    # Identify outliers based on the threshold
    outliers = np.abs(z_scores) > threshold

    return outliers

# Example usage
data = pd.Series([2, 4, 6, 8, 10, 200, 12, 14, 16, 18])

outliers = detect_outliers_zscore(data)

if outliers.any():
    print("Outliers detected:")
    print(data[outliers])
else:
    print("No outliers detected.")

