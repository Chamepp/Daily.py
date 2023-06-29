import pandas as pd

def missing_values_analysis(data):
    # Calculate the percentage and count of missing values in each column
    missing_values = data.isnull().sum()
    missing_percentage = (missing_values / len(data)) * 100

    # Create a summary dataframe
    summary_df = pd.DataFrame({'Missing Values': missing_values, 'Missing Percentage': missing_percentage})
    summary_df.sort_values(by='Missing Percentage', ascending=False, inplace=True)

    return summary_df

# Example usage
data = pd.read_csv('your_dataset.csv')  # Replace 'your_dataset.csv' with your actual dataset filename or path
missing_values_summary = missing_values_analysis(data)
print(missing_values_summary)

