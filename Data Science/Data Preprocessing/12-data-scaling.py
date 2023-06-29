import pandas as pd
from sklearn.preprocessing import StandardScaler

# Sample dataset
data = pd.DataFrame({
    'Age': [25, 30, 35, 40, 45],
    'Income': [50000, 75000, 100000, 125000, 150000],
    'Savings': [10000, 25000, 40000, 55000, 70000]
})

# Extract numerical columns for scaling
numerical_columns = data.select_dtypes(include='number').columns

# Perform data scaling using StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data[numerical_columns])

# Create a new DataFrame with scaled values
scaled_df = pd.DataFrame(scaled_data, columns=numerical_columns)

# Print the original and scaled data
print("Original Data:")
print(data)
print("\nScaled Data:")
print(scaled_df)

