import pandas as pd

def deduplicate_data(df, key_columns):
    # Identify duplicate records based on key columns
    duplicates = df.duplicated(subset=key_columns, keep='first')

    # Remove duplicate records
    deduplicated_df = df[~duplicates]

    return deduplicated_df

# Example usage
# Assuming you have a CSV file 'data.csv' with columns 'id', 'name', 'email'
data = pd.read_csv('data.csv')

# Select the key columns based on which duplicates will be identified
key_columns = ['id']

# Perform data deduplication
deduplicated_data = deduplicate_data(data, key_columns)

# Display the deduplicated data
print(deduplicated_data)

