import pandas as pd

# Load the dataset
data = pd.read_csv('your_dataset.csv')  # Replace 'your_dataset.csv' with the path to your dataset

# Identify columns with missing values
columns_with_missing_values = data.columns[data.isnull().any()].tolist()

# Perform mean imputation for each column with missing values
for column in columns_with_missing_values:
    mean_value = data[column].mean()
    data[column].fillna(mean_value, inplace=True)

# Save the imputed dataset
data.to_csv('imputed_dataset.csv', index=False)  # Replace 'imputed_dataset.csv' with the desired output filename

