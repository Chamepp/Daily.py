import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def normalize_data(df):
    # Select the numeric columns for normalization
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    # Apply standardization using z-score normalization
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    return df

def standardize_data(df):
    # Select the numeric columns for standardization
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    # Apply min-max scaling for standardization
    scaler = MinMaxScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    return df

# Example usage
# Assuming df is a pandas DataFrame containing your data

# Normalize the data using z-score normalization
normalized_df = normalize_data(df)
print("Normalized Data:")
print(normalized_df)

# Standardize the data using min-max scaling
standardized_df = standardize_data(df)
print("Standardized Data:")
print(standardized_df)

