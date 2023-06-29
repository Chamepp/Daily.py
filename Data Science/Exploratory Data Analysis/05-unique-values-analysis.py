import pandas as pd

def unique_values_analysis(dataframe):
    unique_values = {}
    for column in dataframe.columns:
        unique_values[column] = dataframe[column].nunique()
    
    return unique_values

# Example usage
# Assuming you have a DataFrame called 'data' containing your dataset
unique_values_result = unique_values_analysis(data)
for column, count in unique_values_result.items():
    print(f"Column '{column}' has {count} unique values.")

