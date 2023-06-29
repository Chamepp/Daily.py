import pandas as pd

def calculate_missing_data_percentage(data):
    # Calculate the percentage of missing values in each column
    missing_data_percentage = (data.isnull().sum() / len(data)) * 100
    
    # Create a DataFrame to store the results
    missing_data_df = pd.DataFrame({'Column': data.columns, 'Missing Percentage': missing_data_percentage})
    
    # Sort the DataFrame by missing percentage in descending order
    missing_data_df.sort_values(by='Missing Percentage', ascending=False, inplace=True)
    
    return missing_data_df

# Load your dataset into a pandas DataFrame
data = pd.read_csv('your_dataset.csv')

# Calculate and display the missing data percentage
missing_data_df = calculate_missing_data_percentage(data)
print(missing_data_df)

