import pandas as pd

# Load your dataset
dataset_path = "path/to/your/dataset.csv"
df = pd.read_csv(dataset_path)

# Check missing data in the dataset
missing_data = df.isnull().sum()
print("Missing Data:")
print(missing_data)

# Perform mean imputation for missing values
df_imputed = df.copy()
for column in df.columns:
    if df[column].isnull().any():
        column_mean = df[column].mean()
        df_imputed[column].fillna(column_mean, inplace=True)

# Check missing data after imputation
imputed_missing_data = df_imputed.isnull().sum()
print("\nMissing Data after Imputation:")
print(imputed_missing_data)

# Save the imputed dataset to a new file
imputed_dataset_path = "path/to/save/imputed_dataset.csv"
df_imputed.to_csv(imputed_dataset_path, index=False)

print("\nImputation complete. Imputed dataset saved to:", imputed_dataset_path)

