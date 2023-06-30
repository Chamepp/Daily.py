import pandas as pd

def data_validation(dataframe):
    # Check for missing values
    missing_values = dataframe.isnull().sum()
    print("Missing Values:")
    print(missing_values)

    # Check for duplicate rows
    duplicate_rows = dataframe.duplicated()
    print("Duplicate Rows:")
    print(duplicate_rows)

    # Check for data inconsistencies or anomalies
    # Add your own custom validation checks here

    # Additional validation checks can be added based on specific requirements

# Example usage
# Assuming you have a dataframe named 'df' containing your data
data_validation(df)

