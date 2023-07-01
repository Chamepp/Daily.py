import pandas as pd

# Read the input CSV file
input_file = "input_data.csv"
df = pd.read_csv(input_file)

# Perform data cleaning and preprocessing
# Example: Remove duplicate rows
df = df.drop_duplicates()

# Example: Fill missing values with mean
df.fillna(df.mean(), inplace=True)

# Example: Remove outliers
Q1 = df['column_name'].quantile(0.25)
Q3 = df['column_name'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['column_name'] >= Q1 - 1.5 * IQR) & (df['column_name'] <= Q3 + 1.5 * IQR)]

# Save the cleaned data to a new CSV file
output_file = "cleaned_data.csv"
df.to_csv(output_file, index=False)

print("Data cleaning and preprocessing completed. Cleaned data saved to", output_file)
