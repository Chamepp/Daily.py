import pandas as pd
from sklearn.preprocessing import StandardScaler

# Sample dataset
data = pd.DataFrame({
    'Feature1': [10, 20, 30, 40, 50],
    'Feature2': [2, 4, 6, 8, 10],
    'Feature3': [100, 200, 300, 400, 500]
})

# Extract numerical columns
numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns

# Perform z-score normalization
scaler = StandardScaler()
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

# Print normalized dataset
print(data)

