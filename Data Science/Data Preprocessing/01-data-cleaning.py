import pandas as pd

# Load the dataset
data = pd.read_csv('your_dataset.csv')

# Remove duplicate records
data = data.drop_duplicates()

# Handle missing values
data = data.dropna()  # Drop rows with any missing values
# or
data = data.fillna(0)  # Replace missing values with 0
# or
data['column_name'].fillna(data['column_name'].mean(), inplace=True)  # Replace missing values with column mean

# Correct inconsistent data
data['column_name'] = data['column_name'].str.upper()  # Convert to uppercase
# or
data['column_name'] = data['column_name'].replace({'incorrect_value': 'correct_value'})  # Replace incorrect values

# Save the cleaned dataset
data.to_csv('cleaned_dataset.csv', index=False)

