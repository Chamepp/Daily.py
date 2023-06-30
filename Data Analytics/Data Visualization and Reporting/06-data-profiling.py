import pandas as pd

def data_profiling(data):
    # Calculate basic statistics
    summary_stats = data.describe()
    
    # Calculate data distribution
    data_distribution = data.value_counts().reset_index()
    data_distribution.columns = ['Value', 'Count']
    
    # Calculate missing value percentages
    missing_values = data.isnull().mean().reset_index()
    missing_values.columns = ['Column', 'Missing Percentage']
    
    # Calculate unique value counts
    unique_values = data.nunique().reset_index()
    unique_values.columns = ['Column', 'Unique Count']
    
    # Combine results into a profiling report
    profiling_report = {
        'Summary Statistics': summary_stats,
        'Data Distribution': data_distribution,
        'Missing Values': missing_values,
        'Unique Values': unique_values
    }
    
    return profiling_report

# Example usage
data = pd.read_csv('your_data_file.csv')  # Replace with your data file
profiling_result = data_profiling(data)
print(profiling_result)

